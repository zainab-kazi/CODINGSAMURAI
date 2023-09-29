import sys # for system exit in main code
import time # for pause delay in checking data
# initialize empty dictionary
# curly brackets used for ease in formating string later
tasks = {}

# using def function to seperately execute code for
# add_task, view_task, delete_task respectively
def add_task():
    task_description = input("\nEnter a new task: ")
    task_number = len(tasks) + 1
    tasks[task_number] = task_description
    time.sleep(2)
    print("\nTo-do TASK ADDED..")
    
def view_tasks():
    if not tasks:
        print("\nChecking system.....")
        time.sleep(2)
        print("\nNo tasks.")
    else:
        print("\nNEW TO-DO LIST")
        for task_number, task_description in tasks.items():
            print(f'\n{task_number}.{task_description}')

def delete_task():
    if not tasks:
        print("\nChecking sytem...")
        time.sleep(3)
        print("\nData empty..no tasks to delete!")
       
    else:
        print("\nTo-do tasks: ")
        for task_number, task_description in tasks.items():
            print(f'{task_number}.{task_description}')
        task_number = int(input('\nEnter the task number to delete: '))
        
        if task_number in tasks:
            del tasks[task_number]
            print('\nTASK DELETED!')
        else:
            print('Invalid task number.')

# def main() --> main code to be executed
def main():
    while True:
        print('\n ****** To-Do List using Command Line******')
        print("\n****Enter your choice as 1,2,3 or 4****")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Quit")
        
        choice = int(input("\nYour choice? "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
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
         
