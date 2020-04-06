class Library:
    def __init__(self, availablebooks):
        self.availablebooks = availablebooks
    
    def displaybooks(self):
        for book in self.availablebooks:
            print (books)
            
    def lendbook(self, tolend):
        if tolend in self.availablebooks:
            self.availablebooks.remove(tolend)
        else:
            print ("Book unavailable")
    def returnbook(self, returned)
        self.availablebooks.append(returned)

class Student:
    def requestBook(self):
        self.book=input()
        return self.book

    def returnBook(self):
        self.book=input()
        return self.book
        
def main():            
      library=Library(["list of books"])
      student=Student()
            
      print(""" -----LIBRARY MENU-------
                  1. Display available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
        
            option=int(input("Enter option: "))
            
            if option==1:
                library.displaybooks()
            elif option==2:
                library.lendbook(student.requestbook())
            elif option==3:
                library.returnbook(student.returnbook())
            elif option==4:
                exit()
                  