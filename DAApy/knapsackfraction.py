# Take custom inputs
arr = []
n = int(input("Enter the number of items: "))

# Input each item's price and weight
for i in range(n):
    item_price = float(input(f"Enter the price of item {i + 1}: "))
    item_weight = float(input(f"Enter the weight of item {i + 1}: "))
    arr.append([item_price, item_weight])

# Input the knapsack weight
w = float(input("Enter the maximum weight the knapsack can hold: "))

# Sort items by price-to-weight ratio in descending order
arr = sorted(arr, key=lambda x: x[0] / x[1], reverse=True)

# Calculate the maximum price
price = 0
for item in arr:
    itemWt = item[1]
    itemP = item[0]
    if itemWt > w:
        price += w * (itemP / itemWt)  # Add fractional part of the item
        break
    else:
        price += itemP  # Add the whole item price
        w -= itemWt

print(f"The maximum price obtainable in the knapsack is: {price}")
