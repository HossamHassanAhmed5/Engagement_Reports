from openerp import fields,models,api

class audit(models.Model):
    _name = "audit"

    client_name = fields.Many2one("res.partner", String="Client name : ")
    from_date = fields.Date(String="From: ")
    to_date = fields.Date(String="To: ")

    key_stren_id = fields.One2many('key_strenghts','user_id',"Key Strenghts")

    key_cont_id = fields.One2many('key_control', 'user_id', "Key Control")

    key_accel = fields.One2many('key_accel', 'user_id', "Key Accelerators")


    details = fields.Text()

class key_strenghts(models.Model):
    _name = "key_strenghts"

    user_id = fields.Many2one("audit", "Audit", ondelete="cascade")
    key_cont = fields.Text("Key Controls ")
    incont = fields.Text("Highlighted incotrols and processes")
    recom = fields.Text("Recommendations for better practice improvement")

class key_control(models.Model):
    _name = "key_control"

    user_id = fields.Many2one("audit", "Audit", ondelete="cascade")
    key_cont_anal = fields.Text("Key Controls")
    dis_openion = fields.Text("Discreet openion")
    nig_openion = fields.Text("Negative openion")
    man_action = fields.Text("Management action ")

class key_accel(models.Model):
    _name = "key_accel"

    user_id = fields.Many2one("audit", "Audit", ondelete="cascade")
    empowered = fields.Text("Empowered")
    target_date = fields.Date("Target Date")