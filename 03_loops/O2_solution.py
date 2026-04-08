N = 10
even_num = 0
odd_num = 0


for num in range(1,N+1):
    if num%2==0:
        even_num += 1
    else:
        odd_num += 1

print("even_num: ", even_num ,"odd_num:", odd_num)
