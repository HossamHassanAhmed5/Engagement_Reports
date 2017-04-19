from openerp import fields,models,api

class test(models.Model):
    _name = "test"

    client_name = fields.Many2one("res.partner", String="Client name : ")
    from_date = fields.Date(String="From: ")
    to_date = fields.Date(String="To: ")

    work_ratio = fields.Float()
    work_score = fields.Float(compute="_get_work_score", Store=True) #compute

    equilty_ratio_asset = fields.Float()
    equilty_score_asset = fields.Float(compute="_get_equilty_score_asset", Store=True)  # compute

    ebit_ratio = fields.Float()
    ebit_score = fields.Float(compute="_get_ebit_score", Store=True)  # compute

    equilty_ratio_liab = fields.Float()
    equilty_score_liab = fields.Float(compute="_get_equilty_score_liab", Store=True)  # compute

    tot_score = fields.Float(compute="_get_total_score", Store=True) #compute

    dept_past = fields.Float()
    dept_cur = fields.Float()
    dept_fut = fields.Float()   #compute
    dept_avrg = fields.Float()  #compute
    dept_weight =fields.Float()  #compute

    non_cur_past = fields.Float()
    non_cur_cur = fields.Float()
    non_cur_fut = fields.Float()  # compute
    non_cur_avrg = fields.Float()  # compute
    non_cur_weight = fields.Float()  # compute

    cur_past = fields.Float()
    cur_cur = fields.Float()
    cur_fut = fields.Float()  # compute
    cur_avrg = fields.Float()  # compute
    cur_weight = fields.Float()  # compute

    quick_past = fields.Float()
    quick_cur = fields.Float()
    quick_fut = fields.Float()  # compute
    quick_avrg = fields.Float()  # compute
    quick_weight = fields.Float()  # compute

    cash_past = fields.Float()
    cash_cur = fields.Float()
    cash_fut = fields.Float()  # compute
    cash_avrg = fields.Float()  # compute
    cash_weight = fields.Float()  # compute

    total_1 = fields.Float() #compute
    rat_scale_1 = fields.Float()  #compute

    ret_equilty_past = fields.Float()
    ret_equilty_cur = fields.Float()
    ret_equilty_fut = fields.Float()  # compute
    ret_equilty_avrg = fields.Float()  # compute
    ret_equilty_weight = fields.Float()  # compute

    ret_asset_past = fields.Float()
    ret_asset_cur = fields.Float()
    ret_asset_fut = fields.Float()  # compute
    ret_asset_avrg = fields.Float()  # compute
    ret_asset_weight = fields.Float()  # compute

    rev_grow_past = fields.Float()
    rev_grow_cur = fields.Float()
    rev_grow_fut = fields.Float()  # compute
    rev_grow_avrg = fields.Float()  # compute
    rev_grow_weight = fields.Float()  # compute

    total_2 = fields.Float()  # compute
    rat_scale_2 = fields.Float()  #compute

    total_rat_scale = fields.Float() #compute





    @api.one
    @api.depends('work_ratio')
    def _get_work_score(self):
        self.work_score = self.work_ratio * 6.56

    @api.one
    @api.depends('equilty_ratio_asset')
    def _get_equilty_score_asset(self):
        self.equilty_score_asset = self.equilty_ratio_asset * 3.36

    @api.one
    @api.depends('ebit_ratio')
    def _get_ebit_score(self):
        self.ebit_score = self.ebit_ratio * 6.72

    @api.one
    @api.depends('equilty_ratio_liab')
    def _get_equilty_score_liab(self):
        self.equilty_score_liab = self.equilty_ratio_liab * 1.05

    @api.one
    @api.depends('work_score','equilty_score_asset','ebit_score','equilty_score_liab')
    def _get_total_score(self):
        self.tot_score = self.work_score + self.equilty_score_asset + self.ebit_score + self.equilty_score_liab


