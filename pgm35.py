class publisher:
    def read(self):
        print("books")
class book(publisher):
    def title(self):
        print("operating system")
    def author(self):
        print("karl")
class python(book):
    def price(self):
        print("500-")
    def pages(self):
        print("280")
a=python()
a.read()
a.title()
a.author()
a.price()

