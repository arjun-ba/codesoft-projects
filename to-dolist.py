list=[]
def addTask():
     NumTasks=int(input("How many task you want add:"))
     for i in range(1,NumTasks+1):
         Task=input(f"Enter the {i} task:")
         list.append(Task)
     print("Tasks are sucssfully added")

def displayTask():
    if len(list)==0:
        print("you don't have any task.\nplease add the task.")
    else:
        print("***Tasks***")
        for i in range(len(list)):
            print(f"{i+1}.{list[i]}")
            
     
def updateTask():
    update=int(input("Enter the task you want to update:"))
    if update<len(list):
       list[update-1]=input("Enter the new task:")
       print("updated sucssfully.")
    else:
        print(f"{update}th task is not in the list of tasks")

    
def deleteTask():
    if len(list)==0:
        print("there is not task to delete.\nplease add the task to delete.")
    else:
     try:
      print("press 1 to delete the any specific task.\npress 2 to delete all tasks.")
      value=int(input())
      if value==1:
        deletedtask=int(input("Enter the task you want to delete"))
        list.remove(list[deletedtask])
        print(f"{list[deletedtask]} is deleted sucssfully.")
      elif value==2:
          list.clear()
          print("All tasks are removed.")
      else:
           print("invalid input")
     except IndexError:
          print(f"the {deletedtask}th list not in list of tasks")

def main():   
 while True:
  print("****To-Do List****")
  print("Menu")
  print("Press 1 to add Task")
  print("Press 2 to Display the Tasks")
  print("Press 3 to Update the Task")
  print("Press 4 to Delete the task")
  print("Press 5 to Exit")

  InputValue=int(input("Enter the option avalible in the above:"))

  if(InputValue == 1):
      addTask()

  elif(InputValue == 2):
      displayTask()
    
  elif(InputValue == 3):
     updateTask()

  elif(InputValue == 4):
      deleteTask()
    
  elif(InputValue == 5):
      break
        
  else :
     print("invalid input\nplease select the avalible option")

        
if __name__=="__main__" :
    main()


        
        
