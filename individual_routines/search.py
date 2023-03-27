import serial_mapper

GRID_PATTERN = [
    # first row
    (0, -1),
    (0, -1),
    (0, -1),
    (1,  0),

    # second row
    (0,  1),
    (0,  1),
    (0,  1),
    (1,  0),
    None,

    # third row
    (0, -1),
    (0, -1),
    (0, -1),
    (1,  0),

    # fourth row
    (0,  1),
    (0,  1),
    (0,  1),
    (1,  0),
    None,

    # last row
    (0, -1),
    (0, -1),
    (0, -1),
]


def grid_search(tello, pad, fly):
    """
    Perform a grid search independently. Should be executed in a separate thread with
    `fly.run_individual`.

    :param tello: The MAC address that should be used for grid search.
    :param pad: The target pad to find.
    :param fly: The `FlyTello` global object.
    """
    found, coordinates = fly.search_pattern(
        pattern=GRID_PATTERN,
        dist=100,
        height=100,
        speed=50,
        pad=pad,
        tello=tello
    )
    if found:
        print(f"[Grid Search] Found a victim at {coordinates}")
        fly.reorient(height=100, pad='m-2')
        fly.land(tello=tello)
    else:
        print('[Grid Search] Bopes, going back home')
        fly.straight(-435, 300, 0, 50, tello=tello)
        fly.reorient(height=100, pad='m-2')