import pygame

FPS = 50


def draw_circle(screen, center, radius=20):
    pygame.draw.circle(screen, 'red', center, radius)


def run(screen, v, x, y, x_pos, y_pos):
    while x != x_pos and y != y_pos:
        clock = pygame.time.Clock()
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
        pygame.display.flip()
        clock.tick(FPS)

def main():
    x_pos = y_pos = 250
    size = 501, 501
    screen = pygame.display.set_mode(size)
    running = True
    v = 100
    clock = pygame.time.Clock()
    draw_circle(screen, (x_pos, y_pos))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    run(screen, v, x, y, x_pos, y_pos)
                    x_pos, y_pos = x, y
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()