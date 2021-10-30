class Setting:
    width   = 800
    height  = 800
    size    = (width, height)
    fps     = 60
    window = None

    cell_size = 20
    cols = width//cell_size
    rows = height//cell_size

    EMPTY   = 0
    SAND    = 1
    WATER   = 2
    ROCK    = 3
    
    Colors  = [(0, 0, 0), (255, 255, 0), (0, 0, 255), (100, 100, 100)]
