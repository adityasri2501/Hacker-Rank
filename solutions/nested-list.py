# arr = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#  OR

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
#  to get marks as a list
marks = [i[1] for i in arr]
marks.sort()
second = marks[1]
for i in marks:
    if (i > marks[0]):
        second = i
        break
        
# get the names using list comprehension
final_names = [i[0] for i in arr if (i[1] == second)]
final_names.sort()
for i in final_names:
    print(i)

#  ANOTHER APPROACH 

# second = sorted(set([i[1] for i in arr]))[1]
# final_names = [i[0] for i in arr if (i[1] == second)]
# print(final_names.sort())