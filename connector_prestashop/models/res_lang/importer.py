# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
import logging
from openerp.addons.connector.unit.backend_adapter import BackendAdapter
from ...unit.direct_binder import DirectBinder
from ...backend import prestashop
from openerp import _, exceptions

_logger = logging.getLogger(__name__)


@prestashop
class LangImporter(DirectBinder):
    _model_name = 'prestashop.res.lang'
    _erp_field = 'code'
    _ps_field = 'language_code'
    _copy_fields = [
        ('active', 'active'),
    ]

    def _compare_function(self, ps_val, erp_val, ps_dict, erp_dict):
        if len(erp_val) >= 2 and len(ps_val) >= 2:
                if len(ps_val) == 2:
                    if erp_val[0:2].lower() == ps_val[0:2].lower():
                        return True
                elif len(ps_val) == 4:
                    if ps_val.replace('-', '_').lower() == erp_val.lower():
                        return True
        return False
