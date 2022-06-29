import turtle


def loser():
    """Функция, вызываемая при поражении в игре battle_game.py"""
    def movement(x_coord, y_coord):
        """Функция для перемещения курсора."""
        x.up()
        x.goto(x_coord, y_coord)
        x.down()

    # Создали новую переменную, чтобы потом настроить настройки размера экрана.
    size_of_the_screen = turtle.Screen()
    size_of_the_screen.setup(width=1920, height=1080)

    turtle.bgcolor('black')
    x = turtle.Turtle()
    x.speed(5)
    x.color('white')
    x.pensize(10)

    # Первая буква
    movement(-300, 100)
    x.right(90)
    x.forward(100)
    x.left(90)
    x.forward(65)
    # print(x.pos())

    # Вторая буква
    movement(-200, 0)
    x.forward(65)
    x.left(90)
    x.forward(100)
    x.left(90)
    x.forward(65)
    x.left(90)
    x.forward(100)
    # print(x.pos())

    # Третья буква
    movement(-100, 0)
    x.left(90)
    x.forward(65)
    x.left(90)
    x.forward(50)
    x.left(90)
    x.forward(65)
    x.right(90)
    x.forward(50)
    x.right(90)
    x.forward(65)
    # print(x.pos())

    # Четвертая буква
    movement(65, 0)
    x.right(180)
    x.forward(65)
    x.right(90)
    x.forward(50)
    x.right(90)
    x.forward(65)
    x.right(180)
    x.forward(65)
    x.right(90)
    x.forward(50)
    x.right(90)
    x.forward(65)
    # print(x.pos())

    # Пятая буква
    movement(90, 0)
    x.left(90)
    x.forward(100)
    x.right(90)
    x.forward(65)
    x.right(90)
    x.forward(50)
    x.right(90)
    x.forward(65)
    movement(110, 50)
    x.left(130)
    x.forward(65)

    turtle.done()

