def sum_combinations(set_of_digits):
    s = sum(set_of_digits)
    arr = []
    for i in range(len(set_of_digits) + 1):
        row = []
        for j in range(s + 1):
            row.append(0)
        row[0] = 1
        arr.append(row)

    for i in range(1, len(set_of_digits) + 1):
        for j in range(1, s + 1):
            if set_of_digits[i - 1] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                if arr[i - 1][j - set_of_digits[i - 1]]:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j]

    all_combs = []
    for i in range(1, s):
        if arr[len(set_of_digits)][i]:
            all_combs.append(i)
    return all_combs


if __name__ == '__main__':
    set_of_digits = [5, 6, 7, 10]
    print(sum_combinations(set_of_digits))
