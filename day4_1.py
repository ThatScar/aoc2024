import re
xmas = "XMAS"

with open("day4.txt") as file:
    word_search = [line.strip() for line in file.readlines()]
    assert(len(word_search) == len(word_search[0]))

    def check_quarter(word_search):
        total = 0
        for y in range(len(word_search)):
            total += len(re.findall(xmas, word_search[y]))
        total += len(re.findall(xmas, "".join([word_search[x][x] for x in range(len(word_search))])))
        for y in range(1,len(word_search)):
            total += len(re.findall(xmas, "".join([word_search[x][x+y] for x in range(len(word_search)-y)])))
            total += len(re.findall(xmas, "".join([word_search[x+y][x] for x in range(len(word_search)-y)])))
        return total
    def rotate(word_search):
        transpose = list("".join(x) for x in zip(*word_search))
        return transpose[::-1]
    def print_word_search(word_search):
        for line in word_search:
            print(line)
        print()

    total = 0
    total += check_quarter(word_search)
    print(total)
    #print_word_search(word_search)
    word_search = rotate(word_search)
    #print_word_search(word_search)
    total += check_quarter(word_search)
    print(total)
    word_search = rotate(word_search)
    total += check_quarter(word_search)
    print(total)
    word_search = rotate(word_search)
    total += check_quarter(word_search)
    print(total)
    #word_search = rotate(word_search)
