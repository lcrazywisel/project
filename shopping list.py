









products = []
prices = []


def add_product():
    product = input("Enter product name: ").strip()
    if product == "":
        print("Product name cannot be empty!")
        return
    price = input("Enter product price: ")
    if not price.isdigit() or int(price) <= 0:
        print("Invalid price!")
        return
    price = int(price)
    products.append(product)
    prices.append(price)
    print("Product added successfully!")


def show_cart():
    if len(products) == 0:
        print("Your shopping cart is empty!")
        return
    print("--- Shopping Cart ---")
    for i in range(len(products)):
        print(str(i + 1) + ". " + products[i] + " - " + str(prices[i]))
    print("---------------------")


def remove_product():
    if len(products) == 0:
        print("Your shopping cart is empty!")
        return
    product = input("Enter product name to remove: ").strip()
    found = False
    for i in range(len(products)):
        if products[i].lower() == product.lower():
            products.pop(i)
            prices.pop(i)

            print("Product removed successfully!")
            found = True
            break
    if found == False:
        print("Product not found!")


def count_products():
    print("Number of products:", len(products))


def check_product():
    product = input("Enter product name to search: ").strip()
    found = False
    for i in range(len(products)):
        if products[i].lower() == product.lower():
            print("Product exists in your shopping cart!")
            print("Price:", prices[i])
            found = True
            break
    if found == False:
        print("Product not found!")


def calculate_total():
    total = 0
    for price in prices:
        total = total + price
    print("Total price:", total)


while True:
    print("===== Shopping Cart =====")
    print("1. Add product")
    print("2. Show shopping cart")
    print("3. Remove product")
    print("4. Count products")
    print("5. Check product")
    print("6. Calculate total price")
    print("7. Exit")
    choice = input("Choose an option: ")
    match choice:
        case "1":
            add_product()
        case "2":
            show_cart()
        case "3":
            remove_product()
        case "4":
            count_products()
        case "5":
            check_product()
        case "6":
            calculate_total()
        case "7":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice!")