from datetime import datetime

#====================File paths=====================#
#USER_DATA_FILE = "user_data.txt"
ADMIN_USERNAME = "HHS"
ADMIN_PASSWORD = "HHSTrio"
CART_HISTORY_FILE= "cart_history.txt"

#===================Product list=====================#
products = [
    {"id": 1, "name": "cricket bat", "price": 1200},
    {"id": 2, "name": "cricket ball", "price": 250},
    {"id": 3, "name": "football", "price": 750},
    {"id": 4, "name": "basket ball", "price": 800},
    {"id": 5, "name": "badminton", "price": 850},
    {"id": 6, "name": "table tennis", "price": 500},
    {"id": 7, "name": "frisbee", "price": 200},
    {"id": 8, "name": "hockey", "price": 550},
    {"id": 9, "name": "volley ball", "price": 450},
    {"id": 10, "name": "carrom board", "price": 2000}
]

#Cart and Shopping History(GLOBAL LIST)
users = []
history = []

def display_list():
    with open('displaylist.txt', "r") as file:
        print(file.read())

def display_products():
    for i, product in enumerate(products, 0):
        print(f"{i}. {product['name']} - Rs.{product['price']}")

#=====================ACCOUNT CREATION AND LOGIN====================#

def create_account():
    user_info = {
        "first_name": input("Enter your first name: "),
        "last_name": input("Enter your last name: "),
        "username": input("Enter username: "),
        "password": input("Enter password: "),
        "cart": []
    }
    users.append(user_info)
    print("Account created successfully!\nPlease Login now to proceed shopping!")
    

def save_user_data():
    with open("user_data.txt", "a+") as file:
        for user in users:
            file.write(f"{user['username']}:{user['password']}\n")

def load_user_data():
    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                data = line.strip().split(":")
                if len(data) == 4:
                    users.append({
                        "username": data[0],
                        "password": data[1],
                        "first_name": data[2],
                        "last_name": data[3],
                        "cart": []
                    })
    except FileNotFoundError:
        pass

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful as Admin!")
        return admin()
    
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            return user
    
    print("Invalid username or password. Please try again.")
    return None

#==============================CART===========================#
def add_to_cart(user):
    while True:
        display_products()
        try:
            product_index = int(input("Enter the product number to add to the cart: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        quantity = input("Enter the quantity: ")
        if not quantity.isdigit():
            print("Please enter a valid integer")
            return add_to_cart(user)
        else:
            quantity=int(quantity)
    

        if 0 <= product_index < len(products):
            product = products[product_index]
            user["cart"].append({"name": product["name"], "price": product["price"], "quantity": quantity, "id": product["id"]})
            print("Product added to the cart.")
        else:
            print("Invalid product number.")

        more_products = input("Do you want to add more products to your cart? (yes/no): ").lower()
        if more_products != 'yes':
            break

def remove_items(user):
    display_cart(user)
    print("To remove items from the cart:")
    while True:
        removed_item = input('Enter the item number you want to remove OR Enter "done" to exit: ')
        if removed_item == 'done':
            break
        if not removed_item.isdigit():
            return"Please enter an integer value"
        else:
            removed_item = int(removed_item)

        if 0 <= removed_item < len(user["cart"]):
            removed_product = user["cart"].pop(removed_item)
            print(f'Item {removed_item} ({removed_product["name"]}) removed from cart.')
            
            print("Updated Cart:")
            display_cart(user)

            with open(CART_HISTORY_FILE, 'a+') as cart_file:
                cart_file.write(f"Removed from Cart: Product ID: {removed_product['id']}, Name: {removed_product['name']}, Price: {removed_product['price']}, Quantity: {removed_product['quantity']}\n")
        else:
            print(f'Invalid item number.')

def display_cart(user):
    print("Your Cart:")
    total_price = 0
    for i, item in enumerate(user["cart"]):
        total_price += item["price"] * item["quantity"]
        print(f"{i}. {item['name']} - Rs.{item['price']} x {item['quantity']}")
    print(f"Total Price: Rs.{total_price}")

#===========================SAVE INFO USING FILING===================#
def save_login_credentials():
    with open("user_data.txt", "a+") as file:
        for user in users:
            file.write(f"{user['username']}:{user['password']}\n")

def load_login_credentials():
    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                data = line.strip().split(":")
                if len(data) == 2:
                    users.append({
                        "username": data[0],
                        "password": data[1],
                        "cart": []
                    })
    except FileNotFoundError:
        pass
#==================================ADMIN PREVILLAGES==============================#

def admin():
    print('Admin operations:')
    
    while True:
        print('\t1. View Shopping History\n\t2. View User History\n\t3. Continue as User\n\t4. Exit')
        operation = input('Enter the operation (1-4): ')
        if operation == '1':
            view_shopping_history(admin)
        elif operation == '2':
            view_user_history(admin)
        elif operation == '3':
            break
        elif operation == '4':
            print('Exiting Admin operations.')
            break
        else:
            print('Invalid operation. Please enter a valid number.')

def view_shopping_history(admin):
    print("Viewing Shopping History:")
    try:
        with open(CART_HISTORY_FILE, 'r') as file:
            print(file.read())
    except FileNotFoundError:
            print("No shopping history found.")
    print("YOU DONT HAVE THE PROPPER CREDENTIALS")  
    return login()

def view_user_history(admin):
    print('To view the USER histories of the users who have logged in to the website')
    try :
        with open("user_data.txt", 'r') as file:
           print(file.read())
    except FileNotFoundError:
        print("No shopping history found.")
    print("YOU DONT HAVE THE PROPPER CREDENTIALS")
    return login()
#------------------------------PROGRAM REACHING ITS CLIMAX--------------------------

def checkout(user):
    print("You are approaching the last stage of this process")
    ques = input("Would you like us to deliver the order at your doorstep or will you pick it up from the store?\ntype 'deliver' for home delivery or 'store' for pick up: ").lower()
    if 'deliver' in ques:
        deli = input("Please write your delivery address of your current location: ")
        print("Please be patient as the order may take around 30 minutes to be delivered")
    elif 'store' in ques:
        print('We have received your order and are now working on it; in the meantime, please drop by')
    else:
        print("Please enter a valid response")
    print("Thank you for using our website on this platform\nHope we will get to serve you again !!!")

#==================================MAIN PROGRAMM=========================================#

while True:
    print("******** WELCOME TO HHS SPORTS ********\n\t1. Display items\n\t2. Login\n\t3. Create Account\n\t4. Access As An Admin\n\t5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_list()
    elif choice == "2":
        load_user_data()
        load_login_credentials()
        user = login()
        if user:
            save_user_data()
            break
    elif choice == "3":
        create_account()
        save_user_data()
        save_login_credentials()
    elif choice == "4":
        login()
    elif choice == "5":
        print("Thanks for visiting. Goodbye!")
        break
    else:
        print("Invalid choice, please try again!")

# After successful login, select your options
while True:
    print("******** WELCOME TO HHS SPORTS ********\n\t1. Display list\n\t2. Add to Cart\n\t3. Remove from Cart\n\t4. View cart\n\t5. View Shopping History(FOR ADMIN)\n\t6. Checkout\n\t7. Logout")
    choice = input("Enter your choice: ")

    if choice == "1":
        display_list()
    elif choice == "2":
        add_to_cart(user)
    elif choice == "3":
        remove_items(user)
    elif choice == "4":
        display_cart(user)
    elif choice == "5":
        usd=input("ENTER ADMIN USER_NAME: ")
        psd=input("ENTER ADMIN PASSWORD: ")
        if usd == ADMIN_USERNAME and psd == ADMIN_PASSWORD:
            view_shopping_history(admin)
        else:
            print("YOU DONT HAVE THE PROPPER CREDENTIALS")
    elif choice == "6":
        checkout(user)
    elif choice == "7":
        print("Logout successful!")
        break
    else:
        print("Invalid choice, please try again!")
