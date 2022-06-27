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
                record.salaire_de_base = 633.622
            elif record.echlon == "E0" and record.echelle == 2:
                record.salaire_de_base = 634.110
            elif record.echlon == "E0" and record.echelle == 3:
                record.salaire_de_base = 634.638
            elif record.echlon == "E0" and record.echelle == 4:
                record.salaire_de_base = 635.175
            elif record.echlon == "E0" and record.echelle == 5:
                record.salaire_de_base = 635.745
            elif record.echlon == "E0" and record.echelle == 6:
                record.salaire_de_base = 636.344
            elif record.echlon == "E0" and record.echelle == 7:
                record.salaire_de_base = 636.973
            elif record.echlon == "E0" and record.echelle == 8:
                record.salaire_de_base = 637.633
            elif record.echlon == "E0" and record.echelle == 9:
                record.salaire_de_base = 640.499
            elif record.echlon == "E0" and record.echelle == 10:
                record.salaire_de_base = 643.116
            elif record.echlon == "E0" and record.echelle == 11:
                record.salaire_de_base = 645.865
            elif record.echlon == "E0" and record.echelle == 12:
                record.salaire_de_base = 648.817
            elif record.echlon == "E0" and record.echelle == 13:
                record.salaire_de_base = 654.868

            elif record.echlon == "E1" and record.echelle == 1:
                record.salaire_de_base = 639.677
            elif record.echlon == "E1" and record.echelle == 2:
                record.salaire_de_base = 640.288
            elif record.echlon == "E1" and record.echelle == 3:
                record.salaire_de_base = 640.898
            elif record.echlon == "E1" and record.echelle == 4:
                record.salaire_de_base = 641.580
            elif record.echlon == "E1" and record.echelle == 5:
                record.salaire_de_base = 642.306
            elif record.echlon == "E1" and record.echelle == 6:
                record.salaire_de_base = 643.048
            elif record.echlon == "E1" and record.echelle == 7:
                record.salaire_de_base = 645.603
            elif record.echlon == "E1" and record.echelle == 8:
                record.salaire_de_base = 648.235
            elif record.echlon == "E1" and record.echelle == 9:
                record.salaire_de_base = 650.997
            elif record.echlon == "E1" and record.echelle == 10:
                record.salaire_de_base = 653.920
            elif record.echlon == "E1" and record.echelle == 11:
                record.salaire_de_base = 657.016
            elif record.echlon == "E1" and record.echelle == 12:
                record.salaire_de_base = 663.479
            elif record.echlon == "E1" and record.echelle == 13:
                record.salaire_de_base = 6667.189

            elif record.echlon == "E2" and record.echelle == 1:
                record.salaire_de_base = 645.732
            elif record.echlon == "E2" and record.echelle == 2:
                record.salaire_de_base = 646.538
            elif record.echlon == "E2" and record.echelle == 3:
                record.salaire_de_base = 647.385
            elif record.echlon == "E2" and record.echelle == 4:
                record.salaire_de_base = 648.274
            elif record.echlon == "E2" and record.echelle == 5:
                record.salaire_de_base = 650.211
            elif record.echlon == "E2" and record.echelle == 6:
                record.salaire_de_base = 653.855
            elif record.echlon == "E2" and record.echelle == 7:
                record.salaire_de_base = 655.586
            elif record.echlon == "E2" and record.echelle == 8:
                record.salaire_de_base = 658.477
            elif record.echlon == "E2" and record.echelle == 9:
                record.salaire_de_base = 661.725
            elif record.echlon == "E2" and record.echelle == 10:
                record.salaire_de_base = 665.955
            elif record.echlon == "E2" and record.echelle == 11:
                record.salaire_de_base = 671.536
            elif record.echlon == "E2" and record.echelle == 12:
                record.salaire_de_base = 675.051
            elif record.echlon == "E2" and record.echelle == 13:
                record.salaire_de_base = 678.673

            elif record.echlon == "E3" and record.echelle == 1:
                record.salaire_de_base = 651.795
            elif record.echlon == "E3" and record.echelle == 2:
                record.salaire_de_base = 652.955
            elif record.echlon == "E3" and record.echelle == 3:
                record.salaire_de_base = 654.410
            elif record.echlon == "E3" and record.echelle == 4:
                record.salaire_de_base = 657.005
            elif record.echlon == "E3" and record.echelle == 5:
                record.salaire_de_base = 659.729
            elif record.echlon == "E3" and record.echelle == 6:
                record.salaire_de_base = 662.525
            elif record.echlon == "E3" and record.echelle == 7:
                record.salaire_de_base = 665.307
            elif record.echlon == "E3" and record.echelle == 8:
                record.salaire_de_base = 671.127
            elif record.echlon == "E3" and record.echelle == 9:
                record.salaire_de_base = 674.376
            elif record.echlon == "E3" and record.echelle == 10:
                record.salaire_de_base = 677.783
            elif record.echlon == "E3" and record.echelle == 11:
                record.salaire_de_base = 681.362
            elif record.echlon == "E3" and record.echelle == 12:
                record.salaire_de_base = 685.119
            elif record.echlon == "E3" and record.echelle == 13:
                record.salaire_de_base = 689.064

            elif record.echlon == "E4" and record.echelle == 1:
                record.salaire_de_base = 657.847
            elif record.echlon == "E4" and record.echelle == 2:
                record.salaire_de_base = 660.519
            elif record.echlon == "E4" and record.echelle == 3:
                record.salaire_de_base = 662.904
            elif record.echlon == "E4" and record.echelle == 4:
                record.salaire_de_base = 665.408
            elif record.echlon == "E4" and record.echelle == 5:
                record.salaire_de_base = 669.036
            elif record.echlon == "E4" and record.echelle == 6:
                record.salaire_de_base = 670.991
            elif record.echlon == "E4" and record.echelle == 7:
                record.salaire_de_base = 676.882
            elif record.echlon == "E4" and record.echelle == 8:
                record.salaire_de_base = 680.200
            elif record.echlon == "E4" and record.echelle == 9:
                record.salaire_de_base = 683.683
            elif record.echlon == "E4" and record.echelle == 10:
                record.salaire_de_base = 687.340
            elif record.echlon == "E4" and record.echelle == 11:
                record.salaire_de_base = 691.179
            elif record.echlon == "E4" and record.echelle == 12:
                record.salaire_de_base = 695.212
            elif record.echlon == "E4" and record.echelle == 13:
                record.salaire_de_base = 699.444

            elif record.echlon == "M1" and record.echelle == 1:
                record.salaire_de_base = 738.080
            elif record.echlon == "M1" and record.echelle == 2:
                record.salaire_de_base = 743.908
            elif record.echlon == "M1" and record.echelle == 3:
                record.salaire_de_base = 747.156
            elif record.echlon == "M1" and record.echelle == 4:
                record.salaire_de_base = 750.567
            elif record.echlon == "M1" and record.echelle == 5:
                record.salaire_de_base = 754.149
            elif record.echlon == "M1" and record.echelle == 6:
                record.salaire_de_base = 757.909
            elif record.echlon == "M1" and record.echelle == 7:
                record.salaire_de_base = 761.858
            elif record.echlon == "M1" and record.echelle == 8:
                record.salaire_de_base = 766.005
            elif record.echlon == "M1" and record.echelle == 9:
                record.salaire_de_base = 770.359
            elif record.echlon == "M1" and record.echelle == 10:
                record.salaire_de_base = 774.930
            elif record.echlon == "M1" and record.echelle == 11:
                record.salaire_de_base = 782.462
            elif record.echlon == "M1" and record.echelle == 12:
                record.salaire_de_base = 787.502
            elif record.echlon == "M1" and record.echelle == 13:
                record.salaire_de_base = 792.794

            elif record.echlon == "M2" and record.echelle == 1:
                record.salaire_de_base = 756.674
            elif record.echlon == "M2" and record.echelle == 2:
                record.salaire_de_base = 760.050
            elif record.echlon == "M2" and record.echelle == 3:
                record.salaire_de_base = 763.595
            elif record.echlon == "M2" and record.echelle == 4:
                record.salaire_de_base = 767.316
            elif record.echlon == "M2" and record.echelle == 5:
                record.salaire_de_base = 771.224
            elif record.echlon == "M2" and record.echelle == 6:
                record.salaire_de_base = 775.426
            elif record.echlon == "M2" and record.echelle == 7:
                record.salaire_de_base = 779.634
            elif record.echlon == "M2" and record.echelle == 8:
                record.salaire_de_base = 784.158
            elif record.echlon == "M2" and record.echelle == 9:
                record.salaire_de_base = 791.640
            elif record.echlon == "M2" and record.echelle == 10:
                record.salaire_de_base = 796.627
            elif record.echlon == "M2" and record.echelle == 11:
                record.salaire_de_base = 801.864
            elif record.echlon == "M2" and record.echelle == 12:
                record.salaire_de_base = 807.361
            elif record.echlon == "M2" and record.echelle == 13:
                record.salaire_de_base = 813.134

            elif record.echlon == "M3" and record.echelle == 1:
                record.salaire_de_base = 849.003
            elif record.echlon == "M3" and record.echelle == 2:
                record.salaire_de_base = 854.625
            elif record.echlon == "M3" and record.echelle == 3:
                record.salaire_de_base = 860.538
            elif record.echlon == "M3" and record.echelle == 4:
                record.salaire_de_base = 869.473
            elif record.echlon == "M3" and record.echelle == 5:
                record.salaire_de_base = 875.986
            elif record.echlon == "M3" and record.echelle == 6:
                record.salaire_de_base = 882.825
            elif record.echlon == "M3" and record.echelle == 7:
                record.salaire_de_base = 890.005
            elif record.echlon == "M3" and record.echelle == 8:
                record.salaire_de_base = 897.545
            elif record.echlon == "M3" and record.echelle == 9:
                record.salaire_de_base = 905.461
            elif record.echlon == "M3" and record.echelle == 10:
                record.salaire_de_base = 913.774
            elif record.echlon == "M3" and record.echelle == 11:
                record.salaire_de_base = 922.305
            elif record.echlon == "M3" and record.echelle == 12:
                record.salaire_de_base = 931.667
            elif record.echlon == "M3" and record.echelle == 13:
                record.salaire_de_base = 941.289

            elif record.echlon == "M4" and record.echelle == 1:
                record.salaire_de_base = 895.635
            elif record.echlon == "M4" and record.echelle == 2:
                record.salaire_de_base = 902.325
            elif record.echlon == "M4" and record.echelle == 3:
                record.salaire_de_base = 909.349
            elif record.echlon == "M4" and record.echelle == 4:
                record.salaire_de_base = 916.725
            elif record.echlon == "M4" and record.echelle == 5:
                record.salaire_de_base = 924.468
            elif record.echlon == "M4" and record.echelle == 6:
                record.salaire_de_base = 932.600
            elif record.echlon == "M4" and record.echelle == 7:
                record.salaire_de_base = 941.137
            elif record.echlon == "M4" and record.echelle == 8:
                record.salaire_de_base = 950.102
            elif record.echlon == "M4" and record.echelle == 9:
                record.salaire_de_base = 959.515
            elif record.echlon == "M4" and record.echelle == 10:
                record.salaire_de_base = 969.398
            elif record.echlon == "M4" and record.echelle == 11:
                record.salaire_de_base = 979.775
            elif record.echlon == "M4" and record.echelle == 12:
                record.salaire_de_base = 990.671
            elif record.echlon == "M4" and record.echelle == 13:
                record.salaire_de_base = 1002.112

            elif record.echlon == "C1" and record.echelle == 1:
                record.salaire_de_base = 971.219
            elif record.echlon == "C1" and record.echelle == 2:
                record.salaire_de_base = 978.745
            elif record.echlon == "C1" and record.echelle == 3:
                record.salaire_de_base = 986.647
            elif record.echlon == "C1" and record.echelle == 4:
                record.salaire_de_base = 994.943
            elif record.echlon == "C1" and record.echelle == 5:
                record.salaire_de_base = 1003.655
            elif record.echlon == "C1" and record.echelle == 6:
                record.salaire_de_base = 1012.802
            elif record.echlon == "C1" and record.echelle == 7:
                record.salaire_de_base = 1022.406
            elif record.echlon == "C1" and record.echelle == 8:
                record.salaire_de_base = 1032.492
            elif record.echlon == "C1" and record.echelle == 9:
                record.salaire_de_base = 1043.081
            elif record.echlon == "C1" and record.echelle == 10:
                record.salaire_de_base = 1054.199
            elif record.echlon == "C1" and record.echelle == 11:
                record.salaire_de_base = 1065.875
            elif record.echlon == "C1" and record.echelle == 12:
                record.salaire_de_base = 1078.133
            elif record.echlon == "C1" and record.echelle == 13:
                record.salaire_de_base = 1091.045

            elif record.echlon == "C2" and record.echelle == 1:
                record.salaire_de_base = 1004.950
            elif record.echlon == "C2" and record.echelle == 2:
                record.salaire_de_base = 1013.519
            elif record.echlon == "C2" and record.echelle == 3:
                record.salaire_de_base = 1022.300
            elif record.echlon == "C2" and record.echelle == 4:
                record.salaire_de_base = 1031.518
            elif record.echlon == "C2" and record.echelle == 5:
                record.salaire_de_base = 1041.200
            elif record.echlon == "C2" and record.echelle == 6:
                record.salaire_de_base = 1051.363
            elif record.echlon == "C2" and record.echelle == 7:
                record.salaire_de_base = 1062.036
            elif record.echlon == "C2" and record.echelle == 8:
                record.salaire_de_base = 1073.241
            elif record.echlon == "C2" and record.echelle == 9:
                record.salaire_de_base = 1085.008
            elif record.echlon == "C2" and record.echelle == 10:
                record.salaire_de_base = 1097.361
            elif record.echlon == "C2" and record.echelle == 11:
                record.salaire_de_base = 1110.333
            elif record.echlon == "C2" and record.echelle == 12:
                record.salaire_de_base = 1123.954
            elif record.echlon == "C2" and record.echelle == 13:
                record.salaire_de_base = 1138.256

            elif record.echlon == "C3" and record.echelle == 1:
                record.salaire_de_base = 1060.324
            elif record.echlon == "C3" and record.echelle == 2:
                record.salaire_de_base = 1070.081
            elif record.echlon == "C3" and record.echelle == 3:
                record.salaire_de_base = 1080.324
            elif record.echlon == "C3" and record.echelle == 4:
                record.salaire_de_base = 1091.079
            elif record.echlon == "C3" and record.echelle == 5:
                record.salaire_de_base = 1102.373
            elif record.echlon == "C3" and record.echelle == 6:
                record.salaire_de_base = 1114.230
            elif record.echlon == "C3" and record.echelle == 7:
                record.salaire_de_base = 1126.682
            elif record.echlon == "C3" and record.echelle == 8:
                record.salaire_de_base = 1139.755
            elif record.echlon == "C3" and record.echelle == 9:
                record.salaire_de_base = 1153.482
            elif record.echlon == "C3" and record.echelle == 10:
                record.salaire_de_base = 1167.895
            elif record.echlon == "C3" and record.echelle == 11:
                record.salaire_de_base = 1178.900
            elif record.echlon == "C3" and record.echelle == 12:
                record.salaire_de_base = 1198.920
            elif record.echlon == "C3" and record.echelle == 13:
                record.salaire_de_base = 1215.606
            else:
                record.salaire_de_base = 0


