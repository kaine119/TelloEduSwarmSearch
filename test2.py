from typing import List
from fly_tello import FlyTello
from individual_routines.search import grid_search
import serial_mapper
search_tellos = serial_mapper.get_mac_addr_from_num([
    26,
    # 25,
    # 24,
    # 23,
    # 22,
    # 21,
    # 20,
    # 19,
])


def land_immediately(tellos: List[str]):
    for tello in tellos:
        fly.land(tello)


def go_to_room(tellos: List[str]):
    with fly.sync_these():
        fly.straight_from_pad(360, 0, 80, 50, 'm-2', tello=tellos[2])
        fly.straight_from_pad(360, 0, 80, 50, 'm-2', tello=tellos[1])
        fly.straight_from_pad(360, 0, 80, 50, 'm-2', tello=tellos[0])

    with fly.sync_these():
        fly.reorient(80, 'm-2', tello=tellos[2])
        fly.reorient(80, 'm-2', tello=tellos[1])
        fly.reorient(80, 'm-2', tello=tellos[0])

    with fly.sync_these():
        fly.straight_from_pad(400, 0, 80, 50, 'm-2', tello=tellos[2])
        fly.straight_from_pad(400, 0, 80, 50, 'm-2', tello=tellos[1])
        fly.straight_from_pad(400, 0, 80, 50, 'm-2', tello=tellos[0])

    with fly.sync_these():
        fly.reorient(80, 'm1', tello=tellos[2])
        fly.reorient(80, 'm1', tello=tellos[1])
        fly.reorient(80, 'm7', tello=tellos[0])

    with fly.sync_these():
        fly.straight_from_pad(0, 150, 75, 100, "m7", tello=tellos[2])
        fly.straight_from_pad(0, 100, 75, 100, "m1", tello=tellos[1])
        fly.straight_from_pad(0, 100, 75, 100, "m1", tello=tellos[0])

    with fly.sync_these():
        fly.straight_from_pad(-200, 0, 75, 100, "m7", tello=tellos[2])
        fly.straight_from_pad(0, 150, 75, 100, "m7", tello=tellos[1])
        fly.straight_from_pad(0, 100, 75, 100, "m1", tello=tellos[0])

    with fly.sync_these():
        fly.straight_from_pad(-200, 0, 75, 100, "m1", tello=tellos[2])
        fly.straight_from_pad(-200, 0, 75, 100, "m7", tello=tellos[1])
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
            grid_width=3,
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


with FlyTello(search_tellos) as fly:
    fly.set_top_led()
    fly.takeoff()
    fly.reorient(height=100, pad='m-2')
    with fly.individual_behaviours():
        fly.run_individual(land_immediately, tellos=serial_mapper.get_mac_addr_from_num([26]))
        # fly.run_individual(land_immediately, tellos=serial_mapper.get_mac_addr_from_num([26, 22, 21, 20, 19]))
        # fly.run_individual(go_to_room, tellos=serial_mapper.get_mac_addr_from_num([21, 20, 19]))
