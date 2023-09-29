import sys # for system exit in main code
import time # for pause delay in checking data
# initialize empty dictionary
# curly brackets used for ease in formating string later
tasks = {}

# using def function to seperately execute code for
# add_task, view_task, delete_task respectively
def add_task():
    task_title = input("Enter task title: ")
    counter = 1
    while True:
        print("\nHit ENTER key to return to main menu.")
        task_description = input(f'Your tasks: \n{counter} ')
        if not task_description:
            main()
        
        print(f'Your tasks {counter}: {task_description}')
        counter = counter + 1
        task_number = len(tasks) + 1
        tasks[task_number] = {'title': task_title,'description': task_description} 
        time.sleep(1)
        print("\n", task_number ,"To-do TASK ADDED..")
    
def view_tasks():
    if not tasks:
        print("\nChecking system.....")
        time.sleep(1)
        print("\nNo tasks.")
    else:
        print("\nNEW TO-DO LIST")
        for task_number, task in tasks.items():
            print(f'{task_number}.Title: {task["title"]}, \nDescription: {task["description"]}')
            
def delete_task():
    if not tasks:
        print("\nChecking sytem...")
        time.sleep(1)
        print("\nData empty..no tasks to delete!")
       
    else:
        print("\nTo-do tasks: ")
        for task_number, task in tasks.items():
            print(f'{task_number}. Title: {task["title"]}, \nDescription: {task["description"]}')    
        task_number = int(input('\nEnter the task number to delete: '))
        
        if task_number in tasks:
            del tasks[task_number]
            print('\nID NO.', task_number ,'DELETED!')
        else:
            print('Invalid task number.')
            
def save_tasks():

    try:
        with open('tasks.txt','w') as file:
            for task_number, task in tasks.items():
                file.write(f'{task_number}: {task["title"]}\n{task["description"]}')
        print('Task saved successfully.')
    except Exception as e:
        print("\nChecking system...")
        time.sleep(1)
        print(f"\nNo file available: {e}")
    
def load_tasks():
    try:
        with open('tasks.txt','r') as file:
            for line in file:
                task_number, task_info = line.strip().split(': ', 1)
                task_title, task_description = task_info.split(',\n', 1)
                tasks[int(task_number)] = {'title': task_title, '\ndescription': task_description}
        print('Task loaded successfully.')
    except FileNotFoundError:
        print('\nNo saved tasks found. ')

# def main() --> main code to be executed
def main():
    while True:
        print('\n ****** To-Do List using Command Line******')
        print("\n****Enter your choice as 1,2,3,4 or 5****")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Save task")
        print("5. Quit")
        
        choice = int(input("\nYour choice? "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            save_tasks()
        elif choice == 5:
            print("Do you want to Quit? ")
            choice = input("Enter yes  or no: ")
            if choice == "yes":
                print("\nSee you later!")
                sys.exit() #exit the script
            elif choice == "no":
                main()
            else:
                return
        else:
            print("Invalid choice. Please try again!")
    

# calling the main() function already defined above    
if __name__ == "__main__":
    main()
    load_tasks()
    save_tasks()
