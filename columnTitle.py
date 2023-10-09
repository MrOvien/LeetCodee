columnTitle = "FXSHRXW"
if len(columnTitle) == 1:
    print(ord(columnTitle) - 64)

lists = list(columnTitle)
# print(lists)
math=0
for i in range(0 , len(lists)):

    math += 26**i * (ord(lists[len(lists) - i - 1]) - 64)
    # math2 = (ord(lists[len(lists) - i - 1]))
    # print(lists[i])
    # print(math, math2)2
print(math)