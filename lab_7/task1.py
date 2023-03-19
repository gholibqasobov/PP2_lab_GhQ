import pygame, datetime

pygame.init()

path = 'C:/Users/qasob/OneDrive/Documents/GitHub/PP2_lab_GhQ/lab_7/data/img/'

screen_size = screen_width, screen_height = 800, 800
center = (screen_width/2, screen_height/2)
screen = pygame.display.set_mode(screen_size)

clock_img = pygame.transform.scale(pygame.image.load(path + 'main-clock.png'), screen_size)

rot_clock = clock_img.get_rect(center=center)
sec = pygame.image.load(path + 'left-hand.png')
min = pygame.image.load(path + 'right-hand.png')

run = True
while run:

    screen.fill('white')
    screen.blit(clock_img, rot_clock)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    time = datetime.datetime.now()
    minutes, seconds = time.minute, time.second

    rot_sec = pygame.transform.rotate(sec, (-6 * seconds) + 90)
    rot_sec_rect = rot_sec.get_rect(center=center)
    screen.blit(rot_sec, rot_sec_rect)

    rot_min = pygame.transform.rotate(min, (-6 * minutes) + 90)
    rot_min_rect = rot_min.get_rect(center=center)
    screen.blit(rot_min, rot_min_rect)


    pygame.display.flip()
    pygame.quit()
