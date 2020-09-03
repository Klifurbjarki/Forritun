last=0
mid=1
first=0
sum1=0
n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i  in range(1,n+1):
    
    sum1 = first +mid+last 
    last = mid
    mid = first
    first = sum1
    print(sum1)


