class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        cost_total = self.item_price * self.item_quantity
        print(self.item_name + " " + str(self.item_quantity) +
              " @ $" + str(self.item_price) + " = $" + str(cost_total))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found_flag = False
        index = 0
        while index < len(self.cart_items):
            current = self.cart_items[index]

            if current.item_name == item_name:
                self.cart_items.pop(index)
                found_flag = True
                break

            index += 1

        if found_flag == False:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        match_found = False

        for cart_item in self.cart_items:
            if cart_item.item_name == item_to_modify.item_name:
                match_found = True

                if item_to_modify.item_quantity != 0:
                    cart_item.item_quantity = item_to_modify.item_quantity

                if item_to_modify.item_price != 0:
                    cart_item.item_price = item_to_modify.item_price

                if item_to_modify.item_description != "none":
                    cart_item.item_description = item_to_modify.item_description

                break

        if match_found == False:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_qty = 0
        i = 0

        while i < len(self.cart_items):
            total_qty += self.cart_items[i].item_quantity
            i += 1

        return total_qty

    def get_cost_of_cart(self):
        cart_total = 0

        for cart_item in self.cart_items:
            item_total = cart_item.item_price * cart_item.item_quantity
            cart_total += item_total

        return cart_total

    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Number of Items:", self.get_num_items_in_cart())

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for entry in self.cart_items:
                entry.print_item_cost()

        total_amount = self.get_cost_of_cart()
        print("Total: $" + str(total_amount))

    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Item Descriptions")

        for entry in self.cart_items:
            print(entry.item_name + ": " + entry.item_description)


def print_menu(cart):
    user_choice = ""

    while user_choice != 'q':
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        user_choice = input("Choose an option:\n")

        if user_choice == 'a':
            item_obj = ItemToPurchase()

            name_input = input("Enter the item name:\n")
            item_obj.item_name = name_input

            desc_input = input("Enter the item description:\n")
            item_obj.item_description = desc_input

            price_input = float(input("Enter the item price:\n"))
            item_obj.item_price = price_input

            qty_input = int(input("Enter the item quantity:\n"))
            item_obj.item_quantity = qty_input

            cart.add_item(item_obj)

        elif user_choice == 'r':
            remove_name = input("Enter name of item to remove:\n")
            cart.remove_item(remove_name)

        elif user_choice == 'c':
            updated_item = ItemToPurchase()

            name_input = input("Enter the item name:\n")
            updated_item.item_name = name_input

            new_qty = int(input("Enter the new quantity:\n"))
            updated_item.item_quantity = new_qty

            cart.modify_item(updated_item)

        elif user_choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif user_choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif user_choice == 'q':
            break

        else:
            print("Invalid option. Try again.")


def main():
    cust_name = input("Enter customer's name:\n")
    today_date = input("Enter today's date:\n")

    print("\nCustomer name:", cust_name)
    print("Today's date:", today_date)

    cart_obj = ShoppingCart(cust_name, today_date)

    print_menu(cart_obj)

if __name__ == "__main__":
    main()
