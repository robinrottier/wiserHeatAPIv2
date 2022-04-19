from typing import Any
from params import HOST, KEY

import pathlib
import sys
import time

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from wiserHeatAPIv2.const import TEXT_UNKNOWN
from wiserHeatAPIv2 import wiserhub

BOOL = [True, False]
LEVELCOLOURS = ["\033[95m","\033[94m","\033[96m","\033[92m"]

class bcolors:
    HEADER = "\033[94m"
    LINK = "\033[95m"
    NORMAL = "\033[97m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def fn(h: object, fn_name: str, args: dict = {}):
    output = ""

    print(f"Calling function {fn_name} with parameters {args}")

    try:
        fn = getattr(h, fn_name)
        result = fn(**args)
        if result:
            if type(result) != bool:
                print(f"Result: {result.name}")
            print(f"{bcolors.OKGREEN}Passed{bcolors.NORMAL}")
        else:
            print(f"{bcolors.WARNING} ERROR - {result}{bcolors.NORMAL}")
    except Exception as ex:
        print(f"{bcolors.FAIL}ERROR - {ex}{bcolors.NORMAL}")
        raise ex

def p(h: object, prop_name: str, value):
    print(f"Setting property {prop_name} with value {value}")
    try:
        p = setattr(h, prop_name, value)
        print(f"{bcolors.OKGREEN}Passed{bcolors.NORMAL}")
    except Exception as ex:
        print(f"{bcolors.FAIL}ERROR - {ex}{bcolors.NORMAL}")
 
print("**********************************************************")
print ("WiserHub API - hotwater cancel")
print("**********************************************************")
try:
    h = wiserhub.WiserAPI(HOST, KEY)
    
    # Test Hotwater
    if h.hotwater:
        #fn(h.hotwater, "boost", {"duration": 1800})
        #fn(h.hotwater, "override_state", {"state":"on"})
        #fn(h.hotwater, "override_state_for_duration", {"duration":30, "state":"on"})
        fn(h.hotwater, "cancel_overrides", {})
    else:
        print(f"{bcolors.OKBLUE}No hot water in system to test{bcolors.NORMAL}")
except Exception as ex:
    print (f"Error: {ex}")
