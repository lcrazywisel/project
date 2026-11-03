









contacts = []


def is_valid_phone(phone):
    if len(phone) == 11 and phone.isdigit() and phone.startswith("09"):
        return True
    return False


def phone_exists(phone, ignored_index):
    for i in range(len(contacts)):
        if i != ignored_index and contacts[i][1] == phone:
            return True
    return False


def add_contact():
    name = input("Enter contact name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return
    phone = input("Enter phone number: ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number!")
        return
    if phone_exists(phone, -1):
        print("This phone number already exists!")
        return
    contact = [name, phone]
    contacts.append(contact)
    print("Contact added successfully!")


def show_all_contacts():
    if len(contacts) == 0:
        print("Contact list is empty!")
        return
    print("===== ALL CONTACTS =====")
    for i in range(len(contacts)):
        print("Contact Number:", i + 1)
        print("Name:", contacts[i][0])
        print("Phone:", contacts[i][1])
    print("========================")


def search_contact():
    if len(contacts) == 0:
        print("Contact list is empty!")
        return
    print("1. Search by name")
    print("2. Search by phone number")
    choice = input("Choose search type: ")
    found = False
    match choice:
        case "1":
            name = input("Enter contact name: ").strip().lower()
            if name == "":
                print("Search name cannot be empty!")
                return
            for i in range(len(contacts)):
                if name in contacts[i][0].lower():
                    print("Name:", contacts[i][0])
                    print("Phone:", contacts[i][1])
                    found = True
        case "2":
            phone = input("Enter phone number: ").strip()
            for i in range(len(contacts)):
                if contacts[i][1] == phone:
                    print("Name:", contacts[i][0])
                    print("Phone:", contacts[i][1])
                    found = True
        case _:
            print("Invalid choice!")
            return
    if found == False:
        print("Contact not found!")


def edit_contact():
    if len(contacts) == 0:
        print("Contact list is empty!")
        return
    show_all_contacts()
    number = input("Enter contact number to edit: ")
    if not number.isdigit():
        print("Invalid number!")
        return
    number = int(number)
    if number < 1 or number > len(contacts):
        print("Contact does not exist!")
        return
    index = number - 1
    print("1. Edit name")
    print("2. Edit phone number")
    print("3. Edit both")

    choice = input("Choose an option: ")
    match choice:
        case "1":
            new_name = input("Enter new name: ").strip()
            if new_name == "":
                print("Name cannot be empty!")
                return
            contacts[index][0] = new_name
            print("Name updated successfully!")
        case "2":
            new_phone = input("Enter new phone number: ").strip()
            if not is_valid_phone(new_phone):
                print("Invalid phone number!")
                return
            if phone_exists(new_phone, index):
                print("This phone number already belongs to another contact!")
                return
            contacts[index][1] = new_phone
            print("Phone number updated successfully!")
        case "3":
            new_name = input("Enter new name: ").strip()
            if new_name == "":
                print("Name cannot be empty!")
                return
            new_phone = input("Enter new phone number: ").strip()
            if not is_valid_phone(new_phone):
                print("Invalid phone number!")
                return
            if phone_exists(new_phone, index):
                print("This phone number already belongs to another contact!")
                return
            contacts[index][0] = new_name
            contacts[index][1] = new_phone
            print("Contact updated successfully!")
        case _:
            print("Invalid choice!")
            return
    print("Updated Contact:")
    print("Name:", contacts[index][0])
    print("Phone:", contacts[index][1])


def delete_contact():
    if len(contacts) == 0:
        print("Contact list is empty!")
        return
    show_all_contacts()
    number = input("Enter contact number to delete: ")
    if not number.isdigit():
        print("Invalid number!")
        return
    number = int(number)
    if number < 1 or number > len(contacts):
        print("Contact does not exist!")
        return
    index = number - 1
    print("Selected Contact:")
    print("Name:", contacts[index][0])
    print("Phone:", contacts[index][1])
    confirm = input("Are you sure? (y/n): ").lower()
    match confirm:
        case "y":
            contacts.pop(index)
            print("Contact deleted successfully!")
        case "n":
            print("Deletion cancelled!")
        case _:
            print("Invalid confirmation!")


def count_contacts():
    print("Total contacts:", len(contacts))


while True:
    print("======= CONTACT MANAGER =======")
    print("1. Add Contact")
    print("2. Show All Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Count Contacts")
    print("7. Exit")
    print("================================")
    choice = input("Choose: ")
    match choice:
        case "1":
            add_contact()
        case "2":
            show_all_contacts()
        case "3":
            search_contact()
        case "4":
            edit_contact()
        case "5":
            delete_contact()
        case "6":
            count_contacts()
        case "7":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice!")