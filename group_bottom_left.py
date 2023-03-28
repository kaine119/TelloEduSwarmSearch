from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num
from individual_routines.landers import *
from status_manager import *

# Edit this with the drones we're sending to land
landers = []

my_tellos = landers

if __name__ == "__main__":
    with FlyTello(my_tellos) as fly:
        fly.pad_detection_on()
        fly.set_pad_detection(direction='downward')
        fly.takeoff()

        with fly.sync_these():
            fly.reorient(height=80, pad="m-2", tello='All')

        with fly.individual_behaviours():
            fly.run_individual(landers,
                               fly=fly,
                               tellos=get_mac_addr_from_num(landers),
                               update_status=update_status,
                               get_status=get_status)

        fly.land()
