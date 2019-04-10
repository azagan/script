import sqlite3 # Импортируем библиотеку, соответствующую типу нашей базы данных
from matplotlib import pyplot #для графиков

conn = sqlite3.connect("calls.sqlite3") # цепляемся к бд
cursor = conn.cursor() # создаем курсор, который делает запросы и получает их результаты


# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
k=0
for i in cursor.execute(" SELECT CallTimeStart FROM calls WHERE CallTimeStart LIKE '%2016-01-01%'"):
 k=k+1
 #print(i)
print(k)

n=0
for i in cursor.execute(" SELECT CallTimeStart FROM calls WHERE CallTimeStart LIKE '%2017-01-01%'"):
 n=n+1
print(n)

# Получаем результат сделанного запроса
#results = cursor.fetchall()

#print(results)

#в арма модель на вход "Year-Month-Day Hour: Minute: Second" и количество звонков в определенный день






















conn.close()