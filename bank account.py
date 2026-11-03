









def deposit(balance, transactions):
    """VARIZ POUL"""
    amount = input("ENTER DEPOSIT AMOUNT: ").strip()
    if amount.isdigit():
        amount = int(amount)
        if amount > 0:
            balance = balance + amount
            transactions.append(amount)
            print("VARIZ POUL MOVAFAGH BOOD!")
            print("MOJOODI JADID:", balance)
        else:
            print("MEGHDAR BAYAD MOSBAT BASHAD!")
    else:
        print("FAGHAT ADAD VARED KONID!")
    return balance


def withdraw(balance, transactions):
    """BARDASHT POUL"""
    amount = input("ENTER WITHDRAWAL AMOUNT: ").strip()
    if amount.isdigit():
        amount = int(amount)
        if amount > 0:
            if amount <= balance:
                balance = balance - amount
                transactions.append(-amount)
                print("BARDASHT POUL MOVAFAGH BOOD!")
                print("MOJOODI JADID:", balance)
            else:
                print("MEGHDAR NAMOJOOD!")
        else:
            print("MEGHDAR BAYAD MOSBAT BASHAD!")
    else:
        print("FAGHAT ADAD VARED KONID!")
    return balance


def show_balance(balance):
    """MEGHDAR MOJOODI DAR LAHZE"""
    print("MOJOODI DAR LAHZE:", balance)


def show_transactions(transactions):
    """NAMAYESH TAMAM TARAKONESH HA."""
    if len(transactions) == 0:
        print("HICH TARAKONESHI NIST!")
    else:
        print("SABEGHE TARAKONESH:")
        for transaction in transactions:
            if transaction > 0:
                print("+" + str(transaction))
            else:
                print(transaction)


def total_deposits(transactions):
    """MAJMOOE TAMAME VARIZI HA"""
    total = 0
    for transaction in transactions:
        if transaction > 0:
            total = total + transaction
    print("MAJMOOE:", total)



balance = 0
transactions = []

while True:
    print()
    print("========== BANK MENU ==========")
    print("1. VARIZ POUL")
    print("2. BARDASHT POUL")
    print("3. MOJOODI")
    print("4. TARAKONESH HA")
    print("5. MAJMOOE VARIZI HA")
    print("0. KHOROOJ")
    print("===============================")
    choice = input("ENTEKHAB KONID: ").strip()
    match choice:
        case "1":
            balance = deposit(balance, transactions)
        case "2":
            balance = withdraw(balance, transactions)
        case "3":
            show_balance(balance)
        case "4":
            show_transactions(transactions)
        case "5":
            total_deposits(transactions)
        case "0" | "6":
            print("MAMNOON!")
            break
        case _:
            print("AZ 0-6 ENTEKHAB KONID!")
