# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee"

    categorie = fields.Selection([
        ('Cadre', 'Cadre'),
        ('Maitrise', 'Maitrise'),
        ('Agent ', 'Agent exécution')], string='Catégorie', groups="hr.group_hr_user", tracking=True)

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
        ('C3', 'C3')], string='echlon', groups="hr.group_hr_user", tracking=True)

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
                record.salaire_de_base = 594
            elif record.echlon == "E0" and record.echelle == 2:
                record.salaire_de_base = 595
            elif record.echlon == "E0" and record.echelle == 3:
                record.salaire_de_base = 595
            elif record.echlon == "E0" and record.echelle == 4:
                record.salaire_de_base = 596
            elif record.echlon == "E0" and record.echelle == 5:
                record.salaire_de_base = 597
            elif record.echlon == "E0" and record.echelle == 6:
                record.salaire_de_base = 597
            elif record.echlon == "E0" and record.echelle == 7:
                record.salaire_de_base = 598
            elif record.echlon == "E0" and record.echelle == 8:
                record.salaire_de_base = 598
            elif record.echlon == "E0" and record.echelle == 9:
                record.salaire_de_base = 601
            elif record.echlon == "E0" and record.echelle == 10:
                record.salaire_de_base = 604
            elif record.echlon == "E0" and record.echelle == 11:
                record.salaire_de_base = 607
            elif record.echlon == "E0" and record.echelle == 12:
                record.salaire_de_base = 610
            elif record.echlon == "E0" and record.echelle == 13:
                record.salaire_de_base = 616

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

   
