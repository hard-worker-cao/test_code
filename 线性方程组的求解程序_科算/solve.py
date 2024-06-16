def gauss_elimination(a, b):
    n = len(b)
    # 主元消去过程
    for k in range(n):
        # 选择主元
        max_index = max(range(k, n), key=lambda i: abs(a[i][k]))
        a[k], a[max_index] = a[max_index], a[k]
        b[k], b[max_index] = b[max_index], b[k]
        # 使下三角矩阵所有元素为0
        for i in range(k+1, n):
            factor = a[i][k] / a[k][k]
            b[i] -= factor * b[k]
            for j in range(k, n):
                a[i][j] -= factor * a[k][j]

    # 回代过程
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x

def input_equations():
    while True:
        try:
            n = int(input('请输入方程的数量：'))
            a = []
            b = []
            for i in range(n):
                row = list(map(float, input(f'请输入第{i+1}个方程的系数，以空格分隔：').split()))
                if len(row) != n + 1:
                    raise ValueError("输入的系数数量不正确，请重新输入。")
                a.append(row[:-1])  # 最后一个值之前的所有值都是系数
                b.append(row[-1])   # 最后一个值是常数项
            return a, b
        except ValueError as e:
            print(f"输入错误: {e}\n请重新输入。")

def main():
    while True:
        print('高斯消元法求解线性方程组')
        a, b = input_equations()
        solution = gauss_elimination(a, b)
        print('线性方程组的解是:', solution)

        rerun = input("是否重新运行程序? (y/n): ").strip().lower()
        if rerun != 'y':
            break

if __name__ == '__main__':
    main()
