// Copyright (c) 2024, Bhuvanes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Custom Project', {
	refresh: function(frm) {
		frm.doc.start_date = frappe.datetime.get_today();
	},
	validate: function(frm) {
		
		if (frm.doc.end_date <= frm.doc.start_date) {
			frappe.throw('End date cannot be a before from start date')
		}
	},
});
