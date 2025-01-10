import sys

# Dictionary to store child entries
child_records = {}

# Function to generate a unique 5-digit child ID
def generate_child_id():
    import random
    while True:
        child_id = str(random.randint(10000, 99999))
        if child_id not in child_records:
            return child_id

# Function to add a child entry
def add_child_entry():
    print("\n--- Add Child Entry ---")
    name = input("Enter child's name: ")
    dob = input("Enter child's date of birth (DD-MM-YYYY): ")
    gender = input("Enter child's gender (M/F): ")
    parent_name = input("Enter parent's name: ")
    contact_no = input("Enter contact number: ")

    child_id = generate_child_id()
    child_records[child_id] = {
        "Name": name,
        "DOB": dob,
        "Gender": gender,
        "Parent Name": parent_name,
        "Contact No": contact_no
    }
    print(f"Child entry added successfully with Child ID: {child_id}\n")

# Function to delete a child entry
def delete_child_entry():
    print("\n--- Delete Child Entry ---")
    child_id = input("Enter Child ID to delete: ")
    if child_id in child_records:
        del child_records[child_id]
        print("Child entry deleted successfully.\n")
    else:
        print("Child ID not found.\n")

# Function to show a child entry
def show_child_entry():
    print("\n--- Show Child Entry ---")
    child_id = input("Enter Child ID to view details: ")
    if child_id in child_records:
        print("\nChild Details:")
        for key, value in child_records[child_id].items():
            print(f"{key}: {value}")
        print()
    else:
        print("Child ID not found.\n")

# Function to update a child entry
def update_child_entry():
    print("\n--- Update Child Entry ---")
    child_id = input("Enter Child ID to update details: ")
    if child_id in child_records:
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Date of Birth")
        print("3. Gender")
        print("4. Parent's Name")
        print("5. Contact Number")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            child_records[child_id]["Name"] = input("Enter new name: ")
        elif choice == "2":
            child_records[child_id]["DOB"] = input("Enter new date of birth (DD-MM-YYYY): ")
        elif choice == "3":
            child_records[child_id]["Gender"] = input("Enter new gender (M/F): ")
        elif choice == "4":
            child_records[child_id]["Parent Name"] = input("Enter new parent's name: ")
        elif choice == "5":
            child_records[child_id]["Contact No"] = input("Enter new contact number: ")
        else:
            print("Invalid choice.\n")
            return

        print("Child entry updated successfully.\n")
    else:
        print("Child ID not found.\n")

# Main menu function
def main_menu():
    while True:
        print("\n--- Child Vaccination Management System ---")
        print("1. Add Child Entry")
        print("2. Delete Child Entry")
        print("3. Show Child Entry")
        print("4. Update Child Entry")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_child_entry()
        elif choice == "2":
            delete_child_entry()
        elif choice == "3":
            show_child_entry()
        elif choice == "4":
            update_child_entry()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main_menu()