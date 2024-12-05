posteriors_by_priors = dict()
from dataclasses import dataclass

with open("day05.txt") as file:
    for line in file:
        line = line.strip()
        if not line:
            break

        pre, post = line.split("|")
        pre = int(pre)
        post = int(post)
        posteriors_by_priors.setdefault(pre, set())
        posteriors_by_priors[pre].add(post)

    total = 0
    for line in file:
        pages = [int(x) for x in line.strip().split(",")]
        @dataclass
        class Swapped:
            was_correct: bool
            pages: list
        def insert_page(pages):
            #print(pages)
            updated = []
            was_correct = True
            for page in pages:
                #print(page, updated)
                updated.append(page)
                if page in posteriors_by_priors:
                    conflict = set(updated) & set(posteriors_by_priors[page])
                    if conflict:
                        was_correct = False
                        pos = updated.index(conflict.pop())
                        #one conflict only (any); swap with latest page
                        updated[-1] = updated[pos]
                        updated[pos] = page
            return Swapped(was_correct, updated)
        swapped = insert_page(pages)
        if not swapped.was_correct:
            #print(swapped.pages)
            while not (swapped:=insert_page(swapped.pages)).was_correct:
                pass
            total += swapped.pages[len(swapped.pages)//2]
    print(total)
