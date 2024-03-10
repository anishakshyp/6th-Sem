#2. WAP to calculate simple interest where ROI is fixed at 8.5% using a function:

def calculate_simple_interest(principal, time):
    rate_of_interest = 8.5
    interest = (principal * rate_of_interest * time) / 100
    return interest

principal_amount = 2500
time_period = 3
interest_amount = calculate_simple_interest(principal_amount, time_period)
print(f"Simple Interest: {interest_amount}")