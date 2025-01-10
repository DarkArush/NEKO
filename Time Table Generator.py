import sys

# Dictionary to store the timetable
timetable = {}

def generate_timetable():
    print("\n--- Generate Timetable ---")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("For each day, define the schedule with time slots (e.g., 8:00 AM - 9:00 AM).")

    for day in days:
        print(f"\nEnter details for {day}:")
        timetable[day] = []
        while True:
            time_slot = input("Enter time slot (or type 'done' to finish for this day): ")
            if time_slot.lower() == 'done':
                break
            activity = input(f"Enter activity for {time_slot}: ")
            timetable[day].append({"Time Slot": time_slot, "Activity": activity})

    print("\nTimetable generated successfully!\n")

def show_timetable():
    print("\n--- Show Timetable ---")
    if not timetable:
        print("No timetable found. Please generate one first.\n")
        return

    for day, activities in timetable.items():
        print(f"\n{day}:")
        for entry in activities:
            print(f"{entry['Time Slot']}: {entry['Activity']}")

def update_timetable():
    print("\n--- Update Timetable ---")
    if not timetable:
        print("No timetable found. Please generate one first.\n")
        return

    day = input("Enter the day to update (e.g., Monday): ")
    if day not in timetable:
        print("Invalid day.\n")
        return

    time_slot = input("Enter the time slot to update (e.g., 8:00 AM - 9:00 AM): ")
    for entry in timetable[day]:
        if entry["Time Slot"] == time_slot:
            new_activity = input("Enter the new activity: ")
            entry["Activity"] = new_activity
            print("Time slot updated successfully!\n")
            return

    print("Time slot not found.\n")

def feedback_system():
    print("\n--- Feedback System ---")
    feedback = input("Enter your feedback about the timetable system: ")
    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")
    print("Thank you for your feedback!\n")

def main_menu():
    while True:
        print("\n--- Timetable Generator ---")
        print("1. Generate Timetable")
        print("2. Show Timetable")
        print("3. Update Timetable")
        print("4. Feedback System")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            generate_timetable()
        elif choice == "2":
            show_timetable()
        elif choice == "3":
            update_timetable()
        elif choice == "4":
            feedback_system()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()