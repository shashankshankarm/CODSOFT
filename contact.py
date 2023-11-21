def add_contact(contacts):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        'Name': name,
        'Phone': phone_number,
        'Email': email,
        'Address': address
    }
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts(contacts):
    if contacts:
        print("===== Contact List =====")
        for index, contact in enumerate(contacts, start=1):
            print(f"Contact {index}:")
            for key, value in contact.items():
                print(f"{key}: {value}")
            print("------------------------------")
    else:
        print("Contact list is empty.")

def search_contact(contacts, search_query):
    found = False
    for contact in contacts:
        if search_query.lower() in [contact['Name'].lower(), contact['Phone']]:
            print("Contact found:")
            for key, value in contact.items():
                print(f"{key}: {value}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact(contacts, search_query):
    for contact in contacts:
        if search_query.lower() in [contact['Name'].lower(), contact['Phone']]:
            name = input("Enter updated name: ")
            phone_number = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            address = input("Enter updated address: ")
            contact.update({
                'Name': name,
                'Phone': phone_number,
                'Email': email,
                'Address': address
            })
            print("Contact updated successfully.")
            break
    else:
        print("Contact not found.")

def delete_contact(contacts, search_query):
    contacts_copy = contacts.copy()
    for contact in contacts_copy:
        if search_query.lower() in [contact['Name'].lower(), contact['Phone']]:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            break
    else:
        print("Contact not found.")

def main():
    contacts = []

    while True:
        print("\n====== Contact Management System ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_query = input("Enter name or phone number to search: ")
            search_contact(contacts, search_query)
        elif choice == '4':
            search_query = input("Enter name or phone number to update: ")
            update_contact(contacts, search_query)
        elif choice == '5':
            search_query = input("Enter name or phone number to delete: ")
            delete_contact(contacts, search_query)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
