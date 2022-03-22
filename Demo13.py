import collections
from pprint import pprint
course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=20, remote=True)
aiocv = course(name='aiocv', field='python', attendee=5, remote=False)
andbiz = course(name='andbiz', field="android", attendee=10, remote=True)
courses = (poop, bdpy, pykt, aiocv, andbiz)
pprint(courses)


result1 = filter(lambda x: x.remote is True, courses)
pprint([x for x in result1])
result2 = filter(lambda x: x.attendee >= 10, courses)
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))
# print(next(result2))
# pprint([x for x in result2])
result3 = filter(lambda x: x.remote is True, courses)
result4 = filter(lambda x: x.attendee >= 10, result3)
pprint([x for x in result4])


result1 = tuple(filter(lambda x: x.remote is True and x.attendee >= 10, courses))
pprint(result1)
##

pprint(tuple(filter(lambda x: x.remote is True and x.attendee >= 10, courses)))
