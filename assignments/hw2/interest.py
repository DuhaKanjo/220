"""
Name: Duha Kanjo
interest.py

problem: calculate monthly interest charge.

certification of authenticity:
I certify that this assignment is entirely my own work.
"""
# evaluate (the annual interest rate, billing cycle,
# net balance, payment made,and the day of billing)
# compute each step
# the final answer should have only the monthly interest charge.

def main():
    annual_interest_rate = eval(input("enter the annual interest rate"))
    billing_cycle = eval(input("enter the number of days in the billing cycle "))
    the_previous_net_balance = eval(input("enter the previous net balance"))
    the_payment_amount = eval(input("enter the payment amount"))
    the_day_of_billing = eval(input("enter the day in which the payment was made"))
    the_first_step = the_previous_net_balance * billing_cycle
    the_second_step = billing_cycle - the_day_of_billing
    the_third_step = the_payment_amount * the_second_step
    the_fourth_step = the_first_step - the_third_step
    the_fifth_step = the_fourth_step / billing_cycle
    the_monthly_interest_rate = (annual_interest_rate / 12)/100
    the_monthly_interest_charge = the_monthly_interest_rate * the_fifth_step
    final = round(the_monthly_interest_charge, 2)
    print(final)

if __name__=="__main__":
    main()
