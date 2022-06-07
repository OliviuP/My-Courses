
with open('file.txt') as f:
#obiectul f este iterabil, astfel putem accesa fiecare linie din fisier
    for line in f:
        print(line.strip())