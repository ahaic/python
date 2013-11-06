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
        sql=("INSERT INTO usr "
             "(name,id_type,id,Gender,Birthday,Address,District2,Mobile,Tel,Email,Nation,Education,Company,Version,uid)"
             "VALUES(%(name)s,$(id_type)s,%(id)s,$(Gender)s,%(Birthday)s,%(Address)s,$(District2)s,%(Mobile)s,$(Tel)s,%(Email)s,$(Nation)s,%(Edication)s,$(Company)s,%(Version)s),%(uid)s")
        data={
            'name':i[0],
            'id_type':i[3],
            'id':i[4],
            'Gender':i[5],
            'Birthday':i[6],
            'Address':i[7],
            'District':i[11],
            'Mobile':i[19],
            'Tel':i[20],
            'Email':i[22],
            'Nation':i[23],
            'Education':i[25],
            'Company':i[26],
            'Version':i[31],
            'uid':i[32],
            }
        try:
            cursor.execute(sql,data)
        except mysql.connector.Error as e:
            print("insert data --",e.msg)
            break
        
        
    
    
