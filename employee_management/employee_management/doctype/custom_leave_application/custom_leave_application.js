// Copyright (c) 2024, Bhuvanes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Custom Leave Application', {
	validate: function(frm) {
			// if (frm.doc.from_date < frappe.datetime.get_today()){
			// 	frappe.throw('From date cannot be a past date')
			// }
			if (frm.doc.to_date < frm.doc.from_date) {
				frappe.throw('To date cannot be a before from from date')
			}
		},
});
