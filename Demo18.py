import collections
from pprint import pprint
from functools import reduce

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=20, remote=True)
aiocv = course(name='aiocv', field='python', attendee=5, remote=False)
andbiz = course(name='andbiz', field="android", attendee=10, remote=True)
courses = (poop, bdpy, pykt, aiocv, andbiz)
pprint(courses)

total_income_tuple = tuple({'name': c.name, 'income': c.attendee * 8000} for c in courses)
total_income = reduce(lambda acc, val: acc + val['income'], total_income_tuple, 0)
pprint(total_income_tuple)
pprint(total_income)
print(sum(t['income'] for t in total_income_tuple))