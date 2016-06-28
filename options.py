#scons parameters file
#use this file to pass custom parameter to SConstruct script

#build_prefix="build_scons"

import sys
if('win' in sys.platform):
    print "WIN"
    #compiler='msvc'
    compiler= 'mingw' # by default on windows

boost_includes = "/usr/include/boost"
boost_lib = "/usr/lib/x86_64-linux-gnu/"

# boost_libs_suffix = ".1.48.0"
pthread_lib = "/usr/lib/x86_64-linux-gnu/"
python_libpath = "/usr/lib/x86_64-linux-gnu/"
