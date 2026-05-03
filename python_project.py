"""This program is a food ordering system."""
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

class Order:
    """Class that holds the order objects"""

    def __init__(self, orderer_name, order_amount, order_content, order_cost):
        """Each order object will have the orderer's name, order's cost and the """

        self.orderer_name = orderer_name
        self.order_amount = order_amount
        self.order_content = order_content
        self.order_cost = order_cost

class Food:
    """Class that holds the food objects."""

    def __init__(self, name, cost):
        """Each food object will have a name and cost"""

        self.name = name
        self.cost = cost #In NZD

class OrderMenu:
    """Main GUI."""

    def __init__(self, parent):
        """Main GUI Framework."""

        #Start Code
        self.food_list = [Food("Burger", 10), Food("Pizza", 18), Food("Donut", 3), Food("Ice Cream", 4), Food("7 Layer Cake", 170)]
        self.order_list = []

        #Frame 1: Start Menu
        self.frame1 = Frame(parent)
        self.ordering_menu_lb = Label(self.frame1, text = "Menu")
        self.ordering_menu_lb.grid(row = 0, column = 4)

        self.order_btn = Button(self.frame1, text = "Order", command=lambda: self.switch_frames(1, 3))
        self.order_btn.grid(row = 4, column = 2 )
        
        self.history_btn = Button(self.frame1, text = "History", command = self.history_setup)
        self.history_btn.grid(row = 4, column = 6 )

        #Frame 2: Order History
        self.frame2 = Frame(parent)

        self.order_menu_btn_1 = Button(self.frame2, text = "Order Menu", command=lambda: self.switch_frames(2, 1))
        self.order_menu_btn_1.grid(row = 0, column = 6 )

        self.orderer_name = StringVar()
        self.orderer_name.set("FNA")

        self.past_orderer_name_lb = Label(self.frame2, textvar = self.orderer_name)
        self.past_orderer_name_lb.grid(row = 2, column = 4)

        self.content_message_var = StringVar()
        self.content_message_var.set("Empty")
        
        self.past_content_message = Message(self.frame2, textvar = self.content_message_var)
        self.past_content_message .grid(row = 3, column = 4, columnspan = 2)

        self.order_cost = StringVar()  #Figure out how to store the order content
        self.order_cost.set("FNA")

        self.past_order_cost_lb = Label(self.frame2, textvar =  self.order_cost)
        self.past_order_cost_lb.grid(row = 6, column = 4)

        self.prev_btn = Button(self.frame2, text = "Previous", command = self.prev)
        self.prev_btn.grid(row = 8, column = 2)

        self.next_btn = Button(self.frame2, text = "Next", command = self.next)
        self.next_btn.grid(row = 8, column = 6 )
        
        #Frame 3: Order enter first frame:
        self.frame3 = Frame(parent)
        
        self.input_orderer_name_lb = Label(self.frame3, text = "Orderer Name: ")
        self.input_orderer_name_lb .grid(row = 0, column = 0)

        self.input_orderer_name_en = Entry(self.frame3)
        self.input_orderer_name_en .grid(row = 0, column = 2)

        self.input_order_amount_lb = Label(self.frame3, text = "Amount of items: ")
        self.input_order_amount_lb.grid(row = 2, column = 0)

        self.input_order_amount_en = Entry(self.frame3)
        self.input_order_amount_en.grid(row = 2, column = 2)

        self.confirm_btn_1 = Button(self.frame3, text = "Confirm", command = self.confirm_1)
        self.confirm_btn_1.grid(row = 4, column = 0)

        #Frame 4: Order enter second frame:
        self.frame4 = Frame(parent)

        self.food_name_list = []

        for food in self.food_list:
            self.food_name_list.append(food.name)

        self.option = StringVar()
        self.option.set(self.food_name_list[0])

        self.item_number = IntVar()
        self.item_number.set(1)

        self.item_number_tx_lb = Label(self.frame4, text = "Amount of items left to confirm")
        self.item_number_tx_lb.grid(row = 0, column = 0)

        self.item_number_lb = Label(self.frame4, textvar = self.item_number)
        self.item_number_lb.grid(row = 0, column = 2)

        self.item_drop_down = OptionMenu(self.frame4, self.option, *self.food_name_list)
        self.item_drop_down.grid(row = 2, column = 2)

        self.confirm_btn_2 = Button(self.frame4, text = "Confirm",  command = self.confirm_2)
        self.confirm_btn_2.grid(row = 4, column = 2)

        #Frame 5: : Receipt
        self.frame5 = Frame(parent)

        self.orderer_name_lb = Label(self.frame5, textvar = self.orderer_name)
        self.orderer_name_lb.grid(row = 0, column = 4)

        print(self.content_message_var.get())
        self.content_message = Message(self.frame5, textvar = self.content_message_var)
        self.content_message.grid(row = 3, column = 4, columnspan = 2)

        self.order_cost_lb = Label(self.frame5, textvar = self.order_cost)
        self.order_cost_lb.grid(row = 4, column = 4)

        self.order_menu_btn_2 = Button(self.frame5, text = "Order Menu", command=lambda: self.switch_frames(5, 1))
        self.order_menu_btn_2.grid(row = 6, column = 6)

        #Set Up Code
        self.frame_list = [self.frame1, self.frame2, self.frame3, self.frame4, self.frame5]
        self.frame5.grid()

    def switch_frames(self, start_frame, end_frame):
        """When method is run it would switch to the frame given by the argument 
        and remove the previous frame."""

        for frame in self.frame_list:
            if start_frame == (self.frame_list.index(frame) + 1):
                frame.grid_forget()
            elif end_frame == (self.frame_list.index(frame) + 1):
                frame.grid()


    def test(self, index):
        #Remove this function later
        print(self.order_list[index].orderer_name)
        print(self.order_list[index].order_amount)
        if self.order_list[index].order_content == None:
           print(self.order_list[index].order_content)
        else:
            for food in self.order_list[index].order_content:
                print(food.name)
        print(self.order_list[index].order_cost)
        

    def confirm_1(self):
        """Checks if what the user in frame 3 entered is valid and contniues onto """
        self.input_order_amount_en.focus()
        try:
            if len(self.input_orderer_name_en.get()) == 0:
                messagebox.showerror("ErroR", "Must input name")
                self.input_orderer_name_en.focus()
            elif len(self.input_order_amount_en.get()) == 0:
                messagebox.showerror("ErroR", "Must input amount of items")
                self.input_order_amount_en.focus()
            elif int(self.input_order_amount_en.get()) <= 0:
                messagebox.showerror("ErroR", "Amount must be a positive interger")
                self.input_order_amount_en.delete(0, END)
                self.input_order_amount_en.focus()
            elif int(self.input_order_amount_en.get()) > 5:
                messagebox.showerror("ErroR", "Amount must be less than or equal to 5")
                self.input_order_amount_en.delete(0, END)
                self.input_order_amount_en.focus()
            else:
                order = Order(self.input_orderer_name_en.get(), self.input_order_amount_en.get(), None, None)
                print(order.orderer_name)
                print(order.order_amount)
                print(order.order_cost)
                print(order.order_content)
                self.order_list.append(order)
                self.test(-1) #Delete later
                self.switch_frames(3, 4)
                self.item_number.set(self.order_list[-1].order_amount)
                self.content_list = []
        except:
             messagebox.showerror("ErroR", "Amount must be a positive interger")
             self.input_order_amount_en.delete(0, END)
             self.input_order_amount_en.focus()
    
    def confirm_2(self):
        """Allows the user to add the amount of items they wanted"""
        print(self.item_number.get())
        for food in self.food_list:
            if food.name == self.option.get():
                print(f"{food.name}")
                self.content_list.append(food)
        self.item_number.set(self.item_number.get()-1) 
        if self.item_number.get() < 1:
            self.order_list[-1].order_content = self.content_list
            print("")
            self.test(-1) #Delete later
            self.cost_calc()
            self.final_result(-1)
            self.switch_frames(4, 5)

    def cost_calc(self):
        self.total_cost = 0
        for food in self.order_list[-1].order_content:
            print(food.name)
            self.total_cost += food.cost
        self.order_list[-1].order_cost = self.total_cost
        self.total_cost = 0
        self.test(-1)
    
    def final_result(self, index):
        self.orderer_name.set(self.order_list[index].orderer_name)
        self.order_cost.set(self.order_list[index].order_cost)
        formating = ""
        order_num = 1
        for order in self.order_list[index].order_content:
            formating += order.name
            if order_num < len(self.order_list[index].order_content):
                formating += "\n"
            order_num += 1
        self.content_message_var.set(formating)

    def history_setup(self):
        self.prev_btn.configure(state = "disabled")
        self.final_result(0)
        self.switch_frames(1, 2)
        self.history_page_num = 1
        if len(self.order_list) == 1:
            self.next_btn.configure(state = "disabled")
        else:
            self.next_btn.configure(state = "active") 
        

    def next(self):
        self.history_page_num += 1
        if self.history_page_num == len(self.order_list):
            self.next_btn.configure(state = "disabled")
        else:
            self.next_btn.configure(state = "active") 
        self.prev_btn.configure(state = "active") 
        self.final_result(self.history_page_num-1)


    def prev(self):
        self.history_page_num -= 1
        if self.history_page_num == 1:
            self.prev_btn.configure(state = "disabled")
        else:
            self.prev_btn.configure(state = "active") 
        self.next_btn.configure(state = "active") 
        self.final_result(self.history_page_num-1)

        
if __name__=="__main__":
    root = Tk()
    order_menu = OrderMenu(root)
    root.mainloop()