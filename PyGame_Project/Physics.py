import pygame
from random import choice

FPS = 20  # количество кадров в секунду
SIZE = WIDTH, HEIGHT = 800, 400


class Board:
    # создание поля
    def __init__(self, width):
        self.width = width
        self.board = [
            0 for _ in range(width)
        ]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.live = 3

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self,  screen):
        end_x = self.width * self.cell_size + self.left
        for x in range(self.left, end_x, self.cell_size):
            col = (x - self.left) // self.cell_size
            pygame.draw.rect(
                screen,
                'white',
                (x, 320, self.cell_size, self.cell_size),
                width=1
            )
            if self.board[col] == 'a':
                pygame.draw.line(
                    screen,
                    'blue',
                    (x + 4, 364),
                    (x + self.cell_size - 8, 320 + self.cell_size - 8),
                    width=2
                )
                pygame.draw.line(
                    screen,
                    'blue',
                    (x + 4, 364),
                    (x + self.cell_size - 8, 328),
                    width=2
                )
            if self.board[col] == 's':
                pygame.draw.line(
                    screen,
                    'yellow',
                    (x - 8 + self.cell_size, 324),
                    (x + self.cell_size // 2, 392),
                    width=2
                )
                pygame.draw.line(
                    screen,
                    'yellow',
                    (x + 8, 324),
                    (x + self.cell_size // 2, 392),
                    width=2
                )
            if self.board[col] == 'w':
                pygame.draw.line(
                    screen,
                    'green',
                    (x - 8 + self.cell_size, 392),
                    (x + self.cell_size // 2, 324),
                    width=2
                )
                pygame.draw.line(
                    screen,
                    'green',
                    (x + 8, 392),
                    (x + self.cell_size // 2, 324),
                    width=2
                )
            if self.board[col] == 'd':
                pygame.draw.line(
                    screen,
                    'red',
                    (x + 75, 364),
                    (x + 8, 320 + self.cell_size - 8),
                    width=2
                )
                pygame.draw.line(
                    screen,
                    'red',
                    (x + 75, 364),
                    (x + 8, 328),
                    width=2
                )
            if self.board[col] == 'Yes':
                pygame.draw.rect(
                    screen,
                    'green',
                    (x, 320, 80, 80),
                )
            elif self.board[col] == 'No':
                pygame.draw.rect(
                    screen,
                    'red',
                    (x, 320, 80, 80),
                )

    def turn_left(self):
        choi = choice(['a', 'w', 'd', 's'])
        self.board.pop(0)
        self.board.append(choi)

    def click(self, a):
        print(a)
        if a == self.board[0]:
            self.board[0] = 'Yes'
        elif self.board[0] != 0 and self.board[0] != 'Yes' and self.board[0] != 'No':
            self.board[0] = 'No'
            self.live -= 1


def main():
    pygame.display.set_caption('Клетчатое поле начало')
    screen = pygame.display.set_mode(SIZE)

    clock = pygame.time.Clock()
    running = True
    turn = 0  # Нужно для подсчета скорости движения стрелок

    # поле 5 на 7
    board = Board(10)
    board.set_view(0, 320, 80)
    board.turn_left()
    end = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            board.click('a')
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            board.click('d')
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            board.click('w')
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            board.click('s')

        turn = turn % FPS + 1
        if FPS / turn == 1:  # был тут end вместо 1
            board.turn_left()
            # end += 1

        if not board.live:
            running = False
        screen.fill('black')
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()

