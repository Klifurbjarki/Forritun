length = int(input("Input the length of series: "))
num=2
sums=0
for i in range(1,length+1):
    print(num)
    num = num

else:
    print("Sum:", sums)
    


length = int(input("Input the length of series: "))
sums = 0
for i in range(0,length):
    
    num = (i+1) * ( ((-1)**i ) * 2)
    sums = num + sums
    print(num)

print("Sum:",sums)