import time
#Per litre price
Milk_price=50
print(type(Milk_price))
curd_price=30
# Capacity in liters
Max_Vol=100
# volume_qty=[0.5,1,5]
# Milk_Price_list=[25,50,250]
# Curd_Price_list= [15,30,150]

Master_dit ={"price": [[25,50,250],[15,30,150]]}
print(Master_dit["price"][0])


# Nicely formatted time string
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)

###To calculate payment###
def payment(pay,total):
    while pay < total:
        pay = float(input("Please enter an amount more than payment: "))
    change = pay - total
    print("Your change will be Rs", change)
    print('Thank you, next please')
    
###To check max Capacity###
def check_max_Vol(entry):
    while entry> Max_Vol:
        entry= float(input("Maximum allowed per user is 10L, please enter a value less than 10: "))
    else:
        pass
        return entry

# Function to calculate cost
def cost_calculation(price_list,price):
    cus_choice=input("Would you have any choice on packets. Available packets are for 0.5L, 1L,5L. plase enter yes/no: " )
    cost=0
    if cus_choice=='yes':
        selection = input((("Qty of 0.5L pack: "), ("Qty of 1L pack: "), ("Qty of 5L pack: ")))
        for i in range(0,len(price_list)):
            price=int(selection[i])*int(price_list[i])
            cost=cost+price
    else:
        qty = int(input("Kindly enter the quantity in liters: "))
        Lit = check_max_Vol(qty)
        cost = Lit*price
    print("Kindly enter Rupees "+str(cost)+" below" )
    cus_paid=int(input("Kindly enter the amount to be paid: "))
    payment(cus_paid,cost)



###MAIN CODE###
print ("Welcome to the Python Vending Machine.") 

try:   
    while True:
        start = time.time()
        time.sleep(2)
        # Asking User on type of product.
        item = input("Would you like to buy Milk,Curd:  " )
        item=item.lower()
        if item == 'milk':
            c=0
            cost_calculation(Master_dit["price"][c],Milk_price)
        elif item == 'curd': 
            c=1
            cost_calculation(Master_dit["price"][c],curd_price)
        else:
            print("Sorry, Looks like you made a mistake in entry")
        elapsed = time.time()-start
        print (f'user time: {hms_string(elapsed)}')
                 
except KeyboardInterrupt:
    print("User Input to stop programme")
    pass       