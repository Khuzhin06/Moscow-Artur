import pygame

FPS = 50


def draw_circle(screen, center, radius=20):
    pygame.draw.circle(screen, 'red', center, radius)


def main():
    x_pos = y_pos = 250
    x = y = 250
    size = 501, 501
    screen = pygame.display.set_mode(size)
    running = True
    v = 100
    runninng = False
    clock = pygame.time.Clock()
    draw_circle(screen, (x_pos, y_pos))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    runninng = True
                    x, y = event.pos
        if runninng:
            screen.fill('black')
            if x > x_pos:
                x_pos += v / FPS
            if y > y_pos:
                y_pos += v / FPS
            if x < x_pos:
                x_pos -= v / FPS
            if y < y_pos:
                y_pos -= v / FPS
            draw_circle(screen, (x_pos, y_pos))
        if x == x_pos and y == y_pos:
            runninng = False
            x_pos, y_pos = x, y
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()