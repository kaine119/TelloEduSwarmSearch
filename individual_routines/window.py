def pass_window(fly, tellos=[], pad="m7"):
    with fly.sync_these():
        fly.straight_from_pad(200, 0, 80, 50, pad)
        fly.reorient(height=80, pad=pad)
        fly.rotate_cw(angle=90)
        fly.straight_from_pad(150, 0, 80, 80, pad)
        fly.reorient(height=80, pad=pad)
