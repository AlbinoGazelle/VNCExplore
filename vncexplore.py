import argparse
import sys
from shutil import which
import subprocess

#check to ensure vncsnapshot is installed
if ((which("vncsnapshot") is not None) == False):
    print("Missing vncsnapshot. Please install (apt-get install vncsnapshot)")
    sys.exit()

#parse arguments
parser = argparse.ArgumentParser(description="Dump VNC Server Screenshots")
parser.add_argument("target_list", help="List of IP Addresses to scan for VNC snapshots.")
args = parser.parse_args()
def get_screenshots():
    try:
        #get length of target list
        lines = len(open(args.target_list).readlines())
        #start counting variable
        count = 0
        #open target list for reading
        f = open(args.target_list, "r")
        for target in f:
            #run vncsnapshot silently and check for errors
            run_snapshot(target)
            #increment count variable
            count += 1
            #print status
            print(f"{count} out of {lines} completed ({(count / lines) * 100}%)")
    except FileNotFoundError:
        print("Cannot Find File!")

def run_snapshot(target):
    try:
        subprocess.check_call(["vncsnapshot", f"{target}", f"{target}.jpg"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print(f"Couldn't get screenshot for {target}")
if __name__ == '__main__':
    get_screenshots()