s1 = s2 = s3 = list()
s1, s2, s3 = (input("1: ").split(", ")), (input("2: ").split(", ")), (input("3: ").split(", "))
s1, s2, s3 = set(s1), set(s2), set(s3)
intersection = s2 & s3
print(intersection)
difference = intersection - s1
answer = list(difference)
"; ".join(answer)
print(answer)
inc = 0
for i in answer:
    if inc == 0:
        new = i
    elif inc != 0:
        new = up + i
    inc = inc + 1
print(new)


