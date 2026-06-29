#2. Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
import random


def replace_odds_with_zero(matrix: list[list[int]]) -> list[list[int]]:
    return [
        [0 if element % 2 != 0 else element for element in row]
        for row in matrix
    ]


def main():
    rows, cols = 4, 4
    source_matrix = [
        [random.randint(1, 20) for _ in range(cols)]
        for _ in range(rows)
    ]

    print("матрица:")
    for row in source_matrix:
        print(row)

    result_matrix = replace_odds_with_zero(source_matrix)

    print("\n ответ:")
    for row in result_matrix:
        print(row)


if __name__ == "__main__":
    main()


