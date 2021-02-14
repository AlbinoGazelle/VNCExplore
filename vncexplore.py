import argparse
import sys
from shutil import which

def is_installed(name):
    return which(name) is not None

if(is_installed("vncsnapshot") == False):
    print("Missing vncsnapshot. Please install (apt-get install vncsnapshot)")

print(is_installed("vncsnapshot"))
parser = argparse.ArgumentParser(description="Dump VNC Server Screenshots")
parser.add_argument("target_list", help="List of IP Addresses to scan for VNC snapshots.")
args = parser.parse_args()

test_server = "216.48.95.180"



print(args.target_list)