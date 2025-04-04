# -*- coding: utf-8 -*-
#############################################################################
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import fields, models, _


class ResCompany(models.Model):
    """Inherited the res company for setting the company stamp"""

    _inherit = 'res.company'
    _description = 'Company'

    stamp = fields.Binary(string=_("Stamp"), help=_("Company stamp"))
    position = fields.Selection(selection=[
        ('left', _('Left')),
        ('right', _('Right')),
        ('center', _('Center')),
    ], string=_('Position'), tracking=True, default="left",
        help=_("The position is used to position the signature and company stamp in reports"))
