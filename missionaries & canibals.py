def valid(m,c): return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)

def solve():
    st=[((3,3,'L'),[])]
    vis=set()
    while st:
        (m,c,s),p=st.pop()
        if (m,c)==(0,0):
            for step in p+[(m,c,s)]: print(step)
            print("Goal Reached")
            return
        if (m,c,s) in vis: continue
        vis.add((m,c,s))
        for dm,dc in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
            nm,nc = (m-dm,c-dc) if s=='L' else (m+dm,c+dc)
            if 0<=nm<=3 and 0<=nc<=3 and valid(nm,nc):
                st.append(((nm,nc,'R' if s=='L' else 'L'),p+[(m,c,s)]))
solve()
