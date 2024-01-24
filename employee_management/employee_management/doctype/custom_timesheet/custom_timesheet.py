# Copyright (c) 2024, Bhuvanes and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class CustomTimesheet(Document):

	def before_save(self):
		
		#Checking Timesheet already submitted for the given date 
		if frappe.db.exists("Custom Timesheet", {"date": self.date}) :
			frappe.throw("Timesheet already submitted  for the selected date.")
		
		tot_hour = 0
		for TD in self.timesheet_details:
			tot_hour +=TD.hours
		#setting total hours
		self.total_hours = tot_hour

	def on_submit(self):
		#Creating Attendance record
		attendance = frappe.new_doc('Attendance')
		attendance.employee = self.employee
		attendance.employee_name = self.employee_name
		attendance.attendance_date = self.date
		#getting dept name
		emp = frappe.get_doc('Custom Employee', attendance.employee)
		attendance.department = emp.department

		if self.half_day :
			attendance.attendance_status = 'Half day'
		elif self.work_from_home:
			attendance.attendance_status = 'Work from home'
		else:
			attendance.attendance_status = 'Present'
		attendance.insert()
		attendance.submit()
		attendance.reload()