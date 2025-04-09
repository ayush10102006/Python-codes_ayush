grocery_prices = {
    'Rice': 50,
    'Sugar': 40,
    'Milk': 25,
    'Eggs': 5,
    'Bread': 30
}
grocery_quantity = {
    'Rice': 2,   
    'Sugar': 1,  
    'Milk': 3,  
    'Eggs': 12, 
    'Bread': 1   
}
total_bill = 0
for item in grocery_prices:
    if item in grocery_quantity:
        total_bill += grocery_prices[item] * grocery_quantity[item]
print("Total Grocery Bill: ₹", total_bill)
