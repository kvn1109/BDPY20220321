import collections
import itertools
from pprint import pprint

course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field='python', attendee=10, remote=False)
bdpy = course(name='bdpy', field='python', attendee=15, remote=True)
andbiz = course(name='andbiz', field="android", attendee=10, remote=True)
pykt = course(name='pykt', field='python', attendee=20, remote=True)
aiocv = course(name='aiocv', field='python', attendee=5, remote=False)
courses = (poop, bdpy, andbiz, pykt, aiocv)
pprint(courses)
courses = sorted(courses, key=lambda x: x.field)
pprint(courses)
print("---" * 80)
for c in itertools.groupby(courses, lambda x: x.field):
    print(type(c))
    print(type(c[0]), type(c[1]))
    print(f"***{c[0]}***")
    for x in c[1]:
        print(f"....{x}")
print("---" * 80)
courses_by_field = {c[0]: list(c[1]) for c in itertools.groupby(courses, lambda x: x.field)}
pprint(courses_by_field)
pprint([(c[0], list(c[1])) for c in itertools.groupby(courses, lambda x: x.field)])
print("---" * 80)
pprint([(c[0], [c.name for c in c[1]]) for c in itertools.groupby(courses, lambda x: x.field)])