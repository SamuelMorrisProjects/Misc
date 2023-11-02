
WizardsBag = ["Dragon Scale Wand", "Enchanted Grimoire","Eye of Newt",] 
def Show_Menu():
     return("COMMAND MENU"+"\n"+"show- Shows all items"+"\n"+"add- Add an Item"+"\n"+"drop - Drop a Item"+"\n"+"edit- Edit an Item"+"\n"+"exit- exit the program")

def If_In_List(edit, list1): 
    if edit in range(1, (len(list1))+1): 
        return edit-1  
    return "Invalid Number selection"+"\n"   

def Show_Items(list1):
    output= ""
    if len(list1) == 0:  
        return ("Nothing is currently in the bag. Add something first to display it."+"\n")
    for item in range(len(list1)):
        output += (f"{item+1}. {list1[item]}"+"\n")
    return output

def Add_Item(list1):
    if len(list1) == 4: 
        return ("The wizard can't carry any more items. Drop something first. "+"\n")
    name = input(("Name: ")) 
    list1.append(name) 
    return (f"{(name).capitalize()} was added."+"\n") #

def Edit_Item(list1):
    index_value = If_In_List(int(input("Number: ")),list1) 
    if isinstance(index_value, str):
        return index_value
    del list1[index_value]
    list1.insert(index_value, (input("Updated Name: ")))
    return (f"Item Number {index_value+1} was updated."+"\n")

def Drop_Item(list1): 
    index_value = If_In_List(int(input(("Number: "))), list1)
    if isinstance(index_value, str): 
        return index_value
    dropped_item = (list1[(index_value)])  
    del list1[(index_value)] 
    return(f"{(dropped_item).capitalize()} was dropped."+"\n") 

def Exit_Program(Param):  
    print("Bye!")
    quit()

UserCommands = {"edit":Edit_Item, "add":Add_Item, "show":Show_Items, "drop":Drop_Item, "exit":Exit_Program }
def main():
    print("The Wizards Inventory Program"+"\n"+"\n"+Show_Menu()+"\n") 
    while True:
        Command = input("Command: ").rstrip()
        if Command not in UserCommands:
            print("Not a valid command. Please try again."+"\n")
        else:
            print(UserCommands[Command](WizardsBag))
main()