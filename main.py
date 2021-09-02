import pygame
from math import floor
from Grid import Grid

Width = 800
Height = 800
cell_size = 10
Resolution = (Width, Height)
r, c= Width//cell_size, Height//cell_size

screen = pygame.display.set_mode(Resolution)
clock = pygame.time.Clock()
fps = 60

black, white = (0, 0, 0), (255, 255, 255)

grid = Grid(r, c, cell_size)

instatiate_radius = 70;

updateRate = 0.04;
countDownMS = updateRate;
toggleCounterMS = 0.0;
toggleThresholdMS = 0.125;

isPaused = False
run = True
while run:
    clock.tick(fps)
    pygame.display.set_caption("Falling Sand - FPS: {}".format(int(clock.get_fps())))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                isPaused = not isPaused

    sec = clock.get_rawtime()/100;
    countDownMS -= sec;
    toggleCounterMS += sec;

    if countDownMS < 0.0:
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            _x = floor(mx/cell_size)
            _y = floor(my/cell_size)
            grid.Instantiate(_x, _y, 1)

        if isPaused == False:
            screen.fill(black)
            grid.UpdateGrid()
            countDownMS = updateRate
            grid.Draw(screen)

    pygame.display.flip()

pygame.quit()
