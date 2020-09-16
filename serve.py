# use python http.server to serve local presentation
# call this script from the talk root directory

# You can also run manually from command line
#
# python2 -m SimpleHTTPServer 8000
# python3 -m http.server 8000

import sys

try:
    port = int(sys.argv[1])
except:
    port = 8000

try:
    # Python 2
    from SimpleHTTPServer import test, SimpleHTTPRequestHandler
except ImportError:
    # Python 3
    from http.server import test, SimpleHTTPRequestHandler

test(SimpleHTTPRequestHandler)
