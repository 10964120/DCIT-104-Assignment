# python code

lst = []
sum = 0

end = int(input("Please enter the end range of the list:"))
for i in range(1,end + 1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        lst += [i]
for j in lst:
    sum += j
print(lst)

n = len(lst)
Average = sum / n
print("The Average of the prime numbers are:", Average)
    
        

