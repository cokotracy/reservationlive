{
    'name': 'MK Reservation',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Tools',
    'description':
        """
        This Module add below functionality into odoo

        1.MK Reservation\n

    """,
    'summary': 'MK Reservation',
    'author': 'Master Key',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/main_menus_view.xml',
        'views/floor_view.xml',
        'views/area_view.xml',
        'views/table_view.xml',
        'views/reservation_view.xml',
        'views/table_shape_view.xml',
        'views/time_slot_view.xml',
        'wizard/clean_tables_view.xml'
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}