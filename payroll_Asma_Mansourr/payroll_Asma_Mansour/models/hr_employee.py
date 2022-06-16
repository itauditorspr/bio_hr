# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee"

    categorie = fields.Selection([
        ('Cadre', 'Cadre'),
        ('Maitrise', 'Maitrise'),
        ('Agent ', 'Agent exécution')], string='Catégorie', groups="hr.group_hr_user", default='single', tracking=True)

    echelle = fields.Integer(string="Echelle", required=False)

    echlon = fields.Selection([
        ('E0', 'E0'),
        ('E1', 'E1'),
        ('E2', 'E2'),
        ('E3', 'E3'),
        ('E4', 'E4'),
        ('M1', 'M1'),
        ('M2', 'M2'),
        ('M3', 'M3'),
        ('M4', 'M4'),
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('C3', 'C3')], string='echlon', groups="hr.group_hr_user", default='single', tracking=True)

    salaire_de_base = fields.Char(string='Salaire de base selon la convention', compute='_compute_salaire_de_base')
    chef_de_famille = fields.Boolean(string='Chef de famille', default=False)
    soumis_aux_heures_sup = fields.Boolean(string='Soumis aux heures sup', default=False)

    matricule_cnss = fields.Char(
        string="Numéro CNSS", required=False,
    )

    num_chezemployeur = fields.Integer(
        string="Numero chez l\'employeur", required=False,
    )
    # slip_ids = fields.One2many(
    #     "hr.payslip", "employee_id", string="Payslips", readonly=True
    # )
    # payslip_count = fields.Integer(
    #     compute="_compute_payslip_count",
    #     string="Payslip Count",
    #     groups="l10n_tunisia_payroll.group_payroll_user",
    # )

    def _compute_payslip_count(self):
        for employee in self:
            employee.payslip_count = len(employee.slip_ids)

    @api.depends('echelle', 'echlon')
    def _compute_salaire_de_base(self):
        for record in self:
            if record.echlon == "E0" and record.echelle == 1:
                record.salaire_de_base = 594.95
            elif record.echlon == "E0" and record.echelle == 2:
                record.salaire_de_base = 595.439
            elif record.echlon == "E0" and record.echelle == 3:
                record.salaire_de_base = 595.967
            elif record.echlon == "E0" and record.echelle == 4:
                record.salaire_de_base = 596.504
            elif record.echlon == "E0" and record.echelle == 5:
                record.salaire_de_base = 597.074
            elif record.echlon == "E0" and record.echelle == 6:
                record.salaire_de_base = 597.673
            elif record.echlon == "E0" and record.echelle == 7:
                record.salaire_de_base = 598.302
            elif record.echlon == "E0" and record.echelle == 8:
                record.salaire_de_base = 598.962
            elif record.echlon == "E0" and record.echelle == 9:
                record.salaire_de_base = 601.828
            elif record.echlon == "E0" and record.echelle == 10:
                record.salaire_de_base = 604.445
            elif record.echlon == "E0" and record.echelle == 11:
                record.salaire_de_base = 607.194
            elif record.echlon == "E0" and record.echelle == 12:
                record.salaire_de_base = 610.146
            elif record.echlon == "E0" and record.echelle == 13:
                record.salaire_de_base = 616.197

            elif record.echlon == "E1" and record.echelle == 1:
                record.salaire_de_base = 600.636
            elif record.echlon == "E1" and record.echelle == 2:
                record.salaire_de_base = 601.247
            elif record.echlon == "E1" and record.echelle == 3:
                record.salaire_de_base = 601.857
            elif record.echlon == "E1" and record.echelle == 4:
                record.salaire_de_base = 602.539
            elif record.echlon == "E1" and record.echelle == 5:
                record.salaire_de_base = 603.265
            elif record.echlon == "E1" and record.echelle == 6:
                record.salaire_de_base = 604.007
            elif record.echlon == "E1" and record.echelle == 7:
                record.salaire_de_base = 606.562
            elif record.echlon == "E1" and record.echelle == 8:
                record.salaire_de_base = 609.164
            elif record.echlon == "E1" and record.echelle == 9:
                record.salaire_de_base = 611.956
            elif record.echlon == "E1" and record.echelle == 10:
                record.salaire_de_base = 614.879
            elif record.echlon == "E1" and record.echelle == 11:
                record.salaire_de_base = 617.975
            elif record.echlon == "E1" and record.echelle == 12:
                record.salaire_de_base = 624.438
            elif record.echlon == "E1" and record.echelle == 13:
                record.salaire_de_base = 628.148

            elif record.echlon == "E2" and record.echelle == 1:
                record.salaire_de_base = 606.321
            elif record.echlon == "E2" and record.echelle == 2:
                record.salaire_de_base = 607.127
            elif record.echlon == "E2" and record.echelle == 3:
                record.salaire_de_base = 607.974
            elif record.echlon == "E2" and record.echelle == 4:
                record.salaire_de_base = 608.863
            elif record.echlon == "E2" and record.echelle == 5:
                record.salaire_de_base = 610.800
            elif record.echlon == "E2" and record.echelle == 6:
                record.salaire_de_base = 614.444
            elif record.echlon == "E2" and record.echelle == 7:
                record.salaire_de_base = 616.175
            elif record.echlon == "E2" and record.echelle == 8:
                record.salaire_de_base = 619.066
            elif record.echlon == "E2" and record.echelle == 9:
                record.salaire_de_base = 622.314
            elif record.echlon == "E2" and record.echelle == 10:
                record.salaire_de_base = 626.544
            elif record.echlon == "E2" and record.echelle == 11:
                record.salaire_de_base = 632.125
            elif record.echlon == "E2" and record.echelle == 12:
                record.salaire_de_base = 635.640
            elif record.echlon == "E2" and record.echelle == 13:
                record.salaire_de_base = 639.262

            elif record.echlon == "E3" and record.echelle == 1:
                record.salaire_de_base = 612.014
            elif record.echlon == "E3" and record.echelle == 2:
                record.salaire_de_base = 613.174
            elif record.echlon == "E3" and record.echelle == 3:
                record.salaire_de_base = 614.629
            elif record.echlon == "E3" and record.echelle == 4:
                record.salaire_de_base = 617.224
            elif record.echlon == "E3" and record.echelle == 5:
                record.salaire_de_base = 619.948
            elif record.echlon == "E3" and record.echelle == 6:
                record.salaire_de_base = 622.744
            elif record.echlon == "E3" and record.echelle == 7:
                record.salaire_de_base = 625.526
            elif record.echlon == "E3" and record.echelle == 8:
                record.salaire_de_base = 631.346
            elif record.echlon == "E3" and record.echelle == 9:
                record.salaire_de_base = 634.595
            elif record.echlon == "E3" and record.echelle == 10:
                record.salaire_de_base = 638.002
            elif record.echlon == "E3" and record.echelle == 11:
                record.salaire_de_base = 641.581
            elif record.echlon == "E3" and record.echelle == 12:
                record.salaire_de_base = 645.338
            elif record.echlon == "E3" and record.echelle == 13:
                record.salaire_de_base = 649.283

            elif record.echlon == "E4" and record.echelle == 1:
                record.salaire_de_base = 617.696
            elif record.echlon == "E4" and record.echelle == 2:
                record.salaire_de_base = 620.368
            elif record.echlon == "E4" and record.echelle == 3:
                record.salaire_de_base = 622.753
            elif record.echlon == "E4" and record.echelle == 4:
                record.salaire_de_base = 625.257
            elif record.echlon == "E4" and record.echelle == 5:
                record.salaire_de_base = 628.885
            elif record.echlon == "E4" and record.echelle == 6:
                record.salaire_de_base = 630.840
            elif record.echlon == "E4" and record.echelle == 7:
                record.salaire_de_base = 636.731
            elif record.echlon == "E4" and record.echelle == 8:
                record.salaire_de_base = 640.049
            elif record.echlon == "E4" and record.echelle == 9:
                record.salaire_de_base = 643.532
            elif record.echlon == "E4" and record.echelle == 10:
                record.salaire_de_base = 647.189
            elif record.echlon == "E4" and record.echelle == 11:
                record.salaire_de_base = 651.028
            elif record.echlon == "E4" and record.echelle == 12:
                record.salaire_de_base = 655.061
            elif record.echlon == "E4" and record.echelle == 13:
                record.salaire_de_base = 659.293

            elif record.echlon == "M1" and record.echelle == 1:
                record.salaire_de_base = 693.032
            elif record.echlon == "M1" and record.echelle == 2:
                record.salaire_de_base = 698.860
            elif record.echlon == "M1" and record.echelle == 3:
                record.salaire_de_base = 702.108
            elif record.echlon == "M1" and record.echelle == 4:
                record.salaire_de_base = 705.519
            elif record.echlon == "M1" and record.echelle == 5:
                record.salaire_de_base = 709.101
            elif record.echlon == "M1" and record.echelle == 6:
                record.salaire_de_base = 712.861
            elif record.echlon == "M1" and record.echelle == 7:
                record.salaire_de_base = 716.810
            elif record.echlon == "M1" and record.echelle == 8:
                record.salaire_de_base = 720.957
            elif record.echlon == "M1" and record.echelle == 9:
                record.salaire_de_base = 725.311
            elif record.echlon == "M1" and record.echelle == 10:
                record.salaire_de_base = 729.882
            elif record.echlon == "M1" and record.echelle == 11:
                record.salaire_de_base = 737.414
            elif record.echlon == "M1" and record.echelle == 12:
                record.salaire_de_base = 742.454
            elif record.echlon == "M1" and record.echelle == 13:
                record.salaire_de_base = 747.746

            elif record.echlon == "M2" and record.echelle == 1:
                record.salaire_de_base = 710.492
            elif record.echlon == "M2" and record.echelle == 2:
                record.salaire_de_base = 713.868
            elif record.echlon == "M2" and record.echelle == 3:
                record.salaire_de_base = 717.413
            elif record.echlon == "M2" and record.echelle == 4:
                record.salaire_de_base = 721.134
            elif record.echlon == "M2" and record.echelle == 5:
                record.salaire_de_base = 725.042
            elif record.echlon == "M2" and record.echelle == 6:
                record.salaire_de_base = 729.244
            elif record.echlon == "M2" and record.echelle == 7:
                record.salaire_de_base = 733.452
            elif record.echlon == "M2" and record.echelle == 8:
                record.salaire_de_base = 737.976
            elif record.echlon == "M2" and record.echelle == 9:
                record.salaire_de_base = 745.458
            elif record.echlon == "M2" and record.echelle == 10:
                record.salaire_de_base = 750.445
            elif record.echlon == "M2" and record.echelle == 11:
                record.salaire_de_base = 755.682
            elif record.echlon == "M2" and record.echelle == 12:
                record.salaire_de_base = 761.179
            elif record.echlon == "M2" and record.echelle == 13:
                record.salaire_de_base = 766.952

            elif record.echlon == "M3" and record.echelle == 1:
                record.salaire_de_base = 797.186
            elif record.echlon == "M3" and record.echelle == 2:
                record.salaire_de_base = 802.808
            elif record.echlon == "M3" and record.echelle == 3:
                record.salaire_de_base = 808.721
            elif record.echlon == "M3" and record.echelle == 4:
                record.salaire_de_base = 817.656
            elif record.echlon == "M3" and record.echelle == 5:
                record.salaire_de_base = 824.169
            elif record.echlon == "M3" and record.echelle == 6:
                record.salaire_de_base = 831.008
            elif record.echlon == "M3" and record.echelle == 7:
                record.salaire_de_base = 838.188
            elif record.echlon == "M3" and record.echelle == 8:
                record.salaire_de_base = 845.728
            elif record.echlon == "M3" and record.echelle == 9:
                record.salaire_de_base = 853.644
            elif record.echlon == "M3" and record.echelle == 10:
                record.salaire_de_base = 861.957
            elif record.echlon == "M3" and record.echelle == 11:
                record.salaire_de_base = 870.488
            elif record.echlon == "M3" and record.echelle == 12:
                record.salaire_de_base = 879.850
            elif record.echlon == "M3" and record.echelle == 13:
                record.salaire_de_base = 889.472

            elif record.echlon == "M4" and record.echelle == 1:
                record.salaire_de_base = 840.972
            elif record.echlon == "M4" and record.echelle == 2:
                record.salaire_de_base = 847.662
            elif record.echlon == "M4" and record.echelle == 3:
                record.salaire_de_base = 854.686
            elif record.echlon == "M4" and record.echelle == 4:
                record.salaire_de_base = 862.062
            elif record.echlon == "M4" and record.echelle == 5:
                record.salaire_de_base = 869.805
            elif record.echlon == "M4" and record.echelle == 6:
                record.salaire_de_base = 877.937
            elif record.echlon == "M4" and record.echelle == 7:
                record.salaire_de_base = 886.474
            elif record.echlon == "M4" and record.echelle == 8:
                record.salaire_de_base = 895.439
            elif record.echlon == "M4" and record.echelle == 9:
                record.salaire_de_base = 904.852
            elif record.echlon == "M4" and record.echelle == 10:
                record.salaire_de_base = 914.735
            elif record.echlon == "M4" and record.echelle == 11:
                record.salaire_de_base = 925.112
            elif record.echlon == "M4" and record.echelle == 12:
                record.salaire_de_base = 936.008
            elif record.echlon == "M4" and record.echelle == 13:
                record.salaire_de_base = 947.449

            elif record.echlon == "C1" and record.echelle == 1:
                record.salaire_de_base = 911.943
            elif record.echlon == "C1" and record.echelle == 2:
                record.salaire_de_base = 919.469
            elif record.echlon == "C1" and record.echelle == 3:
                record.salaire_de_base = 927.371
            elif record.echlon == "C1" and record.echelle == 4:
                record.salaire_de_base = 935.667
            elif record.echlon == "C1" and record.echelle == 5:
                record.salaire_de_base = 944.379
            elif record.echlon == "C1" and record.echelle == 6:
                record.salaire_de_base = 953.526
            elif record.echlon == "C1" and record.echelle == 7:
                record.salaire_de_base = 963.130
            elif record.echlon == "C1" and record.echelle == 8:
                record.salaire_de_base = 973.216
            elif record.echlon == "C1" and record.echelle == 9:
                record.salaire_de_base = 983.805
            elif record.echlon == "C1" and record.echelle == 10:
                record.salaire_de_base = 994.923
            elif record.echlon == "C1" and record.echelle == 11:
                record.salaire_de_base = 1006.599
            elif record.echlon == "C1" and record.echelle == 12:
                record.salaire_de_base = 1018.857
            elif record.echlon == "C1" and record.echelle == 13:
                record.salaire_de_base = 1031.769

            elif record.echlon == "C2" and record.echelle == 1:
                record.salaire_de_base = 943.615
            elif record.echlon == "C2" and record.echelle == 2:
                record.salaire_de_base = 952.184
            elif record.echlon == "C2" and record.echelle == 3:
                record.salaire_de_base = 960.965
            elif record.echlon == "C2" and record.echelle == 4:
                record.salaire_de_base = 970.183
            elif record.echlon == "C2" and record.echelle == 5:
                record.salaire_de_base = 979.865
            elif record.echlon == "C2" and record.echelle == 6:
                record.salaire_de_base = 990.028
            elif record.echlon == "C2" and record.echelle == 7:
                record.salaire_de_base = 1000.701
            elif record.echlon == "C2" and record.echelle == 8:
                record.salaire_de_base = 1011.906
            elif record.echlon == "C2" and record.echelle == 9:
                record.salaire_de_base = 1023.673
            elif record.echlon == "C2" and record.echelle == 10:
                record.salaire_de_base = 1036.026
            elif record.echlon == "C2" and record.echelle == 11:
                record.salaire_de_base = 1048.998
            elif record.echlon == "C2" and record.echelle == 12:
                record.salaire_de_base = 1062.619
            elif record.echlon == "C2" and record.echelle == 13:
                record.salaire_de_base = 1076.921

            elif record.echlon == "C3" and record.echelle == 1:
                record.salaire_de_base = 995.609
            elif record.echlon == "C3" and record.echelle == 2:
                record.salaire_de_base = 1005.366
            elif record.echlon == "C3" and record.echelle == 3:
                record.salaire_de_base = 1015.609
            elif record.echlon == "C3" and record.echelle == 4:
                record.salaire_de_base = 1026.364
            elif record.echlon == "C3" and record.echelle == 5:
                record.salaire_de_base = 1037.658
            elif record.echlon == "C3" and record.echelle == 6:
                record.salaire_de_base = 1049.515
            elif record.echlon == "C3" and record.echelle == 7:
                record.salaire_de_base = 1061.967
            elif record.echlon == "C3" and record.echelle == 8:
                record.salaire_de_base = 1075.040
            elif record.echlon == "C3" and record.echelle == 9:
                record.salaire_de_base = 1088.767
            elif record.echlon == "C3" and record.echelle == 10:
                record.salaire_de_base = 1103.180
            elif record.echlon == "C3" and record.echelle == 11:
                record.salaire_de_base = 1114.185
            elif record.echlon == "C3" and record.echelle == 12:
                record.salaire_de_base = 1134.205
            elif record.echlon == "C3" and record.echelle == 13:
                record.salaire_de_base = 1150.891
            else:
                record.salaire_de_base = 0

    # """
    # NB: Any field only available on the model hr.employee (i.e. not on the
    # hr.employee.public model) should have `groups="hr.group_hr_user"` on its
    # definition to avoid being prefetched when the user hasn't access to the
    # hr.employee model. Indeed, the prefetch loads the data for all the fields
    # that are available according to the group defined on them.
    # """
    # _name = "hr.employee"
    # _description = "Employee"
    # _order = 'name'

    # _mail_post_access = 'read'

    # resource and user
    # required on the resource, make sure required="True" set in the view
    # name = fields.Char(string="Employee Name", related='resource_id.name', store=True, readonly=False, tracking=True)
    # user_id = fields.Many2one('res.users', 'User', related='resource_id.user_id', store=True, readonly=False)
    # user_partner_id = fields.Many2one(related='user_id.partner_id', related_sudo=False, string="User's partner")
    # active = fields.Boolean('Active', related='resource_id.active', default=True, store=True, readonly=False)
    # company_id = fields.Many2one('res.company',required=True)
    # company_country_id = fields.Many2one('res.country', 'Company Country', related='company_id.country_id', readonly=True)
    # company_country_code = fields.Char(related='company_country_id.code', readonly=True)
    # # private partner
    # address_home_id = fields.Many2one(
    #     'res.partner', 'Address', help='Enter here the private address of the employee, not the one linked to your company.',
    #     groups="hr.group_hr_user", tracking=True,
    #     domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    # is_address_home_a_company = fields.Boolean(
    #     'The employee address has a company linked',
    #     compute='_compute_is_address_home_a_company',
    # )
    # private_email = fields.Char(related='address_home_id.email', string="Private Email", groups="hr.group_hr_user")
    # lang = fields.Selection(related='address_home_id.lang', string="Lang", groups="hr.group_hr_user", readonly=False)
    # country_id = fields.Many2one(
    #     'res.country', 'Nationality (Country)', groups="hr.group_hr_user", tracking=True)

    # marital = fields.Selection([
    #     ('single', 'Single'),
    #     ('married', 'Married'),
    #     ('cohabitant', 'Legal Cohabitant'),
    #     ('widower', 'Widower'),
    #     ('divorced', 'Divorced')
    # ], string='Marital Status', groups="hr.group_hr_user", default='single', tracking=True)
    # spouse_complete_name = fields.Char(string="Spouse Complete Name", groups="hr.group_hr_user", tracking=True)
    # spouse_birthdate = fields.Date(string="Spouse Birthdate", groups="hr.group_hr_user", tracking=True)
    # children = fields.Integer(string='Number of Children', groups="hr.group_hr_user", tracking=True)
    # place_of_birth = fields.Char('Place of Birth', groups="hr.group_hr_user", tracking=True)
    # country_of_birth = fields.Many2one('res.country', string="Country of Birth", groups="hr.group_hr_user", tracking=True)
    # birthday = fields.Date('Date of Birth', groups="hr.group_hr_user", tracking=True)
    # ssnid = fields.Char('SSN No', help='Social Security Number', groups="hr.group_hr_user", tracking=True)
    # sinid = fields.Char('SIN No', help='Social Insurance Number', groups="hr.group_hr_user", tracking=True)
    # identification_id = fields.Char(string='Identification No', groups="hr.group_hr_user", tracking=True)
    # passport_id = fields.Char('Passport No', groups="hr.group_hr_user", tracking=True)
    # bank_account_id = fields.Many2one(
    #     'res.partner.bank', 'Bank Account Number',
    #     domain="[('partner_id', '=', address_home_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    #     groups="hr.group_hr_user",
    #     tracking=True,
    #     help='Employee bank salary account')
    # permit_no = fields.Char('Work Permit No', groups="hr.group_hr_user", tracking=True)
    # visa_no = fields.Char('Visa No', groups="hr.group_hr_user", tracking=True)
    # visa_expire = fields.Date('Visa Expire Date', groups="hr.group_hr_user", tracking=True)
    # work_permit_expiration_date = fields.Date('Work Permit Expiration Date', groups="hr.group_hr_user", tracking=True)
    # has_work_permit = fields.Binary(string="Work Permit", groups="hr.group_hr_user", tracking=True)
    # work_permit_scheduled_activity = fields.Boolean(default=False, groups="hr.group_hr_user")
    # additional_note = fields.Text(string='Additional Note', groups="hr.group_hr_user", tracking=True)
    # certificate = fields.Selection([
    #     ('graduate', 'Graduate'),
    #     ('bachelor', 'Bachelor'),
    #     ('master', 'Master'),
    #     ('doctor', 'Doctor'),
    #     ('other', 'Other'),
    # ], 'Certificate Level', default='other', groups="hr.group_hr_user", tracking=True)
    # study_field = fields.Char("Field of Study", groups="hr.group_hr_user", tracking=True)
    # study_school = fields.Char("School", groups="hr.group_hr_user", tracking=True)
    # emergency_contact = fields.Char("Emergency Contact", groups="hr.group_hr_user", tracking=True)
    # emergency_phone = fields.Char("Emergency Phone", groups="hr.group_hr_user", tracking=True)
    # km_home_work = fields.Integer(string="Home-Work Distance", groups="hr.group_hr_user", tracking=True)
    #
    # job_id = fields.Many2one(tracking=True)
    # phone = fields.Char(related='address_home_id.phone', related_sudo=False, readonly=False, string="Private Phone", groups="hr.group_hr_user")
    # # employee in company
    # child_ids = fields.One2many('hr.employee', 'parent_id', string='Direct subordinates')
    # category_ids = fields.Many2many(
    #     'hr.employee.category', 'employee_category_rel',
    #     'emp_id', 'category_id', groups="hr.group_hr_manager",
    #     string='Tags')
    # # misc
    # notes = fields.Text('Notes', groups="hr.group_hr_user")
    # color = fields.Integer('Color Index', default=0)
    # barcode = fields.Char(string="Badge ID", help="ID used for employee identification.", groups="hr.group_hr_user", copy=False)
    # pin = fields.Char(string="PIN", groups="hr.group_hr_user", copy=False,
    #     help="PIN used to Check In/Out in the Kiosk Mode of the Attendance application (if enabled in Configuration) and to change the cashier in the Point of Sale application.")
    # departure_reason_id = fields.Many2one("hr.departure.reason", string="Departure Reason", groups="hr.group_hr_user",
    #                                       copy=False, tracking=True, ondelete='restrict')
    # departure_description = fields.Html(string="Additional Information", groups="hr.group_hr_user", copy=False, tracking=True)
    # departure_date = fields.Date(string="Departure Date", groups="hr.group_hr_user", copy=False, tracking=True)
    # message_main_attachment_id = fields.Many2one(groups="hr.group_hr_user")
    # id_card = fields.Binary(string="ID Card Copy", groups="hr.group_hr_user")
    # driving_license = fields.Binary(string="Driving License", groups="hr.group_hr_user")
    #
    # _sql_constraints = [
    #     ('barcode_uniq', 'unique (barcode)', "The Badge ID must be unique, this one is already assigned to another employee."),
    #     ('user_uniq', 'unique (user_id, company_id)', "A user cannot be linked to multiple employees in the same company.")
    # ]
    #
    # @api.depends('name', 'user_id.avatar_1920', 'image_1920')
    # def _compute_avatar_1920(self):
    #     super()._compute_avatar_1920()
    #
    # @api.depends('name', 'user_id.avatar_1024', 'image_1024')
    # def _compute_avatar_1024(self):
    #     super()._compute_avatar_1024()
    #
    # @api.depends('name', 'user_id.avatar_512', 'image_512')
    # def _compute_avatar_512(self):
    #     super()._compute_avatar_512()
    #
    # @api.depends('name', 'user_id.avatar_256', 'image_256')
    # def _compute_avatar_256(self):
    #     super()._compute_avatar_256()
    #
    # @api.depends('name', 'user_id.avatar_128', 'image_128')
    # def _compute_avatar_128(self):
    #     super()._compute_avatar_128()
    #
    # def _compute_avatar(self, avatar_field, image_field):
    #     for employee in self:
    #         avatar = employee._origin[image_field]
    #         if not avatar:
    #             if employee.user_id:
    #                 avatar = employee.user_id[avatar_field]
    #             else:
    #                 avatar = employee._avatar_get_placeholder()
    #         employee[avatar_field] = avatar
    #
    # def name_get(self):
    #     if self.check_access_rights('read', raise_exception=False):
    #         return super(HrEmployeePrivate, self).name_get()
    #     return self.env['hr.employee.public'].browse(self.ids).name_get()
    #
    # def _read(self, fields):
    #     if self.check_access_rights('read', raise_exception=False):
    #         return super(HrEmployeePrivate, self)._read(fields)
    #
    #     res = self.env['hr.employee.public'].browse(self.ids).read(fields)
    #     for r in res:
    #         record = self.browse(r['id'])
    #         record._update_cache({k:v for k,v in r.items() if k in fields}, validate=False)
    #
    # @api.model
    # def _cron_check_work_permit_validity(self):
    #     # Called by a cron
    #     # Schedule an activity 1 month before the work permit expires
    #     outdated_days = fields.Date.today() + relativedelta(months=+1)
    #     nearly_expired_work_permits = self.search([('work_permit_scheduled_activity', '=', False), ('work_permit_expiration_date', '<', outdated_days)])
    #     employees_scheduled = self.env['hr.employee']
    #     for employee in nearly_expired_work_permits.filtered(lambda employee: employee.parent_id):
    #         responsible_user_id = employee.parent_id.user_id.id
    #         if responsible_user_id:
    #             employees_scheduled |= employee
    #             lang = self.env['res.partner'].browse(responsible_user_id).lang
    #             formated_date = format_date(employee.env, employee.work_permit_expiration_date, date_format="dd MMMM y", lang_code=lang)
    #             employee.activity_schedule(
    #                 'mail.mail_activity_data_todo',
    #                 note=_('The work permit of %(employee)s expires at %(date)s.',
    #                     employee=employee.name,
    #                     date=formated_date),
    #                 user_id=responsible_user_id)
    #     employees_scheduled.write({'work_permit_scheduled_activity': True})
    #
    # def read(self, fields, load='_classic_read'):
    #     if self.check_access_rights('read', raise_exception=False):
    #         return super(HrEmployeePrivate, self).read(fields, load=load)
    #     private_fields = set(fields).difference(self.env['hr.employee.public']._fields.keys())
    #     if private_fields:
    #         raise AccessError(_('The fields "%s" you try to read is not available on the public employee profile.') % (','.join(private_fields)))
    #     return self.env['hr.employee.public'].browse(self.ids).read(fields, load=load)
    #
    # @api.model
    # def load_views(self, views, options=None):
    #     if self.check_access_rights('read', raise_exception=False):
    #         return super(HrEmployeePrivate, self).load_views(views, options=options)
    #     return self.env['hr.employee.public'].load_views(views, options=options)
    #
    # @api.model
    # def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
    #     """
    #         We override the _search because it is the method that checks the access rights
    #         This is correct to override the _search. That way we enforce the fact that calling
    #         search on an hr.employee returns a hr.employee recordset, even if you don't have access
    #         to this model, as the result of _search (the ids of the public employees) is to be
    #         browsed on the hr.employee model. This can be trusted as the ids of the public
    #         employees exactly match the ids of the related hr.employee.
    #     """
    #     if self.check_access_rights('read', raise_exception=False):
    #         return super(HrEmployeePrivate, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
    #     ids = self.env['hr.employee.public']._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
    #     if not count and isinstance(ids, Query):
    #         # the result is expected from this table, so we should link tables
    #         ids = super(HrEmployeePrivate, self.sudo())._search([('id', 'in', ids)])
    #     return ids
    #
    # def get_formview_id(self, access_uid=None):
    #     """ Override this method in order to redirect many2one towards the right model depending on access_uid """
    #     if access_uid:
    #         self_sudo = self.with_user(access_uid)
    #     else:
    #         self_sudo = self
    #
    #     if self_sudo.check_access_rights('read', raise_exception=False):
    #         return super(HrEmployeePrivate, self).get_formview_id(access_uid=access_uid)
    #     # Hardcode the form view for public employee
    #     return self.env.ref('hr.hr_employee_public_view_form').id
    #
    # def get_formview_action(self, access_uid=None):
    #     """ Override this method in order to redirect many2one towards the right model depending on access_uid """
    #     res = super(HrEmployeePrivate, self).get_formview_action(access_uid=access_uid)
    #     if access_uid:
    #         self_sudo = self.with_user(access_uid)
    #     else:
    #         self_sudo = self
    #
    #     if not self_sudo.check_access_rights('read', raise_exception=False):
    #         res['res_model'] = 'hr.employee.public'
    #
    #     return res
    #
    # @api.constrains('pin')
    # def _verify_pin(self):
    #     for employee in self:
    #         if employee.pin and not employee.pin.isdigit():
    #             raise ValidationError(_("The PIN must be a sequence of digits."))
    #
    # @api.onchange('user_id')
    # def _onchange_user(self):
    #     if self.user_id:
    #         self.update(self._sync_user(self.user_id, (bool(self.image_1920))))
    #         if not self.name:
    #             self.name = self.user_id.name
    #
    # @api.onchange('resource_calendar_id')
    # def _onchange_timezone(self):
    #     if self.resource_calendar_id and not self.tz:
    #         self.tz = self.resource_calendar_id.tz
    #
    # def _sync_user(self, user, employee_has_image=False):
    #     vals = dict(
    #         work_email=user.email,
    #         user_id=user.id,
    #     )
    #     if not employee_has_image:
    #         vals['image_1920'] = user.image_1920
    #     if user.tz:
    #         vals['tz'] = user.tz
    #     return vals
    #
    # @api.model
    # def create(self, vals):
    #     if vals.get('user_id'):
    #         user = self.env['res.users'].browse(vals['user_id'])
    #         vals.update(self._sync_user(user, bool(vals.get('image_1920'))))
    #         vals['name'] = vals.get('name', user.name)
    #     employee = super(HrEmployeePrivate, self).create(vals)
    #     if employee.department_id:
    #         self.env['mail.channel'].sudo().search([
    #             ('subscription_department_ids', 'in', employee.department_id.id)
    #         ])._subscribe_users_automatically()
    #     # Launch onboarding plans
    #     url = '/web#%s' % url_encode({
    #         'action': 'hr.plan_wizard_action',
    #         'active_id': employee.id,
    #         'active_model': 'hr.employee',
    #         'menu_id': self.env.ref('hr.menu_hr_root').id,
    #     })
    #     employee._message_log(body=_('<b>Congratulations!</b> May I recommend you to setup an <a href="%s">onboarding plan?</a>') % (url))
    #     return employee
    #
    # def write(self, vals):
    #     if 'address_home_id' in vals:
    #         account_id = vals.get('bank_account_id') or self.bank_account_id.id
    #         if account_id:
    #             self.env['res.partner.bank'].browse(account_id).partner_id = vals['address_home_id']
    #     if vals.get('user_id'):
    #         # Update the profile pictures with user, except if provided
    #         vals.update(self._sync_user(self.env['res.users'].browse(vals['user_id']),
    #                                     (bool(self.image_1920))))
    #     if 'work_permit_expiration_date' in vals:
    #         vals['work_permit_scheduled_activity'] = False
    #     res = super(HrEmployeePrivate, self).write(vals)
    #     if vals.get('department_id') or vals.get('user_id'):
    #         department_id = vals['department_id'] if vals.get('department_id') else self[:1].department_id.id
    #         # When added to a department or changing user, subscribe to the channels auto-subscribed by department
    #         self.env['mail.channel'].sudo().search([
    #             ('subscription_department_ids', 'in', department_id)
    #         ])._subscribe_users_automatically()
    #     return res
    #
    # def unlink(self):
    #     resources = self.mapped('resource_id')
    #     super(HrEmployeePrivate, self).unlink()
    #     return resources.unlink()
    #
    # def _get_employee_m2o_to_empty_on_archived_employees(self):
    #     return ['parent_id', 'coach_id']
    #
    # def _get_user_m2o_to_empty_on_archived_employees(self):
    #     return []
    #
    # def toggle_active(self):
    #     res = super(HrEmployeePrivate, self).toggle_active()
    #     unarchived_employees = self.filtered(lambda employee: employee.active)
    #     unarchived_employees.write({
    #         'departure_reason_id': False,
    #         'departure_description': False,
    #         'departure_date': False
    #     })
    #     archived_addresses = unarchived_employees.mapped('address_home_id').filtered(lambda addr: not addr.active)
    #     archived_addresses.toggle_active()
    #
    #     archived_employees = self.filtered(lambda e: not e.active)
    #     if archived_employees:
    #         # Empty links to this employees (example: manager, coach, time off responsible, ...)
    #         employee_fields_to_empty = self._get_employee_m2o_to_empty_on_archived_employees()
    #         user_fields_to_empty = self._get_user_m2o_to_empty_on_archived_employees()
    #         employee_domain = [[(field, 'in', archived_employees.ids)] for field in employee_fields_to_empty]
    #         user_domain = [[(field, 'in', archived_employees.user_id.ids) for field in user_fields_to_empty]]
    #         employees = self.env['hr.employee'].search(expression.OR(employee_domain + user_domain))
    #         for employee in employees:
    #             for field in employee_fields_to_empty:
    #                 if employee[field] in archived_employees:
    #                     employee[field] = False
    #             for field in user_fields_to_empty:
    #                 if employee[field] in archived_employees.user_id:
    #                     employee[field] = False
    #
    #     if len(self) == 1 and not self.active and not self.env.context.get('no_wizard', False):
    #         return {
    #             'type': 'ir.actions.act_window',
    #             'name': _('Register Departure'),
    #             'res_model': 'hr.departure.wizard',
    #             'view_mode': 'form',
    #             'target': 'new',
    #             'context': {'active_id': self.id},
    #             'views': [[False, 'form']]
    #         }
    #     return res
    #
    # @api.onchange('company_id')
    # def _onchange_company_id(self):
    #     if self._origin:
    #         return {'warning': {
    #             'title': _("Warning"),
    #             'message': _("To avoid multi company issues (loosing the access to your previous contracts, leaves, ...), you should create another employee in the new company instead.")
    #         }}
    #
    # def generate_random_barcode(self):
    #     for employee in self:
    #         employee.barcode = '041'+"".join(choice(digits) for i in range(9))
    #
    # @api.depends('address_home_id.parent_id')
    # def _compute_is_address_home_a_company(self):
    #     """Checks that chosen address (res.partner) is not linked to a company.
    #     """
    #     for employee in self:
    #         try:
    #             employee.is_address_home_a_company = employee.address_home_id.parent_id.id is not False
    #         except AccessError:
    #             employee.is_address_home_a_company = False
    #
    # def _get_tz(self):
    #     # Finds the first valid timezone in his tz, his work hours tz,
    #     #  the company calendar tz or UTC and returns it as a string
    #     self.ensure_one()
    #     return self.tz or\
    #            self.resource_calendar_id.tz or\
    #            self.company_id.resource_calendar_id.tz or\
    #            'UTC'
    #
    # def _get_tz_batch(self):
    #     # Finds the first valid timezone in his tz, his work hours tz,
    #     #  the company calendar tz or UTC
    #     # Returns a dict {employee_id: tz}
    #     return {emp.id: emp._get_tz() for emp in self}
    #
    # # ---------------------------------------------------------
    # # Business Methods
    # # ---------------------------------------------------------
    #
    # @api.model
    # def get_import_templates(self):
    #     return [{
    #         'label': _('Import Template for Employees'),
    #         'template': '/hr/static/xls/hr_employee.xls'
    #     }]
    #
    # def _post_author(self):
    #     """
    #     When a user updates his own employee's data, all operations are performed
    #     by super user. However, tracking messages should not be posted as OdooBot
    #     but as the actual user.
    #     This method is used in the overrides of `_message_log` and `message_post`
    #     to post messages as the correct user.
    #     """
    #     real_user = self.env.context.get('binary_field_real_user')
    #     if self.env.is_superuser() and real_user:
    #         self = self.with_user(real_user)
    #     return self
    #
    # def _get_unusual_days(self, date_from, date_to=None):
    #     # Checking the calendar directly allows to not grey out the leaves taken
    #     # by the employee
    #     # Prevents a traceback when loading calendar views and no employee is linked to the user.
    #     if not self:
    #         return {}
    #     self.ensure_one()
    #     calendar = self.resource_calendar_id
    #     if not calendar:
    #         return {}
    #     dfrom = datetime.combine(fields.Date.from_string(date_from), time.min).replace(tzinfo=pytz.UTC)
    #     dto = datetime.combine(fields.Date.from_string(date_to), time.max).replace(tzinfo=pytz.UTC)
    #
    #     works = {d[0].date() for d in calendar._work_intervals_batch(dfrom, dto)[False]}
    #     return {fields.Date.to_string(day.date()): (day.date() not in works) for day in rrule(DAILY, dfrom, until=dto)}
    #
    # # ---------------------------------------------------------
    # # Messaging
    # # ---------------------------------------------------------
    #
    # def _message_log(self, **kwargs):
    #     return super(HrEmployeePrivate, self._post_author())._message_log(**kwargs)
    #
    # @api.returns('mail.message', lambda value: value.id)
    # def message_post(self, **kwargs):
    #     return super(HrEmployeePrivate, self._post_author()).message_post(**kwargs)
    #
    # def _sms_get_partner_fields(self):
    #     return ['user_partner_id']
    #
    # def _sms_get_number_fields(self):
    #     return ['mobile_phone']
    #
