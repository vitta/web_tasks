# -*- encoding:cp1251 -*-


try:
    days = {"1":"Pn", "2":"��","3":"��","4":"��","5":"��","6":"��","7":"��"}
    s = raw_input("������� �����: ")
    s = int(s)
except ValueError:
    print "�� �����"
else:
    s=str(s)
    print days[s]


monthes = {"������":1, "�������":2,"����":3,"������":4}
m = raw_input("������� �����")
print monthes[m]
