t = int(input())

for _ in range(t):
    count = 0

    for i in range(10):
        y = input()

        for j in range(10):
            if y[j] == 'X':
                if i < 5 and j < 5:
                    count += min(i, j) + 1

                elif i < 5 and j >= 5:
                    count += min(i, 9-j) + 1

                elif i >= 5 and j < 5:
                    count += min(9-i, j) + 1

                else:
                    count += min(9-i, 9-j) + 1

    print(count)
