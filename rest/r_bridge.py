import rpy2
from rpy2.rinterface import R_VERSION_BUILD
import rpy2.robjects as ro

def rpy2_version():
    return rpy2.__version__

def r_version_on_build():
    return R_VERSION_BUILD
#source() is relative by default
log_calc_r = ro.r("source('rsource/log_calc.R')")

def calculate_log(b, x):
    return log_calc_r[0](b, x)
