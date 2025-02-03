# This program calculates monthly and yearly net income based on user input

# Input
gross_income = float(input("Enter your monthly gross income: $"))
deductions = float(input("Enter your monthly paycheck deductions: $"))

# Processing
net_monthly_income = gross_income - deductions
yearly_gross_pay = gross_income * 12
yearly_net_pay = net_monthly_income * 12

# Output
print(f"Monthly net income is: ${net_monthly_income:,.2f}")
print(f"Yearly gross pay: ${yearly_gross_pay:,.2f}")
print(f"Yearly net pay: ${yearly_net_pay:,.2f}")