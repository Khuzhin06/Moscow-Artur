import pygame


def main():
    n = int(input("Введите кол-во эллипсов: "))
    screen = pygame.display.set_mode((300, 300))

    step = 300 // n // 2
    w = 300
    for i in range(n):
        pygame.draw.ellipse(
            screen,
            pygame.Color('white'),
            (i * step, 0, w, 300),
            width=1
        )
        w -= step * 2
    w = 300
    for i in range(n):
        pygame.draw.ellipse(
            screen,
            pygame.Color('white'),
            (0, i * step, 300, w),
            width=1
        )
        w -= step * 2

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Крест")
    main()
    pygame.quit()