import ttkbootstrap as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from ttkbootstrap.tooltip import ToolTip

class RestaurantBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Billing System")
        self.root.geometry("500x500") 
        # Initialize variables
        self.total_amount = 0
        self.items = []
        self.tip_percentage = tk.DoubleVar(value=10.0)  # Default tip percentage

        # Create widgets
        self.label_item = tk.Label(root, bootstyle=("success"),text="Enter Item:")
        self.entry_item = tk.Entry(root)
        self.label_price = tk.Label(root, bootstyle=("success"),text="Enter Price:")
        self.entry_price = tk.Entry(root)
        self.add_button = tk.Button(root, bootstyle=("outline,success"),text="Add Item", command=self.add_item)
        self.calculate_button = tk.Button(root,bootstyle=("outline,success"), text="Calculate Total", command=self.calculate_total)
        self.display_button = tk.Button(root, bootstyle=("outline,success"),text="Display Bill", command=self.display_bill)

        # Tip calculator widgets
        self.label_tip = tk.Label(root, bootstyle=("success"),text="Tip Percentage:")
        self.entry_tip = tk.Entry(root, textvariable=self.tip_percentage)
        self.tip_button = tk.Button(root, bootstyle=("outline,success"),text="Calculate Tip", command=self.calculate_tip)

        # Place widgets on the screen
        self.label_item.pack()
        self.entry_item.pack()
        self.label_price.pack()
        self.entry_price.pack()
        self.add_button.pack(padx=10, pady=5)
        self.calculate_button.pack(padx=10, pady=5)
        self.display_button.pack(padx=10, pady=5)
        self.image_label = tk.Label(root)
        self.load_image("C:\\Users\\chris kent\\Desktop\\python tutorials\\gui development\\github projects\\rest.jpeg")

        # Tip calculator widgets placement
        self.label_tip.pack()
        self.entry_tip.pack()
        self.tip_button.pack(padx=10, pady=5)
        self.image_label.pack()

    def add_item(self):
        item = self.entry_item.get()
        price = self.entry_price.get()

        if item and price:
            try:
                price = float(price)
                self.items.append((item, price))
                self.entry_item.delete(0, tk.END)
                self.entry_price.delete(0, tk.END)
                messagebox.showinfo("Success", f"{item} added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid price. Please enter a valid number.")
        else:
            messagebox.showerror("Error", "Please enter both item and price.")

    def calculate_total(self):
        self.total_amount = sum(price for _, price in self.items)
        messagebox.showinfo("Total Amount", f"Total Amount: ${self.total_amount:.2f}")

    def calculate_tip(self):
        tip_percentage = self.tip_percentage.get()
        tip_amount = self.total_amount * (tip_percentage / 100)
        total_with_tip = self.total_amount + tip_amount
        messagebox.showinfo("Tip Calculation", f"Tip Amount: ${tip_amount:.2f}\nTotal with Tip: ${total_with_tip:.2f}")

    def display_bill(self):
        if self.items:
            bill_text = "\n".join(f"{item}: ${price:.2f}" for item, price in self.items)
            bill_text += f"\nTotal Amount: ${self.total_amount:.2f}"
            messagebox.showinfo("Bill", bill_text)
        else:
            messagebox.showwarning("Warning", "No items added yet!")

    
    def load_image(self, image_path):
        try:
            image = Image.open(image_path)
            image = image.resize((200, 100))  # Resize the image
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")
       
if __name__ == "__main__":
    root = tk.Window(themename="solar")
    app = RestaurantBillingApp(root)    
    root.mainloop()
