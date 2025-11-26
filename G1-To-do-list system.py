from datetime import datetime

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks (with Filter)")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Search Tasks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        while True:
            description = ""
            while True:
                description = input("Enter task description (or 0 to cancel): ").strip()
                if description == '0':
                    break
                if not description:
                    print("Error: Description cannot be empty.")
                elif description.isdigit():
                    print("Error: Description cannot be only numbers.")
                else:
                    break
            if description == '0':
                print("Add task canceled.")
                break 

            priority = ""
            while True:
                print("Enter priority (or 0 to cancel):")
                print("1. High")
                print("2. Medium")
                print("3. Low")
                priority_choice = input("Enter choice (1-3): ")
                if priority_choice == '0':
                    priority = '0'
                    break
                if priority_choice == '1':
                    priority = "High"
                    break
                if priority_choice == '2':
                    priority = "Medium"
                    break
                if priority_choice == '3':
                    priority = "Low"
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            if priority == '0':
                print("Add task canceled.")
                break 

            task_datetime = None
            
            while True:
                task_date_str = input("Enter date (YYYY-MM-DD) (or 0 to cancel): ")
                if task_date_str == '0':
                    break
                try:
                    datetime.strptime(task_date_str, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            
            if task_date_str == '0':
                print("Add task canceled.")
                break 

            while True:
                task_time_str = input("Enter time (HH:MMAM/PM) (or 0 to cancel): ")
                if task_time_str == '0':
                    task_date_str = '0' 
                    break
                
                task_time_cleaned = task_time_str.replace(" ", "").upper()
                try:
                    task_datetime = datetime.strptime(f"{task_date_str} {task_time_cleaned}", "%Y-%m-%d %I:%M%p")
                    is_conflict = False
                    for t in tasks:
                        if t['datetime'] == task_datetime:
                            is_conflict = True
                            break
                    if is_conflict:
                        print("Error: A task already exists at this date and time.")
                    else:
                        break
                except ValueError:
                    print("Invalid time format. Use HH:MMAM/PM (e.g., 03:00PM)")
            
            if task_date_str == '0':
                print("Add task canceled.")
                break 

            new_task_details = {
                "description": description,
                "priority": priority,
                "datetime": task_datetime
            }
            
            add_another = '0' 
            confirm_choice = '0' 

            while True:
                print("\n--- Confirm New Task ---")
                print(f"1. Description: {new_task_details['description']}")
                print(f"2. Priority:    {new_task_details['priority']}")
                print(f"3. Time:        {new_task_details['datetime'].strftime('%Y-%m-%d %I:%M %p')}")
                print("-------------------------")
                print("4. Confirm and Add Task")
                print("5. Cancel")
                confirm_choice = input("Enter choice (1-3 to edit, 4 to confirm, 5 to cancel): ")

                if confirm_choice == '1':
                    while True:
                        new_desc = input("Enter new description: ").strip()
                        if not new_desc:
                            print("Error: Description cannot be empty.")
                        elif new_desc.isdigit():
                            print("Error: Description cannot be only numbers.")
                        else:
                            new_task_details['description'] = new_desc
                            break
                elif confirm_choice == '2':
                    while True:
                        print("Enter new priority:")
                        print("1. High")
      