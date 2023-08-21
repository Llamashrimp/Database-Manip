import sqlite3
db = sqlite3.connect('data/student_db')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE python_programming(id INTERGER PRIMARY KEY, name TEXT,
               grade INTEGER)

''')
db.commit()

id1 = 55
name1 = 'Carl Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

table_data = [(id1, name1, grade1), (id2, name2, grade2), (id3, name3, grade3), (id4, name4, grade4), (id5, name5, grade5)]

cursor.executemany('''INSERT INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', table_data)
print("Users have been added")

db.commit()

cursor.execute('''
    SELECT id, name, grade FROM python_programming WHERE grade >= 60 AND grade <=80
''')
range_students = cursor.fetchall()

for row in range_students:
    print(f"id: {row[0]}, name: {row[1]}, grade: {row[2]}")

grade = 65
name = "Carl Davis"
cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ? ''', (grade, name))
print('Student data updated!')

grade = 20
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id < 55 = ? ''', (grade, 55))
db.commit()
print("Student Data Updated!")



