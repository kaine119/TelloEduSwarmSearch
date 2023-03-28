from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num
from individual_routines import *
from individual_routines.bonus_search import *
from individual_routines.top_search import *
from individual_routines.landers import *
from status_manager import *
from arp import all_drones_ready

# 1st entry is closest to window
back = [1, 2, 3]

# 1st entry is closest to window
bonus = [4, 5, 6]

my_tellos = bonus + back


def begin():
    with FlyTello(get_mac_addr_from_num(my_tellos)) as fly:
        fly.set_top_led()
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


if __name__ == "__main__":
        begin()
