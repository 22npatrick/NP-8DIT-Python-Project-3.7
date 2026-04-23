from tkinter import *
"""This program is a food ordering system."""

class OrderMenu:
    """Main GUI."""
    def __init__(self, parent):
        """Main GUI Framework"""
        self.ordering_menu_lb = Label(parent, text = "MENU")
        self.ordering_menu_lb.grid()


if __name__=="__main__":
    root = Tk()
    order_menu = OrderMenu(root)
    root.mainloop()