import rpy2
import db

from rpy2.rinterface import R_VERSION_BUILD
import rpy2.robjects as ro
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage

from db.db2_interface import get_all_events

def rpy2_version():
    return rpy2.__version__

def r_version_on_build():
    return R_VERSION_BUILD

#open() is relative by default
def get_r_func_handle():
    with open('rsrc/log_calc.R', 'r') as log_cal_r_file:
        log_cal_r_str = log_cal_r_file.read()
    r_func_handle = SignatureTranslatedAnonymousPackage(log_cal_r_str, "r_func_handle")
    return r_func_handle

r_func_handle = get_r_func_handle()

def calculate_log(b, x):
    return r_func_handle.calcLog(b, x)[0]

def get_event_count():
    events_dataframe = get_all_events()
    return len(events_dataframe)
