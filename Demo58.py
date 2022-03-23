import wikipedia

print(wikipedia.summary("pythonidae"))
print(wikipedia.search("C++"))

taipei = wikipedia.page('Taipei')
print(taipei.title)
print(taipei.url)