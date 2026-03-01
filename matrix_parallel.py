import multiprocessing

def multiply_row(args):
    A, B, i = args
    result_row = []
    for j in range(len(B[0])):
        sum_val = 0
        for k in range(len(B)):
            sum_val += A[i][k] * B[k][j]
        result_row.append(sum_val)
    return result_row

if __name__ == "__main__":
    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]

    pool = multiprocessing.Pool()

    tasks = [(A, B, i) for i in range(len(A))]
    C = pool.map(multiply_row, tasks)

    pool.close()
    pool.join()

    print("Hasil Matrix C:")
    print(C)