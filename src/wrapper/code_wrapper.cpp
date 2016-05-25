#include <boost/python.hpp>
#include "../cpp/code.h"


BOOST_PYTHON_MODULE(_oacpp)
{
    using namespace boost::python;
    def("code", code_func);
}
