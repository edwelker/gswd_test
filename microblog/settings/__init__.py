from .base import *

try:
    from .local import *
except ImportError as e:
    print "No local settings file found"
