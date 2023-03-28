from individual_routines.search import *
from individual_routines.constants import *


def top_search_party(fly, tellos, update_status, get_status):
    R1, R2, R3 = tellos
    while not get_status("bonus_vacated"):
        with fly.sync_these():
            fly.reorient(height=80, pad=NEAREST, tello=R1)
            fly.reorient(height=80, pad=NEAREST, tello=R2)
            fly.reorient(height=80, pad=NEAREST, tello=R3)

    with fly.sync_these():
        fly.straight_from_pad(100, 0, 80, 50, NEAREST, tello=R1)
        fly.straight_from_pad(100, 0, 80, 50, NEAREST, tello=R2)
        fly.straight_from_pad(100, 0, 80, 50, NEAREST, tello=R3)

    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R1)
        fly.reorient(height=80, pad=NEAREST, tello=R2)
        fly.reorient(height=80, pad=NEAREST, tello=R3)

    # R1 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 300, 80, 50, WINDOW, tello=R1)
        fly.straight_from_pad(0, 100, 80, 50, NEAREST, tello=R2)
        fly.straight_from_pad(0, 100, 80, 50, NEAREST, tello=R3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=WINDOW, tello=R1)
        fly.reorient(height=80, pad=NEAREST, tello=R2)
        fly.reorient(height=80, pad=NEAREST, tello=R3)

    # R1 goes through window
    # R2 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=R1)
        fly.straight_from_pad(0, 300, 80, 50, NEAREST, tello=R2)
        fly.straight_from_pad(0, 100, 80, 50, NEAREST, tello=R3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=WINDOW, tello=R1)
        fly.reorient(height=80, pad=WINDOW, tello=R2)
        fly.reorient(height=80, pad=NEAREST, tello=R3)

    # R1 goes top
    # R2 goes through window
    # R3 goes to window
    with fly.sync_these():
        fly.straight_from_pad(-200, 0, 80, 80, NEAREST, tello=R1)
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=R2)
        fly.straight_from_pad(0, 300, 80, 50, WINDOW, tello=R3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R1)
        fly.reorient(height=80, pad=WINDOW, tello=R2)
        fly.reorient(height=80, pad=WINDOW, tello=R3)

    # R1 idles
    # R2 goes bottom
    # R3 goes through window
    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R1)
        fly.straight_from_pad(300, 0, 80, 80, NEAREST, tello=R2)
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=R3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=NEAREST, tello=R1)
        fly.reorient(height=80, pad=NEAREST, tello=R2)
        fly.reorient(height=80, pad=WINDOW, tello=R3)

    with fly.individual_behaviours():
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=R1,
            pad=END,
            grid_width=2,
            grid_length=4
        )
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=R2,
            pad=END,
            grid_width=3,
            grid_length=4
        )
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=R3,
            pad=END,
            grid_width=2,
            grid_length=4
        )
