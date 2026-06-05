def merge_tools(str,k):
    n = len(str)
    # str_list = list()
    # i = 0
    # while (i<n):
    #     str_list.append(str[i:i+k])
    #     i+=k

    
    # for i in str_list:
    #     res_list = list()
    #     for j in i:
    #         if j in res_list:
    #             continue
    #         else:
    #             res_list.append(j)
    #     print("".join(res_list))

    #  or   below and belo if faster as list has O(n) and set has O(1)
    for i in range(0,n,+k):
        sub_str = str[i:i+k]
        res_set = set()
        res_list = list()
        for j in sub_str:
            if j in res_set:
                continue
            else:
                res_set.add(j)
                res_list.append(j)
        print("".join(res_list))

if __name__ == '__main__':
    str,k = input().strip(), int(input())
    merge_tools(str,k)