from typing import Tuple
from individual_routines.search import grid_search
from fly_tello import FlyTello
my_tellos = list()


#
# SIMPLE EXAMPLE - TWO TELLOs FLYING IN SYNC, DEMO'ING ALL KEY TELLO CAPABILITIES
#
# SETUP: Tello both facing away from controller, first Tello on the left, approx 0.5-1m apart
#

# Test example, should be replaced
search_tellos: dict[str, str] = {
    "B1": "d2:71:04"
    # "B2": "",
    # "B3": "",
}


def get_label_for_mac(target_mac: str):
    for label, mac in search_tellos.items():
        if mac == target_mac:
            return label
    raise RuntimeError(f"MAC not found: {target_mac}")


with FlyTello(list(search_tellos.values())) as fly:
    fly.takeoff()
    fly.reorient(height=100, pad='m-2')
    with fly.individual_behaviours():
        fly.run_individual(grid_search, tello=search_tellos['B1'], pad='m7', fly=fly)
    fly.reorient(height=100, pad='m-2')
    fly.land()
