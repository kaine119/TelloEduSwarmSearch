from individual_routines.constants import *


def landers_full_send(fly, tellos):
    with fly.sync_these():
        for tello in tellos:
            fly.straight_from_pad(400, 0, 80, 80, NEAREST, tello=tello)

    with fly.sync_these():
        for tello in tellos:
            fly.reorient(height=80, pad=NEAREST, tello=tello)

    with fly.sync_these():
        for tello in tellos:
            fly.straight_from_pad(450, 0, 80, 80, NEAREST, tello=tello)

    with fly.sync_these():
        for tello in tellos:
            fly.reorient(height=80, pad=NEAREST, tello=tello)

    with fly.sync_these():
        for tello in tellos:
            fly.land(tello=tello)
            fly.flight_complete(tello=tello)


# def landers_top_send(fly, tellos=[]):
#     with fly.sync_these():
#         fly.straight_from_pad(300, 0, 80, 50, 'm1', tello=tellos)
#         fly.reorient(height=80, pad='m-2', tello=tellos)
#     with fly.sync_these():
#         fly.straight_from_pad(250, 0, 80, 50, 'm1', tello=tellos)
#         fly.reorient(height=80, pad='m-2', tello=tellos)
#     with fly.sync_these():
#         fly.straight_from_pad(400, 0, 80, 50, 'm1', tello=tellos)
#         fly.reorient(height=80, pad='m-2', tello=tellos)
#     with fly.sync_these():
#         fly.flight_complete(tello=tellos)


# def landers_bottom_send(fly, tellos=[]):
#     with fly.sync_these():
#         fly.straight_from_pad(350, 0, 80, 50, 'm1', tello=tellos)
#         fly.reorient(height=80, pad='m-2', tello=tellos)
#     with fly.sync_these():
#         fly.straight_from_pad(400, 0, 80, 50, 'm1', tello=tellos)
#         fly.reorient(height=80, pad='m-2', tello=tellos)
#     with fly.sync_these():
#         fly.straight_from_pad(300, 0, 80, 50, 'm1', tello=tellos)
#         fly.reorient(height=80, pad='m-2', tello=tellos)
#     with fly.sync_these():
#         fly.flight_complete(tello=tellos)
