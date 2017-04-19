from openerp import fields,models,api

class balance_sheet(models.Model):

    _name = "balance.sheet"

    client_name = fields.Many2one("res.partner", String="Client name : ")
    from_date = fields.Date(String="From: ")
    to_date = fields.Date(String="To: ")

    current_asset_id= fields.One2many('current_asset', 'user_id', 'Current Asset')

    non_current_asset_id = fields.One2many('non_current_asset', 'user_id', 'Current Asset')

    current_liab_id = fields.One2many('current_liab', 'user_id', 'Current Asset')

    non_current_liab_id = fields.One2many('non_current_liab', 'user_id', 'Current Asset')

    equity_id = fields.One2many('equality', 'user_id', 'Equality')

    net_asset_val = fields.Float()
    net_asset_balance = fields.Float()
    net_asset_year = fields.Float()
    net_asset_change = fields.Float()

    tot_equity_val = fields.Float()
    tot_equity_balance = fields.Float()  # computed value
    tot_equity_year = fields.Float()
    tot_equity_change = fields.Float()  # computed value

    details = fields.Text();

class current_asset(models.Model):
    _name="current_asset"

    user_id = fields.Many2one('balance.sheet', "Current Asset", ondelete="cascade")
    current_asset_add = fields.Char("Indicator")
    current_asset_val = fields.Float("Current Value")
    current_asset_balance = fields.Float("Balance ")
    current_asset_year = fields.Float("Year on Year")
    current_asset_change = fields.Float("Change%")  # computed value

class current_liab(models.Model):
    _name="current_liab"

    user_id = fields.Many2one('balance.sheet', "Current liab", ondelete="cascade")
    current_liab_add = fields.Char("Indicator")
    current_liab_val = fields.Float("Current Value")
    current_liab_balance = fields.Float("Balance ")
    current_liab_year = fields.Float("Year on Year")
    current_liab_change = fields.Float("Change%")  # computed value

class non_current_liab(models.Model):
    _name="non_current_liab"

    user_id = fields.Many2one('balance.sheet', "Non Current liab", ondelete="cascade")
    non_current_liab_add = fields.Char("Indicator")
    non_current_liab_val = fields.Float("Current Value")
    non_current_liab_balance = fields.Float("Balance ")
    non_current_liab_year = fields.Float("Year on Year")
    noncurrent_liab_change = fields.Float("Change%")  # computed value

class non_current_asset(models.Model):
    _name="non_current_asset"

    user_id = fields.Many2one('balance.sheet', "Non Current Asset", ondelete="cascade")
    non_current_asset_add = fields.Char("Indicator")
    non_current_asset_val = fields.Float("Current Value")
    non_current_asset_balance = fields.Float("Balance ")
    non_current_asset_year = fields.Float("Year on Year")
    non_current_asset_change = fields.Float("Change%")  # computed value

class equilty(models.Model):
    _name="equality"

    user_id = fields.Many2one('balance.sheet', "Equality", ondelete="cascade")

    equity_add = fields.Char("Indicator")
    equity_val = fields.Float("Current Value")
    equity_balance = fields.Float("Balance")  # computed value
    equity_year = fields.Float("Year on Year")
    equity_change = fields.Float("Change%")  # computed value

