# 🛒 Smart Grocery Bill Calculator

A beginner-friendly **Smart Grocery Bill Calculator** built using Python. The application allows users to generate a grocery bill by selecting items from a predefined grocery list, calculating the total amount, and applying discounts based on the final bill.

This project is part of my **Python Roadmap** and was created to practice Python fundamentals.

---

## 📌 Features

- 👤 Accepts customer name and phone number
- 🛍️ Displays available grocery items with prices
- ➕ Add multiple grocery items
- 📦 Enter quantity for each item
- 🧮 Automatically calculates item total
- 🧾 Generates a complete bill
- 💰 Applies a **10% discount** for bills of ₹1000 or more
- 📋 Displays the final payable amount

---

## 🛠️ Technologies Used

- Python 3

---

## 📂 Project Structure

```
Smart Grocery Bill Calculator/
│── grocery_bill.py
│── README.md
```

---

## ▶️ How to Run
Run the program.

```bash
python grocery_bill.py
```

---

## 📋 Available Grocery Items

| Item | Price (₹) |
|------|----------:|
| Sugar | 70 |
| Basmati Rice | 76 |
| Kolam Rice | 88 |
| Rava | 45 |
| Poha | 48 |
| Soyabean Oil | 120 |
| Sunflower Oil | 115 |
| Salt | 28 |
| Moong Dal | 42 |
| Masoor Dal | 42 |
| Peanuts | 90 |
| Coconut | 110 |
| Jeera | 120 |
| Turmeric | 60 |
| Chilli Powder | 70 |

---

## 💻 Sample Output

```text
__________________________________________
               Grocery Bill              
__________________________________________

Enter Customer Name :Akashay Aakash
Enter phone number :35237724724

Available items-
sugar : 70
basmati rice : 76
kolam rice : 88
rava : 45
poha : 48
soyabeen oil : 120
sunflower oil : 115
salt : 28
moongdal : 42
massordal : 42
peanuts : 90
coconut : 110
jeera : 120
turmeric : 60
chilli powder : 70

Enter item name :soys
Enter quantity :7
item not available
Do you want to add another item? (yes/no)yes 

Enter item name :sugar
Enter quantity :6
Price =  70
Total =  420
Do you want to add another item? (yes/no)yes 

Enter item name :coconut
Enter quantity :10
Price =  110
Total =  1100
Do you want to add another item? (yes/no)no


 Final Bill
__________________________________________
Name :  Akashay Aakash
Phone no.: 35237724724
__________________________________________
sugar    6  70  420
coconut 10 110 1100
Grand Total =  1520
__________________________________________
Discount apply 10%
Total bill -->  1368.0
```

---

## 📚 Python Concepts Practiced

- Variables
- Dictionaries
- Lists
- List of Dictionaries
- Loops (`while`, `for`)
- Conditional Statements (`if-else`)
- User Input
- Arithmetic Operations
- Data Storage
- Bill Generation

---

## 🚀 Future Improvements

- ✅ Add GST calculation
- ✅ Generate invoice number automatically
- ✅ Print current date and time
- ✅ Save bill to a text file
- ✅ Search items without case sensitivity
- ✅ Update item prices
- ✅ Add/remove grocery items
- ✅ Generate PDF invoice
- ✅ Build a GUI using Tkinter
- ✅ Store products in a database (SQLite/MySQL)

---

## 🎯 Learning Outcome

This project helped me understand how dictionaries and lists can be combined to build a real-world billing application. It also improved my understanding of loops, conditional statements, data storage, and formatted output in Python.

---

⭐ If you found this project helpful, don't forget to **Star** the repository!
