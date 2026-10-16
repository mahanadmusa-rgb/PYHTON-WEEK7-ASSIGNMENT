shopping_list = []

while True:
    print("\n--- Shopping List Manager ---")
    print("add / remove / show / done")
    choice = input("Choose an action: ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(item, "has been added.")
        else:
            print("Please enter a valid item.")


    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")
    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Invalid choice. Please type add, remove, show, or done.")
