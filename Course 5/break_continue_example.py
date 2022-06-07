n = 0
while n < 5:
    n += 1
    if n == 4:
        #daca n este egal cu 4, se iese din bucla
        break
    if n == 1:
        # daca n este egal u 1, se trece la iteratia urmatoare
        # se sare peste randul print(n)
        continue
    print(n)