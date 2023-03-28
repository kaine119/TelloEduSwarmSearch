from individual_routines.search import *
from individual_routines.constants import *


def bottom_search_party(fly, tellos, update_status):
    R4, R5, R6 = tellos
    with fly.sync_these():
        fly.straight_from_pad(250, 0, 80, 50, NEAREST, tello=R4)
        fly.straight_from_pad(250, 0, 80, 50, NEAREST, tello=R5)
        fly.straight_from_pad(250, 0, 80, 50, NEAREST, tello=R6)
        update_status('bottom_search')

    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R4)
        fly.reorient(height=80, pad=NEAREST, tello=R5)
        fly.reorient(height=80, pad=NEAREST, tello=R6)

    with fly.sync_these():
        fly.straight_from_pad(300, 0, 80, 50, NEAREST, tello=R4)
        fly.straight_from_pad(300, 0, 80, 50, NEAREST, tello=R5)
        fly.straight_from_pad(300, 0, 80, 50, NEAREST, tello=R6)

    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R4)
        fly.reorient(height=80, pad=NEAREST, tello=R5)
        fly.reorient(height=80, pad=NEAREST, tello=R6)

    with fly.sync_these():
        fly.straight_from_pad(300, 0, 80, 50, NEAREST, tello=R4)
        fly.straight_from_pad(300, 0, 80, 50, NEAREST, tello=R5)
        fly.straight_from_pad(300, 0, 80, 50, NEAREST, tello=R6)

    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R4)
        fly.reorient(height=80, pad=NEAREST, tello=R5)
        fly.reorient(height=80, pad=NEAREST, tello=R6)

    # R4 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 300, 80, 50, WINDOW, tello=R4)
        fly.straight_from_pad(0, 100, 80, 50, NEAREST, tello=R5)
        fly.straight_from_pad(0, 100, 80, 50, NEAREST, tello=R6)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=WINDOW, tello=R4)
        fly.reorient(height=80, pad=NEAREST, tello=R5)
        fly.reorient(height=80, pad=NEAREST, tello=R6)

    # R4 goes through window
    # R5 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=R4)
        fly.straight_from_pad(0, 300, 80, 50, NEAREST, tello=R5)
        fly.straight_from_pad(0, 100, 80, 50, NEAREST, tello=R6)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=WINDOW, tello=R4)
        fly.reorient(height=80, pad=WINDOW, tello=R5)
        fly.reorient(height=80, pad=NEAREST, tello=R6)

    # R4 goes top
    # R5 goes through window
    # R6 goes to window
    with fly.sync_these():
        fly.straight_from_pad(-250, 0, 80, 80, NEAREST, tello=R4)
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=R5)
        fly.straight_from_pad(0, 300, 80, 50, WINDOW, tello=R6)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R4)
        fly.reorient(height=80, pad=WINDOW, tello=R5)
        fly.reorient(height=80, pad=WINDOW, tello=R6)

    # R4 goes top
    # R5 goes top
    # R6 goes through window
    with fly.sync_these():
        fly.straight_from_pad(-300, 0, 80, 80, NEAREST, tello=R4)
        fly.straight_from_pad(-250, 0, 80, 80, NEAREST, tello=R5)
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=R6)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R4)
        fly.reorient(height=80, pad=NEAREST, tello=R5)
        fly.reorient(height=80, pad=WINDOW, tello=R6)

    # R4 goes idle
    # R5 goes top
    # R6 goes through window
    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R4)
        fly.straight_from_pad(-250, 0, 80, 80, NEAREST, tello=R5)
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=R6)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R4)
        fly.reorient(height=80, pad=NEAREST, tello=R5)
        fly.reorient(height=80, pad=WINDOW, tello=R6)

    # initiate search
    # return if not found
