import os

if not os.path.exists('task.txt'):
    with open('task.txt', 'w') as f:
        pass


def menu():
    print("""
1.ADD TASK
2.REMOVE TASK
3.MARK AS DONE
4.LIST TASK
5.EXIT

""")
    
    while True:
     option = input('Choose an option: ')
     if option.isdigit() and 1<=int(option)<=4:
         return option
     else:
       print('Invalid input ')
       
def update_status():
   task_to_change = input('Enter task to update: ')
   with open('task.txt') as f:
      tasks = f.readlines()
   new_list = []
      
   for i in tasks:
      task,status = i.strip().split(' - ')
   
      if task_to_change ==task:
        new_list.append(f'{task} - Completed \n')
        continue
        
      else:
        new_list.append(i)

   with open('task.txt','w') as f:
      for line in new_list:
       f.write(line)

def add_task(status):
   task_name = input('Task name: ')
   status = 'Uncompleted'
   
   with open('task.txt','a') as f :
      f.write(f'{task_name} - {status}'+'\n')

def list_task():
   with open('task.txt') as f:
    for line in f:
       print(line.strip())

def remove_task():
   remove_task = input('Name of Task: ').title().strip()
   with open('task.txt') as f:
      a = f.readlines()
      new_list = []
      for task in a:
         tasks,status = task.strip().split(' - ')
         new_list.append(tasks)
      


      if remove_task in new_list:
            new_list.clear()
            for i in a:
              
              
              task,status = i.strip().split(' - ')
          
          
              if remove_task == task:
                print(f'Task: {remove_task} has been removed')
                continue
               
              else:
                new_list.append(i)
            with open('task.txt', 'w') as f:
              for line in new_list:
                f.write(line)
    
      else:
         print('Task not found')

while True:
    option = menu()
    if option == '1':
        add_task(...)
    elif option == '2':
        remove_task()
    elif option == '3':
        update_status()
    elif option == '4':
        list_task()
    elif option == '5':
       break
    else:
       print('Invalid input')


