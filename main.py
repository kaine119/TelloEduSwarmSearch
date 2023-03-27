from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num
from individual_routines.find_victims import *
from individual_routines.landers import *

my_tellos = get_mac_addr_from_num([10])

bonus = []
top_search = []
bottom_search = []
landers_top = []
landers_bottom = []

if __name__ == "__main__":
    with FlyTello(my_tellos) as fly:
        fly.pad_detection_on()
        fly.set_pad_detection(direction='downward')
        fly.takeoff()

        with fly.individual_behaviours():
            fly.run_individual(bonus_search_party,
                               tellos=get_mac_addr_from_num(bonus))
            fly.run_individual(start_search_party,
                               tellos=get_mac_addr_from_num(top_search))
            fly.run_individual(bottom_search_party,
                               tellos=get_mac_addr_from_num(bottom_search))
            fly.run_individual(landers_top_send,
                               tellos=get_mac_addr_from_num(landers_top))
            fly.run_individual(landers_bottom_send,
                               tellos=get_mac_addr_from_num(landers_bottom))

        fly.land()
