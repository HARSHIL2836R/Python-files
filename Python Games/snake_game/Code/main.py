import pygame
from pygame.locals import *
import time
import random

# for the console window
print('This is the console..... you need not worry about it....')
print('if the game is not starting, move the resources folder to the folder where the game is.')

SIZE = 40
RESOLUTION_X = 1200
RESOLUTION_Y = 600


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, int(RESOLUTION_X / SIZE) - 1) * SIZE
        self.y = random.randint(1, int(RESOLUTION_Y / SIZE) - 1) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):

        # update body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()


def play_background_music():
    pygame.mixer.music.load("resources/bg_music_1.mp3")
    pygame.mixer.music.play()


class Game:
    @staticmethod
    def agreed():
        return False

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("A simple Game")

        pygame.mixer.init()
        play_background_music()
        self.surface = pygame.display.set_mode((RESOLUTION_X, RESOLUTION_Y))
        self.TIME = 0.2
        self.surface.fill((110, 110, 1))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    @staticmethod
    def is_collision(x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (1000, 10))

    @staticmethod
    def play_sound(sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake colliding with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("1_snake_game_resources_ding")
            self.snake.increase_length()
            self.apple.move()
            self.TIME -= 0.001

        # snake colliding with itself
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("1_snake_game_resources_crash")
                raise Exception('Game over')

        # snake colliding with the boundaries of the window
        if not (0 <= self.snake.x[0] <= RESOLUTION_X and 0 <= self.snake.y[0] <= RESOLUTION_Y):
            self.play_sound('crash')
            raise Exception("Hit the boundary error")

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render(f"To play again press ENTER, to exit press ESCAPE!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()

        pygame.mixer.music.pause()

    def game_pause(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render("The game is paused, to resume, press RETURN / ENTER.", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def prologue(self):
        self.render_background()
        font = pygame.font.SysFont('Comic Sans MS', 30)
        line1 = font.render("You are going to play a game similar to the classic 'snake and apple game', ", True,
                            (255, 255, 255))
        self.surface.blit(line1, (50, 100))
        line2 = font.render("it is nothing more than a casual version of it, made with the aim to develop python ",
                            True, (255, 255, 255))
        self.surface.blit(line2, (50, 150))
        line3 = font.render("skills. Hope you enjoy it.", True, (255, 255, 255))
        self.surface.blit(line3, (50, 200))
        line4 = font.render("Explore rules on your own and score the best.", True, (255, 255, 255))
        self.surface.blit(line4, (50, 400))
        line5 = font.render("Press ENTER / RETURN to start the Game! And press ESC to escape any time.", True,
                            (255, 255, 255))
        self.surface.blit(line5, (50, 450))
        line6 = font.render("To pause the game anytime, press SPACEBAR.", True,
                            (255, 255, 255))
        self.surface.blit(line6, (50, 500))
        font2 = pygame.font.SysFont('Consolas', 20)
        end = font2.render("Made by Harshil Solanki", True, (255, 255, 255))
        self.surface.blit(end, (900, 550))
        pygame.display.flip()

    def run(self):
        self.prologue()
        pause = True
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.game_pause()
                        pause = True
                        if event.key == K_RETURN:
                            pause = False

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(self.TIME)


if __name__ == "__main__":
    game = Game()
    game.run()
