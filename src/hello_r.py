import rpy2
from rpy2.rinterface import R_VERSION_BUILD

def rpy2_version():
    return rpy2.__version__
def r_version_on_build():
    return R_VERSION_BUILD
