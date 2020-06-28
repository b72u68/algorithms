T = int(input())

for i in range(T):
    S, N = input().split()
    P = input().split()
    P = sorted([int(x) for x in P])
    cost = sum(P[:int(N)-1])
    print(f'Case {i+1}: {cost}')
