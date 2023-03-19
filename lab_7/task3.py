import pygame

pygame.init()
screen_size = screen_width, screen_height = 600, 400
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Moving Ball')

clock = pygame.time.Clock()

pygame.mixer.init()



ball_radius = 25
ball_color = (54, 119, 224)
ball_x = 50
ball_y = 50
step = 20
run = True
while run:
    screen.fill((255, 255, 255))
    ball = pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT] and ball.right <= screen_width - ball_radius:
        ball_x += step
    if key[pygame.K_LEFT] and ball.left >= ball_radius:
        ball_x -= step
    if key[pygame.K_UP] and ball.top >= ball_radius:
        ball_y -= step
    if key[pygame.K_DOWN] and ball.bottom <= screen_height - ball_radius:
        ball_y += step


    clock.tick(30)

    pygame.display.flip()
