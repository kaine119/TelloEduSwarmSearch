from typing import List
from fly_tello import FlyTello
from individual_routines.search import grid_search
import serial_mapper
from arp import all_drones_ready

searchers = [
    26,
    # 25,
    # 24,
    # 23,
    # 22,
    # 21,
    # 20,
    # 19,
]

search_tellos = serial_mapper.get_mac_addr_from_num(searchers)


def land_immediately(fly, tellos: List[str]):
    for tello in tellos:
        fly.land(tello)


def go_to_room(fly, tellos: List[str]):
    with fly.sync_these():
        fly.straight_from_pad(300, 0, 80, 50, 'm-2', tello=tellos[2])
        fly.straight_from_pad(100, 0, 80, 50, 'm-2', tello=tellos[1])
        fly.straight_from_pad(100, 0, 80, 50, 'm-2', tello=tellos[0])

    with fly.sync_these():
        fly.reorient(80, 'm-2', tello=tellos[2])
        fly.reorient(80, 'm-2', tello=tellos[1])
        fly.reorient(80, 'm-2', tello=tellos[0])

    with fly.sync_these():
        fly.straight_from_pad(300, 0, 80, 50, 'm-2', tello=tellos[2])
        fly.straight_from_pad(300, 0, 80, 50, 'm-2', tello=tellos[1])
        fly.straight_from_pad(100, 0, 80, 50, 'm-2', tello=tellos[0])

    with fly.sync_these():
        fly.reorient(80, 'm1', tello=tellos[2])
        fly.reorient(80, 'm1', tello=tellos[1])
        fly.reorient(80, 'm7', tello=tellos[0])

    with fly.sync_these():
        fly.straight_from_pad(300, 0, 80, 50, 'm-2', tello=tellos[2])
        fly.straight_from_pad(300, 0, 80, 50, 'm-2', tello=tellos[1])
        fly.straight_from_pad(300, 0, 80, 50, 'm-2', tello=tellos[0])

    with fly.sync_these():
        fly.reorient(80, 'm1', tello=tellos[2])
        fly.reorient(80, 'm1', tello=tellos[1])
        fly.reorient(80, 'm1', tello=tellos[0])

    with fly.sync_these():
        # localise [2] to pad
        fly.straight_from_pad(50, 300, 80, 50, 'm1', tello=tellos[2])

        # move [1] one pad down
        fly.straight_from_pad(300, 0, 80, 50, 'm1', tello=tellos[1])

        # move [0] one pad down
        fly.straight_from_pad(300, 0, 80, 50, 'm1', tello=tellos[0])

    with fly.sync_these():
        # sideways into window
        fly.straight_from_pad(0, 150, 75, 100, "m7", tello=tellos[2])

        # localise [1] to pad
        fly.straight_from_pad(10, 300, 75, 100, "m1", tello=tellos[1])

        # move the last one ot the left
        fly.straight_from_pad(300, 0, 75, 100, "m1", tello=tellos[0])

    with fly.sync_these():
        # move [2] down to search points
        fly.straight_from_pad(-200, 0, 75, 100, "m7", tello=tellos[2])

        # move [1] through the window
        fly.straight_from_pad(0, 150, 75, 100, "m7", tello=tellos[1])

        # move [0] to the window pad
        fly.straight_from_pad(50, 300, 75, 100, "m1", tello=tellos[0])

    with fly.sync_these():
        # move [2] down to final search pad
        fly.straight_from_pad(-200, 0, 75, 100, "m1", tello=tellos[2])

        # move [1] to the first search pad
        fly.straight_from_pad(-200, 0, 75, 100, "m7", tello=tellos[1])

        # move [0] through the window
        fly.straight_from_pad(0, 150, 75, 100, "m7", tello=tellos[0])

    with fly.sync_these():
        fly.reorient(80, 'm-2', tello=tellos[2])
        fly.reorient(80, 'm-2', tello=tellos[1])
        fly.reorient(80, 'm-2', tello=tellos[0])

    with fly.individual_behaviours():
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=tellos[2],
            pad='m8',
            grid_width=3,
            grid_length=4
        )
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=tellos[1],
            pad='m8',
            grid_width=2,
            grid_length=4
        )
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=tellos[0],
            pad='m8',
            grid_width=2,
            grid_length=4
        )

    with fly.sync_these():
        fly.reorient(80, 'm-2', tello=tellos[2])
        fly.reorient(80, 'm-2', tello=tellos[1])
        fly.reorient(80, 'm-2', tello=tellos[0])

    with fly.sync_these():
        fly.land(tello=tellos[2])
        fly.land(tello=tellos[1])
        fly.land(tello=tellos[0])


def begin():
    with FlyTello(search_tellos) as fly:
        fly.set_top_led()
        fly.pad_detection_on()
        fly.set_pad_detection(direction='downward')
        fly.takeoff()

        with fly.sync_these():
            fly.reorient(height=80, pad="m-2", tello='All')

        with fly.individual_behaviours():
            fly.run_individual(
                go_to_room, fly=fly,
                tellos=serial_mapper.get_mac_addr_from_num(searchers))
            # fly.run_individual(land_immediately, tellos=serial_mapper.get_mac_addr_from_num([26, 22, 21, 20, 19]))
            # fly.run_individual(go_to_room, tellos=serial_mapper.get_mac_addr_from_num([21, 20, 19]))


if __name__ == "__main__":
    resp = ""
    if all_drones_ready(search_tellos, mode=1):
        resp = input(f"ALL {len(search_tellos)} DRONES READY. START? (Y/N)")
    if resp.lower() == "y":
        print("LET'S GOOOOOOOO. I'M STARTING THE BOTTOM RIGHT GROUP (THE FOOLS!!)")
        begin()
