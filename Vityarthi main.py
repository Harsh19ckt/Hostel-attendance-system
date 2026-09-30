# default recorded student data
records = {
    "Ekansh gupta": "Present",
    "Lakshay kumar": "Present",
    "Bhavya": "Absent",
    "raghav": "absent"
}

def get_clean_name():
    return input("Enter student name: ").strip().title()

def show_attendance():
    print(f"\n{'='*10} Hostel Attendance {'='*10}")
    for student, status in records.items():
        print(f"{student:<20} -> {status}")

def update_status():
    name = get_clean_name()
    if name not in records:
        return print(f" '{name}' is not registered.")

    print(f"Current status: {records[name]}")
    new_status = input("Change to (Present/Absent): ").strip().title()
    
    if new_status in ("Present", "Absent"):
        records[name] = new_status
        print(" Status updated.")
    else:
        print(" Invalid input.")

def register_student():
    name = get_clean_name()
    if name in records:
        return print(" Student already exists.")
        
    records[name] = "Present"
    print(f" Registered {name}.")

def main():
   
    menu_actions = {
        '1': show_attendance,
        '2': update_status,
        '3': register_student
    }

    while True:
        print("\n HOSTEL MENU ")
        print("1. View Attendance\n2. Update Attendance\n3. Add New Student\n4. Exit")
        
        action = input("Select an option: ").strip()
        
        if action == '4':
            print("Attendance completed.")
            break
            
        menu_actions.get(action, lambda: print("Invalid option. Try again."))()

if __name__ == "__main__":
    main()
