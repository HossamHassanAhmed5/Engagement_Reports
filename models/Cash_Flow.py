from openerp import fields,models,api

class cash_flow(models.Model):
    _name = "cash.flow"

    client_name = fields.Many2one("res.partner", String="Client name : ")
    from_date = fields.Date(String="From: ")
    to_date = fields.Date(String="To: ")

    cash_beg = fields.Float()

    op_id= fields.One2many('op_cash', 'user_id', 'Operating Activities ')
    op_paid_id= fields.One2many('op_paid' , 'user_id')

    op_cash_total= fields.Float(readonly=True)  #computed value

    inv_id = fields.One2many('inv_cash', 'user_id', 'Operating Activities ')
    inv_paid_id = fields.One2many('inv_paid', 'user_id')



    inv_cash_total = fields.Float(readonly=True )  #computed value

    fin_id = fields.One2many('fin_cash', 'user_id', 'Operating Activities ')
    fin_paid_id = fields.One2many('fin_paid', 'user_id')


    fin_cash_total = fields.Float(readonly=True )   #computed value

    net_incr = fields.Float(readonly=True)     #computed value
    cash_end = fields.Float(readonly=True )  #computed value


class op_cash(models.Model):
    _name = "op_cash"

    user_id = fields.Many2one("cash.flow", "operting activities", ondelete="cascade")
    op_cash_rec_from = fields.Char()
    op_cash_rec_val = fields.Float()

class op_paid(models.Model):
    _name="op_paid"

    user_id = fields.Many2one("cash.flow", "operting activities", ondelete="cascade")
    op_paid_rec_to = fields.Char()
    op_paid_rec_val = fields.Float()

class inv_cash(models.Model):
    _name="inv_cash"

    user_id = fields.Many2one("cash.flow","investment", ondelete="cascade")
    inv_cash_rec_from = fields.Char()
    inv_cash_rec_val = fields.Float()

class inv_paid(models.Model):
    _name="inv_paid"

    user_id = fields.Many2one("cash.flow", ondelete="cascade")
    inv_paid_rec_to = fields.Char()
    inv_paid_rec_val = fields.Float()


class fin_cash(models.Model):
    _name = "fin_cash"

    user_id = fields.Many2one("cash.flow", ondelete="cascade")
    fin_cash_rec_from = fields.Char()
    fin_cash_rec_val = fields.Float()


class fin_paid(models.Model):
    _name = "fin_paid"

    user_id = fields.Many2one("cash.flow", ondelete="cascade")
    fin_paid_rec_to = fields.Char()
    fin_paid_rec_val = fields.Float()


