#course: Object-oriented programming, year 2, semester 1
#academic year: 2021-22
#author: B. Schoen-Phelan
#date: 07-10-2021
#purpose: Lab 3

# Tasks:
#  1. Run the file as is
#  2. Follow the comments in the file and try to solve the
#     exercises. Use the Python documentation to identify
#     functions that could help you.
#  3. Answer the quiz questions.


class Types_and_Strings:
    def __init__(self):
        pass
    

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #
        print("My own print statement: "+ message)
        # 1. print only first and last of the sentence:
        print(message[0] ,message[-1] )

        # 2. use slice notation:
        print(message[::-1])

        # 3. escaping a character, such as an apostrophe or & sign:
        i = 1
        
        while i < len(message):
            if message[i] == "*":
                message = message[:i] + message[(i +1):]
                i = i + 1
            else:
                i = i + 1
        print('This is your new string: '+message)

        # 4. find all a's in the input word and count how many there are:
        
        j = 0
        z = 0
        
        while j < len(message):
            if message[j] == "a":
                z = z + 1
                j = j + 1
            else:
                j = j + 1
        print("Number of a's: ", z)
        
        
            
        # 5. replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        
        x = message.replace("a", "-")
        print(x)


    # to run the tasks associated with this file, you must first
    # uncomment line number 75 and comment line 74
    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # 6. hand the input string to a list and print it out:
        list1 = list(message)
        print(list1)

        # 7. append a new element to the list and print:
        list1.append("whats good")
        print(list1)

        # 8. remove from the list in 3 ways:
        list1.pop(3)
        message = ' '.join(list1)
        print(message)

        # 9. check if the word cake is in your input list:
        index = message.find("m y")
        print(index)

        # 10. reverse the items in the list and print using a function:
        print(message[::-1])

        # 11. reverse the list with the slicing trick:
        print(message[::-1])

        # 12. print the list 3 times by using multiplication:
        print((message) * 3)


tas = Types_and_Strings() # creates an instance of the object
#tas.play_with_strings() # calls the method play_with_strings()
tas.play_with_lists()
