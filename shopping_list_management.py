
# SHOPPING LIST
# A Python program that collects items and prices,
# validates user input, calculates the total using a while loop,
# and prints the list while skipping zero‑priced items.

# Dictionary that will store item names as keys and prices as values
shopping_list = {}

# Asking the user how many items they want to buy
n_items = int(input("How many items do you want to buy? "))

# Collecting item names and prices
for _ in range(n_items):
    item_name = input("Enter the item name: ")

    # Allowing immediate exit if the user types "exit"
    if item_name == "exit":
        break

    # Validating price input using a loop + try/except
    while True:
        item_price = input("Enter the item price: ")
        try:
            item_price = float(item_price)   # Convert to decimal number
            break
        except ValueError:
            print("Invalid input, please try again.")

    # Storing the item in the dictionary
    shopping_list[item_name] = item_price


# CALCULATING TOTAL (USING A WHILE LOOP)

# Extracting only the prices into a list
price_values = list(shopping_list.values())

i = 0          # Index for iteration
total = 0      # Accumulator for the sum / total cost

# Sum of all prices manually using a while loop
while i < len(price_values):
    total = total + price_values[i]
    i += 1


# PRINTING ITEMS (USING A FOR LOOP)
# SKIPPING ITEMS WITH PRICE 0 (USING CONTINUE)

# Converting dictionary items into a list of tuples (name, price)
shopping_items = list(shopping_list.items())

# Printing each item unless its price is zero
for name, price in shopping_items:
    if price == 0:
        continue
    print(name, price)


# PRINTING TOTAL
print(f"The total cost of your shopping is {total}")
