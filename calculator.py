class Calculator:
    """Обычный калькулятор, который способен обрабатывать пользовательский ввод и делать простые вычисления"""

    @staticmethod
    def summing(x, y):
        """Функция сложения двух чисел."""
        result = (int(x) + int(y))
        return result

    @staticmethod
    def subtraction(x, y):
        """Функция вычитания второго числа из первого."""
        result = (int(x) - int(y))
        return result

    @staticmethod
    def division(x, y):
        """Функция деления первого числа на второе."""
        while y == 0:
            y = input('Ошибка!\nНельзя делить на нуль!\nВведите другое второе число:\t')
        result = (int(x) / int(y))
        return result

    @staticmethod
    def multiplication(x, y):
        """Функция умножения двух чисел."""
        result = (int(x) * int(y))
        return result

    @staticmethod
    def square_root(x, y):
        """Функция взятия корня степени, равно1 второму числу, из первого числа."""
        while y == 0:
            y = input('Ошибка!\nНельзя взять квадратный корень из нуля!\nВведите другое второе число:\t')
        result = (int(x) ** (1 / int(y)))
        return result

    @staticmethod
    def exponentiation(x, y):
        """Функция возведения первого числа в степень, равную второму числу."""
        result = (int(x) ** int(y))
        return result

    def calculation(self, x, y, z):
        """Функция-алгоритм для использования в основном коде в зависимости от выбора пользователя."""
        if z == '+':
            return self.summing(x, y)
        elif z == '-':
            return self.subtraction(x, y)
        elif z == '*':
            return self.multiplication(x, y)
        elif z == '/':
            return self.division(x, y)
        elif z == '^':
            return self.exponentiation(x, y)
        elif z == 'sqr':
            return self.square_root(x, y)

    @staticmethod
    def input_check(users_input):
        """Проверка пользовательского ввода, не является ли он пустыми или не числовым."""
        while users_input == '':
            users_input = input('Вы ничего не ввели, попробуйте снова:\n')
        while users_input.isdigit() is False:
            users_input = input('Ошбика!\nНужно ввести число!\nВведите первое число:\t')
        return users_input

    @staticmethod
    def options_check(users_option_input):
        """Проверка, что введенная пользователем операция возможна для использования в программе."""
        available_options = ['+', '-', '/', '*', '^', 'sqr']
        while users_option_input not in available_options:
            users_option_input = input(
                'Вы допустили ошибку, пожалуйста, попытайтесь снова:\nЧто вы хотите сделать с данным числом? '
                '\nСложить (+),Вычесть (-), Делить (/), Умножить (*), Возвести в степень (^), '
                'Взять квадратный корень (sqr)\n')
        return users_option_input

    @staticmethod
    def cont_input_check(users_cont_input):
        """Проверка, корректное ли значение ввел пользователь, чтобы продолжить
        или закончить использование программы."""
        while users_cont_input.isnumeric() is False:
            users_cont_input = \
                input('Ошибка!\nНужно ввести число!\nВведите "1" для продолжения или "0" для завершения программы:\t')
        while int(users_cont_input) != 1 and int(users_cont_input) != 0:
            users_cont_input = \
                input('Ошибка!\nВы ввели не то число!\nВведите "1" для продолжения или "0" для завершения программы:\n')
        return users_cont_input

    @staticmethod
    def new_calc_or_cont_with_current_result_input_check(users_input):
        """Проверка, корректно ли пользователь ввел значения для определения, работать ли с результатом или
        начать работу калькулятора заново."""
        while users_input.isnumeric() is False:
            users_input = input(
                'Ошибка!\nНужно ввести число!\nВведите "1" для продолжения вычислений с полученным результатом или "0" '
                'для запуска программы с начала:\t')
        while int(users_input) != 1 and int(users_input) != 0:
            users_input = input(
                'Ошибка!\nВы ввели не то число!\nВведите "1" для продолжения вычислений с полученным результатом '
                'или "0" для запуска программы с начала:\t')
        return users_input

    def new_calc_or_cont_with_current_result(self, result):
        """Обработка пользовательского ввода и работа с результатом, либо начало нового цикла подсчета (новые данные)"""
        cont2 = input(
            'Хотите продолжить вычисления с полученным результатом (Введите "1") или начать с начала (Введите "0")?:\t')
        cont2 = self.new_calc_or_cont_with_current_result_input_check(cont2)
        if int(cont2) == 0:
            new_result = self.run_calculation()
            print(result[-1])
            cont = self.cont_check()
        if int(cont2) == 1:
            new_result = self.run_calculation_with_result(result[0], result[1], result[2])
            cont = self.cont_check()
        return new_result

    def cont_check(self):
        """Проверка, желает ли пользователь продолжить или завершить программу."""
        cont = input('\nЖелаете продолжить? Введите "1" для продолжения или "0" для завершения программы:\t')
        cont = self.cont_input_check(cont)
        if int(cont) == 0:
            exit()
        return cont

    def run_calculation(self):
        """Получение от пользователя первого числа, операции с этим числом
        и второго числа для осуществления операции."""
        x = input('Введите первое число:\t')
        x = self.input_check(x)
        z = str(input(
            'Что вы хотите сделать с данным числом? '
            '\nСложить (+),Вычесть (-), Делить (/), Умножить (*), Возвести в степень (^), '
            'Взять квадратный корень (sqr)\n'))
        z = self.options_check(z)
        y = input('Введите второе число:\t')
        y = self.input_check(y)
        return [x, y, z, print('\nИдет процесс подсчета...', '\nРезультат:\t', self.calculation(x, y, z))]

    def run_calculation_with_result(self, x, y, z):
        """Продолжение операций с полученным результатом."""
        x = self.calculation(x, y, z)
        z = str(input(
            'Что вы хотите сделать с данным числом? \nСложить (+),Вычесть (-), Делить (/), Умножить (*), Возвести в '
            'степень (^), Взять квадратный корень (sqr)\n'))
        z = self.options_check(z)
        y = input('Введите второе число:\t')
        y = self.input_check(y)
        return [x, y, z, print('\nИдет процесс подсчета...', '\nРезультат:\t', self.calculation(x, y, z))]

    def main_func(self):
        """Основная функция для запуска программы."""
        print('Добро пожаловать в калькулятор!\n')
        result = self.run_calculation()
        print(result[3])
        cont = self.cont_check()
        while int(cont) == 1:
            result = self.new_calc_or_cont_with_current_result(result)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.main_func()
