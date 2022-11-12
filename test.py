arr = [[0 for j in range(9)] for i in range(9)]
for p in range(9):
    for q in range(9):
        print(arr[p][q] ,end=" ")
    print()
print("==================")    
# 판 지정 ----------------------------------------------------------------------------------------------------------------

while True:
    while True:
        blackwin = 0
        pb1 = int(input())
        pb2 = int(input())
        b1 = pb1 - 1
        b2 = pb2 - 1

        if arr[b1][b2] == 0:
            arr[b1][b2] = "@"
            for p in range(9):
                for q in range(9):
                    print(arr[p][q] ,end=" ")
                print()
            print("==================")
            break
        else:
            for p in range(9):
                for q in range(9):
                    print(arr[p][q] ,end=" ")
                print()
            print("==================")
            print("다른곳에 수를 놓아주세요.")
            
        # 돌 지정 ----------------------------------------------------------------------------------------------------------------

    plen = 9 - pb2
    if plen > 5:
        plen = 5
        
    mlen = pb2 - 1
    if mlen > 5:
        mlen = 5

    for i in range(1, plen):
        if (arr[b1][b2 + i] == "@"):
            blackwin += 1
        if (arr[b1][b2 + i] != "@"):
            break

    for i in range(mlen):
        if (arr[b1][b2 - i - 1] == "@"):
            blackwin += 1
        if (arr[b1][b2 - i - 1] != "@"):
            break

    if blackwin != 4:
        blackwin = 0

    if blackwin == 4:
        print("\n흑돌이 승리하였습니다!")
        break
    
    # 가로 승리 조건 ----------------------------------------------------------------------------------------------------------------
    
    plen = 9 - pb1
    if plen > 5:
        plen = 5
        
    mlen = pb1 - 1
    if mlen > 5:
        mlen = 5
    
    for i in range(1, plen):
        if (arr[b1 + i][b2] == "@"):
            blackwin += 1
        if (arr[b1 + i][b2] != "@"):
            break

    for i in range(mlen):
        if (arr[b1 - i - 1][b2] == "@"):
            blackwin += 1
        if (arr[b1 - i - 1][b2] != "@"):
            break

    if blackwin != 4:
        blackwin = 0
    
    if blackwin == 4:
        print("\n흑돌이 승리하였습니다!")
        break
    
    # 세로 승리 조건 ----------------------------------------------------------------------------------------------------------------

    lplen = 9 - pb1
    lmlen = pb1 - 1 
    wplen = 9 - pb2
    wmlen = pb2 - 1

    if lmlen <= wmlen:
        mlen = lmlen

    elif wmlen <= lmlen:
        mlen = wmlen

    if lplen <= wplen:
        plen = lplen

    elif wplen <= lplen:
        plen = wplen
    
    if plen > 5:
        plen = 5

    if mlen > 5:
        mlen = 5

    for i in range(1, plen):
        if (arr[b1 + i][b2 + i] == "@"):
            blackwin += 1
        if (arr[b1 + i][b2 + i] != "@"):
            break

    for i in range(mlen):
        if (arr[b1 - i - 1][b2 - i - 1] == "@"):
            blackwin += 1
        if (arr[b1 - i - 1][b2 - i - 1] != "@"):
            break

    if blackwin != 4:
        blackwin = 0

    if blackwin == 4:
        print("\n흑돌이 승리하였습니다!")
        break
    
    # 아래로 내려가는 대각선 승리 조건 ----------------------------------------------------------------------------------------------------------------

    for i in range(1, wplen):
        if (arr[b1 - i][b2 + i] == "@"):
            blackwin += 1
        if (arr[b1 - i][b2 + i] != "@"):
            break

    for i in range(lplen):
        if (arr[b1 + i + 1][b2 - i - 1] == "@"):
            blackwin += 1
        if (arr[b1 + i + 1][b2 - i - 1] != "@"):
            break
    
    if blackwin != 4:
        blackwin = 0

    if blackwin == 4:
        print("\n흑돌이 승리하였습니다!")
        break
    
    # 위로 올라가는 대각선 승리 조건 ----------------------------------------------------------------------------------------------------------------

    # 흑돌 ===================================================================================================================
    
    while True:
        whitewin = 0
        pw1 = int(input())
        pw2 = int(input())
        w1 = pw1 - 1
        w2 = pw2 - 1
        if arr[w1][w2] == 0:
            arr[w1][w2] = "*"
            for p in range(9):
                for q in range(9):
                    print(arr[p][q] ,end=" ")
                print()
            print("==================")
            break
        else:
            for p in range(9):
                for q in range(9):
                    print(arr[p][q] ,end=" ")
                print()
            print("==================")
            print("다른곳에 수를 놓아주세요.")
    # 돌 지정 ----------------------------------------------------------------------------------------------------------------

    plen = 9 - pw2
    if plen > 5:
        plen = 5
        
    mlen = pw2 - 1
    if mlen > 5:
        mlen = 5

    for i in range(1, plen):
        if (arr[w1][w2 + i] == "*"):
            whitewin += 1
        if (arr[w1][w2 + i] != "*"):
            break

    for i in range(mlen):
        if (arr[w1][w2 - i - 1] == "*"):
            whitewin += 1
        if (arr[w1][w2 - i - 1] != "*"):
            break

    if whitewin != 4:
        whitewin = 0
    
    if whitewin == 4:
        print("\n백돌이 승리하였습니다!")
        break

    # 가로 승리 조건 ----------------------------------------------------------------------------------------------------------------
    
    plen = 9 - pw1
    if plen > 5:
        plen = 5
        
    mlen = pw1 - 1
    if mlen > 5:
        mlen = 5
    
    for i in range(1, plen):
        if (arr[w1 + i][w2] == "*"):
            whitewin += 1
        if (arr[w1 + i][w2] != "*"):
            break

    for i in range(mlen):
        if (arr[w1 - i - 1][w2] == "*"):
            whitewin += 1
        if (arr[w1 - i - 1][w2] != "*"):
            break

    if whitewin != 4:
        whitewin = 0

    if whitewin == 4:
        print("\n백돌이 승리하였습니다!")
        break

    # 세로 승리 조건 ----------------------------------------------------------------------------------------------------------------

    lplen = 9 - pw1
    lmlen = pw1 - 1 
    wplen = 9 - pw2
    wmlen = pw2 - 1

    if lmlen <= wmlen:
        mlen = lmlen

    elif wmlen <= lmlen:
        mlen = wmlen

    if lplen <= wplen:
        plen = lplen

    elif wplen <= lplen:
        plen = wplen
    
    if plen > 5:
        plen = 5

    if mlen > 5:
        mlen = 5

    for i in range(1, plen):
        if (arr[w1 + i][w2 + i] == "*"):
            whitewin += 1
        if (arr[w1 + i][w2 + i] != "*"):
            break

    for i in range(mlen):
        if (arr[w1 - i - 1][w2 - i - 1] == "*"):
            whitewin += 1
        if (arr[w1 - i - 1][w2 - i - 1] != "*"):
            break

    if whitewin != 4:
        whitewin = 0
    
    if whitewin == 4:
        print("\n백돌이 승리하였습니다!")
        break

    # 아래로 내려가는 대각선 승리 조건 ----------------------------------------------------------------------------------------------------------------

    for i in range(1, wplen):
        if (arr[w1 - i][w2 + i] == "*"):
            whitewin += 1
        if (arr[w1 - i][w2 + i] != "*"):
            break

    for i in range(lplen):
        if (arr[w1 + i + 1][w2 - i - 1] == "*"):
            whitewin += 1
        if (arr[w1 + i + 1][w2 - i - 1] != "*"):
            break

    if whitewin != 4:
        whitewin = 0

    if whitewin == 4:
        print("\n백돌이 승리하였습니다!")
        break

    # 위로 올라가는 대각선 승리 조건 ----------------------------------------------------------------------------------------------------------------

    # 백돌 ===================================================================================================================