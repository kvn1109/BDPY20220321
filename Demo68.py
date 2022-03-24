class Emp:
    #pass表示這邊內縮，暫時沒有放東西
    pass

#這邊開始的類別繼承上方的類別(Emp)
class Engineer(Emp):
    pass


class Pm(Emp):
    pass


class Hr(Emp):
    pass


emp1 = Emp()
engineer1 = Engineer()
pm1 = Pm()
hr1 = Hr()

staffs = [(emp1, "Employee1"), (engineer1, "Engineer1"), (pm1, "Pm1"), (hr1, "Hr1")]
classes = [Emp, Engineer, Pm, Hr]

for staff, name in staffs:
    for c in classes:
        isA = isinstance(staff, c)
        message1 = 'is a' if isA else 'is not a'
        print(name, message1, c.__name__)
print("**" * 50)
for c1 in classes:
    for c2 in classes:
        isSub = issubclass(c1, c2)
        message = '{} a subclass of'.format('is' if isSub else 'is not')
        print(c1.__name__, message, c2.__name__)