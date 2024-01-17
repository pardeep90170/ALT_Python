from data import MENU as m
from data import resources as r
from data import profit as p

class Report:
    def __init__(self,m,r,p):
        self.menu = m
        self.resource = r
        self.profit = p

class Order(Report):
    
    def __init__(self,data):
        Report.__init__(self,m,r,p)
        self. data = data
        
    def resouces(self):
        
         if self.menu[data]["ingredients"]["water"] < self.resource["water"] and self.menu[data]["ingredients"]["milk"] < self.resource["milk"] and self.menu[data]["ingredients"]["coffee"] < self.resource["coffee"]:
            print("Insert Money")
              
         else:
            if self.menu[data]["ingredients"]["water"] > self.resource["water"]:
             
                print(f"Sorry there is not enough water!!!")
              
            elif self.menu[data]["ingredients"]["milk"] > self.resource["milk"] :
                print(f"Sorry there is not enough milk!!!")
             
            elif self.menu[data]["ingredients"]["coffee"] > self.resource["coffee"]:
                print(f"Sorry there is not enough coffee!!!")
    
class Money(Order):
    def __init__(self,money):
        Order.__init__(self,data)
        self.money = money
        
    def transaction_succesfully(self):
        if self.menu[data]["cost"] == self.money:
            print(f"****Enjoy of your {self.data} coffee***")
        else:
            if self.menu[data]["cost"] > self.money:
                c = self.menu[data]["cost"] - self.money
                
                print(f"not enough money:{c}??")
            else:
                
                count = self.money - self.menu[data]["cost"]
                print(f"Total change----{count}")
                list = [1,2,5,10,20,50,100,200,500]
                i =0
                print(f"Here's your change: ")
                while i < len(list):
                    if list[i] <= count:
                        pass
                    else:
                        i -=1
                        count -= list[i]
                        print(list[i])
                        i = 0 
                    if count ==0:
                        break
                    i +=1
            print("-"*40)   
            print("****Enjoy of your coffee****")
            print("-"*40)  

   
#  startup this code order and report and exit
while True:
    
    print("""***** Self service coffee machine ****
             Press 1.. for order
             Press 2.. for Report
             Press3.. for Exit...""")
    choice=int(input("Enter your choice (1-3):"))
    if choice == 1:
        print("""What would you like ? 
              ***Latte.. Price..169***
              ***Espresso.. Price..149***
              ***Cappuccino.. Price..170***""")
        data1 = input("Enter your order:")
        data=data1.lower()
        obj = Order(data)
        if data == "latte" or data == "espresso" or data == "cappuccino" :
            obj.resouces()
            money = int(input("Enter the amount:"))
            obj2 = Money(money)
            obj2.transaction_succesfully()
        else:
            print("Wrong Order...?")
        
        
    elif choice == 2:
        print(r)
        
    elif choice == 3:
        exit()
        
    else:
        print("<<<<<....Wrong choice input......>>>>>")