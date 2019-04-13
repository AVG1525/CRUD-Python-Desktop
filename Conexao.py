import pymysql

try:
    conn =pymysql.connect(host="localhost",user="root",password="",database="py")
    cursor = conn.cursor()
except:
    print("\nError:\n- verifique o MySQL\n")
    exit()


