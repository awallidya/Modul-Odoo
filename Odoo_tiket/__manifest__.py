{
    'name': 'pesawat',
    'version': '1.0',
    'author': 'Awal Lidya Musaffak',
    'summary': 'module yang berisikan Pesawat, Form pesawat, Harga',
    'description': """ini adalah module penjualan tiket pesawat""",
    'website': 'https://www.odootiketpesawat.com',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/tiket.xml',
        'views/dashboard.xml',
        'views/template.xml',
        'views/daftar.xml',
        'reports/report.xml',
        'reports/tiket.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OEEL-1',

    'qweb': [
        'static/xml/*.xml',
    ]
}
