from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num
from individual_routines.landers import *
from individual_routines.bonus_search import bonus_search_party
from status_manager import update_status

# my_tellos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_tellos = [1, 2, 3, 5, 6, 10]


# my_tellos = [13, 15]

bonus = [6, 5, 10]
top_search = [1, 2, 3]
bottom_search = []
landers_top = []
landers_bottom = []

if __name__ == "__main__":
    with FlyTello(my_tellos) as fly:
        fly.pad_detection_on()
        fly.set_pad_detection(direction='downward')
        fly.takeoff()

        with fly.individual_behaviours():
            fly.run_individual(bonus_search_party, fly=fly,
                               tellos=get_mac_addr_from_num(bonus))
            # fly.run_individual(start_search_party,
            #                    tellos=get_mac_addr_from_num(top_search),
            #                    update_status=update_status)
            # fly.run_individual(bottom_search_party,
            #                    tellos=get_mac_addr_from_num(bottom_search))
            fly.run_individual(landers_top_send,
                               tellos=get_mac_addr_from_num(landers_top))
            fly.run_individual(landers_bottom_send,
                               tellos=get_mac_addr_from_num(landers_bottom))

        fly.land()
