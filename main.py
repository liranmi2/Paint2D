
import pygame


# def draw_some(screen):
#     x, y = 10, 620
#     d_range = max(abs(x), abs(y))
#
#     # square
#     for i in range(d_range):
#         screen.set_at((50+i, 50), (0, 0, 0))
#         screen.set_at((100, 50+i), (0, 0, 0))
#         screen.set_at((50+i, 100), (0, 0, 0))
#         screen.set_at((50, 50+i), (0, 0, 0))
#
#     # triangle
#     j = 24
#     for i in range(26):
#         screen.set_at((120+i, 100), (0, 0, 0))
#         screen.set_at((120+i+j, 100), (0, 0, 0))
#         screen.set_at((145+i, 50+i*2), (0, 0, 0))
#         screen.set_at((145+i, 50+i*2-1), (0, 0, 0))
#         screen.set_at((145-i, 50+i*2), (0, 0, 0))
#         screen.set_at((145-i, 50+i*2-1), (0, 0, 0))


def plot_circle_points(Xc, Yc, x, y):
    screen.set_at((Xc+x, Yc+y), (255, 0, 0))
    screen.set_at((Xc+x, Yc-y), (255, 0, 0))
    screen.set_at((Xc-x, Yc+y), (255, 0, 0))
    screen.set_at((Xc-x, Yc-y), (255, 0, 0))
    screen.set_at((Xc+y, Yc+x), (255, 0, 0))
    screen.set_at((Xc+y, Yc-x), (255, 0, 0))
    screen.set_at((Xc-y, Yc+x), (255, 0, 0))
    screen.set_at((Xc-y, Yc-x), (255, 0, 0))


def my_circle(Xc, Yc, r):
    x, y = 0,  r
    p = 3 - 2 * r
    while x <= y:
        plot_circle_points(Xc, Yc, x, y)
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1
        x += 1


def dda_line(x1, y1, x2, y2, color):
    dx, dy = (x2 - x1), (y2 - y1)
    d_range = max(abs(dx), abs(dy))
    try:
        dx, dy = dx/d_range, dy/d_range
    except ZeroDivisionError:
        dx, dy = 10, 0.1
        pass
    print("d_range",d_range)
    for i in range(d_range):
        # screen.set_at((round(x1), round(y1)), (255 - (i % 255), i % 255, (i % 255)))
        screen.set_at((round(x1), round(y1)), color)
        x1 += dx
        y1 += dy


def draw_arrow():
    for i in range(20):
        dda_line(10+i, 640, 20, 620, (0, 0, 0))
    for i in range(20):
        dda_line(10+i, 650, 20, 670, (0, 0, 0))


def bresenham_line(screen, x1, y1, x2, y2, color):
    # f = False
    # if (x2-x1) < 0 or (y2-y1) < 0:
    #     # f = True
    #     x1, y1, x2, y2 = x2, y2, x1, y1
    dx, dy = x2 - x1, y2 - y1
    d_range = max(abs(dx), abs(dy))
    # dx, dy = abs(x2 - x1) / d_range, abs(y2 - y1) / d_range
    err = dy/dx - 0.5 if dx > dy else dx/dy - 0.5
    # errp = 2 * dy - dx
    xp = x1
    yp = y1
    d = 1 if y1 < y2 else -1
    f = 1 if x1 < x2 else -1
    # screen.set_at((xp, yp), color)
    print("dx:", dx, "dy:", dy,"d:",d)
    print(xp, yp, "to", x2, y2)
    for _ in range(d_range):
        # print(err)
        screen.set_at((xp, yp), color)
        # if errp > 0:
        if err > 0:
            yp = yp + d
            # errp = errp - 2 * dx
            err = err - 1
        xp = xp + f
        # errp = errp + 2 * dy
        err += dy/dx if dx > dy else dx/dy


def bezier_curve(x1, y1, x2, y2, x3, y3, x4, y4, n):
    ax = 3*x2 + x4 - 3*x3 - x1
    bx = 3*x1 - 6*x2 + 3*x3
    cx = 3*x2 - 3*x1
    dx = x1
    ay = 3*y2 + y4 - 3*y3 - y1
    by = 3*y1 - 6*y2 + 3*y3
    cy = 3*y2 - 3*y1
    dy = y1
    t = 0
    points = list()
    points.append((round(x1), round(y1)))
    for _ in range(n):
        t += 1/n
        xt = ax * (t**3) + bx * (t**2) + cx * t + dx
        yt = ay * (t**3) + by * (t**2) + cy * t + dy
        points.append((round(xt), round(yt)))
    for i in range(len(points)-1):
        print(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
        dda_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], (0, 0, 0))


def draw(x1, y1, x2, y2, n):
    Xc, Yc = round(x1 + (x2 - x1) / 2), round(y1 + (y2 - y1) / 2)
    r = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 / 2)
    x3, x4 = round(x2 + r / 2), round(x1 - r / 2)
    y3, y4 = y1, y2
    dda_line(x1, y1, x2, y2, (0, 0, 255))
    dda_line(x1, y1, x3, y3, (0, 0, 255))
    dda_line(x2, y2, x4, y4, (0, 0, 255))
    dda_line(x1, y1, x4, y4, (0, 0, 255))
    dda_line(x2, y2, x3, y3, (0, 0, 255))
    dda_line(x3, y3, x4, y4, (0, 0, 255))
    print(Xc, Yc, r)
    my_circle(Xc, Yc, r)
    bezier_curve(x1, y1, x3, y3, x4, y4, x2, y2, n)


def gui(n):
    screen.fill((255, 255, 255))
    screen.blit(button_font.render("Clear", True, (0, 0, 0)), (580, 620))
    screen.blit(button_font.render(str(n), True, (0, 0, 0)), (50, 620))
    draw_arrow()


def main():
    run = True
    first = 1
    n = 25
    while run:
        clock.tick(30)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # x, y = event.pos
                if first % 2 != 0:
                    x, y = event.pos
                    if x > 580 and y > 620:
                        n = 25
                        gui(n)
                    elif 10 < x < 30 and 620 < y < 640:
                        screen.blit(button_font.render(str(n), True, (255, 255, 255)), (50, 620))
                        n += 1
                        screen.blit(button_font.render(str(n), True, (0, 0, 0)), (50, 620))
                        if first == 3:
                            gui(n)
                            draw(x1, y1, x2, y2, n)
                    elif 10 < x < 30 and 650 < y < 670:
                        screen.blit(button_font.render(str(n), True, (255, 255, 255)), (50, 620))
                        n -= 1
                        screen.blit(button_font.render(str(n), True, (0, 0, 0)), (50, 620))
                        if first == 3:
                            gui(n)
                            draw(x1, y1, x2, y2, n)
                    else:
                        x1, y1 = x, y
                        first = 2
                else:
                    x2, y2 = event.pos
                    draw(x1, y1, x2, y2, n)
                    first = 3
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((700, 700))
    button_font = pygame.font.SysFont('arial', 50)
    gui(25)
    main()

