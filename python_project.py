"""This is a food ordering system. This program is used to input a customers order for the program to calculate the orders total cost. It is also used to store the detail of all previously entered orders."""

from tkinter import *
from tkinter import messagebox


class Order:
    """Class that is used to create order objects."""

    def __init__(self, orderer_name, order_amount, order_content, order_cost):
        """Each order object will have the orderer's name, the amount of items ordered, the order's content and the order's cost."""
        self.orderer_name = orderer_name
        self.order_amount = order_amount
        self.order_content = order_content
        self.order_cost = order_cost


class Food:
    """Class that is used to create food objects."""

    def __init__(self, name, cost):
        """Each food object will have a name and cost."""
        self.name = name
        self.cost = cost  # In NZD


class OrderMenu:
    """Class responsible for the main GUI."""

    def __init__(self, parent):
        """Create the GUI with 5 different frames."""
        # Creates list that stores the food objects and list that stores the order ojects
        self.food_list = [Food("Burger", 10), Food("Pizza", 18), Food("Donut", 3), Food("Ice Cream", 4), Food("7 Layer Cake", 170)]
        self.order_list = []

        # Frame 1: Start Menu / Order Menu
        self.frame_1 = Frame(parent)
        self.ordering_menu_lb = Label(self.frame_1, text="Menu")
        self.ordering_menu_lb.grid(row=0, column=4)

        self.description_lb = Label(self.frame_1, text="This is a food ordering system.\n Only a maximum of 5 total items can be ordered in one order.\n Currently 5 differnt food items are available")
        self.description_lb.grid(row=2, column=4, sticky=N)

        self.order_btn = Button(self.frame_1, text="Order", command=lambda: self.switch_frames(1, 3))
        self.order_btn.grid(row=4, column=2)

        self.history_btn = Button(self.frame_1, text="History", command=self.history_setup)
        self.history_btn.grid(row=4, column=6)
        self.history_btn.configure(state="disabled")

        # Frame 2: Order History
        self.frame_2 = Frame(parent)

        self.order_menu_btn_1 = Button(self.frame_2, text="Order Menu", command=lambda: self.switch_frames(2, 1))
        self.order_menu_btn_1.grid(row=0, column=6)

        # Creates a StringVar called orderer_name which stores the orderer_name that needs to be shown on screen
        self.orderer_name_var = StringVar()
        self.orderer_name_var.set(None)

        self.past_orderer_name_tx_lb = Label(self.frame_2, text="Orderer's name")
        self.past_orderer_name_tx_lb.grid(row=2, column=0)

        self.past_orderer_name_lb = Label(self.frame_2, textvar=self.orderer_name_var)
        self.past_orderer_name_lb.grid(row=2, column=4)

        # Creates a StringVar called content_message_var which stores a formated verison of the order_content that needs to be shown on screen
        self.content_message_var = StringVar()
        self.content_message_var.set(None)

        self.past_content_tx_lb = Label(self.frame_2, text="Orderer's content")
        self.past_content_tx_lb.grid(row=4, column=0)

        self.past_content_message = Message(self.frame_2, textvar=self.content_message_var, width=150)
        self.past_content_message .grid(row=4, column=4, columnspan=2)

        # Creates a StringVar called order_cost_var which stores the order_cost that needs to be shown on screen
        self.order_cost_var = StringVar()
        self.order_cost_var.set(None)

        self.past_order_cost_tx_lb = Label(self.frame_2, text="Total order cost (in NZD)")
        self.past_order_cost_tx_lb.grid(row=6, column=0)

        self.past_order_cost_lb = Label(self.frame_2, textvar=self.order_cost_var)
        self.past_order_cost_lb.grid(row=6, column=4)

        self.prev_btn = Button(self.frame_2, text="Previous", command=self.prev)
        self.prev_btn.grid(row=8, column=2)

        self.next_btn = Button(self.frame_2, text="Next", command=self.next)
        self.next_btn.grid(row=8, column=6)

        # Frame 3: Order enter first frame
        self.frame_3 = Frame(parent)

        self.input_orderer_name_lb = Label(self.frame_3, text="Orderer Name: ")
        self.input_orderer_name_lb .grid(row=0, column=0)

        self.input_orderer_name_en = Entry(self.frame_3)
        self.input_orderer_name_en .grid(row=0, column=2)

        self.input_order_amount_lb = Label(self.frame_3, text="Amount of items: ")
        self.input_order_amount_lb.grid(row=2, column=0)

        self.input_order_amount_en = Entry(self.frame_3)
        self.input_order_amount_en.grid(row=2, column=2)

        self.confirm_btn_1 = Button(self.frame_3, text="Confirm", command=self.confirm_1)
        self.confirm_btn_1.grid(row=4, column=0)

        # Frame 4: Order enter second frame
        self.frame_4 = Frame(parent)

        self.food_name_list = []

        # Goes through all the food objects in the food lists and adds their names to the food_name_list
        for food in self.food_list:
            self.food_name_list.append(food.name)

        self.option = StringVar()
        self.option.set(self.food_name_list[0])

        self.amount_num = IntVar()
        self.amount_num.set(1)

        self.amount_num_tx_lb = Label(self.frame_4, text="Amount of items left to confirm")
        self.amount_num_tx_lb.grid(row=0, column=0)

        self.amount_num_lb = Label(self.frame_4, textvar=self.amount_num)
        self.amount_num_lb.grid(row=0, column=2)

        self.item_drop_down = OptionMenu(self.frame_4, self.option, *self.food_name_list)
        self.item_drop_down.grid(row=2, column=2)

        self.confirm_btn_2 = Button(self.frame_4, text="Confirm",  command=self.confirm_2)
        self.confirm_btn_2.grid(row=4, column=2)

        # Frame 5: Order result frame
        self.frame_5 = Frame(parent)

        self.orderer_name_tx_lb = Label(self.frame_5, text="Orderer's name")
        self.orderer_name_tx_lb.grid(row=0, column=0)

        self.orderer_name_lb = Label(self.frame_5, textvar=self.orderer_name_var)
        self.orderer_name_lb.grid(row=0, column=4)

        self.content_message_tx_lb = Label(self.frame_5, text="Orderer's content")
        self.content_message_tx_lb.grid(row=2, column=0)

        self.content_message = Message(self.frame_5, textvar=self.content_message_var, width=150)
        self.content_message.grid(row=2, column=4, columnspan=2)

        self.order_cost_tx_lb = Label(self.frame_5, text="Total order cost (in NZD)")
        self.order_cost_tx_lb.grid(row=4, column=0)

        self.order_cost_lb = Label(self.frame_5, textvar=self.order_cost_var)
        self.order_cost_lb.grid(row=4, column=4)

        self.order_menu_btn_2 = Button(self.frame_5, text="Order Menu", command=lambda: self.switch_frames(5, 1))
        self.order_menu_btn_2.grid(row=6, column=6)

        # Set Up Code
        self.frame_list = [self.frame_1, self.frame_2, self.frame_3, self.frame_4, self.frame_5]
        self.frame_1.grid()

    def switch_frames(self, start_frame, end_frame):
        """When method is run it would switch to the frame given by the start_frame argument and leave behind the frame given by the end frame argument."""
        for frame in self.frame_list:
            if start_frame == (self.frame_list.index(frame) + 1):
                frame.grid_forget()
            elif end_frame == (self.frame_list.index(frame) + 1):
                frame.grid()

    def confirm_1(self):
        """Check if what the user in frame 3 entered is valid and will contniue onto frame 4 if so."""
        self.input_orderer_name_en.focus()
        try:
            # Checks if valid input is entered
            if len(self.input_orderer_name_en.get()) == 0:  # Check for if nothing is entered into the orderer name entry
                messagebox.showerror("ErroR", "Must input name")
                self.input_orderer_name_en.focus()
            elif len(self.input_order_amount_en.get()) == 0:  # Check for if nothing is entered into the order amount entry
                messagebox.showerror("ErroR", "Must input amount of items")
                self.input_order_amount_en.focus()
            elif int(self.input_order_amount_en.get()) <= 0:  # Check for if amount entered is not a positive interger (is a negative number or is zero)
                messagebox.showerror("ErroR", "Amount must be a positive integer")
                self.input_order_amount_en.delete(0, END)
                self.input_order_amount_en.focus()
            elif int(self.input_order_amount_en.get()) > 5:  # Check for if amount is greater than 5
                messagebox.showerror("ErroR", "Amount must be less than or equal to 5")
                self.input_order_amount_en.delete(0, END)
                self.input_order_amount_en.focus()
            else:
                # Creates the order object with orderer_name and order_amount = to what the user has inputted while order_content and order_cost are set to None
                order = Order(self.input_orderer_name_en.get(), self.input_order_amount_en.get(), None, None)
                self.order_list.append(order)
                self.switch_frames(3, 4)
                self.amount_num.set(self.order_list[-1].order_amount)
                # Clears what is currently inside both entry widgets
                self.input_orderer_name_en.delete(0, END)
                self.input_order_amount_en.delete(0, END)
                self.content_list = []
        except ValueError:
            messagebox.showerror("ErroR", "Write an integer not a string")  # Check if what the user had type is not an integer
            self.input_order_amount_en.delete(0, END)
            self.input_order_amount_en.focus()

    def confirm_2(self):
        """Will add confirmed items from option menu into order list and will set up the order infomation page."""
        # Goes through the food object list and if the objects name matches what is currently selected in the OptionMenu will add that object into the content_list
        for food in self.food_list:
            if food.name == self.option.get():
                self.content_list.append(food)
        self.amount_num.set(self.amount_num.get()-1)
        # When the final item has been chosen sets the order_content of the latest order object to be the content_list
        if self.amount_num.get() < 1:
            self.order_list[-1].order_content = self.content_list
            self.cost_calc()
            self.final_result(-1)
            self.option.set(self.food_name_list[0])
            self.switch_frames(4, 5)

    def cost_calc(self):
        """Calculate the total cost of the order by summing each foods cost and sets the latest order oject's order_cost to be the calculated cost."""
        self.total_cost = 0
        for food in self.order_list[-1].order_content:
            self.total_cost += food.cost
        self.order_list[-1].order_cost = self.total_cost
        self.total_cost = 0

    def final_result(self, index):
        """Use the index argument to prepare the presentation of the order objects information."""
        # Sets orderer_name_var and order_cost_var (which are both StringVar) to orderer_name and order_cost of the current order object dependent of the index argument
        self.orderer_name_var.set(self.order_list[index].orderer_name)
        self.order_cost_var.set(self.order_list[index].order_cost)
        self.formating = ""
        self.order_num = 1
        self.name_order_content_list = []
        self.final_content_list = []
        # Adds the name of each food object from order_list[index].order_content (which is a list of food objects) to the name_order_content_list
        for order_content in self.order_list[index].order_content:
            self.name_order_content_list.append(order_content.name)
        # Checks if there are multiple of the same food in name_order_content_list and if so adds string with food name and
        # the amount of the food into the final list. After this it removes the remaing same duplicates of the food name from the list
        # Else just adds a string with food name and amount of the food (which is always 1) into the final list.
        for food in self.name_order_content_list:
            self.food_count = self.name_order_content_list.count(food)
            if self.food_count > 1:
                self.final_content_list.append(f"{food} x {self.food_count}")
                while self.food_count > 1:
                    # Removes the last food item in the list as .remove(food) only removes the first occurence
                    # Due to the while loop it will remove every duplicate of food except the first one
                    self.name_order_content_list.reverse()
                    self.name_order_content_list.remove(food)
                    self.name_order_content_list.reverse()
                    self.food_count = self.name_order_content_list.count(food)
            else:
                self.final_content_list.append(f"{food} x {1}")

        # Formats the final contents by creating a string with each of the food from the final_content_list seperated by a new line(by using the \n)
        for order in self.final_content_list:
            self.formating += order
            if self.order_num < len(self.final_content_list):
                self.formating += "\n"
            self.order_num += 1
        self.content_message_var.set(self.formating)
        self.history_btn.configure(state="active")

    def history_setup(self):
        """Set up the history frame by showing the info for the first order on the list and sets up the buttons acordingly."""
        self.final_result(0)
        self.switch_frames(1, 2)
        self.history_page_num = 1
        self.prev_btn.configure(state="disabled")  # Since the history button always shows the first order recorded, prev btn should be disabled
        # Checks if only 1 order has been made and if so disables the next button
        if len(self.order_list) == 1:
            self.next_btn.configure(state="disabled")
        else:
            self.next_btn.configure(state="active")

    def next(self):
        """Show the information of the next order on the list and activates/disables the  next and prev buttons acordingly."""
        self.history_page_num += 1
        # Checks the page number we are on is = to the amount of orders, meaning are we on the last page and if so will disable the next button
        if self.history_page_num == len(self.order_list):
            self.next_btn.configure(state="disabled")
        self.prev_btn.configure(state="active")
        self.final_result(self.history_page_num-1)

    def prev(self):
        """Show the information of the next order on the list and activates/disables the next and prev buttons acordingly."""
        self.history_page_num -= 1
        # Checks if we are on the first page an if so the prev button will be disabled
        if self.history_page_num == 1:
            self.prev_btn.configure(state="disabled")
        self.next_btn.configure(state="active")
        self.final_result(self.history_page_num-1)


if __name__ == "__main__":
    root = Tk()
    order_menu = OrderMenu(root)
    root.mainloop()
