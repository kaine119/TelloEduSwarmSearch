from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num
from individual_routines.landers import *
# from status_manager import *
from arp import all_drones_ready

landers = [7, 8, 10, 11, 12, 16, 17]

my_tellos = get_mac_addr_from_num(landers)


def begin():
    with FlyTello(my_tellos) as fly:
        fly.set_top_led()
        fly.pad_detection_on()
        fly.set_pad_detection(direction='downward')
        fly.takeoff()

        with fly.sync_these():
            fly.reorient(height=80, pad="m-2", tello='All')

        with fly.individual_behaviours():
            fly.run_individual(landers_full_send,
                               fly=fly,
                               tellos=get_mac_addr_from_num(landers))

        fly.land()


if __name__ == "__main__":
    print("LET'S GOOOOOOOO. I'M STARTING THE BOTTOM LEFT GROUP (THE LANDERS!!)")
    begin()
