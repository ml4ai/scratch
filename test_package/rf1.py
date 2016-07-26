import sys
import rf2

for i, path in enumerate(sys.path):
    print i, path

import b1.b1f1
import b1.b1f1 as b1f1


def r_hello():
    print 'hello from root'

r_hello()

rf2.rf2_hello()
b1.b1f1.b1f1_hello()
b1f1.b1f1_hello()
