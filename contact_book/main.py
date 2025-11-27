def display_menu():
    print("Contact Book Menu:\n1. Add Contact\n2. View Contact\n3. Edit Contact\n4. Delete Contact\n5. List All Contacts\n6. Exit")

contact_book = {}


def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()

    if name in contact_book:
        print("Contact already exists!")
    else: 
        contact_book[name] = {
            "Phone": phone, 
            "Email": email, 
            "Address": address
            }
        print("Contact added successfully!")
    
def view_contact(contact_book):
    name = input()
    if name in contact_book:
        contact = contact_book[name]
        print(f"""Name: {name}
Phone: {contact['phone']}
Email: {contact['email']}
Address: {contact['address']}""")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()
    

    if name in contact_book:
        phone = input()
        email = input()
        address = input()
    
        contact = contact_book[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found!")
    
def delete_contact(contact_book):
    name = input()
    
    if name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if len(contact_book) == 0:
        print("No contacts available.")
    else:
        for name, contact in contact_book.items():
            print(f"""Name: {name}
Phone: {contact['phone']}
Email: {contact['email']}
Address: {contact['address']}\n""")


while True:
    contact_book = {}

while True:
    display_menu()
    choice = input()

    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")

 