def prime(number):
    is_prime=True
    for n in range(2,number):
        if number%n==0:
            is_prime=False
    if is_prime==True:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number")

no=int(input("Give a number"))
prime(no)





# def my_function(a):
#     if a < 40:
#         print("Terrible")
#     if a < 80:
#         return 
#     else:
#         return "Great"
# print(my_function(25))


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Example usage:
# result = factorial(5)
# print(result)


