# Copyright 2019 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import odoo.tests


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_01_pos_is_loaded(self):
        self.phantom_js(
            '/web',

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".run('pos_menu_tour')",

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_menu_tour.ready",

            login="admin",
            timeout=240,
        )
