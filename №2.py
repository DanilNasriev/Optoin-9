s1 = s2 = s3 = list()
s1, s2, s3 = (input("1-ая строка: ").split(" ")), (input("2-ая строка: ").split(" ")), (input("3-ья: ").split(" "))
s1, s2, s3 = set(s1), set(s2), set(s3)
intersection = s2 & s3
difference = intersection - s1
answer = list(difference)
print("; ".join(answer))
l1 = list()
for i in answer:
    l1.append(int(i))
print(sum(l1))

