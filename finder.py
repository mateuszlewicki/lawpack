#! /usr/bin/python

import os, sys, re

print(sys.argv[1])
lsd = os.listdir("/lawtrans")
for d in lsd:
    #print(os.path.join('/lawtrans',d))
    if re.match("^ALM.*$", d):
       lsd[lsd.index(d)]=os.path.join('/lawtrans',d)
       print(d)
    else:
        lsd.remove(d)

for d in lsd:
    for root, dirs, files in os.walk(d):
        for name in dirs:
#           print(name)
            if re.match("^.*"+sys.argv[1]+"$",name):
                print(os.path.join(root, name))
