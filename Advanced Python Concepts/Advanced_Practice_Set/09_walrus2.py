list1 = ["Python", "Rocks","Ai"]


res = [n for w in list1 if (n:=len(w))>=4]

print(res)