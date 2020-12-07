def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        ct = 1
        if window == h*bounce:
            return 1
        while h >= window:
            print("new h= ", h)
            h = h * bounce
            if h >= window:
                ct = ct + 2
        return ct
    return -1

print(bouncing_ball(3, 0.66, 1.5))