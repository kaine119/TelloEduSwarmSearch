from constants import *


def corner_search_party(fly, tellos, update_status):
    b1, b2, b3, b4 = tellos
    # navigate down
    with fly.sync_these():
        fly.straight_from_pad(350, 0, 80, 50, 'm1', tello=b1)
        fly.straight_from_pad(350, 0, 80, 50, 'm1', tello=b2)
        fly.straight_from_pad(350, 0, 80, 50, 'm1', tello=b3)
        fly.straight_from_pad(350, 0, 80, 50, 'm1', tello=b4)
        update_status('corner')

    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=b1)
        fly.reorient(height=80, pad=NEAREST, tello=b2)
        fly.reorient(height=80, pad=NEAREST, tello=b3)
        fly.reorient(height=80, pad=NEAREST, tello=b4)

    # navigate through the corridor horizontally (coord D-->G)
    with fly.sync_these():
        fly.straight_from_pad(0, 350, 80, 50, 'm1', tello=b1)
        fly.straight_from_pad(0, 350, 80, 50, 'm1', tello=b2)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=b3)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=b4)

    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=b1)
        fly.reorient(height=80, pad=NEAREST, tello=b2)
        fly.reorient(height=80, pad=NEAREST, tello=b3)
        fly.reorient(height=80, pad=NEAREST, tello=b4)

    # navigate through the corridor horizontally (coord G-->K)
    with fly.sync_these():
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=b1)
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=b2)
        fly.straight_from_pad(0, 350, 80, 50, 'm1', tello=b3)
        fly.straight_from_pad(0, 350, 80, 50, 'm1', tello=b4)

    # navigate through the corridor horizontally (coord G-->K)
    with fly.sync_these():
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=b1)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=b2)
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=b3)
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=b4)

    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=b1)
        fly.reorient(height=80, pad=NEAREST, tello=b2)
        fly.reorient(height=80, pad=NEAREST, tello=b3)
        fly.reorient(height=80, pad=NEAREST, tello=b4)

    # navigate through the corridor horizontallly (coord K-->N)
    with fly.sync_these():
        fly.straight_from_pad(-300, 0, 80, 50, 'm1', tello=b1)
        fly.straight_from_pad(-300, 0, 80, 50, 'm1', tello=b2)
        fly.straight_from_pad(300, 0, 80, 50, 'm1', tello=b3)
        fly.straight_from_pad(300, 0, 80, 50, 'm1', tello=b4)

    # separate path, 2 drones top corner 2 drones bottom corner
    with fly.sync_these():
        fly.straight_from_pad(-200, 0, 80, 50, 'm1', tello=b1)
        fly.straight_from_pad(-200, 0, 80, 50, 'm1', tello=b2)
        fly.straight_from_pad(200, 0, 80, 50, 'm1', tello=b3)
        fly.straight_from_pad(200, 0, 80, 50, 'm1', tello=b4)

    # fill in the pattern to fly to search
    # with fly.sync_these():
    #     fly.search_pattern()
    #     fly.search_pattern()
    #     fly.search_pattern()
    #     fly.search_pattern()

    # return if none found
