import time
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


def transform(x):
    print(f"start record:{x.name}")
    time.sleep(3)
    result = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f"end record:{x.name}")
    return result


start = time.time()
result = tuple(map(transform, courses))
end = time.time()
print("total time={}".format(end - start))
pprint(result)