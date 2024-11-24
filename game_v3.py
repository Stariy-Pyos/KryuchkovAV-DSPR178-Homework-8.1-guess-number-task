"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Рандомно угадываем число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0 # счетчик количества попыток
    lower_limit = 0 # нижняя граница предполагаемых чисел
    upper_limit = 101 # верхняя граница предполагаемых чисел
    predict_number = (lower_limit + upper_limit)//2   # задаем первое предполагаемое число как среднее значение
    while number != predict_number:   # цикл сравнения предполагаемого и загаданного чисел
        count += 1 #  прибавляем к счетчику попыток единицу
        if predict_number > number:    # проверка условия предполагаемое число больше загаданного
            upper_limit = predict_number    # делаем верхней границей среденее значение
        elif predict_number < number:    # проверка условия предполагаемое число меньше загаданного
            lower_limit = predict_number      # делаем нижней границей среденее значение
        predict_number = (lower_limit + upper_limit)//2   # задаем  предполагаемое число как среднее значение по новым пределам
    return count


def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм методом бинарного поиска угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
