import pygame
import random


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_image = pygame.image.load("mole.png")
        mole_size = 32
        mole_x, mole_y = 0, 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + mole_size and mole_y <= mouse_y < mole_y + mole_size:
                        mole_x = random.randrange(0, 20) * mole_size
                        mole_y = random.randrange(0, 16) * mole_size

            screen.fill("light green")

            for x in range(0, 640, mole_size):
                pygame.draw.line(screen, "white", (x, 0), (x, 512))
            for y in range(0, 512, mole_size):
                pygame.draw.line(screen, "white", (0, y), (640, y))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

