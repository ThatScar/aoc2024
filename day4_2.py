import re
xmas = "XMAS"

with open("day4.txt") as file:
    word_search = [line.strip() for line in file.readlines()]
    assert(len(word_search) == len(word_search[0]))

    L = len(word_search)
    cross = "(?=M.M" + "."*(L-2) + "A" + "."*(L-2) + "S.S)"
    def check_quarter(word_search):
        word_cat = "".join(word_search)
        total = 0
        for match in re.finditer(cross, word_cat):
            if match.start()%L <= (L-3):
                total += 1
        return total
    def rotate(word_search):
        transpose = list("".join(x) for x in zip(*word_search))
        return transpose[::-1]
    def print_word_search(word_search):
        for line in word_search:
            print(line)

    total = 0
    #print_word_search(word_search)
    total += check_quarter(word_search)
    print(total)
    word_search = rotate(word_search)
    #print_word_search(word_search)
    total += check_quarter(word_search)
    print(total)
    word_search = rotate(word_search)
    #print_word_search(word_search)
    total += check_quarter(word_search)
    print(total)
    word_search = rotate(word_search)
    total += check_quarter(word_search)
    print(total)
    #word_search = rotate(word_search)
