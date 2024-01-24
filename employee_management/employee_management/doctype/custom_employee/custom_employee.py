# Copyright (c) 2024, Bhuvanes and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import date_diff

class CustomEmployee(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""} {self.middle_name or ""}'

		years_difference = date_diff(self.date_of_joining, self.date_of_birth) // 365
		emp_set = frappe.get_doc("Employee Settings")
		if emp_set.employee_joining_age_limit > years_difference:
			frappe.throw("Employee age should be above 18.")

