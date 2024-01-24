// Copyright (c) 2024, Bhuvanes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Custom Timesheet', {
	onload: function(frm) {
		//date as todays date
		frm.set_value('date', frappe.datetime.get_today());
	},
	validate: function(frm) {
		if (frm.doc.date > frappe.datetime.get_today()){
			frappe.throw('Date cannot be a future date')
		}
	},
});
