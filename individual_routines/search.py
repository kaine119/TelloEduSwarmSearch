from serial_mapper import get_number_from_mac_addr


def generate_grid(length, width):
    """
    Generate a grid pattern to pass to `fly.search_pattern`.

    :param length: Forward distance the drone will search across.
    :param width: Sideways distance (rightwards) the drone will search across.

    Along the drawn map, `length` is along the letter axis, `width` is along the number axis.
    """
    res = []
    for row in range(length):
        for column in range(width - 1):
            res.append((0, -1 if row % 2 == 0 else 1))  # right, then left
        if row != length - 1:
            res.append((1, 0))
            if row == 0:
                res.append(None)
    return res


def grid_search(tello, pad, fly, grid_length, grid_width):
    """
    Perform a grid search independently. Should be executed in a separate thread with
    `fly.run_individual`.

    :param tello: The MAC address that should be used for grid search.
    :param pad: The target pad to find.
    :param fly: The `FlyTello` global object.
    :param grid_length: The length of the grid to search over (letter axis)
    :param grid_width: The width of the grid to search over (number axis)
    """
    found, coordinates = fly.search_pattern(
        pattern=generate_grid(grid_length, grid_width),
        dist=100,
        height=100,
        speed=50,
        pad=pad,
        tello=tello
    )
    if found:
        print(f"[Grid Search] Unit #{get_number_from_mac_addr(tello)} found a victim at {coordinates}")
        fly.reorient(height=100, pad='m-2')
        fly.land(tello=tello)
    else:
        print('[Grid Search] Bopes, going back home')
        fly.straight(-grid_length * 100,
                     grid_width * 100 if grid_length % 2 != 0 else 0,
                     0,
                     50,
                     tello=tello
                     )
        fly.reorient(height=100, pad='m-2')
