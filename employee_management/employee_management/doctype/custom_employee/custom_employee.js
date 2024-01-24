// Copyright (c) 2024, Bhuvanes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Custom Employee', {
	refresh: function(frm) {
		
		frm.fields_dict['reporting_manager'].get_query = function(doc){
			return {
				filters: [
					['status','=','Active'],
				]
			};
		};
		frm.fields_dict['designation'].get_query = function(doc) {
			return {
				filters: [
					['docstatus','=','1'],
				]
			}
		}
	},
	validate: function(frm) {

		if (frm.doc.date_of_joining > frappe.datetime.get_today()) {
            frappe.throw('Date of Joining cannot be a future date.');
            
        };
	},
});
