from individual_routines.search import grid_search

# def bonus_search_party(fly, tellos, update_status):
def bonus_search_party(fly, tellos):

    B1, B2, B3 = tellos

    # B1 goes to window
    with fly.sync_these():
        fly.straight_from_pad(0, 300, 80, 50, 'm1', tello=B1)
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
        fly.straight_from_pad(0, 300, 80, 50, 'm1', tello=B2)
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
        fly.straight_from_pad(200, 400, 80, 50, 'm7', tello=B1)
        fly.straight_from_pad(0, 150, 80, 80, 'm7', tello=B2)
        fly.straight_from_pad(0, 300, 80, 50, 'm1', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad='m7', tello=B2)
        fly.reorient(height=80, pad='m7', tello=B3)

    # B1 continues making way to bonus room
    # B2 starts making way to bonus room
    # B3 goes through window
    with fly.sync_these():
        fly.straight_from_pad(0, 300, 80, 50, 'm-2', tello=B1)
        fly.straight_from_pad(200, 400, 80, 50, 'm7', tello=B2)
        fly.straight_from_pad(0, 150, 80, 80, 'm7', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad='m-2', tello=B2)
        fly.reorient(height=80, pad='m7', tello=B3)

    # B1 reaches to bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(0, 250, 80, 50, 'm-2', tello=B1)
        fly.straight_from_pad(0, 300, 80, 50, 'm-2', tello=B2)
        fly.straight_from_pad(200, 400, 80, 50, 'm7', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m7', tello=B1)
        fly.reorient(height=80, pad='m-2', tello=B2)
        fly.reorient(height=80, pad='m-2', tello=B3)

    # B1 reaches goes through bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(150, 0, 80, 80, 'm7', tello=B1)
        fly.straight_from_pad(0, 250, 80, 50, 'm-2', tello=B2)
        fly.straight_from_pad(0, 300, 80, 50, 'm-2', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m7', tello=B1)
        fly.reorient(height=80, pad='m7', tello=B2)
        fly.reorient(height=80, pad='m-2', tello=B3)

    # B1 reaches goes through bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(0, -150, 80, 50, 'm7', tello=B1)
        fly.straight_from_pad(150, 0, 80, 80, 'm7', tello=B2)
        fly.straight_from_pad(0, 250, 80, 50, 'm-2', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad='m7', tello=B2)
        fly.reorient(height=80, pad='m7', tello=B3)

    # B1 reaches goes through bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(250, 0, 80, 50, 'm-2', tello=B1)
        fly.straight_from_pad(0, -150, 80, 50, 'm7', tello=B2)
        fly.straight_from_pad(150, 0, 80, 80, 'm7', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad='m-2', tello=B2)
        fly.reorient(height=80, pad='m7', tello=B3)

    # B1 reaches goes through bonus room window
    # B2 continues making way to bonus room
    # B3 starts making way to bonus room
    with fly.sync_these():
        fly.straight_from_pad(250, 0, 80, 50, 'm-2', tello=B1)
        fly.straight_from_pad(250, 0, 80, 50, 'm-2', tello=B2)
        fly.straight_from_pad(0, -150, 80, 50, 'm7', tello=B3)

    # reorient
    with fly.sync_these():
        fly.reorient(height=80, pad='m-2', tello=B1)
        fly.reorient(height=80, pad='m-2', tello=B2)
        fly.reorient(height=80, pad='m-2', tello=B3)

    with fly.sync_these():
        grid_search(B1, 'm8', fly, 2, 3)
        grid_search(B2, 'm8', fly, 3, 3)
        grid_search(B3, 'm8', fly, 2, 3)
