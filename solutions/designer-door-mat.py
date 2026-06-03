n,m = map(int, input().strip().split())

# Top part
for i in range (1,n,2):
    print((".|."*i).center(m,"-"))

#  Middle Part
print(("WELCOME").center(m,"-"))

# Last Part
for i in range (n-2, -1, -2):
    print((".|."*i).center(m,"-"))