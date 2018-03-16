import pymysql
import io
fl=open("C:\Users\HP\PycharmProjects\Sample\Employee.txt",'w')
db = pymysql.connect('localhost', 'mysql1', 'mysql1', 'organization')
cursor=db.cursor()
#cursor.execute("INSERT INTO EMPLOYEE VALUES(100,'abcd','900')")
cursor.execute("SELECT * FROM EMPLOYEE")
data=cursor.fetchall()
#print('data is:', data)
emplist = []
count=0
for row in data:
    count += 1
    emplist.append(row)
    fl.write(str(row))
    while(count<len(data)):
        fl.write(',')
        break
db.close()
fl.close()
print("employee list: ", emplist)




