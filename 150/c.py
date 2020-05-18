import itertools as it

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

pe = sorted(list(it.permutations([i for i in range(1,n+1)])))

print(abs((pe.index(p)+1) - (pe.index(q)+1)))