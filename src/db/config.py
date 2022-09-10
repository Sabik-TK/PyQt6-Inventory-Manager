import sqlite3
connection,cursor=None,None

try:
    connection = sqlite3.connect('src/db/products.db')
    cursor = connection.cursor()
    print("DB connected")
except:
    print("DB connection Error")

def add_product(id=None,name=None,stock=None,category=None):
    global connection,cursor
    try:
        print('started')
        cursor.execute(f"INSERT INTO Product (name,stock,category) VALUES('{name}',{stock},'{category}')")
        print('data added to db')
        connection.commit()
    except:
        print('db_error @add_product')

def del_product(id):
    global connection,cursor
    try:
        print('started')
        cursor.execute(f"delete from Product where id={id}")
        print('data deleted from db')
        connection.commit()
    except:
        print('db_error @del_product')

def find_user(username=None,password=None):
    global connection,cursor
    try:
        user = {}
        print('user find func')
        result = cursor.execute(f"SELECT * FROM User WHERE username='{username}' AND password='{password}'")
        for row in result:
            user['id'] = row[0]
            user['username'] = row[1]      
        return user
    except:
        print('db_error @find_user')


def create_user(id=None,username=None,password=None):
    global connection,cursor
    try:
        print('user add func')
        cursor.execute(f"INSERT INTO User (username,password) VALUES('{username}',{password})")
        print('user added to db')
        connection.commit()
    except:
        print('db_error @create_user')

def list_product():
    global connection,cursor
    try:
        print('@list_product')
        result=cursor.execute(f"SELECT * FROM Product ORDER BY -id")
        products = []
        for product in result:
            print(product[0])
            products.append({'id':product[0],'name':product[1],'stock':product[2],'category':product[3]})   
        return products
    except:
        print('db_error @list_product')
        return []


# def list_products

