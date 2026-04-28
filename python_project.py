from tkinter import *
"""This program is a food ordering system."""

class OrderMenu:
    """Main GUI."""
    def __init__(self, parent):
        """Main GUI Framework"""
        #Frame 1: Start Menu
        self.frame1 = Frame(parent)
        self.ordering_menu_lb = Label(self.frame1, text = "Menu")
        self.ordering_menu_lb.grid(row = 0, column = 4)

        self.order_btn = Button(self.frame1, text = "Order ")
        self.order_btn.grid(row = 4, column = 2 )
        
        self.history_btn = Button(self.frame1, text = "History")
        self.history_btn.grid(row = 4, column = 6 )

        #Frame 2: Order History
        self.frame2 = Frame(parent)
        
        past_order_name = StringVar()
        past_order_name.set("NA")
        self.past_order_name_lb = Label(self.frame2, textvar = past_order_name)
        self.past_order_name_lb.grid(row = 0, column = 4)

        past_order_content = StringVar()  #Figure out how to store the order content
        past_order_content.set("NC")
        self.past_order_content_lb = Label(self.frame2, textvar = past_order_content)
        self.past_order_content_lb.grid(row = 2, column = 4)

        past_order_cost = StringVar() 
        past_order_cost.set("NA")
        self.past_order_cost_lb = Label(self.frame2, textvar = past_order_cost)
        self.past_order_cost_lb.grid(row = 4, column = 4)

        self.prev_btn = Button(self.frame2, text = "Previous")
        self.prev_btn.grid(row = 6, column = 2)

        self.next_btn = Button(self.frame2, text = "Next")
        self.next_btn.grid(row = 6, column = 6 )
        
        
        #Frame 3: Order enter first frame:
        self.frame3 = Frame(parent)
        
        self.input_order_name_lb = Label(self.frame3, text = "Order Name: ")
        self.input_order_name_lb .grid(row = 0, column = 0)

        self.input_order_name_en = Entry(self.frame3)
        self.input_order_name_en .grid(row = 0, column = 2)

        self.input_order_amount_lb = Label(self.frame3, text = "Amount of items: ")
        self.input_order_amount_lb.grid(row = 2, column = 0)

        self.input_order_name_en = Entry(self.frame3)
        self.input_order_name_en.grid(row = 2, column = 2)

        self.confirm_btn_1 = Button(self.frame3, text = "Confirm")
        self.confirm_btn_1.grid(row = 4, column = 0)

        #Frame 4: Order enter second frame:
        self.frame4 = Frame(parent)

        self.test_list = ["Burger", "Pizza", "Carrot"]
        option = StringVar()
        option.set(self.test_list [0])
    
        self.item_drop_down = OptionMenu(self.frame4, option, *self.test_list)
        self.item_drop_down.grid(row = 0, column = 0)

        self.confirm_btn_2 = Button(self.frame4, text = "Confirm")
        self.confirm_btn_2.grid(row = 4, column = 0)
        

        #Frame 5: : Receipt
        self.frame5 = Frame(parent)

        order_name = StringVar()
        order_name.set("FNA")
        self.order_name_lb = Label(self.frame5, textvar = order_name)
        self.order_name_lb.grid(row = 0, column = 4)

        order_content = StringVar()  #Figure out how to store the order content
        order_content.set("FNC")
        self.order_content_lb = Label(self.frame5, textvar = order_content)
        self.order_content_lb.grid(row = 2, column = 4)

        order_cost = StringVar()  #Figure out how to store the order content
        order_cost.set("FNA")
        self.order_cost_lb = Label(self.frame5, textvar = order_cost)
        self.order_cost_lb.grid(row = 4, column = 4)

        self.order_btn_2 = Button(self.frame5, text = "New Order")
        self.order_btn_2.grid(row = 6, column = 6 )


        self.frame5.grid()


if __name__=="__main__":
    root = Tk()
    order_menu = OrderMenu(root)
    root.mainloop()