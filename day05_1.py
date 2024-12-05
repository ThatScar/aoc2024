posteriors_by_priors = dict()

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
        updated = set()
        correct = True
        for page in pages:
            #print(page, updated)
            if page in posteriors_by_priors and \
               updated & posteriors_by_priors[page]:
                correct = False
                break
            updated.add(page)
        #print(correct)
        if correct:
            total += pages[len(pages)//2]
    print(total)
