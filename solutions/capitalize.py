def capit(str):
    capital_next = True
    res = ""
    for i in str:
        if i == " ":
            res+=i
            capital_next = True
        elif capital_next and i.isalpha():
            res+=i.upper()
            capital_next = False
        else:
            res+=i
            capital_next = False
    return res

if __name__ == '__main__':
    str = input()
    # with open("Capitalize result.txt", "w") as f:
    #     result = capit(str)
    #     f.write(result)
    result = capit(str)
    print(result)