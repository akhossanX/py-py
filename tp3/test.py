
from dictionary import *

a = SortedDictionary()

a["khossan"] = 1
a["ishaq"]   = 2
a["hibot"]   = 3

b = SortedDictionary()

b["sokaina"]   = 4


d = a.add(b)

d.sort()

print(d)

