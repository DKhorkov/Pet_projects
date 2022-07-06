import turtle


# Чтобы картинка открылась, она должна быть в том же директории, что и сама программа
def winner():
    """Функция, вызываемая при победе в игре battle_game.py"""
    size_of_the_screen = turtle.Screen()
    size_of_the_screen.setup(width=1920, height=1080)
    turtle.bgpic('~/Рабочий стол/PythonProjects/Pet_projects/my_battle_game/victory.png')
    turtle.done()


