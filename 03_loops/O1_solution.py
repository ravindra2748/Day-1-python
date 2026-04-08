numberss = [1,-2,3,-4,5,-6,7,-8,9,10]
positive_num = 0
negative_num = 0

for num in numberss:
    if num >0:
        positive_num += 1
    else:
        negative_num += 1

print ("Negative num :", negative_num , "poitive num :", positive_num)