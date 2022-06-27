# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class HrPayslip(models.Model):
    # """
    # Employee contract based on the visa, work permits
    # allows to configure different Salary structure
    # """

    _inherit = "hr.payslip"
    _description = "Employee Pay Slip"

    working_days = fields.Integer(string='Working days', compute='_compute_working_days', default=0)
    jour_de_repos_1 = fields.Selection(related='employee_id.contract_ids.jour_de_repos_1')
    jour_de_repos_2 = fields.Selection(related='employee_id.contract_ids.jour_de_repos_2')
    sum_worked_hours = fields.Float(compute='_compute_worked_hours', store=True,
                                    help='Total hours of attendance and time off (paid or not)')
    @api.depends('worked_days_line_ids.number_of_hours')
    def _compute_worked_hours(self):
        for payslip in self:
            payslip.sum_worked_hours = sum([line.number_of_hours for line in payslip.worked_days_line_ids])

    @api.depends('jour_de_repos_1', 'jour_de_repos_2', 'date_to', 'date_from')
    def _compute_working_days(self):
        for record in self:
            # if record.jour_de_repos_1 == "Lundi":
            #     record.working_days = 20
            # else:
            #     record.working_days = 26
            y = 0
            f = (record.date_to - record.date_from).days
            a = str(record.date_from)[:4]
            b = str(record.date_from)[5:7]
            # b1 = str(record.date_to)[5:7]
            c = str(record.date_from)[-2:]
            if record.jour_de_repos_1 == "Lundi":
                k1 = 0
            elif record.jour_de_repos_1 == "Mardi":
                k1 = 1
            elif record.jour_de_repos_1 == "Mercredi":
                k1 = 2
            elif record.jour_de_repos_1 == "Jeudi":
                k1 = 3
            elif record.jour_de_repos_1 == "Vendredi":
                k1 = 4
            elif record.jour_de_repos_1 == "Samedi":
                k1 = 5
            else:
                k1 = 6
            if record.jour_de_repos_2 == "Lundi":
                q1 = 0
            elif record.jour_de_repos_2 == "Mardi":
                q1 = 1
            elif record.jour_de_repos_2 == "Mercredi":
                q1 = 2
            elif record.jour_de_repos_2 == "Jeudi":
                q1 = 3
            elif record.jour_de_repos_2 == "Vendredi":
                q1 = 4
            elif record.jour_de_repos_2 == "Samedi":
                q1 = 5
            else:
                q1 = 6

            for i in range(0, f + 1):
                x = date(int(a), int(b), int(c)) + timedelta(days=i)
                try:
                    if x.weekday() != int(k1) and x.weekday() != int(q1):
                        y += 1
                        record.working_days = y
                except:
                    if x.weekday() != int(k1):
                        y += 1
                        record.working_days = y
