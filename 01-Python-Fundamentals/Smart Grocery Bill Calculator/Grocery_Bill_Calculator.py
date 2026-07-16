#create grocery dict
grocery = {
    'sugar':70,
    'basmati rice' : 76,
    'kolam rice' :88,
    'rava' : 45,
    'poha' :48,
    'soyabeen oil' :120,
    'sunflower oil':115,
    'salt':28,
    'moongdal':42,
    'massordal':42,
    'peanuts':90,
    'coconut':110,
    'jeera':120,
    'turmeric':60,
    'chilli powder':70
}
bill = []
print("__________________________________________")
print("               Grocery Bill              ")
print("__________________________________________")
nm = input("\nEnter Customer Name :")
phno = int(input("Enter phone number :"))

# display available item names
print("Availabe items")
for item, price in grocery.items():
    print(item, ":",price)

while True:
    #take user input
    item_nm = input("Enter item name :")
    qua = int(input("Enter quantity :"))

    #Check if they exist
    if item_nm in grocery:
        price = grocery[item_nm]
        total = price*qua
        print("Price = ",price)
        print("Total = ",total)
        
        purchase = {
        "Item" : item_nm,
        "Quantity" :qua,
        "Price" :price,
        "Total" : total
        }
        bill.append(purchase)
        
    else:
        print("item not available")

    
    
    q = input("Do you want to add another item? (yes/no)")
    if q == "no":
        break

#Print final bill
print("\n\n Final Bill")

print("__________________________________________")
print("Name : ",nm)
print("Phone no.:",phno)
print("__________________________________________")

grand_total = 0
for item in bill:
    print(item["Item"],item['Quantity'],item['Price'],item["Total"])
    grand_total += item["Total"]
print("Grand Total = ",grand_total)

print("__________________________________________")

if grand_total >= 1000:
    discount = grand_total *(10/100) 
    print("Discount apply 10%")
    grand_total -= discount

print("Total bill --> ",grand_total)
