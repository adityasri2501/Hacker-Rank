def rangoli(n):
    for i in range (n,0,-1):
        l_spaces = 2*(i-1)
        flag = True # for spaces to be printed once

        # left half 
        for j in range(n,i-1,-1):
            if flag:
                print(f"{"-"*l_spaces}{j}",end="-") # so that extra spaces after - does not come
                flag = False
            else:
                print(j,end="-")
        
        # right half
        # for k in range 

        print()


if __name__ == '__main__':
    n=5
    rangoli(n)


# It is not complete, gettinh the logic ;)