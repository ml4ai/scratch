import sys
import dir2.d2f2  # NOTE: when executing this as standalone, now the full inclusion of d2f2 is required


def hello():
    print '----------------------------------------'
    print 'Hello from test_package_02/dir1/dir1_1/d1_1f2.hello()'
    print '__name__', __name__
    print '__package__', __package__
    for i, path in enumerate(sys.path[:5]):
        print i, path

    dir2.d2f2.hello()

# If I include the following line while commenting out the if __name__ part,
# and then execute this file, then it runs twice.
# I suspect that's because one (or more?) of the __init__.py's is importing this;
# perhaps when the call to hello() is within the __name__ test, then the import
# doesn't trigger it as it's not currently being run as __main__.
# hello()

if __name__ == "__main__":
    hello()
