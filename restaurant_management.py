total=0.00
def will_tip(fTotal):
    valueS=input("Do you want to give a tip? y/n :")
    if(valueS=="y"):
        valueP=input("Enter the percentage of the total amount for tip: ")
        valueP=float(valueP)
        valueP=1+(valueP/100)
        fTotal=valueP*fTotal
        print("Your total bill amount is=")
        print(fTotal)
        print("Thank You for placing your order")
        input()
    else:
        print("Your Total bill amount is=")
        print(fTotal)
        print("Thank You for placing your order")
        input()
        
class menu_item:  
    def __init__(self, sl_no,name, price):
        self.sl_no = sl_no  
        self.name = name
        self.price=price
menu_items_list = []  
menu_items_list.append( menu_item(1,'Veg Thali', 60.00) ) 
menu_items_list.append( menu_item(2,'Chicken Thali', 100.00) ) 
menu_items_list.append( menu_item(3,'Fish Thali', 120.00) ) 
menu_items_list.append( menu_item(4,'Roti Sabji', 30.0) ) 

for obj in menu_items_list: 
    print( obj.sl_no, obj.name,obj.price, sep =' ' )
print("\n")
print("Welcome to Ghar ka Khana Restaurant")    
print("Please select the item from above menu")

value = input("Please enter the item no : ")
value = int(value)

for obj in menu_items_list: 
    if(obj.sl_no==value):
        total=total+obj.price
        print("Your cart value is:")
        print(total)
        print("\n")

while True:
    x=input("Do you want anything else? y/n :")
    if x=="y":
        for obj in menu_items_list: 
            print( obj.sl_no, obj.name,obj.price, sep =' ' ) 
        value = input("Please enter item no : ")
        value = int(value)
        for obj in menu_items_list: 
           if(obj.sl_no==value):
                total=total+obj.price
                print("Your cart value is:")
                print(total)
                print("\n")
        continue
        will_tip(total)
        
    elif x =="n":
        will_tip(total)
        break
