what_sequnace = input("Input f|a|b (fibonacci, abundant or both): ")


if what_sequnace=='f' or what_sequnace=='b':
    fibonacci_num = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")
    first =0
    mid = 1
    for i  in range(1,fibonacci_num+1):
        print(first)
        sum1 = first +mid
        first = mid
        mid = sum1

if what_sequnace=='a' or what_sequnace=='b':
    
    Abundant_max = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")

    for num_to_cheak in range(1,Abundant_max+1):
        sum_abundant=0
        for i in range(1,num_to_cheak):
            if num_to_cheak%i==0:
                sum_abundant = i +sum_abundant
        if sum_abundant>num_to_cheak:
               print(num_to_cheak) 




