from operator import itemgetter
import time
time.localtime(time.time())
L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=itemgetter(0)))
print(sorted(a, key=itemgetter(0, 2)))
def by_score(t):
    L = t.copy()
    for x in range(len(L) - 1):
        for y in range(len(L) - 1 -x):
            if L[y][1] > L[y + 1][1]:
                L[y], L[y+1] = L[y+1], L[y]
    return L

def by_score_test(t):
    return t[1]

L2 = sorted(students, key = by_score_test, reverse=True)
print(L2)