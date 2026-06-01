# approach = we will use eval()
# eval() string me mathematical computation karta hai
# agar string me variable ho jiska value defined hai toh use bhi compute karta hai

if __name__ == '__main__':
    x,k=map(int, input().strip().split())
    p=input().strip()
    if (eval(p) == k):
        print("True")
    else:
        print("False")