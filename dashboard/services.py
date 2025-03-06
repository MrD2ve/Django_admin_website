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
        cursor.execute("""SELECT food_product.id, food_product.title, food_category.name as category
         from food_products left join food_category on food_products.category_id = food_category.id, food_products.description,
         food_products.cost, food_products.price, food_products.image, food_products.created_at
         """)
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


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_teacher.id, adminapp_teacher.first_name, adminapp_teacher.last_name,
        adminapp_teacher.age, adminapp_kafedra.name as kafedra_name, adminapp_subject.name as subject_name from 
        adminapp_teacher left join adminapp_kafedra on adminapp_teacher.kafedra_id = adminapp_kafedra.id
        left join adminapp_subject on adminapp_teacher.subject_id = adminapp_subject.id""")
        teachers = dictfetchall(cursor)
        return teachers


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_student.id, adminapp_student.first_name, adminapp_student.last_name, 
        adminapp_student.age, 
        adminapp_group.name as group_name, adminapp_student.image as image  from adminapp_student
        left join adminapp_group on adminapp_student.group_id = adminapp_group.id""")
        student = dictfetchall(cursor)
        return student
