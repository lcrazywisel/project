









notes = []


def show_notes():
    if len(notes) == 0:
        print("Your notebook is empty!")
        return
    print("===== Your Notes =====")
    for i in range(len(notes)):
        print(str(i + 1) + ". " + notes[i])
    print("======================")


def add_note():
    note = input("Write your note: ").strip()
    if note == "":
        print("Note cannot be empty!")
        return
    notes.append(note)
    print("Note added successfully!")
    show_notes()


def edit_note():
    if len(notes) == 0:
        print("There are no notes to edit!")
        return
    show_notes()
    number = input("Enter note number to edit: ")
    if not number.isdigit():
        print("Invalid number!")
        return
    number = int(number)
    if number < 1 or number > len(notes):
        print("Note number does not exist!")
        return
    new_note = input("Enter your new note: ").strip()
    if new_note == "":
        print("Note cannot be empty!")
        return
    notes[number - 1] = new_note
    print("Note edited successfully!")
    show_notes()


def delete_note():
    if len(notes) == 0:
        print("There are no notes to delete!")
        return
    show_notes()
    number = input("Enter note number to delete: ")
    if not number.isdigit():
        print("Invalid number!")
        return
    number = int(number)
    if number < 1 or number > len(notes):
        print("Note number does not exist!")
        return
    notes.pop(number - 1)
    print("Note deleted successfully!")
    show_notes()


def search_notes():
    if len(notes) == 0:
        print("There are no notes to search!")
        return
    word = input("Enter a word to search: ").strip().lower()
    if word == "":
        print("Search word cannot be empty!")
        return
    found = False
    print("\n===== Search Results =====")
    for i in range(len(notes)):
        if word in notes[i].lower():

            print(str(i + 1) + ". " + notes[i])
            found = True
    if found == False:
        print("No matching notes found!")


while True:
    print("===== Notebook Menu =====")
    print("1. Create a note")
    print("2. Show all notes")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. Search notes")
    print("6. Exit")
    choice = input("Choose an option: ")
    match choice:
        case "1":
            add_note()
        case "2":
            show_notes()
        case "3":
            edit_note()
        case "4":
            delete_note()
        case "5":
            search_notes()
        case "6":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice!")