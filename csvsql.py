import mysql.connector
import csv
   
cnx = mysql.connector.connect(user='root', password='admin',
                              host='10.0.0.136',
                              database='people',charset='utf8')

cursor=cnx.cursor()

with open('d:\Hanson\id.csv', newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)
        print(type(i[7]))
        sql = ("INSERT INTO usr "
               "(name, id_type, id, Gender, Birthday,Address,District2,Mobile,Tel,Email,Nation,uid) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
               

        
        data=(i[0],i[3],i[4],i[5],i[6],i[7],i[11],i[19],i[20],i[22],i[23],i[32])
        print(data)
        try:
            cursor.execute(sql,data)
            cnx.commit()
        except mysql.connector.Error as e:
            print("insert data --",e.msg)
            breaka
        
        
    
    
    







'''
import csv
with open('d:\Hanson\id.csv', newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)
        
'''


'''
for i in reader:
        print(i)
        break
    
'''
