s1 = list()
word = set()
number = 0
answer = list()
while "HELLO" not in str(s1): 
	s1 = list()
	s1 = (input("1: ").split(" - "))
for word in s1:
    for g in word:
        if g in "computer":
            number = number + 1
            if number > 3:
                return
            else:
                answer.append(g)
print(g)