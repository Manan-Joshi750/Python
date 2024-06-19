#To find the difference between the maximum and minimum possible number that can be formed from the digits of the entered number...
def foo(n):
    list1 = []
    while n>0:
        x = n%10
        list1.append(x)
        n=n//10

    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)
    a,b = "",""

    for i in range(len(list2)):
        list2[i] = str(list2[i])
        a += list2[i]

    for i in range(len(list3)):
        list3[i] = str(list3[i])
        b += list3[i]

    max_num  = int(b)
    min_num = int(a)
    print("Maximum number possible from the digits of the given number is : ", max_num)
    print("Minimum number possible from the digits of the given number is : ", min_num)
    diff = max_num - min_num

    return diff

n = int(input("Enter the number : "))
value = foo(n)
print("Required value of difference is : ", value)