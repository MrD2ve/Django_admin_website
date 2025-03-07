from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from food_category""")
        categories = dictfetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from food_product""")
        products = dictfetchall(cursor)
        return products


def get_users():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from food_customer""")
        users = dictfetchall(cursor)
        return users


def get_orders():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_subject""")
        orders = dictfetchall(cursor)
        return orders

