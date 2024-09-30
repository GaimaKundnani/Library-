import sys
class Library:
    def __init__(self,listofbooks):
        self.availablebooks=listofbooks
    #Display
    def display(self):
        print("AVAILABLE BOOKS ARE: ")
        for book in self.availablebooks:
            print(book)
        print("\n")
    #Lend Books
    def lendBook(self,requestedBook):
        if requestedBook in self.availablebooks:
            print("The book you requested has now been borrowed")
            self.availablebooks.remove(requestedBook)
        else:
            print("Sorry the book you have requested is currently not in the library")
    # Add Book           
    def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thanks for returning your borrowed book")
class Student:
    # Request Books
    def requestBook(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            return self.book
    #Return Books
    def returnBook(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book
#Main Function
library=Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
student=Student()
while True:
    print("Welcome To Library")
    print("1. List of Avaliable Books")
    print("2. Borrow Books")
    print("3. Return Book")
    print("4. Exit")
    choice=int(input("Enter Choice:"))
    if choice==1: #Display
        library.display()
    elif choice==2: #Borrow
        library.lendBook(student.requestBook())
    elif choice==3: #Return
        library.addBook(student.returnBook())
    elif choice==4: #Exit
        print("Thank You for your visit")
        exit()
    else:
        print("INVALID INPUT!")
