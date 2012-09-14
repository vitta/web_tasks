# -*- encoding:cp1251 -*-


try:
    days = {"1":"Pn", "2":"Вт","3":"Ср","4":"Чт","5":"Пт","6":"Сб","7":"Вс"}
    s = raw_input("введите номер: ")
    s = int(s)
except ValueError:
    print "Не число"
else:
    s=str(s)
    print days[s]


monthes = {"январь":1, "февраль":2,"март":3,"апрель":4}
m = raw_input("введите месяц")
print monthes[m]
