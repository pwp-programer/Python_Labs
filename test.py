A=[[1,2,3],[4,5,6]]

def print_list():
    for i in A[0]:
        print(i, end=" ")
    print()

print("Первый элемент списка:")
print_list()
A[0].reverse()
print()
print("Первый элемент списка в обратном порядке:")
print_list()
