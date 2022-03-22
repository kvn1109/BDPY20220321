from functools import reduce
import collections
from pprint import pprint

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
pykt = course(name='pykt', field='python', attendee=20, remote=True)
aiocv = course(name='aiocv', field='python', attendee=5, remote=False)
andbiz = course(name='andbiz', field="android", attendee=10, remote=True)
cplus = course(name='cplus', field="c", attendee=14, remote=True)
courses = (poop, bdpy, pykt, aiocv, andbiz, cplus)
pprint(courses)


def reducer(acc, val):
    acc.setdefault(val.field, [])
    acc[val.field].append(val.name)
    return acc


courses_by_category = reduce(reducer, courses, {})
print(courses_by_category)