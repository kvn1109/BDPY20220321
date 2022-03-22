import collections

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])

print(type(course))
print(course)

poop = course(name='poop', field='python', attendee=10, remote=False)
print(poop)
print(poop.name, poop.attendee, poop.field, poop.remote)
#poop.name='AIOCV'
#poop.duration='35hr'