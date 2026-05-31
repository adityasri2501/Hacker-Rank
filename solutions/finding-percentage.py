if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # marks = student_marks[query_name]
    # sum_marks = sum(marks)
    # avg = sum_marks/len(marks)
    # print(f"{avg:.2f}")

    #  OR

    avg = sum(student_marks[query_name])/len(student_marks[query_name])
    print(f"{avg:.2f}")