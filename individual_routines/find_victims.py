from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num

# Bonus Drones


def bonus_search_party(fly, tellos=[]):
    S1, S2, S3 = tellos
    with fly.sync_these():
        fly.straight_from_pad(400, 0, 80, 50, 'm-2', tello=tellos[0])
        fly.reorient(height=80, pad='m7', tello=tellos[1])
    with fly.sync_these():
        fly.straight_from_pad(400, 0, 80, 50, 'm-2', tello=tellos[1])
        fly.reorient(height=80, pad='m7', tello=tellos[0])
    with fly.sync_these():
        fly.land(tello=tellos[0])
        fly.land(tello=tellos[1])
    with fly.sync_these():
        fly.flight_complete(tello=tellos[0])
        fly.flight_complete(tello=tellos[1])


def start_search_party(fly, tellos=[]):
    with fly.sync_these():
        fly.right(dist=100, tello=tellos[0])
        fly.right(dist=100, tello=tellos[1])
    with fly.sync_these():
        fly.flight_complete(tello=tellos[0])
        fly.flight_complete(tello=tellos[1])


def bottom_search_party(fly, tellos=[]):
    print('test')


def top_search_party(fly, tellos=[]):
    print('test')


def outside_search_party(fly, tellos=[]):
    print('test')


def landing_party(fly, tellos=[]):
    print('test')
