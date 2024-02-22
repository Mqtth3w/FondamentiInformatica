matrix = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in range(0,4):
    for z in range(0,4):
        print("riga", matrix[i*4+z])
        print()
        print("colonna", matrix[z*4+i])