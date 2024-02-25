from itertools import combinations


def inversions(num):
    count = 0
    for i in combinations(num, r=2):
        if i[0] > i[-1]:
            count += 1
    return count


if __name__ == '__main__':

    sequence = [3, 1, 4, 2]

    print(inversions(sequence))
