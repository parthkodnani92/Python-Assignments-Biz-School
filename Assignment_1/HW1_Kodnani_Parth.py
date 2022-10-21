# Name: Parth Kodnani
# Course: BUDT704
# Section: 0502
# Date: 09/09/2021

principal_amount = float(input("Enter Principal Amount: $")) 
fee_percentage = float(input("Enter Fee Percentage: ")) 
rate_of_interest = float(input("Enter Rate of Interest: ")) 
no_of_years = float(input("Enter Number of Years: ")) 
withdrawal_charge = 74 

rate_of_interest = rate_of_interest/100
fee = (fee_percentage * principal_amount)/100
present_v = principal_amount - fee # Value of Principal Amount after deduction of Fee
compound_interest = present_v*((1+rate_of_interest)**no_of_years) 

future_v = compound_interest

withdrawal = no_of_years*74 # Withdrawal Amount after 'n' years

future_vw = (compound_interest) - (withdrawal) # Amount received after deducting Withdrawal Amount

g_amount = future_vw - principal_amount # Growth Amount
g_percentage = g_amount/100 # Growth Percentage

print(f'Present Value of Investment: ${present_v:.2f}')
print(f'Future Value of Investment, before the withdrawal fee is applied:: ${future_v:.2f}')
print(f'Withdrawal Fee of Investment: ${withdrawal:.2f}')
print(f'Future Value of Investment, after the withdrawal fee is applied:: ${future_vw:.2f}')
print(f'Growth amount: ${g_amount:.2f}')
print(f'Growth percentage: {g_percentage:.1f}%')


# "I pledge on my honor that I have not given nor received any unauthorized
# assistance on this assignment."
# --Parth Kodnani 
