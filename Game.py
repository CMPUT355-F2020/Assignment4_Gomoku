import pygame

def draw_board(screen):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,0,0), (30,30,540,540), 1)
    pygame.draw.rect(screen, (193,154,107), (31,31,538,538))
    for pos in range(1,18):
        pygame.draw.line(screen, (0,0,0) ,(30, 30+30*pos), (569, 30+30*pos))
    for pos in range(1,18):
        pygame.draw.line(screen, (0,0,0) ,(30+30*pos, 30), (30+30*pos, 569))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Gomoku")
    icon = pygame.image.load('assets/gomoku.png')
    pygame.display.set_icon(icon)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_board(screen)
        pygame.display.update()
