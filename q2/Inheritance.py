class Publication: #Represents a publication with title and author.
    def __init__(self, title, author):
        self._title = title 
        self._author = author
        #Both title and author are protected attributes.

    def get_title(self): #This method returns the title of the publication
        return self._title

    def set_title(self, title): #This method sets the title of the publication.
        self._title = title

    def get_author(self): #This method returns the author of the publication. 
        return self._author

    def set_author(self, author): #This method sets the author of the publication.
        self._author = author

    def display_info(self): #This method displays the title and author of the publication.
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")


class Book(Publication): #Represents a book, which is a TYPE of publication with an additional attribute for the number of pages.
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author) 
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self): #This method returns the number of pages in the book.
        return self._number_of_pages

    def set_number_of_pages(self, number_of_pages): #This method sets the number of pages in the book, ensuring that the value inputted is positive.
        if number_of_pages <= 0:
            print("Number of pages must be positive.")
        else:
            self._number_of_pages = number_of_pages

    def display_info(self): #This method overrides the display_info method of the Publication class to include the number of pages in the book.
        super().display_info()
        print(f"Number of pages: {self._number_of_pages}")


class Magazine(Publication): #Represents a magazine which is a TYPE of publication with an additional attribute for the issue number.
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def get_issue_number(self): #This method returns the issue number of the magazine.
        return self._issue_number

    def set_issue_number(self, issue_number): #This method sets the issue number of the magazine, ensuring that the value inputted is positive.
        if issue_number <= 0:
            print("Issue number must be positive.")
        else:
            self._issue_number = issue_number

    def display_info(self): #This method overrides the display_info method of the Publication class to include the issue number  of the magazine.
        super().display_info()
        print(f"Issue number: {self._issue_number}")


#Creating objects based on the assessment guidelines
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#Printing and testing the information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  #Testing invalid value validation
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
