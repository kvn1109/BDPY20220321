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

name_and_field = map(lambda x: {'name': x.name, 'field': x.field}, courses)
pprint(tuple(name_and_field))