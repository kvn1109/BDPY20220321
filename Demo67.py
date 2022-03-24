class Emp():
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel + 1

    def startWork(self):
        print("RD with grade=", self.currentGrade, " start to work")

    def endWork(self):
        print("RD finish work")


class PM(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel

    def startWork(self):
        print("PM with grade=", self.currentGrade, " start to work")

    def endWork(self):
        print("PM end work")


# r1 = RD()
# r1.startWork()
# r1.endWork()
# p1 = PM()
# p1.startWork()
# p1.endWork()

# employees = [RD(), PM(), RD(), RD(), PM()]
# for e in employees:
#     e.startWork()
#     e.endWork()

employees = [RD(), None, PM(), RD(), RD(), PM(), 3.14, 500]
for e in employees:
    if isinstance(e, Emp):
        e.startWork()
        e.endWork()
    else:
        print(e, "is not an Emp type")