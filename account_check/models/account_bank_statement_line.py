# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api
import logging
_logger = logging.getLogger(__name__)


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    def button_cancel_reconciliation(self):
        """
        Avoid deletion of move if it was a debit created from checks
        """
        for st_line in self:
            for move in st_line.journal_entry_ids:
                if self.env['account.check.operation'].search(
                        [('origin', '=', 'account.move,%s' % move.id)]):
                    move.write({'statement_line_id': False})
                    move.line_ids.filtered(
                        lambda x: x.statement_id == st_line.statement_id
                    ).write({'statement_id': False})
                    self -= st_line
        return super(
            AccountBankStatementLine, self).button_cancel_reconciliation()

    def print_statement(self):
        return self.env.ref('account_check.report_bank_statement_line').report_action(self)
