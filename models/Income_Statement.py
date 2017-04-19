from openerp import fields,models,api

class income_statement(models.Model):
    _name="income.statement"

    client_name = fields.Many2one("res.partner", String="Client name : ")
    from_date = fields.Date(String="From: ")
    to_date = fields.Date(String="To: ")

    revenue_id =  fields.One2many('revenue', 'user_id', 'Revenue')

    op_id = fields.One2many('operation', 'user_id', 'Operation')

    revenue_exp_val = fields.Float()
    revenue_exp_tot = fields.Float()
    revenue_exp_budget = fields.Float()             #computed value
    revenue_exp_change = fields.Float()            #computed value
    revenue_exp_year = fields.Float()
    revenue_exp_yoy_change = fields.Float()             #computed value

    finance_val = fields.Float()
    finance_tot = fields.Float()
    finance_budget = fields.Float()                      #computed value
    finance_change = fields.Float()                #computed value
    finance_year = fields.Float()
    finance_yoy_change = fields.Float()               #computed value

    tax_val = fields.Float()
    tax_tot = fields.Float()
    tax_budget = fields.Float()                #computed value
    tax_change = fields.Float()                   #computed value
    tax_year = fields.Float()
    tax_yoy_change = fields.Float()           #computed value

    summary_val = fields.Float()
    summary_tot = fields.Float()
    summary_budget = fields.Float()              #computed value
    summary_change = fields.Float()                #computed value
    summary_year = fields.Float()
    summary_yoy_change = fields.Float()                #computed value

    details = fields.Text()

class revenue(models.Model):
    _name="revenue"

    user_id = fields.Many2one('income.statement', "Income Statement", ondelete="cascade")
    revenue_add = fields.Char("Indicator")
    revenue_val = fields.Float("Current Value")
    revenue_tot = fields.Float("Total%")
    revenue_budget = fields.Float("Budget")  # computed value
    revenue_change = fields.Float("Change%")  # computed value
    revenue_year = fields.Float("YOY")
    revenue_yoy_change = fields.Float("Change%")  # computed value

class operation(models.Model):
    _name="operation"

    user_id = fields.Many2one('income.statement', "Income Statement", ondelete="cascade")
    op_add = fields.Char("Indicator")
    op_val = fields.Float("Current Value")
    op_tot = fields.Float("Total%")
    op_budget = fields.Float("Budget")  # computed value
    op_change = fields.Float("Change%")  # computed value
    op_year = fields.Float("YOY")
    op_yoy_change = fields.Float("Change%")  # computed value