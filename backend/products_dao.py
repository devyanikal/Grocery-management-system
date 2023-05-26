import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):       

    cursor=connection.cursor()

    query=("SELECT p.product_id,p.product_name,p.uom_id,u.uom_name,p.price_per_unit FROM grocerystore.product_table p INNER JOIN grocerystore.uom u "
        "on p.uom_id=u.uom_id")
    cursor.execute(query)
    response=[]

    for (product_id,product_name,uom_id,uom_name,price_per_unit) in cursor:
        # print(product_id,product_name,uom_id,uom_name,price_per_unit)
        response.append(
            {
                'product_id':product_id,
                'product_name':product_name,
                'uom_id':uom_id,
                'uom_name':uom_name,
                'price_per_unit':price_per_unit
            }
        )

    return response

def insert_new_product(connection,product):
    cursor=connection.cursor()
    query=("INSERT INTO product_table (product_name,uom_id,price_per_unit) values (%s, %s, %s)")
    data=(product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)

    connection.commit()
    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor=connection.cursor()
    query=("DELETE FROM product_table where product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid

if __name__=='__main__':
    connection=get_sql_connection()
    print(get_all_products(connection))
    # print(insert_new_product(connection,{
    #     'product_name':'cabbage',
    #     'uom_id':'1',
    #     'price_per_unit':'10'

    # }))
    # print(delete_product(connection,12))