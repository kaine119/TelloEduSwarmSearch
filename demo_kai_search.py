from typing import Tuple
from individual_routines.search import grid_search
from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num
my_tellos = list()


#
# SIMPLE EXAMPLE - TWO TELLOs FLYING IN SYNC, DEMO'ING ALL KEY TELLO CAPABILITIES
#
# SETUP: Tello both facing away from controller, first Tello on the left, approx 0.5-1m apart
#

# Test example, should be replaced
search_tellos = get_mac_addr_from_num([10])


with FlyTello(search_tellos) as fly:
    fly.takeoff()
    fly.reorient(height=100, pad='m-2')
    with fly.individual_behaviours():
        fly.run_individual(grid_search, tello=search_tellos[0], pad='m3', fly=fly, grid_width=2, grid_length=5)
    fly.reorient(height=100, pad='m-2')
    fly.land()
