import pygame


def main():
    try:
        a, n = map(int, input().split())  # or ('.' in n) or (',' in n) or ('.' in a) or (',' in a)
        step = a // n
        if a % n != 0 or a <= 0 or n <= 0:
            a = a / 0
        screen = pygame.display.set_mode((a, a))
        for i in range(n + 1):
            for j in range(n // 2 + 1):
                if i % 2 == 0:
                    pygame.draw.rect(
                        screen,
                        pygame.Color('white'),
                        (j * step * 2, a - i * step, step, step)
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        pygame.Color('white'),
                        (j * step * 2 + step, a - i * step, step, step)
                    )

        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
    except Exception:
        print('Неверный формат')


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Крест")
    main()
    pygame.quit()