from openerp import fields,models,api

class kpi(models.Model):
    _name = "kpi"

    client_name = fields.Many2one("res.partner", String="Client name : ")
    from_date = fields.Date(String="From: ")
    to_date = fields.Date(String="To: ")

    key_per = fields.One2many('performance_row', 'user_id', "KPI")


    details = fields.Text()

class performance_row(models.Model):
    _name= "performance_row"

    user_id = fields.Many2one("kpi", "Key Performance", ondelete="cascade")
    indicator = fields.Char()
    current = fields.Float()
    target = fields.Float()
    Variance = fields.Float(readonly=True)

