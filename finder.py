#! /usr/bin/python

import os, sys, re

print(sys.argv[1])
lsd = os.listdir("/lawtrans")
for d in lsd:
    if !re.match("^ALM.*$", d):
        lsd.remove(d)
# print(os.walk(os.environ["LAWDIR"]).)
# for root, dirs, files in os.walk("/cygwin64" + os.environ["LAWDIR"].replace("/", "\\")):

for d in lsd:
    for root, dirs, files in os.walk(d):
        # print(root, dirs, files)
        # for name in files:
        #   print(os.path.join(root, name))
        for name in dirs:
            if name == sys.argv[1]:
                print(os.path.join(root, name))
