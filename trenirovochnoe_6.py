sec = int(input())
hours = (sec // 3600) % 24
min1 = sec // 60 % 60 // 10
min2 = sec // 60 % 60 % 10
sec1 = sec % 60 // 10
sec2 = sec % 10
print(hours, ":", min1, min2, ":", sec1, sec2, sep="")
