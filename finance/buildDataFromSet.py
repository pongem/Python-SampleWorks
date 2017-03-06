
from mod_SET_Helper import *

helper = SETFetch()
sets = helper.fetchAllSet()

print( "number of set: %d" % len(sets) )

print ( sets )