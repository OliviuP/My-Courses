# daca deschidem fisierul in modul 'w' (write), se suprascrie fisierul la fiecare reluare a codului
# iar daca nu exista, se creeaza si se scrie in el

# with open('new_file.txt', 'w') as f:
#     for i in range(10):
#         f.write(f'This is line number: {i}\n')

# daca deschidem fisierul in modul "a" (append), putem adauga noi randuri la cele existente

with open('new_file.txt', 'a') as f:
    for i in range(10):
        f.write(f'This is line number: {i}\n')

