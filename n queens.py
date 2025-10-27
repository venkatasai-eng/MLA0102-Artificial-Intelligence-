import random
N=4

def cost(b):
    c=0
    for i in range(N):
        for j in range(i+1,N):
            if b[i]==b[j] or abs(b[i]-b[j])==abs(i-j): c+=1
    return c

def hill():
    b=[random.randint(0,N-1) for _ in range(N)]
    while True:
        h=cost(b)
        if h==0: return b
        best=b[:]; bh=h
        for i in range(N):
            for r in range(N):
                nb=b[:]; nb[i]=r
                if cost(nb)<bh: best, bh = nb, cost(nb)
        if bh>=h: return b
        b=best

sol=hill()
print(sol, "Conflicts:", cost(sol))
