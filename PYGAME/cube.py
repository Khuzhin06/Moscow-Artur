import pygame


def draw_cude(screen):
    width = int(input("Сторона куба. Кратное четырём, но не больше 100\n"))
    hue = int(input("Оттенок куба. Цвет. От 0 до 360\n"))
    full_width = width * 1.5
    half = width // 2
    center_x = 300 // 2 - full_width // 2
    center_y = center_x + half
    color_top = pygame.Color(0, 0, 0)
    color_top.hsva = hue, 100, 100, 100
    color_front = pygame.Color(0, 0, 0)
    color_front.hsva = hue, 100, 75, 100
    color_side = pygame.Color(0, 0, 0)
    color_side.hsva = hue, 100, 50, 100
    pygame.draw.rect(
        screen,
        color_front,
        (center_x, center_y, width, width)
    )
    pygame.draw.polygon(
        screen,
        color_top,
        (
            (center_x, center_y),
            (center_x + width // 2, center_y - width // 2),
            (center_x + width // 2 + width, center_y - width // 2),
            (center_x + width, center_y)
        )
    )
    pygame.draw.polygon(
        screen,
        color_side,
        (
            (center_x + width, center_y),
            (center_x + width // 2 + width, center_y - width // 2),
            (center_x + width // 2 + width, center_y - width // 2 + width),
            (center_x + width, center_y + width)
        )
    )


def main():
    screen = pygame.display.set_mode((300, 300))

    draw_cude(screen)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Куб")
    main()
    pygame.quit()