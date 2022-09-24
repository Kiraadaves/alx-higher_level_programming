#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in range(len(matrix)):
        for i in matrix[y]:
            print(i, end= " ")
        print()
