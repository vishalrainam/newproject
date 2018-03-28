	import time
import sys,os
import pandas
import helloworld

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(__file__)

    a = pandas.read_csv(BASE_DIR+"/resource.txt")

    print a
    print sys.argv[1:]
    print 'Python', python_version()

    for x in xrange(1,10):
    	time.sleep(1)
    	print x