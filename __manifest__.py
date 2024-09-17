{
    "name": "Library",
    "version": "1.0",
    "summary": "Library",
    "description": """
      Library
    """,
    "author": "Salameh",
    "website": "",
    "category": "Sales",
    "depends": ["base", "sale_management", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/base_menu.xml",
        "views/book_view.xml",
        "views/category_view.xml",
        'views/order_sale_inherit.xml',
    ],
    "demo": [],
    "assets": {
        "web.assets_backend": [
            "library/static/src/css/style.css",
        ],
    },
    "application": True,
    "sequence": 1,
}
