#coding:utf-8
groupmates = [
    {
        "name": u"Василий",
        "group": u"БСТ1701",
        "age": 20,
        "marks": [2, 3, 3, 5, 4]
        },
    {
        "name": u"Алёна",
        "group": u"БСТ1701",
        "age": 19,
        "marks": [5, 4, 4, 4, 5]
        },
    {
        "name": u"Иван",
        "group": u"БСТ1702",
        "age": 20,
        "marks": [3, 5, 4, 3, 2]
        },
    {
        "name": u"Андрей",
        "group": u"БСТ1702",
        "age": 19,
        "marks": [3, 5, 4, 3, 3]
        },
    {
        "name": u"Ирина",
        "group": u"БСТ1703",
        "age": 19,
        "marks": [5, 5, 5, 4, 5]
        }
    ]


def print_students(students):
    print u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20)
    print "\n"
    for student in students:
        print student["name"].ljust(15), \
              student["group"].ljust(8), \
              str(student["age"]).ljust(8), \
              str(student["marks"]).ljust(20)
        print "\n"
print_students(groupmates)

def filter_st(students):
    print u"Введите среднюю оценку:"
    a=int(raw_input())
    TrueStudents=[]
    print u"Список студентов, удовлетворяющих условию средней оценки\n"
    for student in students:
        l=len(student["marks"])
        k=sum(student["marks"])
        if (k/l)>=a:
            TrueStudents.append(student)
    print_students(TrueStudents)

filter_st(groupmates)
