# Copyright (c) 2024, Bhuvanes and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime,timedelta
from frappe.utils import getdate

class CustomLeaveApplication(Document):
	def before_save(self):
		#checking restrict backdated 
		Emp_doc = frappe.get_doc("Employee Settings")
		if Emp_doc.restrict_backdated_leave_application == 1 and self.from_date < getdate().strftime("%Y-%m-%d"):
			frappe.throw("From date cannot be a past date.")
		
		#Setting Total leave days
		from_date = datetime.strptime(self.from_date, "%Y-%m-%d")
		to_date = datetime.strptime(self.to_date, "%Y-%m-%d")
		self.total_leave_days = (to_date - from_date).days + 1
		
	def on_submit(self):
		from_date = datetime.strptime(self.from_date, "%Y-%m-%d")
		to_date = datetime.strptime(self.to_date, "%Y-%m-%d")
		#getting leave days 
		leave_days = []
		for i in [from_date + timedelta(days=x) for x in range(self.total_leave_days)] :
			leave_days.append(i.strftime("%Y-%m-%d"))
		
		#Creating attendance for each leave days
		for i in leave_days:

			attendance = frappe.new_doc('Attendance')
			attendance.employee = self.employee
			attendance.employee_name = self.employee_name
			attendance.attendance_date = i
			
			emp = frappe.get_doc('Custom Employee', attendance.employee)
			attendance.department = emp.department
			if self.half_day:
				attendance.attendance_status = 'Half day'
			else:
				attendance.attendance_status = 'Leave'
			attendance.insert()
			attendance.submit()
			attendance.reload()
