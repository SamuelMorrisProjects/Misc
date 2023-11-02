from operator import *
from faker import Faker
fake = Faker()

again="y"
Names = [fake.unique.first_name() for i in range(600)]
ModList=[]

totalnames= len(Names)

def lformat(list1, end1, num):
    output = ""
    for element in range(len(list1)):
          if element % num == 1 and element >1:
               output +="\n"
          output += str(list1[element]) + str(end1)
    return output
    
def List_After_Comparison(list1,operator,number,comp):
    for element in range(len(comp)):
        if operator(len(comp[element]),number) == True:
            list1.append(comp[element])

def Longest(List1):
    longest =""
    for element in range(len(List1)):
        if len(longest) <= len(List1[element]):
               longest = List1[element] 
    if longest =="":
        longest="Nothing"
    return longest

def Avg_list(list1):
    totalchar = 0
    for element in range(len(list1)):
          totalchar += len(list1[element])
    avg= totalchar/len(list1)
    return avg
     

while again =="y":
    print(lformat(end1=" | ", list1=Names, num=15))
    ops = {'>': gt,'<': lt,'>=': ge,'<=': le,'==': eq}
    userop = input("\n""What operator would you like to choose(Ex >,<,>=,<=,==): ")
    number = int(input("\n"f"What number do you want to compare the list against(Ex Items in the list that {userop} Number): "))
    comparison = ops.get(userop)
    List_After_Comparison(ModList,(comparison),number,Names)
    print("\n"+f"Below are all the names that are {userop} {number} characters, there are a total of {totalnames} in the list."+
       "\n"+f"The average name in the above list is {Avg_list(Names)} characters long."   
      "\n"+f"There are {len(ModList)} names {userop} {number} characters. The longest name in the list above is {(Longest(Names))}."+"\n"+
      "\n" f"The longest in the list below is {Longest(ModList)}."+"\n")
    print(lformat(ModList," | ",10)+"\n")
    del ModList[:]
    again = input("Go again(y/n): ")