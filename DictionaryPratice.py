
email_dict={} 
def exit1():
    print("Bye!")
    quit()
class Email_Dictionary_Class(): 
        def __init__(self, dict1, name_input):
            self.name_input = name_input 
            self.dict1 = dict1 
            self.infoUpdated ="Information updated.\n"
            self.get_email = self.dict1.get(self.name_input) 
        def look_up(self):
            return f"Name: {self.name_input}\nEmail: {self.get_email}\n"
        def add_new(self):
            if self.get_email is None:
                self.dict1.update({self.name_input:input("Enter a email address: ")})
                return f"Name and address have been added.\n"
            return f"That name already exists.\n"
        def change(self):
            self.dict1.update({self.name_input:input("Enter a email address: ")})
            return self.infoUpdated
        def delete(self):
            del self.dict1[self.name_input]
            return self.infoUpdated
def main(choice):
    while choice<0 or choice>5: 
         choice=(int(input("The choice you entered is invalid. Please enter a valid choice: ")))
    if choice ==5:
        exit1() 
    name = input("Enter a name:")
    EmailObj = Email_Dictionary_Class(email_dict, name) 
    if email_dict.get(name) is None and choice!=2: 
        return"The specified name was not found\n" 
    return(EmailObj.look_up, 
           EmailObj.add_new,
           EmailObj.change,
           EmailObj.delete)[(choice-1)]()
while True:
    print("Menu\n"+"-"*35+"\n1.Look up an email address\n2.Add a new name and email address\n3.Change a existing email address\n4.Delete a name and email address\n5.Quit the program")
    print(main(int(input("\nEnter a choice: ")))) 

    




