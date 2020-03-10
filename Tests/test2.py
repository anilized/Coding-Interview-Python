
def sol(S):
    count = 0
    V = int(S,2)
    while V != 0:
        if V % 2 == 0:
            V = V / 2
            count += 1
            print(V)
        elif V % 2 == 1:
            V = V - 1
            count += 1
            print(V)
    print(count)


sol("011100")