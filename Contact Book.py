class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        search_results = [contact for contact in self.contacts if
                          search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if search_results:
            print("\nSearch Results:")
            for result in search_results:
                print(f"Name: {result.name}, Phone: {result.phone}")
        else:
            print("\nNo matching contacts found.")

    def update_contact(self, contact_name):
        for contact in self.contacts:
            if contact.name.lower() == contact_name.lower():
                new_phone = input("Enter the new phone number: ")
                new_email = input("Enter the new email address: ")
                new_address = input("Enter the new address: ")
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"{contact_name}'s contact details updated.")
                return
        print(f"Contact with the name '{contact_name}' not found.")

    def delete_contact(self, contact_name):
        for contact in self.contacts:
            if contact.name.lower() == contact_name.lower():
                self.contacts.remove(contact)
                print(f"{contact_name}'s contact deleted.")
                return
        print(f"Contact with the name '{contact_name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the contact name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)
            print(f"{name}'s contact added successfully.")
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter the name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == "4":
            contact_name = input("Enter the name of the contact to update: ")
            contact_manager.update_contact(contact_name)
        elif choice == "5":
            contact_name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(contact_name)
        elif choice == "6":
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
