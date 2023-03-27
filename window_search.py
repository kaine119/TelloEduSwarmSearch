from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num
from individual_routines import *
from individual_routines.bonus_search import *
from individual_routines.top_search import *

from individual_routines.landers import *

my_tellos = [2, 3, 5, 6, 8, 10]
bonus = [6, 5, 10]
back = [8, 3, 2]

status = {
    "bonus_vacated": False,
    "corner_vacated": False,
    "bottom_search_vacated": False
}


def get_status(statusType: str = ""):
    if statusType == "all":
        return status["bonus_vacated"] and status["corner_vacated"] and status["bottom_search_vacated"]
    return status[statusType]


def update_status(statusType: str = ""):
    status[f"{statusType}_vacated"] = True


if __name__ == "__main__":
    with FlyTello(my_tellos) as fly:
        fly.pad_detection_on()
        fly.set_pad_detection(direction='downward')
        fly.takeoff()

        with fly.individual_behaviours():
            fly.run_individual(bonus_search_party,
                               fly=fly,
                               tellos=get_mac_addr_from_num(bonus),
                               update_status=update_status)
            fly.run_individual(move_front,
                               fly=fly,
                               tellos=get_mac_addr_from_num(back),
                               update_status=update_status,
                               get_status=get_status)

        fly.land()
