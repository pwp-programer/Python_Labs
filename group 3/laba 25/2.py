import numpy as np


def first():
    v1 = np.zeros(10)
    v2 = np.zeros(55)
    f = open("C:\\Users\\pwp\\Desktop\\first.txt", "w")
    
    for i in v1:
        f.write(str(i))
    f.write("\n")
    
    for i in v2:
        f.write(str(i))
    
    f.close()

def secondary():
    v1, v = np.eye(5, 5, k=0, order='F').flatten(), [int(0) for i in range(25)]
    for i in range(25):
        if v1[i] == 0:
            v[i] = int(2)
        else:
            v[i] = int(v1[i])
    v = np.reshape(v, (5, 5))
    
    f = open("C:\\Users\\pwp\\Desktop\\secondary.txt", "w")
    for i in range(5):
        for q in range(5):
            f.write(str(v[i][q]))
            if (q == 4):
                f.write("\n")


def third():
    f = open("C:\\Users\\pwp\\Desktop\\third.txt", "w")
    for i in range(5):
        for q in range(5):
            f.write(str(i + 1))
            if (q == 4):
                f.write("\n")

first()
secondary()
third()
