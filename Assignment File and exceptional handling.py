
#Exercise 1
#Write a python program to read a file and display its contents
# file = open("C:\\Users\\hp\\OneDrive\\Desktop\\File Handling\\Hello.txt","r")
# print(file.read())


#Exercise 2
#Write a python program to copy the contents of one file to another file
# with open("C:\\Users\\hp\\OneDrive\\Desktop\\File Handling\\Hello.txt","r") as file:
#     with open("C:\\Users\\hp\\OneDrive\\Desktop\\File Handling\\Hello2.txt","w") as file1:
        # file1.write(file.read())


#Exercise 3
#Write a python program to read the content of a file and count the total number of words in that file
# with open("C:\\Users\\hp\\OneDrive\\Desktop\\File Handling\\Hello.txt","r") as file:
#     data = file.read()
#     print(data)
#     print(data.split())
#     print(len(data.split()))


#Exercise 4
#Write a python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle
#any exceptions that might occur

# a=input("The string which is to be converted to an integer")
# try:
#     b = int(a)
#     print(b,"The string converted to integer")
# except ValueError:
#     print("This string cannot be converted to integer")


#Exercise 5
#Write a python program that prompts the user to input a list of integers and raises an exception if any of the integers
#In the list are negative
# try:
#     input = input("Enter a list of integers:")
#     integers = [int(x) for x in input.split()]
#     if any (x < 0 for x in integers):
#         raise ValueError
#     print("All integers are non negative")
# except ValueError:
#     print("Enter Non-negative integers")


#Excercise6
#Write a python program that prompts the user to input a list of integers and computes the average of those integers. Use
#try-except blocks to handle any exceptions that might occur.Use the finally clause to print a message indicating that the program
#has finished running
# try:
#     user_input = input("Enter a list of integers:")
#     integers = [int(x) for x in user_input.split()]
#     if any (x < 0 for x in integers):
#         raise ValueError("Negative integers not allowed")
#     average = sum(integers) / len(integers)
#     print(average)
# except ValueError:
#     print("Invalid Input")
# except ZeroDivisionError:
#     print("Cannot calculate average of an empty list")
# finally:
#     print("Program has finished running")


#Exercise 7
#Write a python program that prompts the user to input a filename and writes a string to that file.Use try-except blocks
#to handle any exceptions that might occur and print a welcome message if there is no exception occured
# try:
#     filename = input("Enter the filename:")
#     with open(filename,"w") as file:
#         user_input = input("Enter a string to write to file:")
#         file.write(user_input)
#     print("Welcome,Your file has been created")
# except FileNotFoundError:
#     print("The file doesn't exist")
# except Exception as e:
#     print("An error Occured")














