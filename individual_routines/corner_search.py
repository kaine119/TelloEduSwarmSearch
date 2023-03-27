def corner_search_party(fly, tellos = []):
    b1,b2,b3,b4 = tellos
    # navigate down
    with fly.sync_these():
        fly.straight_from_pad(350,0,80,50,'m1',tello=b1)
        fly.straight_from_pad(350,0,80,50,'m1',tello=b2)
        fly.straight_from_pad(350,0,80,50,'m1',tello=b3)
        fly.straight_from_pad(350,0,80,50,'m1',tello=b4)

    # navigate through the corridor horizontally (coord D-->G)
    with fly.sync_these():
        fly.straight_from_pad(300,0,80,50,'m1',tello=b1)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b2)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b3)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b4)
    # navigate through the corridor horizontally (coord G-->K)
    with fly.sync_these():
        fly.straight_from_pad(300,0,80,50,'m1',tello=b1)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b2)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b3)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b4)
    # navigate through the corridor horizontallly (coord K-->N)
    with fly.sync_these():
        fly.straight_from_pad(300,0,80,50,'m1',tello=b1)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b2)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b3)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b4)
    # separate path, 2 drones top corner 2 drones bottom corner
    with fly.sync_these():
        fly.straight_from_pad(300,0,80,50,'m1',tello=b1)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b2)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b3)
        fly.straight_from_pad(300,0,80,50,'m1',tello=b4)
    with fly.sync_these():
        fly.straight_from_pad(200,0,80,50,'m1',tello=b1)
        fly.straight_from_pad(200,0,80,50,'m1',tello=b2)
        fly.straight_from_pad(200,0,80,50,'m1',tello=b3)
        fly.straight_from_pad(200,0,80,50,'m1',tello=b4)
    # fill in the pattern to fly to search
    with fly.sync_these():
        fly.search_pattern()
        fly.search_pattern()
        fly.search_pattern()
        fly.search_pattern()
