from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num
from individual_routines import *
from individual_routines.bonus_search import *
from individual_routines.top_search import *
from individual_routines.landers import *
from status_manager import *

bonus = [6, 5, 10]
back = [3, 2, 8]

my_tellos = bonus + back

if __name__ == "__main__":
    with FlyTello(my_tellos) as fly:
        fly.pad_detection_on()
        fly.set_pad_detection(direction='downward')
        fly.takeoff()

        with fly.sync_these():
            fly.reorient(height=80, pad="m-2", tello='All')

        with fly.individual_behaviours():
            fly.run_individual(bonus_search_party,
                               fly=fly,
                               tellos=get_mac_addr_from_num(bonus),
                               update_status=update_status)
            fly.run_individual(top_search_party,
                               fly=fly,
                               tellos=get_mac_addr_from_num(back),
                               update_status=update_status,
                               get_status=get_status)

        fly.land()
