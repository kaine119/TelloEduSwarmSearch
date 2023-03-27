from fly_tello import FlyTello
from serial_mapper import get_mac_addr_from_num

my_tellos = get_mac_addr_from_num([10])
print(my_tellos)

def bonus_search_party(tellos = []):
    with fly.sync_these():
        fly.straight_from_pad(400, 0, 80, 50, 'm3', tello=tellos[0])
        fly.straight_from_pad(400, 0, 80, 50, 'm3', tello=tellos[1])
    with fly.sync_these():
        fly.reorient(height=80, pad='m7', tello=tellos[1])
        fly.reorient(height=80, pad='m7', tello=tellos[0])
    with fly.sync_these():
        fly.land(tello=tellos[0])
        fly.land(tello=tellos[1])
    with fly.sync_these():
        fly.flight_complete(tello=tellos[0])
        fly.flight_complete(tello=tellos[1])

    

def start_search_party(tellos = []):
    with fly.sync_these():
        fly.right(dist=100, tello=tellos[0])
        fly.right(dist=100, tello=tellos[1])
    with fly.sync_these():
        fly.flight_complete(tello=tellos[0])
        fly.flight_complete(tello=tellos[1])
    

with FlyTello(my_tellos) as fly:
    fly.pad_detection_on()
    fly.set_pad_detection(direction='downward')
    fly.takeoff()

    # with fly.individual_behaviours():
    #     fly.run_individual(bonus_search_party, tellos=get_mac_addr_from_num([6, 10]))
    #     fly.run_individual(start_search_party, tellos=get_mac_addr_from_num([11, 18]))
    fly.straight_from_pad(200, 0, 80, 50, 'm7')
    fly.reorient(height=80, pad='m7')
    fly.rotate_cw(angle=90)
    fly.straight_from_pad(150, 0, 80, 80, 'm7')
    fly.reorient(height=80, pad='m2')
    

    fly.land()
