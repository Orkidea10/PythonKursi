numrat=[1,2,3,4,5,6]
target=3
for numer in numrat:
    print(numer)
    if numer==target:
        print('Target found!!!')
        break

#continue
scores=[68,42,57,78,35,62,50,92]
total=0
count=0
for score in scores:
    if score<50:
        continue
    total=total+score
    count+=1
mesatarja=total/count #mesatarja per vlerat e score mbi 50
print("mesatarja e kerkuar ",mesatarja)