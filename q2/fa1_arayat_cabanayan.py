"""
Formative Assessment 1
Cabanayan

Good day, sir! Please accept my sincerest apologies po for the late submission
as I was absent po due to PMO review. Thank you very much po!
"""

class Publication:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def display_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self._number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= 0:
            print("The number of pages must be greater than 0.")
        else:
            self._number_of_pages = number_of_pages

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self._number_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self._issue_number

    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("The issue number must be greater than 0.")
        else:
            self._issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self._issue_number}")


pub = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub.display_info()

print("\nBook Information:")
book.set_number_of_pages(-6767)
book.display_info()

print("\nMagazine Information:")
mag.display_info()
