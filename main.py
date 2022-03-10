
import pygame


def draw_some(screen):
    x, y = 25, 50
    d_range = max(abs(x), abs(y))

    # square
    for i in range(d_range):
        screen.set_at((50+i, 50), (0, 0, 0))
        screen.set_at((100, 50+i), (0, 0, 0))
        screen.set_at((50+i, 100), (0, 0, 0))
        screen.set_at((50, 50+i), (0, 0, 0))

    # triangle
    j = 24
    for i in range(26):
        screen.set_at((120+i, 100), (0, 0, 0))
        screen.set_at((120+i+j, 100), (0, 0, 0))
        screen.set_at((145+i, 50+i*2), (0, 0, 0))
        screen.set_at((145+i, 50+i*2-1), (0, 0, 0))
        screen.set_at((145-i, 50+i*2), (0, 0, 0))
        screen.set_at((145-i, 50+i*2-1), (0, 0, 0))


Xc, Yc, r = 250, 270, 70


def plot_circle_points(screen, x, y):
    if Xc+x > 0 and Yc+y > 0:
        screen.set_at((Xc+x, Yc+y), (0, 0, 0))
        print(Xc+x,Yc+y)
    if Xc+x > 0 and Yc-y > 0:
        screen.set_at((Xc+x, Yc-y), (0, 0, 0))
        print(Xc+x,Yc-y)
    if Xc-x > 0 and Yc+y > 0:
        screen.set_at((Xc-x, Yc+y), (0, 0, 0))
        print(Xc-x,Yc+y)
    if Xc-x > 0 and Yc-y > 0:
        screen.set_at((Xc-x, Yc-y), (0, 0, 0))
        print(Xc-x,Yc-y)
    if Xc+y > 0 and Yc+x > 0:
        screen.set_at((Xc+y, Yc+x), (0, 0, 0))
        print(Xc+y,Yc+x)
    if Xc+y > 0 and Yc-x > 0:
        screen.set_at((Xc+y, Yc-x), (0, 0, 0))
        print(Xc+y,Yc-x)
    if Xc-y > 0 and Yc+x > 0:
        screen.set_at((Xc-y, Yc+x), (0, 0, 0))
        print(Xc-y,Yc+x)
    if Xc-y > 0 and Yc-x > 0:
        screen.set_at((Xc-y, Yc-x), (0, 0, 0))
        print(Xc-y,Yc-x)


def bres(screen):
    x1, y1 = 0,  r
    p = 3 - 2 * r
    while x1 <= y1:
        plot_circle_points(screen, x1, y1)
        if p < 0:
            p = p + 4 * x1 + 6
        else:
            p = p + 4 * (x1 - y1) + 10
            y1 -= 1
        x1 += 1


def dda_line(screen, x1, y1, x2, y2):
    dx, dy = (x2 - x1), (y2 - y1)
    d_range = max(abs(dx), abs(dy))
    dx, dy = dx/d_range, dy/d_range
    for i in range(d_range):
        screen.set_at((round(x1), round(y1)), (255 - (i % 255), i % 255, (i % 255)))
        x1 += dx
        y1 += dy


def bresenham(screen, x1, y1, x2, y2):
    dy = (y2 - y1)
    dx = (x2 - x1)
    errp = 2 * dy - dx
    y = y1
    for x in range(x1, x2 + 1):
        errp = errp + 2 * dy
        if errp >= 0:
            y = y + 1
            errp = errp - 2 * dx
        screen.set_at((x, y), (255-x % 255, 255, 255-x % 255))


def bresenham_line(screen, x1, y1, x2, y2, color):
    # f = False
    if (x2-x1) < 0 or (y2-y1) < 0:
        # f = True
        x1, y1, x2, y2 = x2, y2, x1, y1
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    d_range = max(abs(dx), abs(dy))
    dx, dy = abs(x2 - x1) / d_range, abs(y2 - y1) / d_range
    err = dy/dx - 0.5 if dx > dy else dx/dy - 0.5
    # errp = 2 * dy - dx
    xp = x1
    yp = y1
    d = 1 if y1<y2 else -1
    # screen.set_at((xp, yp), color)
    print("dx:", dx, "dy:", dy)
    print(xp, yp, "to", x2, y2)
    while xp <= x2 and yp <= y2:
        print(err)
        screen.set_at((xp, yp), color)
        # if errp > 0:
        if err > 0:
            yp = yp + d
            # errp = errp - 2 * dx
            err = err - 1
        xp = xp + 1
        # errp = errp + 2 * dy
        err += dy/dx if dx > dy else dx/dy


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))
    screen.fill((255, 255, 255))
    draw_some(screen)
    bres(screen)
    run = True
    first = True
    while run:
        clock.tick(30)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # x, y = event.pos
                if first:
                    x1, y1 = event.pos
                    print(x1, y1)
                    first = False
                else:
                    x2, y2 = event.pos
                    print(x2, y2)
                    # dda_line(screen, x1, y1, x2, y2)
                    # bresenham(screen, x1, y1, x2, y2)
                    bresenham_line(screen, x1, y1, x2, y2, (0, 0, 0))
                    first = True
                    # R = math.sqrt(math.pow(x-t_x, 2)+math.pow(y-t_y, 2))
                    # max_theta = 2 * np.pi
                    # list_t = list(np.arange(0, max_theta))
                    # x_circle = list(set([round(R*math.cos(x_y)) for x_y in list_t]))
                    # y_circle = list(set([round(R*math.sin(x_y)) for x_y in list_t]))
                    # x_circle = [u + x for u in x_circle]
                    # y_circle = [u + y for u in y_circle]
                    # print(x_circle)
                    # print(y_circle)
                    # p_x = x_circle[0]
                    # p_y = y_circle[0]
                    # for i in range(1, len(x_circle)):
                    #     d_range = max(abs(p_x), abs(p_y))
                    #     # print("d_range", d_range)
                    #     dx, dy = p_x / d_range, p_y / d_range
                    #     # p_x = x
                    #     # p_y = y
                    #     # gfxdraw.pixel(screen, x_circle[i]-p_x, y_circle[i]-p_y, (0, 0, 0))
                    #     for _ in range(d_range):
                    #         print(p_x, p_y)
                    #         gfxdraw.pixel(screen, round(p_x), round(p_y), (0, 0, 0))
                    #         p_x -= dx
                    #         p_y -= dy
                    #     p_x = x_circle[i]
                    #     p_y = y_circle[i]
        pygame.display.update()


if __name__ == "__main__":
    main()

