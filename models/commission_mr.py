from odoo import fields, models, api, SUPERUSER_ID


class ResPartnerExtension(models.Model):
    _inherit = "res.partner"

    commission_role_id = fields.Many2one('acs.commission.role', string='Role')
    commission_ids = fields.One2many('acs.hms.commission', 'partner_id', 'Business Commission')
    provide_commission = fields.Boolean('Give Commission')
    commission_percentage = fields.Float('Commission Percentage')
    commission_rule_ids = fields.One2many("acs.commission.rule", "partner_id", string="Commission Rules")

    def commission_action(self):
        action = self.env["ir.actions.actions"]._for_xml_id("acs_hms_commission.acs_hms_commission_action")
        action['domain'] = [('partner_id', '=', self.id)]
        action['context'] = {'default_partner_id': self.id, 'search_default_not_invoiced': 1}
        return action


class MedicalRepresentativeExtension(models.Model):
    _inherit = 'medical.representative'
    _description = "Medical Representative"
    patient_id = fields.Many2one('hms.patient', string='Patient Name')

    def commission_action(self):
        action = self.env["ir.actions.actions"]._for_xml_id("acs_hms_commission.acs_hms_commission_action")
        action['domain'] = [('partner_id', '=', self.partner_id.id)]
        action['context'] = {'default_partner_id': self.partner_id.id, 'search_default_not_invoiced': 1}
        return action


class Appointment(models.Model):
    _inherit = "hms.appointment"

    def create_invoice(self):
        res = super(Appointment, self).create_invoice()
        for rec in self:
            rec.invoice_id.onchange_total_amount()
            rec.invoice_id.onchange_ref_physician()
            rec.invoice_id.onchange_physician()
        return res


class HMSCommissionExtension(models.Model):
    _inherit = 'acs.hms.commission'
    patient = fields.Many2one('hms.patient', string='Patient Name')
    total_commission = fields.Float(string="Total Amount")

    @api.onchange('invoice_id', 'partner_id')
    def total_commission_amount(self):
        print(self.invoice_id.name)
        print(self.partner_id.commission_rule_ids)

        total = 0
        for invoice_line in self.invoice_id.invoice_line_ids:
            for commision_rule in self.partner_id.commission_rule_ids:

                if invoice_line.product_id.product_tmpl_id.id == commision_rule.product_id.id:
                    print("Something found")
                    total += (invoice_line.price_subtotal* commision_rule.percentage)/100
        self.total_commission = total
