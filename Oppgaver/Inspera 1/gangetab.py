def print_table(n):
    for y in range(1, n + 1):
        row = []
        for x in range(1, n + 1):
            row.append(str(x * y))
        print(" ".join(row))
