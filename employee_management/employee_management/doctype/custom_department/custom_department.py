# Copyright (c) 2024, Bhuvanes and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_abbr

class CustomDepartment(Document):
	def before_save(self):
		# Setting abbreviation
		self.abbreviation = get_abbr(self.department_name,max_len=2)