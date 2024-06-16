def gaussian_elimination(a, b):
    n = len(b)

    # Augment the matrix a with the vector b
    for i in range(n):
        a[i].append(b[i])

    # Forward elimination
    for i in range(n):
        # Find the row with the largest element in the current column
        max_row = i
        for k in range(i + 1, n):
            if abs(a[k][i]) > abs(a[max_row][i]):
                max_row = k

        # Swap the current row with the max_row
        a[i], a[max_row] = a[max_row], a[i]

        for k in range(i + 1, n):
            c = -a[k][i] / a[i][i]
            for j in range(i, n + 1):
                if i == j:
                    a[k][j] = 0
                else:
                    a[k][j] += c * a[i][j]

    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n] / a[i][i]
        for k in range(i - 1, -1, -1):
            a[k][n] -= a[k][i] * x[i]

    return x


def get_matrix_and_vector():
    n = int(input("输入方程组的个数: "))

    print("请输入系数矩阵")
    a = []
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        a.append(row)

    print("请输入结果矩阵")
    b = []
    for i in range(n):
        value = float(input(f"b[{i + 1}]: "))
        b.append(value)

    return a, b


def main():
    while True:
        a, b = get_matrix_and_vector()
        solution = gaussian_elimination(a, b)
        print("Solution:", solution)

        rerun = input("是否重新运行程序? (y/n): ").strip().lower()
        if rerun != 'y':
            break


if __name__ == "__main__":
    main()
