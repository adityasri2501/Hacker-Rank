def minion_game(str):
    s_score,k_score = 0,0
    n = len(str)
    for i in range (n):
        if str[i] in "AEIOU":
            k_score+=(n-i)
        else:
            s_score+=(n-i)
    if (s_score > k_score):
        print("Stuart", s_score)
    elif (s_score==k_score):
        print("Draw")
    else:
        print("Kevin",k_score)

if __name__ == '__main__':
    str = input().strip().upper()
    minion_game(str)