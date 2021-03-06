from openerp import fields,models,api;

class performance_snapshot(models.Model):
    _name="performance.snapshot"


    logo = fields.Binary()
    issue_date = fields.Date(String="Issue date")
    auditor = fields.Char(String= "The Auditor: ")
    from_date= fields.Date(String="From: ")
    to_date = fields.Date(String="To: ")
    manager = fields.Char(String="Engagement Manager: ")
    statment_work = fields.Text(String="Statement of Work: ")
    work_hour= fields.Float(String="Total Working Hours :")
    client_rel = fields.Char(String="Client Relations : ")
    client_name= fields.Many2one("res.partner",String="Client name : ")
    Engag_num= fields.Integer(String="Engagement Number : ")
    licen_info = fields.Char(String="License Info : ")
    city = fields.Char(String="City")
    country = fields.Char(String="Country: ")
    busin_activary= fields.Char(String="Business Activity : ")
    report_cur= fields.Char(String="Report Currency : ")
    round_level= fields.Float(String = "Rounding Level : ")
    director_name = fields.Many2one("res.partner",String="Director's Name : ")
    email = fields.Char(related="director_name.email", String="Email: ")
    phone = fields.Char(related="director_name.phone", String="Phone: ")
    address = fields.Char(string="Address: ")
    open_findings = fields.Integer(String="Open Findings ")
    key_findings = fields.Char()
    findings_date = fields.Date()
    open_vouching = fields.Integer(String="Open Vouching  ")
    key_vouching= fields.Char()
    vouching_date = fields.Date()
    discreet_openion = fields.Integer(String="Discreet Openion ")
    key_discreet_openion = fields.Char()
    discreet_openion_date = fields.Date()
    negative_openion = fields.Integer(String="Negative Openion ")
    key_negative_openion = fields.Char()
    negative_openion_date = fields.Date()
    curr_rev = fields.Float()
    budget_rev = fields.Float()
    variance_rev = fields.Float()
    y_on_y_rev = fields.Float()
    variance_y_to_y_rev = fields.Float()
    curr_netprof = fields.Float()
    budget_netprof = fields.Float()
    variance_netprof = fields.Float()
    y_on_y_netprof = fields.Float()
    variance_y_to_y_netprof = fields.Float()
    curr_cash = fields.Float()
    budget_cash = fields.Float()
    variance_cash = fields.Float()
    y_on_y_cash = fields.Float()
    variance_y_to_y_cash = fields.Float()
    curr_asset = fields.Float()
    budget_asset = fields.Float()
    variance_asset = fields.Float()
    y_on_y_asset = fields.Float()
    variance_y_to_y_asset = fields.Float()
    details = fields.Text();
