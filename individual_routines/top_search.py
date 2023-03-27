def idle(fly, tellos, update_status):
    B1, B2, B3 = tellos
    with fly.sync_these():
        fly.straight_from_pad(100, 0, 80, 50, 'm1', tello=B1)
        fly.straight_from_pad(100, 0, 80, 50, 'm1', tello=B2)
        fly.straight_from_pad(100, 0, 80, 50, 'm1', tello=B3)

    update_status("bonus")

    with fly.sync_these():
        fly.flight_complete(tello=tellos)


def move_front(fly, tellos, update_status, get_status):
    B1, B2, B3 = tellos
    while not get_status("bonus_vacated"):
        with fly.sync_these():
            fly.reorient(height=80, pad='m-2', tello=B1)
            fly.reorient(height=80, pad='m-2', tello=B2)
            fly.reorient(height=80, pad='m-2', tello=B3)

    with fly.sync_these():
        fly.straight_from_pad(100, 0, 80, 50, 'm1', tello=B1)
        fly.straight_from_pad(100, 0, 80, 50, 'm1', tello=B2)
        fly.straight_from_pad(100, 0, 80, 50, 'm1', tello=B3)

    # B1 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=B1)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=B2)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m7', tello=B1)
        fly.reorient(height=80, pad='m1', tello=B2)
        fly.reorient(height=80, pad='m1', tello=B3)

    # B1 goes through window
    # B2 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 150, 80, 80, 'm7', tello=B1)
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=B2)
        fly.straight_from_pad(0, 100, 80, 50, 'm1', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m7', tello=B1)
        fly.reorient(height=80, pad='m7', tello=B2)
        fly.reorient(height=80, pad='m1', tello=B3)

    # B1 starts making way to bonus room
    # B2 goes through window
    # B3 goes to window
    with fly.sync_these():
        fly.straight_from_pad(200, 0, 80, 50, 'm7', tello=B1)
        fly.straight_from_pad(0, 150, 80, 80, 'm7', tello=B2)
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=B3)
        update_status('bonus')  # update that bonus party has left take off pad

    # B1 starts making way to bonus room
    # B2 goes through window
    # B3 goes to window
    with fly.sync_these():
        fly.straight_from_pad(200, 0, 80, 80, 'm7', tello=B1)
        fly.straight_from_pad(0, 150, 80, 80, 'm7', tello=B2)
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=B3)
        update_status('bonus')  # update that bonus party has left take off pad

    with fly.sync_these():
        fly.straight_from_pad(0, 150, 80, 80, 'm7', tello=B2)
        fly.straight_from_pad(0, 250, 80, 50, 'm1', tello=B3)
        fly.flight_complete(tello=B1)

    with fly.sync_these():
        fly.straight_from_pad(0, 150, 80, 80, 'm7', tello=B3)
        fly.flight_complete(tello=B2)

    with fly.sync_these():
        fly.flight_complete(tello=B3)
