#Вариант 5.

#1. В матрице элементы второго столбца возвести в квадрат.


def square_second_column(matrix: list[list[int]]) -> list[list[int]]:
    """Возводит во вторую степень все элементы второго столбца (индекс 1)."""
    return [
        [row[i] ** 2 if i == 1 else row[i] for i in range(len(row))]
        for row in matrix
    ]


def main():
    # Исходная матрица (размер 3x3)
    source_matrix = [,
 ,
        [7, 8, 9]
    ]

    print("--- Задача 1: Квадрат второго столбца ---")
    print("Исходная матрица:")
    for row in source_matrix:
        print(row)

    try:
        result_matrix = square_second_column(source_matrix)
        print("\nРезультирующая матрица:")
        for row in result_matrix:
            print(row)
    except IndexError:
        print("\nОшибка: в матрице отсутствуют строки или второй столбец!")


if __name__ == "__main__":
    main()
