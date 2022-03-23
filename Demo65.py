class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.day * self.member

    #如果是類別的method
    @classmethod
    def get_member(cls):
        cls.holidays = 14
        return cls.member

    # 如果是static(靜止)的method
    @staticmethod
    def calculate(x, y):
        return x ** y


t1 = Team()
print(t1.all_working_hour())
print(t1.working_hour())
print(Team.get_member(), t1.get_member())
Team.member = 8
print(Team.get_member(), t1.get_member())
print(t1.calculate(3, 5))
print(t1.calculate(5, 3))