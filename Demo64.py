class Team:
    name = "normal team"

t1 = Team()
t2 = Team()
print(Team.name, t1.name, t2.name)
t1.name = "RD team"
print(t1.name, Team.name, t2.name)
del t1.name
print(t1.name, Team.name, t2.name)
t2.manager = "Kevin"
print(t2.name, t2.manager)
Team.vaule = True
print(t1.vaule, t2.vaule)