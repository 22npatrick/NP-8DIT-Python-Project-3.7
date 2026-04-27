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

        past_order_cost = StringVar()  #Figure out how to store the order content
        past_order_cost.set("NA")
        self.past_order_cost_lb = Label(self.frame2, textvar = past_order_content)
        self.past_order_cost_lb.grid(row = 4, column = 4)

        self.next_btn = Button(self.frame2, text = "Next")
        self.next_btn.grid(row = 6, column = 2 )
    
        self.prev_btn = Button(self.frame2, text = "Previous")
        self.prev_btn.grid(row = 6, column = 6)
        
        self.frame2.grid()


        


if __name__=="__main__":
    root = Tk()
    order_menu = OrderMenu(root)
    root.mainloop()