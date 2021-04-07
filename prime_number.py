my_num = int(input("Enter a number: "))
for x in range (2, 10):
    if (my_num % x) == 0 and (my_num != x):
        print(str(my_num) + ' is not a prime number.')
        break
    elif x == 9:
        print(str(my_num) + ' is a prime number.')