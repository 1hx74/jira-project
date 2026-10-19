def main():
  f = open('in.txt', 'r')
  data = f.read().split()
  f.close()
  
  n = int(data[0])

    A = []
    pos = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(data[pos]))
            pos += 1
        A.append(row)

    w = 0 #произвольная вершина из V

    F = [] #F:=V\{w}
    for i in range(n):
        if i != w:
            F.append(i)

    T = [] #T:=0
    d = [32767] * n #d[v]:=c(v,ближний[v])
    blizh = [-1] * n #имя вершины w из V'

    for v in F:
        blizh[v] = w
        d[v] = A[v][w]

    while len(T) != n - 1:
        v = -1
        for u in F:
            if v == -1 or d[u] < d[v]:
                v = u
        T.append((v, blizh[v]))

        #F:=F\{v}
        newF = []
        for u in F:
            if u != v:
                newF.append(u)
        F = newF

        for u in F:
            if d[u] > A[u][v]:
                blizh[u] = v
                d[u] = A[u][v]


    neighbors = []
    for i in range(n):
        neighbors.append([])

    total = 0
    for e in T:
        a = e[0]
        b = e[1]
        neighbors[a].append(b)
        neighbors[b].append(a)
        total += A[a][b]

    f = open('out.txt', 'w')
    for i in range(n):
        List = sorted(neighbors[i])
        s = ''
        for x in List:
            s += str(x + 1) + ' '
        s += '0'
        f.write(s + '\n')

    f.write(str(total))
    f.close()
main()
