import mysql.connector
import csv
   
cnx = mysql.connector.connect(user='root', password='admin',
                              host='10.0.0.136',
                              database='people',charset='utf8')

cursor=cnx.cursor()


def insert():
    sql = ("INSERT INTO usr "
           "(name, id_type, id, Gender, Birthday,Address,District2,Mobile,Tel,Email,Nation,uid) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    

    try:
        cursor.execute(sql,data)
        cnx.commit()
    except mysql.connector.Error as e:
        print("insert data --",e.msg)
     



with open('d:\Hanson\id.csv', newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    
    for i in reader:
        
        try:
            print(i[0],'--',i[32])
            data=(i[0],i[3],i[4],i[5],i[6],i[7],i[11],i[19],i[20],i[22],i[23],i[32])
            insert()
            
        except Exception as e:
            print('-------------------------------------------',e)
			
			

        

    
