from sql_connection import get_sql_connection
def get_all_product(connection):
    cursor = connection.cursor()
    query =("select product.product_id, product.name, product.uom_id, product.price_per_unit, uom.uom_name "
            "from product "
            "inner join uom on product.uom_id = uom.uom_id")


    cursor.execute(query)
    resonse = []
    for (product_id, name, uom_id, price_per_unit, uom_name ) in cursor:
        resonse.append(
            {
                "product_id":product_id,
                "product_name":name,
                "uom_id":uom_id,
                "price_per_unit":price_per_unit,
                "uom_name":uom_name
            }
        )
    return resonse
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into product"
             "(name, uom_id, price_per_unit)"
             " value(%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("Delete from product where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()



if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_product(connection))
    # print(insert_new_product(connection, {
    #     'product_name':'cabbage',
    #     'uom_id': '1',
    #     'price_per_unit':'10'
    # }))
    print(delete_product(connection,8))