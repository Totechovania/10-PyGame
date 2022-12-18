import pygame
import sys

width = 1200
height = 800
fps = 60

points = []
cords = input()
while cords != '':
    cords = [int(i) for i in cords.split()]
    cords = [cords[0], height - cords[1], 0]
    points.append(cords)
    cords = input()
points.sort()


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for point in points:
                if (point[0] - x) ** 2 + (point[1] - y) ** 2 <= 25:
                    if point[2]:
                        point[2] = 0
                    else:
                        point[2] = 1

    screen.fill((255, 255, 255))
    for i in range(1, len(points)):
        pygame.draw.line(screen, (255, 0, 0), (points[i][0], points[i][1]), (points[i - 1][0], points[i - 1][1]), 2)

    for i in points:
        if i[2]:
            color = (0, 255, 0)
        else:
            color = (0, 0, 0)
        pygame.draw.circle(screen, color, (i[0], i[1]), 5)

    pygame.display.flip()
    clock.tick(fps)
