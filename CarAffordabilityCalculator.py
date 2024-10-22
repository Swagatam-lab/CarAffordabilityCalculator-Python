import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate_payment():
    try:
        car_name = car_name_entry.get()
        car_price = float(price_entry.get())
        monthly_salary = float(salary_entry.get())

        down_payment = down_slider.get()
        loan_tenure_years = tenure_slider.get()
        emi_percentage = emi_slider.get()
        annual_interest_rate = interest_slider.get()

        loan_amount = car_price - down_payment
        monthly_interest_rate = (annual_interest_rate / 100) / 12
        total_payments = loan_tenure_years * 12

        if monthly_interest_rate == 0:
            monthly_emi = loan_amount / total_payments
        else:
            monthly_emi = loan_amount * (
                monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments
            ) / ((1 + monthly_interest_rate) ** total_payments - 1)

        required_monthly_salary = monthly_emi / (emi_percentage / 100)

        result_label.config(
            text=f"Loan Amount: ₹{loan_amount:.2f}\n"
                 f"Monthly EMI: ₹{monthly_emi:.2f}\n"
                 f"Required Monthly Salary: ₹{required_monthly_salary:.2f}"
        )

        if monthly_salary >= required_monthly_salary:
            afford_label.config(text=f"Congratulations! You can afford the {car_name}.")
        else:
            afford_label.config(text=f"You can't afford the {car_name}.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

def update_slider_value(label, value):
    """Updates the label next to the slider with the current value."""
    label.config(text=f"{int(float(value))}")

def create_slider_with_value(row, label_text, from_, to_, command):
    """Creates a slider with a label to show the current value dynamically."""
    # Heading Label
    label = tk.Label(root, text=label_text, bg='#f0f0f0')
    label.grid(row=row, column=0, columnspan=2, sticky='w', padx=10, pady=5)

    # Current Value Label
    value_label = tk.Label(root, text="0", bg='#f0f0f0')
    value_label.grid(row=row + 1, column=1, sticky='e', padx=10)

    # Slider Below Heading
    slider = ttk.Scale(root, from_=from_, to=to_, orient='horizontal',
                       command=lambda value: update_slider_value(value_label, value))
    slider.grid(row=row + 2, column=0, columnspan=2, sticky='ew', padx=10, pady=5)
    
    return slider

# GUI Window Setup
root = tk.Tk()
root.title("Car Affordability Calculator")
root.configure(bg='#f0f0f0')

# Configure grid layout
root.grid_columnconfigure(1, weight=1)

# Car Name Input
tk.Label(root, text="Car Name:", bg='#f0f0f0').grid(row=0, column=0, sticky='w', padx=10, pady=5)
car_name_entry = tk.Entry(root)
car_name_entry.grid(row=0, column=1, sticky='ew', padx=10, pady=5)

# Car Price Input
tk.Label(root, text="Car Price:", bg='#f0f0f0').grid(row=1, column=0, sticky='w', padx=10, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1, sticky='ew', padx=10, pady=5)

# Monthly Salary Input
tk.Label(root, text="Your Monthly Salary:", bg='#f0f0f0').grid(row=2, column=0, sticky='w', padx=10, pady=5)
salary_entry = tk.Entry(root)
salary_entry.grid(row=2, column=1, sticky='ew', padx=10, pady=5)

# Down Payment Slider with Value Display
down_slider = create_slider_with_value(3, "Down Payment (₹):", 0, 500000, None)

# Loan Tenure Slider with Value Display
tenure_slider = create_slider_with_value(6, "Loan Tenure (Years):", 0, 30, None)

# EMI Percentage Slider with Value Display
emi_slider = create_slider_with_value(9, "EMI as % of Salary:", 0, 100, None)

# Interest Rate Slider with Value Display
interest_slider = create_slider_with_value(12, "Interest Rate (%):", 0, 20, None)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_payment)
calculate_button.grid(row=15, column=0, columnspan=2, pady=10)

# Result Labels
result_label = tk.Label(root, text="", bg='#f0f0f0')
result_label.grid(row=16, column=0, columnspan=2, padx=10, pady=5)

afford_label = tk.Label(root, text="", bg='#f0f0f0')
afford_label.grid(row=17, column=0, columnspan=2, padx=10, pady=5)

# Start the Application
root.mainloop()
