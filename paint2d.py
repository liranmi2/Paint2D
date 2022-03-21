"""
Liran Michaelov 204238174
Alona Rozner
"""


import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def plot_circle_points(Xc, Yc, x, y, color):
    """Plotting circle points for every iteration in 'my_circle' (red by definition)"""
    screen.set_at((Xc+x, Yc+y), color)
    screen.set_at((Xc+x, Yc-y), color)
    screen.set_at((Xc-x, Yc+y), color)
    screen.set_at((Xc-x, Yc-y), color)
    screen.set_at((Xc+y, Yc+x), color)
    screen.set_at((Xc+y, Yc-x), color)
    screen.set_at((Xc-y, Yc+x), color)
    screen.set_at((Xc-y, Yc-x), color)


def my_circle(Xc, Yc, r, color):
    """Calculating all available integer points on circle by (Xcenter,Ycenter) and radius"""
    x, y = 0,  r
    p = 3 - 2 * r
    while x <= y:
        plot_circle_points(Xc, Yc, x, y, color)
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1
        x += 1


def dda_line(x1, y1, x2, y2, color):
    """Plotting points on a line from (x1,y1) to (x2,y2) in requested color"""
    dx, dy = (x2 - x1), (y2 - y1)
    d_range = max(abs(dx), abs(dy))
    dx, dy = dx/d_range, dy/d_range
    for i in range(d_range):
        screen.set_at((round(x1), round(y1)), color)
        x1 += dx
        y1 += dy


def bezier_curve(x1, y1, x2, y2, x3, y3, x4, y4, n, color):
    """Drawing a n lines Bezier curve from (x1,y1) to (x2,y2)
       according to (x3,y3) and (x4,y4) curves using dda_line function"""
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
        dda_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], color)


def draw_polygon(x1, y1, x2, y2, x3, y3, x4, y4, color):
    """Drawing a parallelogram using 4 points"""
    dda_line(x1, y1, x2, y2, color)
    dda_line(x1, y1, x3, y3, color)
    dda_line(x2, y2, x4, y4, color)
    dda_line(x1, y1, x4, y4, color)
    dda_line(x2, y2, x3, y3, color)
    dda_line(x3, y3, x4, y4, color)


def draw(x1, y1, x2, y2, n):
    """Main drawing function
    Drawing all the shapes after two clicks on the screen"""

    # Calculating Xcenter, Ycenter and radius by (x1,y1) and (x2,y2)
    Xc, Yc = round(x1 + (x2 - x1) / 2), round(y1 + (y2 - y1) / 2)
    r = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 / 2)

    # Calculating (x3,y3) and (x4,y4) by (x1,y1), (x2,y2) and radius
    x3, x4 = round(x2 + r / 2), round(x1 - r / 2)
    y3, y4 = y1, y2

    # Drawing all shapes by given points above
    draw_polygon(x1, y1, x2, y2, x3, y3, x4, y4, BLUE)
    my_circle(Xc, Yc, r, RED)
    bezier_curve(x1, y1, x3, y3, x4, y4, x2, y2, n, BLACK)


def draw_arrow():
    """Drawing 2 black filled arrows to change the number of lines on Bezier curve"""
    for i in range(20):
        dda_line(10+i, 540, 20, 520, BLACK)
    for i in range(20):
        dda_line(10+i, 550, 20, 570, BLACK)


def gui(n):
    """The gui function, updating the screen at start,
       and after every Bezier curve number of lines change"""
    screen.fill(WHITE)
    screen.blit(button_font.render("Clear", True, BLACK), (480, 520))
    screen.blit(button_font.render(str(n), True, BLACK), (50, 520))
    draw_arrow()


def main():
    """Main function
       Listening to events and responding to every click
       Updating the screen every 30 clock ticks"""
    run = True
    click = "first"
    n = 25
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if click == "first" and y < 520:
                    # if it's the first click and in draw zone (y under 520), place x and y as x1 and y1
                    x1, y1 = x, y
                    click = "second"
                elif click == "second" and y < 520:
                    # if it's the second click and in draw zone (y under 520), place x and y as x2 and y2
                    x2, y2 = x, y
                    draw(x1, y1, x2, y2, n)
                    click = "modify"
                else:
                    if x > 480 and y > 520:
                        # if the clear button clicked, redraw an empty screen
                        gui(n)
                        click = "first"
                    elif 10 < x < 30 and 520 < y < 540:
                        # if the up arrow clicked, add one to n and redraw the shapes
                        screen.blit(button_font.render(str(n), True, WHITE), (50, 520))
                        n += 1
                        screen.blit(button_font.render(str(n), True, BLACK), (50, 520))
                        gui(n)
                        draw(x1, y1, x2, y2, n)
                    elif 10 < x < 30 and 550 < y < 570:
                        # if the down arrow clicked, subtract one from n and redraw the shapes
                        screen.blit(button_font.render(str(n), True, WHITE), (50, 520))
                        if n-1 >= 0:
                            n -= 1
                        screen.blit(button_font.render(str(n), True, BLACK), (50, 520))
                        gui(n)
                        draw(x1, y1, x2, y2, n)
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 600))
    button_font = pygame.font.SysFont('arial', 50)
    gui(25)
    main()

