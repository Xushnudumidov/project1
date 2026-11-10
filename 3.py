def now(abc):
    natija = 1
    for son in abc:
        natija *= son
    return natija
print(now([2, 3, 4]))