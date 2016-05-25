#scons parameters file
#use this file to pass custom parameter to SConstruct script

#build_prefix="build_scons"

import sys
if('win' in sys.platform):
    print "WIN"
    #compiler='msvc'
    compiler= 'mingw' # by default on windows

boost_includes = "/usr/include/boost148"
boost_lib = "/usr/lib64"

# boost_libs_suffix = ".1.48.0"
pthread_lib = "/usr/lib64"
python_libpath = "/usr/lib64"
