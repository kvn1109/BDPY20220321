from functools import reduce
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

courses_by_category = reduce(lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}}
                             , courses, {'python': [], 'android': []})
print(courses_by_category)
dict1 = {'iphone13': 100, 'ipad': 50}
print({**dict1, 'appleWatch': 30})
print({**dict1, 'iphone13': 150})