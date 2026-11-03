









rooms = [
    [101, "Single", 1, 50, "Available"],
    [102, "Double", 2, 80, "Available"],
    [103, "Suite", 4, 150, "Available"],
    [104, "Double", 2, 80, "Available"],
    [105, "Suite", 4, 150, "Available"],
    [106, "Single", 1, 50, "Available"],
    [107, "Double", 2, 80, "Available"],
    [108, "Suite", 4, 150, "Available"]
]

reservations = []

reservation_counter = [1001]


def find_room_index(room_number):
    for i in range(len(rooms)):
        if rooms[i][0] == room_number:
            return i
    return -1


def find_reservation_by_room(room_number):
    for i in range(len(reservations)):
        if reservations[i][3] == room_number:
            return i
    return -1


def find_reservation_by_code(code):
    for i in range(len(reservations)):
        if reservations[i][0].lower() == code.lower():
            return i
    return -1


def show_reservation(reservation):
    print("Reservation Code:", reservation[0])
    print("Customer Name:", reservation[1])
    print("Phone Number:", reservation[2])
    print("Room Number:", reservation[3])
    print("Number Of Guests:", reservation[4])
    print("Number Of Nights:", reservation[5])
    print("Total Price:", reservation[6], "$")


def show_all_rooms():
    print("========== ALL ROOMS ==========")
    for i in range(len(rooms)):
        print("Room Number:", rooms[i][0])
        print("Room Type:", rooms[i][1])
        print("Capacity:", rooms[i][2], "Person")
        print("Price Per Night:", rooms[i][3], "$")
        print("Status:", rooms[i][4])
    print("===============================")


def show_available_rooms():
    found = False
    print("======= AVAILABLE ROOMS =======")
    for i in range(len(rooms)):
        if rooms[i][4] == "Available":
            print("Room Number:", rooms[i][0])
            print("Room Type:", rooms[i][1])
            print("Capacity:", rooms[i][2], "Person")
            print("Price Per Night:", rooms[i][3], "$")
            found = True
    if found == False:
        print("There are no available rooms!")


def reserve_room():
    print("\n======= NEW RESERVATION =======")
    name = input("Enter full name: ").strip()
    if name == "":
        print("Name cannot be empty!")
        return
    phone = input("Enter phone number: ").strip()
    if not phone.isdigit() or len(phone) < 10 or len(phone) > 15:
        print("Invalid phone number!")
        return
    room_number = input("Enter room number: ")
    if not room_number.isdigit():
        print("Invalid room number!")
        return
    room_number = int(room_number)
    room_index = find_room_index(room_number)
    if room_index == -1:
        print("Room does not exist!")
        return
    if rooms[room_index][4] == "Reserved":
        print("This room is already reserved!")
        return
    guests = input("Enter number of guests: ")
    if not guests.isdigit() or int(guests) <= 0:
        print("Invalid number of guests!")
        return
    guests = int(guests)
    if guests > rooms[room_index][2]:
        print("Number of guests exceeds room capacity!")
        return
    nights = input("Enter number of nights: ")
    if not nights.isdigit() or int(nights) <= 0:
        print("Invalid number of nights!")
        return
    nights = int(nights)
    price_per_night = rooms[room_index][3]
    total_price = price_per_night * nights
    code = "R" + str(reservation_counter[0])
    reservation_counter[0] = reservation_counter[0] + 1
    reservation = [
        code,
        name,
        phone,
        room_number,
        guests,
        nights,
        total_price
    ]
    reservations.append(reservation)
    rooms[room_index][4] = "Reserved"
    print("Reservation completed successfully!")
    show_reservation(reservation)


def cancel_reservation():
    if len(reservations) == 0:
        print("There are no reservations!")
        return
    print("1. Search by room number")
    print("2. Search by reservation code")
    choice = input("Choose: ")
    match choice:
        case "1":
            number = input("Enter room number: ")
            if not number.isdigit():
                print("Invalid room number!")
                return
            number = int(number)
            index = find_reservation_by_room(number)
        case "2":
            code = input("Enter reservation code: ").strip()
            if code == "":
                print("Reservation code cannot be empty!")
                return
            index = find_reservation_by_code(code)
        case _:
            print("Invalid choice!")
            return
    if index == -1:
        print("Reservation not found!")
        return
    print("Selected Reservation:")
    show_reservation(reservations[index])
    confirm = input("Are you sure you want to cancel? (y/n): ").lower()
    match confirm:
        case "y":
            room_number = reservations[index][3]
            room_index = find_room_index(room_number)
            reservations.pop(index)
            rooms[room_index][4] = "Available"
            print("Reservation cancelled successfully!")
        case "n":
            print("Cancellation aborted!")
        case _:
            print("Invalid confirmation!")


def search_reservation():
    if len(reservations) == 0:
        print("There are no reservations!")
        return
    print("1. Search by customer name")
    print("2. Search by phone number")
    print("3. Search by room number")
    choice = input("Choose search type: ")
    found = False
    match choice:
        case "1":
            name = input("Enter customer name: ").strip().lower()
            if name == "":
                print("Name cannot be empty!")
                return
            for i in range(len(reservations)):
                if name in reservations[i][1].lower():
                    show_reservation(reservations[i])
                    found = True
        case "2":
            phone = input("Enter phone number: ").strip()
            for i in range(len(reservations)):
                if phone == reservations[i][2]:
                    show_reservation(reservations[i])
                    found = True
        case "3":
            number = input("Enter room number: ")
            if not number.isdigit():
                print("Invalid room number!")
                return
            number = int(number)
            for i in range(len(reservations)):
                if number == reservations[i][3]:
                    show_reservation(reservations[i])
                    found = True
        case _:
            print("Invalid choice!")
            return
    if found == False:
        print("No reservation found!")


def calculate_price():
    room_number = input("Enter room number: ")
    if not room_number.isdigit():
        print("Invalid room number!")
        return
    room_number = int(room_number)
    room_index = find_room_index(room_number)
    if room_index == -1:
        print("Room does not exist!")
        return
    nights = input("Enter number of nights: ")
    if not nights.isdigit() or int(nights) <= 0:
        print("Invalid number of nights!")
        return
    nights = int(nights)
    price = rooms[room_index][3]
    total = price * nights
    print("======= PRICE DETAILS =======")
    print("Room Number:", room_number)
    print("Room Type:", rooms[room_index][1])
    print("Price Per Night:", price, "$")
    print("Number Of Nights:", nights)
    print("Total Price:", total, "$")
    print("=============================")


def show_all_reservations():
    if len(reservations) == 0:
        print("There are no reservations!")
        return
    print("======= ALL RESERVATIONS =======")
    for i in range(len(reservations)):
        print("Reservation Number:", i + 1)
        show_reservation(reservations[i])
    print("================================")


def hotel_statistics():
    total_rooms = len(rooms)
    reserved_rooms = 0
    available_rooms = 0
    total_income = 0
    for i in range(len(rooms)):
        if rooms[i][4] == "Reserved":
            reserved_rooms = reserved_rooms + 1
        else:
            available_rooms = available_rooms + 1
    for i in range(len(reservations)):
        total_income = total_income + reservations[i][6]
    if total_rooms > 0:
        occupancy = reserved_rooms * 100 / total_rooms
    else:
        occupancy = 0
    print("======= HOTEL STATISTICS =======")
    print("Total Rooms:", total_rooms)
    print("Reserved Rooms:", reserved_rooms)
    print("Available Rooms:", available_rooms)
    print("Total Reservation Income:", total_income, "$")
    print("Hotel Occupancy:", round(occupancy, 2), "%")
    print("================================")


while True:
    print("======= HOTEL RESERVATION =======")
    print("1. Show All Rooms")
    print("2. Show Available Rooms")
    print("3. Reserve Room")
    print("4. Cancel Reservation")
    print("5. Search Reservation")
    print("6. Calculate Price")
    print("7. Show All Reservations")
    print("8. Hotel Statistics")
    print("9. Exit")
    print("=================================")
    choice = input("Choose: ")
    match choice:
        case "1":
            show_all_rooms()
        case "2":
            show_available_rooms()
        case "3":
            reserve_room()
        case "4":
            cancel_reservation()
        case "5":
            search_reservation()
        case "6":
            calculate_price()
        case "7":
            show_all_reservations()
        case "8":
            hotel_statistics()
        case "9":
            print("Thank you for using Hotel Reservation System!")
            break
        case _:
            print("Invalid choice!")