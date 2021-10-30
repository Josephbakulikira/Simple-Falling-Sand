import pygame
from math import floor
from Grid import Grid
from setting import Setting

setting = Setting()

screen = pygame.display.set_mode(setting.size)
setting.window = screen
clock = pygame.time.Clock()

grid = Grid(setting)

instatiate_radius = 70;

updateRate = 0.05;
countDownMS = updateRate;
toggleCounterMS = 0.0;
toggleThresholdMS = 0.125;
# screen.fill(setting.black)

isPaused = False
run = True
while run:
    clock.tick(setting.fps)
    pygame.display.set_caption("Falling Sand - FPS: {}".format(int(clock.get_fps())))
    # handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                isPaused = not isPaused
            if event.key == pygame.K_r:
                grid.ResetGrid()

    sec = clock.get_rawtime()/100;
    countDownMS -= sec;
    toggleCounterMS += sec;

    if countDownMS < 0.0:


        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            _x = floor(mx/setting.cell_size)
            _y = floor(my/setting.cell_size)
            grid.Instantiate(_x, _y, 1)

        if isPaused == False:
            grid.UpdateGrid()
            countDownMS = updateRate
            grid.Draw()

    pygame.display.flip()

pygame.quit()
