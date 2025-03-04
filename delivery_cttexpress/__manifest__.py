# Copyright 2022 Tecnativa - David Vidal
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Delivery CTT Express",
    "summary": "Delivery Carrier implementation for CTT Express API",
    "version": "15.0.1.1.0",
    "category": "Delivery",
    "website": "https://github.com/OCA/delivery-carrier",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["delivery_package_number", "delivery_state", "delivery_price_method"],
    "external_dependencies": {"python": ["zeep"]},
    "data": [
        "security/ir.model.access.csv",
        "wizards/cttexpress_manifest_wizard_views.xml",
        "wizards/cttexpress_pickup_wizard.xml",
        "views/delivery_cttexpress_view.xml",
        "views/stock_picking_views.xml",
    ],
}
