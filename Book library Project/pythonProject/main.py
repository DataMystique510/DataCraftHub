import pickle
class Person:
    def __init__(self,adhar_no,name,age):
        self.adhar_no = adhar_no
        self.name = name
        self.age = age

    def __str__(self):
        return f"person adhar no.is{self.adhar_no} and name is {self.name}"

    def __eq__(self,other):
        return isinstance(other,Person) and self.adhar_no == other.adhar_no
    def __hash__(self):
        return hash(self.adhar_no)


class Books:
    def __init__(self, isbnNo,title,author):
       self.isbnNo = isbnNo
       self.title = title
       self.author = author

    def __str__(self):
         return f"ISBN: {self.isbnNo} , Title:{self.title}"

    def __eq__(self,other):
        return isinstance(other,Books) and self.isbnNo == other.isbnNo
    def __hash__(self):
        return hash(self.isbnNo)

class Library:
    def __init__(self,library_name):
        self.library_name=library_name
        self.shelf={}
        self.registered_person={}

    def registerPerson(self, person1):
        if person1 in self.registered_person:
            print("registered already")

        else:
            self.registered_person[person1]=[]


    def isBookInLibrary(self,book1):
        if book1 in self.shelf:
            self.shelf[book1]+=1
        else:
            self.shelf[book1]=1


    def issue_book(self,book1,person1):
        self.shelf[book1]=self.shelf[book1]-1
        self.registered_person[person1].append(book1)


    def to_issue_book(self,adhar_id,isbn_no):

        for key in  self.registered_person.keys():
            if key.adhar_no==adhar_id:

                flagBookFound = False

                for key2 in self.shelf.keys():
                    if key2.isbnNo == isbn_no:
                        self.issue_book(key2,key)
                        flagBookFound = True


                if flagBookFound==False:
                    print("book not found!")
                    return

            else:
                print("sorry u r not registered")


    def returning_book(self,isbnNo,adharNo):
        foundBook = None
        for b in self.shelf.keys():
            if b.isbnNo==isbnNo:
                foundBook = b

        if foundBook==None:
            print("you are returning a book which we never kept")
            return

        foundPerson = None
        for p in self.registered_person.keys():
            if p.adhar_no==adharNo:
                foundPerson = p

        if foundPerson == None:
            print("hum apko nahi jante")
            return

        if foundBook and foundPerson:
            self.shelf[foundBook]-=1
            self.registered_person[foundPerson].remove(foundBook)
            print("kitab lautane k liye shukriya !")






library=Library("python_library")




with open('data.pkl', 'rb') as file:
    library.shelf = pickle.load(file)


with open('person.pkl', 'rb') as file:
     library.registered_person = pickle.load(file)



def registerPerson():
    name=input("input your name")
    adhar_no=input("input your adhar_no")
    age=input("input your age")
    person1=Person(name,adhar_no,age)
    library.registerPerson(person1)


def add_book():
    isbnNo=input("input isbnNo. of book")
    title=input("input title of book")
    author=input("input author\'s name")
    book1=Books(isbnNo,title,author)
    library.isBookInLibrary(book1)


def bookWantTOIssue():
    adhar_no=input("what is your adhar_no.")
    isbn_no=input("which book u want to issue give isbn_no.")
    library.to_issue_book(adhar_no,isbn_no)


def return_book():
    isbn_no=input("give isbn_no.of book u want to return")
    adharNo = input("enter adhar no")
    library.returning_book(isbn_no,adharNo)

def display_books():
    print("---------------Book Store----------------------")
    for x in library.shelf.keys():
        print(f"{x}:{library.shelf[x]}")
    print("------------------------------------------------")


while True:
    prompt="""press 1. to register yourself into library 
              press 2.to issue a book
              press 3.to add a book
              press 4.to return a book
              press 5 to see books
              press 6.to quit\n"""


    option =int(input(prompt))
    if option==1:
        registerPerson()

    if option==2:
        bookWantTOIssue()


    if option==3:
        add_book()


    if option==4:
        return_book()

    if option==5:
        display_books()

    if option==6:
        break


with open('data.pkl', 'wb') as file:
    pickle.dump(library.shelf, file)


with open('person.pkl', 'wb') as file:
    pickle.dump(library.registered_person, file)
