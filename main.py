import sys
from slot_finder import SlotFinder
from pprint import pprint
from time import time, sleep, strftime, localtime
from logger import Logger

sys.stdout = Logger(sys.stdout)

if __name__ == "__main__":
    slot_finder_instance = SlotFinder()
    while True:
        current_time = strftime("%H:%M:%S", localtime())
        print("Time Hit : {}".format(current_time))
        results = slot_finder_instance.find_slots()
        print("Number of slots availabale : {}".format(len(results)))
        pprint(results)
        sleep(slot_finder_instance.interval * 60)