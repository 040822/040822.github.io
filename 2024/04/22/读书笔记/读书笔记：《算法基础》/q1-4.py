def f1(N):
    return(N**3/75-N**2/4+N+10)
def f2(N):
    return(N/2+8)

for i in range(1, 100):
    print("i = ", i)
    print("f1 = ", f1(i))
    print("f2 = ", f2(i))