rom datetime import datetime

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
                        print("2. Medium")
                        print("3. Low")
                        pri_choice = input("Enter choice (1-3): ")
                        if pri_choice == '1':
                            new_task_details['priority'] = "High"
                            break
                        elif pri_choice == '2':
                            new_task_details['priority'] = "Medium"
                            break
                        elif pri_choice == '3':
                            new_task_details['priority'] = "Low"
                            break
                        else:
                            print("Invalid choice.")
                elif confirm_choice == '3':
                    while True:
                        while True:
                            new_date_str = input("Enter new date (YYYY-MM-DD): ")
                            try:
                                datetime.strptime(new_date_str, "%Y-%m-%d")
                                break
                            except ValueError:
                                print("Invalid date format. Please use YYYY-MM-DD.")
                        
                        while True:
                            new_time_str = input("Enter new time (HH:MMAM/PM): ")
                            new_time_cleaned = new_time_str.replace(" ", "").upper()
                            try:
                                datetime.strptime(new_time_cleaned, "%I:%M%p")
                                break
                            except ValueError:
                                print("Invalid time format. Use HH:MMAM/PM (e.g., 03:00PM)")

                        try:
                            new_datetime = datetime.strptime(f"{new_date_str} {new_time_cleaned}", "%Y-%m-%d %I:%M%p")
                            is_conflict = False
                            for t in tasks:
                                if t['datetime'] == new_datetime:
                                    is_conflict = True
                                    break
                            if is_conflict:
                                print("Error: A task already exists at this date and time.")
                            else:
                                new_task_details['datetime'] = new_datetime
                                break
                        except ValueError:
                            print("An unexpected error occurred. Please try again.")
                            
                elif confirm_choice == '4':
                    new_task = {
                        "description": new_task_details['description'],
                        "priority": new_task_details['priority'],
                        "status": "Pending",
                        "datetime": new_task_details['datetime']
                    }
                    tasks.append(new_task)
                    print("Task added successfully!")
                    add_another = input("Add another task? (1. Yes, 2. No): ")
                    if add_another == '1':
                        break 
                    else:
                        break 
                elif confirm_choice == '5':
                    print("Add task canceled.")
                    break 
                else:
                    print("Invalid choice, please try again.")
            
            if (confirm_choice == '4' and add_another != '1') or confirm_choice == '5':
                break

    elif choice == '2':
        while True:
            print("\n--- View Tasks (with Filter) ---")
            print("Filter by:")
            print("1. Pending Tasks")
            print("2. Done Tasks")
            print("3. All Tasks")
            print("4. Go back to menu")
            
            filter_choice = input("Enter choice (1-4): ")

            if filter_choice == '4':
                break
            
            if not tasks:
                print("\nList is empty. Nothing to show.")
                input("Press Enter to continue...")
                continue

            filter_status = 'all'
            if filter_choice == '1':
                filter_status = 'pending'
                title = "--- Showing 'Pending' Tasks ---"
            elif filter_choice == '2':
                filter_status = 'done'
                title = "--- Showing 'Done' Tasks ---"
            elif filter_choice == '3':
                filter_status = 'all'
                title = "--- Showing 'All' Tasks ---"
            else:
                print("Invalid choice, please try again.")
                input("Press Enter to continue...")
                continue

            print(f"\n{title}")
            found_tasks = False
            tasks.sort(key=lambda x: x['datetime'])
            for i, task in enumerate(tasks):
                task_time_str = task['datetime'].strftime("%Y-%m-%d %I:%M %p")
                if filter_status == 'all' or task['status'].lower() == filter_status:
                    print(f"{i + 1}. [{task['status']}] {task['description']} - Priority: {task['priority']} @ {task_time_str}")
                    found_tasks = True
            
            if not found_tasks:
                print(f"No '{filter_status}' tasks found.")
            
            input("\nPress Enter to continue...")

    elif choice == '3':
        if not tasks:
            print("There are no tasks to mark as done.")
        else:
            print("\nYour Tasks:")
            tasks.sort(key=lambda x: x['datetime'])
            for i, task in enumerate(tasks):
                task_time_str = task['datetime'].strftime("%Y-%m-%d %I:%M %p")
                print(f"{i + 1}. [{task['status']}] {task['description']} - Priority: {task['priority']} @ {task_time_str}")
            try:
                task_no = int(input("\nEnter task number to mark done (or 0 to cancel): "))
                if task_no == 0:
                    continue
                index = task_no - 1
                if 0 <= index < len(tasks):
                    confirm = input(f"Mark '{tasks[index]['description']}' as Done? (1. Yes, 2. No): ")
                    if confirm == '1':
                        tasks[index]['status'] = "Done"
                        print(f"Task #{task_no} marked as done!")
                    else:
                        print("Action canceled.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == '4':
        if not tasks:
            print("There are no tasks to delete.")
        else:
            print("\nYour Tasks:")
            tasks.sort(key=lambda x: x['datetime'])
            for i, task in enumerate(tasks):
                task_time_str = task['datetime'].strftime("%Y-%m-%d %I:%M %p")
                print(f"{i + 1}. [{task['status']}] {task['description']} - Priority: {task['priority']} @ {task_time_str}")

            try:
                task_no = int(input("\nEnter task number to delete (or 0 to cancel): "))
                if task_no == 0:
                    continue

                index = task_no - 1
                if 0 <= index < len(tasks):
                    confirm = input(f"Delete '{tasks[index]['description']}'? (1. Yes, 2. No): ")
                    if confirm == '1':
                        removed_task = tasks.pop(index)
                        print(f"Task '{removed_task['description']}' deleted successfully!")
                    else:
                        print("Action canceled.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input.Please enter a number.")

    elif choice == '5':
        if not tasks:
            print("There are no tasks to edit.")
        else:
            print("\nYour Tasks:")
            tasks.sort(key=lambda x: x['datetime'])
            for i, task in enumerate(tasks):
                task_time_str = task['datetime'].strftime("%Y-%m-%d %I:%M %p")
                print(f"{i + 1}. [{task['status']}] {task['description']} - Priority: {task['priority']} @ {task_time_str}")
            try:
                task_no = int(input("\nEnter task number to edit (or 0 to cancel): "))
                if task_no == 0:
                    continue
                index = task_no - 1
                if 0 <= index < len(tasks):
                    task_to_edit = tasks[index]
                    while True:
                        print(f"\nEditing Task #{task_no}:")
                        print(f"  Description: {task_to_edit['description']}")
                        print(f"  Priority:    {task_to_edit['priority']}")
                        print(f"  Time:        {task_to_edit['datetime'].strftime('%Y-%m-%d %I:%M %p')}")
                        print("\nWhat do you want to edit?")
                        print("1. Description")
                        print("2. Priority")
                        print("3. Date/Time")
                        print("4. Finish Editing")
                        edit_choice = input("Enter choice (1-4): ")

                        if edit_choice == '1':
                            while True:
                                new_description = input("Enter new description: ").strip()
                                if not new_description:
                                    print("Error: Description cannot be empty.")
                                elif new_description.isdigit():
                                    print("Error: Description cannot be only numbers.")
                                else:
                                    task_to_edit['description'] = new_description
                                    print("Description updated!")
                                    break
                        elif edit_choice == '2':
                            while True:
                                print("Enter new priority:")
                                print("1. High")
                                print("2. Medium")
                                print("3. Low")
                                priority_choice = input("Enter choice (1-3): ")
                                if priority_choice == '1':
                                    task_to_edit['priority'] = "High"
                                    print("Priority updated!")
                                    break
                                elif priority_choice == '2':
                                    task_to_edit['priority'] = "Medium"
                                    print("Priority updated!")
                                    break
                                elif priority_choice == '3':
                                    task_to_edit['priority'] = "Low"
                                    print("Priority updated!")
                                    break
                                else:
                                    print("Invalid choice. Please enter 1, 2, or 3.")
                        elif edit_choice == '3':
                            while True:
                                while True:
                                    new_date_str = input("Enter new date (YYYY-MM-DD): ")
                                    try:
                                        datetime.strptime(new_date_str, "%Y-%m-%d")
                                        break
                                    except ValueError:
                                        print("Invalid date format. Please use YYYY-MM-DD.")
                                
                                while True:
                                    new_time_str = input("Enter new time (HH:MMAM/PM): ")
                                    new_time_cleaned = new_time_str.replace(" ", "").upper()
                                    try:
                                        datetime.strptime(new_time_cleaned, "%I:%M%p")
                                        break
                                    except ValueError:
                                        print("Invalid time format. Use HH:MMAM/PM (e.g., 03:00PM)")
                                try:
                                    new_datetime = datetime.strptime(f"{new_date_str} {new_time_cleaned}", "%Y-%m-%d %I:%M%p")
                                    is_conflict = False
                                    for i, t in enumerate(tasks):
                                        if i == index:
                                            continue
                                        if t['datetime'] == new_datetime:
                                            is_conflict = True
                                            break
                                    if is_conflict:
                                        print("Error: A task already exists at this date and time.")
                                    else:
                                        task_to_edit['datetime'] = new_datetime
                                        print("Date/Time updated!")
                                        break
                                except ValueError:
                                    print("An unexpected error occurred. Please try again.")

                        elif edit_choice == '4':
                            print("Finished editing.")
                            break
                        else:
                            print("Invalid choice.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == '6':
        if not tasks:
            print("Task list is empty. Nothing to search.")
        else:
            search_term = input("Enter search term to find in description: ").lower()
            print(f"\nSearching for tasks containing '{search_term}'...")
            found_count = 0
            tasks.sort(key=lambda x: x['datetime'])
            for i, task in enumerate(tasks):
                if search_term in task['description'].lower():
                    task_time_str = task['datetime'].strftime("%Y-%m-%d %I:%M %p")
                    print(f"  {i + 1}. [{task['status']}] {task['description']} - Priority: {task['priority']} @ {task_time_str}")
                    found_count += 1
            print(f"Found {found_count} matching task(s).")
            
    elif choice == '7':
        print("Exiting system...")
        break
    else:
        print("Invalid choice, please try again.")
