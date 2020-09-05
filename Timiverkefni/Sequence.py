last=3
mid=2
first=1

n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i  in range(1,n+1):
    print(first)
    sum1 = first +mid+last 
    first = mid
    mid = last
    last = sum1
    
    
    

