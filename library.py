









def add_book(books):
    """AFZOODAN KETAB JADID"""
    book_name = input("ESM KETAB: ").strip()
    if book_name == "":
        print("ESM KETAB VARED KONID!")
    else:
        duplicate = False
        for book in books:
            if book.lower() == book_name.lower():
                duplicate = True
                break
        if duplicate:
            print("ESM KETAB AZ GHABL HAST!")
        else:
            books.append(book_name)
            print("KETAB EZAFE SHOD!")


def show_books(books):
    """NAMAYESH HAME KETAB HA"""
    if len(books) == 0:
        print("KETABKHANE KHALI AST!")
    else:
        print("KETAB HA:")
        number = 1
        for book in books:
            print(number, ".", book)
            number = number + 1


def search_book(books):
    """PEYDA KARDAN KETAB"""
    book_name = input("ESM KETAB: ").strip()
    found = False
    for book in books:
        if book.lower() == book_name.lower():
            found = True
            break
    if found:
        print("KETAB PEYDA SHOD!")
    else:
        print("KETAB PEYDA NASHOD!")


def count_books(books):
    """TEDAD KETAB HA"""
    print("TEDAD KOL:", len(books))


def clear_books(books):
    """HAZF HAME KETAB HA"""
    if len(books) == 0:
        print("KETABKHANE KALI AST!")
    else:
        books.clear()
        print("HAME KETAB HA HAZF SHOD!")




books = []

while True:
    print()
    print("========== LIBRARY MENU ==========")
    print("1. EZAFE KARDAN KETAB")
    print("2. NAMAYESH KETAB")
    print("3. PEYDA KARDAN KETAB")
    print("4. TEDADE KETAB HA")
    print("5. HAZF HAME")
    print("6. KHOROOJ")
    print("==================================")
    choice = input("CHOOSE AN OPTION: ").strip()
    match choice:
        case "1":
            add_book(books)
        case "2":
            show_books(books)
        case "3":
            search_book(books)
        case "4":
            count_books(books)
        case "5":
            clear_books(books)
        case "6":
            print("MAMNOON!")
            break
        case _:
            print("AZ 1-6 ENTEKHAB KONID!")
