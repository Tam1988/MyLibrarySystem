from Book import Book, Library, Ebook, Audiobook
 

def main():
    library = Library("Tamara's Alcove")

    library.add_book(Book("Pride and Prejudice", "Jane Austen", 1813))
    library.add_book(Book("Moby-Dick", "Herman Melville", 1851))
    library.add_book(Book("Wuthering Heights", "Emily Brontë", 1847))
    library.add_book(Ebook("To Kill a Mockingbird", "Harper Lee", 1960, 5))
    library.add_book(Ebook("The Great Gatsby", "F. Scott Fitzgerald", 1925, 3))
    library.add_book(Ebook("The Catcher in the Rye", "J.D. Salinger", 1951, 4))
    library.add_book(Audiobook("The Lord of the Rings", "J.R.R. Tolkien", 1954, 20))
    library.add_book(Audiobook("One Hundred Years of Solitude", "Gabriel García Márquez", 1967, 17))
    library.add_book(Audiobook("The Kite Runner", "Khaled Hosseini", 2003, 12))
    
    while True:
        print("Welcome To Tamara's Alcove")
        print("1. View All Books")
        print("2. Pick A Book To Read")
        print("3. Exit")
        
        choice = input("Choose an option (1-3):")
        print("--------------------------------")

        if choice == "1":
            print("Library Catalogue:")
            for book in library.books:
                print("-", book.get_details())
                print("--------------------------------")

        elif choice == "2":
            title = input("Enter the title of the book you want to read: ")
            book = library.find_book(title)
            if book:
                print(book.read_book())
            else:
                print("Book Not Found.") 

        elif choice == "3":
            print("Exiting Tamara's Alcove. See you next time. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")
            print("--------------------------------")
if __name__ == "__main__":
    main()
                    









