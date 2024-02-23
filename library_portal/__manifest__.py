{
        "name": "library Portal",
        "description": "Portal for library members",
        "author": "Daniel Reis",
        "license": "AGPL-3",
        "depends": [
            "library_checkout", "portal"
        ],
        "data": [
            "security/library_security.xml",
            "security/ir.model.access.csv",
            # "views/checkout_portal_templates.xml",
            "views/main_templates.xml",
            "views/assets.xml",
            "views/portal_templates.xml",
        ],
}
