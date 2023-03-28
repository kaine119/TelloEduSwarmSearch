from individual_routines.search import grid_search
from constants import *


def bonus_search_party(fly, tellos, update_status):

    B1, B2, B3 = tellos

    # B1 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 300, 80, 50, 'm1', tello=B1)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=B2)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=WINDOW, tello=B1)
        fly.reorient(height=80, pad='m1', tello=B2)
        fly.reorient(height=80, pad='m1', tello=B3)

    # B1 goes through window
    # B2 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=B1)
        fly.straight_from_pad(0, 300, 80, 50, 'm1', tello=B2)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=WINDOW, tello=B1)
        fly.reorient(height=80, pad=WINDOW, tello=B2)
        fly.reorient(height=80, pad='m1', tello=B3)

    # B1 starts making way to bonus room
    # B2 goes through window
    # B3 goes to window
    with fly.sync_these():
        fly.straight_from_pad(200, 400, 80, 50, WINDOW, tello=B1)
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=B2)
        fly.straight_from_pad(0, 300, 80, 50, 'm1', tello=B3)
        update_status('bonus')

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad=WINDOW, tello=B2)
        fly.reorient(height=80, pad=WINDOW, tello=B3)

    # B1 continues making way to bonus room
    # B2 starts making way to bonus room
    # B3 goes through window
    with fly.sync_these():
        fly.straight_from_pad(0, 300, 80, 50, 'm-2', tello=B1)
        fly.straight_from_pad(200, 400, 80, 50, WINDOW, tello=B2)
        fly.straight_from_pad(0, 150, 80, 80, WINDOW, tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad='m-2', tello=B2)
        fly.reorient(height=80, pad=WINDOW, tello=B3)

    # B1 reaches to bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(0, 250, 80, 50, 'm-2', tello=B1)
        fly.straight_from_pad(0, 300, 80, 50, 'm-2', tello=B2)
        fly.straight_from_pad(200, 400, 80, 50, WINDOW, tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=WINDOW, tello=B1)
        fly.reorient(height=80, pad='m-2', tello=B2)
        fly.reorient(height=80, pad='m-2', tello=B3)

    # B1 reaches goes through bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(150, 0, 80, 80, WINDOW, tello=B1)
        fly.straight_from_pad(0, 250, 80, 50, 'm-2', tello=B2)
        fly.straight_from_pad(0, 300, 80, 50, 'm-2', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad=WINDOW, tello=B1)
        fly.reorient(height=80, pad=WINDOW, tello=B2)
        fly.reorient(height=80, pad='m-2', tello=B3)

    # B1 reaches goes through bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(0, -150, 80, 50, WINDOW, tello=B1)
        fly.straight_from_pad(150, 0, 80, 80, WINDOW, tello=B2)
        fly.straight_from_pad(0, 250, 80, 50, 'm-2', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad=WINDOW, tello=B2)
        fly.reorient(height=80, pad=WINDOW, tello=B3)

    # B1 reaches goes through bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(250, 0, 80, 50, 'm-2', tello=B1)
        fly.straight_from_pad(0, -150, 80, 50, WINDOW, tello=B2)
        fly.straight_from_pad(150, 0, 80, 80, WINDOW, tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad='m-2', tello=B2)
        fly.reorient(height=80, pad=WINDOW, tello=B3)

    # B1 reaches goes through bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(250, 0, 80, 50, 'm-2', tello=B1)
        fly.straight_from_pad(250, 0, 80, 50, 'm-2', tello=B2)
        fly.straight_from_pad(0, -150, 80, 50, WINDOW, tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad='m-2', tello=B2)
        fly.reorient(height=80, pad='m-2', tello=B3)

    # initiate search
    with fly.individual_behaviours():
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=B3,
            pad=END,
            grid_width=3,
            grid_length=4
        )
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=B2,
            pad=END,
            grid_width=3,
            grid_length=4
        )
        fly.run_individual(
            grid_search,
            fly=fly,
            tello=B1,
            pad=END,
            grid_width=2,
            grid_length=4
        )

    # return if not found
