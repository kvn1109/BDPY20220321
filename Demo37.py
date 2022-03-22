import os
import sys
from pprint import pprint
import time
print(sys.executable)
pprint(sys.path)
print(os.getcwd())
dirname="中文檔名"

os.mkdir(dirname)
os.chdir(dirname)
print("now we are in:",os.getcwd())
time.sleep(10)
os.chdir("..")
os.rmdir(dirname)