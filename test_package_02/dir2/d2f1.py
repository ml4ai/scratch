import sys
import dir1.dir1_1


def hello():
    print '----------------------------------------'
    print 'Hello from test_package_02/dir2/d2f1.hello()'
    print '__name__', __name__
    print '__package__', __package__
    for i, path in enumerate(sys.path[:5]):
        print i, path

    dir1.dir1_1.d1_1f1.hello()
