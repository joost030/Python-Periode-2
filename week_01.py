print("Welcome to the Fantasy Item Shop!")
player_name = input("What is your name? ")
player_gold = 100
inventory = []

print(f"\nHello {player_name}! You have {player_gold} gold.")

shop_items = ["Sword", "Shield", "Potion", "Bow"]
item_prices = [50, 40, 20, 60]

print("\nItems for sale:")
for item in shop_items:
    print(f"- {item}")

shop_open = True

while shop_open:
    print("\n=== Fantasy Item Shop ===\n")
    for number in range(len(shop_items)):
        print(f"{number + 1}. Buy {shop_items[number]} ({item_prices[number]} gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    choice = input("\nWhat would you like to do? ")

    match choice:
        case "1" | "2" | "3" | "4":
            item_index = int(choice) - 1
            item_name = shop_items[item_index]
            item_price = item_prices[item_index]

            if player_gold >= item_price:
                player_gold -= item_price
                inventory.append(item_name)
                print(f"\nYou bought a {item_name}!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")

        case "5":
            if len(inventory) == 0:
                print("\nYour inventory is empty!")
            else:
                print("\nYour inventory:")
                for item in inventory:
                    print(f"- {item}")

        case "6":
            print(f"\nThanks for visiting, {player_name}!")
            print(f"You have {player_gold} gold left.")
            shop_open = False

        case _:
            print("\nInvalid choice! Please choose a number from 1 to 6.")
