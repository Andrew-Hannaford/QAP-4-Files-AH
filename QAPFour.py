# One Stop Insurance Company - Policy Program
# November 25, 2023
# Andrew Hannaford

# Imports
from datetime import datetime, timedelta

# Function to validate province input
def validate_province(province):
    valid_provinces = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'YT', 'NU']
    return province.upper() in valid_provinces

# Function to calculate insurance premium
def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car, basic_premium, discount, extra_liability_cost, glass_cost, loaner_car_cost):
    total_extra_costs = num_cars * (extra_liability * extra_liability_cost + glass_coverage * glass_cost + loaner_car * loaner_car_cost)
    total_premium = basic_premium + (num_cars - 1) * (basic_premium * discount) + total_extra_costs
    hst = total_premium * hst_rate
    total_cost = total_premium + hst
    return total_premium, hst, total_cost

# Function to calculate monthly payment
def calculate_monthly_payment(total_cost, down_payment=0):
    monthly_payment = (total_cost - down_payment + processing_fee) / num_payments
    return monthly_payment

# Default values
next_policy_number = 1944
basic_premium = 869.00
discount = 0.25
extra_liability_cost = 130.00
glass_cost = 86.00
loaner_car_cost = 58.00
hst_rate = 0.15
processing_fee = 39.99
num_payments = 8

# Lists to store previous claims
customers = []
claims = []

# Program loop
while True:
    # Customer information input
    first_name = (input("Enter customer's first name: ")).title()
    last_name = (input("Enter customer's last name: ")).title()
    address = input("Enter customer's address: ")
    city = (input("Enter customer's city: ")).title()
    province = input("Enter customer's province (2-letter code): ").upper()
    
    # Validate province input
    while not validate_province(province):
        print("Invalid province. Please enter a valid 2-letter province code.")
        province = input("Enter customer's province (2-letter code): ").upper()
    
    postal_code = input("Enter customer's postal code: ")
    phone_number = input("Enter customer's phone number: ")
    num_cars = int(input("Enter the number of cars being insured: "))
    
    # Options input
    extra_liability = input("Extra liability coverage? (Y/N): ").upper() == 'Y'
    glass_coverage = input("Glass coverage? (Y/N): ").upper() == 'Y'
    loaner_car = input("Loaner car coverage? (Y/N): ").upper() == 'Y'
    
    # Payment method input
    payment_method = input("Payment method (Full/Monthly/Down Pay): ").title()
    
    # Validate payment method input
    while payment_method not in ['Full', 'Monthly', 'Down Pay']:
        print("Invalid payment method. Please enter Full, Monthly, or Down Pay.")
        payment_method = input("Payment method (Full/Monthly/Down Pay): ").title()
    
    # Calculate premium and costs
    total_premium, hst, total_cost = calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car,basic_premium, discount, extra_liability_cost, glass_cost, loaner_car_cost)
    
    if payment_method == 'Down Pay':
        down_payment = float(input("Enter the down payment amount: "))
        monthly_payment = calculate_monthly_payment(total_cost, down_payment)
    else:
        down_payment = 0
        monthly_payment = calculate_monthly_payment(total_cost)
    
    # Calculate invoice date and first payment date
    invoice_date = datetime.now()
    first_payment_date = invoice_date.replace(day=1) + timedelta(days=31)
    
    # Previous claims input
    print("Enter previous claims (Enter blank to finish):")
    claim_number = 1
    while True:
        claim_date_input = input(f"Enter claim {claim_number} date (YYYY-MM-DD): ")
        if not claim_date_input:
            break
        claim_date = datetime.strptime(claim_date_input, '%Y-%m-%d')
        claim_amount = float(input(f"Enter claim {claim_number} amount: "))
        claims.append((claim_date, claim_amount))
        claim_number += 1

    # Display receipt
    print("========================================")
    print("           Insurance Receipt         ")
    print("========================================")
    print(f"Policy Number: {next_policy_number}")
    print(f"Customer: {first_name} {last_name}")
    print(f"Address: {address}, {city}, {province} {postal_code}")
    print(f"Phone Number: {phone_number}")
    print(f"Number of Cars Insured: {num_cars}")
    print(f"Extra Liability Coverage: {'Yes' if extra_liability else 'No'}")
    print(f"Glass Coverage: {'Yes' if glass_coverage else 'No'}")
    print(f"Loaner Car Coverage: {'Yes' if loaner_car else 'No'}")
    print(f"Payment Method: {payment_method}")
    print("----------------------------------------")
    print(f"Total Premium: ${total_premium:,.2f}")
    print(f"HST (15%): ${hst:,.2f}")
    print("----------------------------------------")
    print(f"Total Cost: ${total_cost:,.2f}")
    print(f"Down Payment: ${down_payment:,.2f}")
    print(f"Monthly Payment: ${monthly_payment:,.2f}")
    print("----------------------------------------")
    print(f"Invoice Date: {invoice_date.strftime('%Y-%m-%d')}")
    print(f"First Payment Date: {first_payment_date.strftime('%Y-%m-%d')}")
    print("========================================")
        
    
    # Display previous claims
    print("  Previous Claims:")
    print("  Claim #  Claim Date        Amount")
    print("  ------------------------------------")

    

    for i, claim in enumerate(claims, 1):
        claim_date, amount = claim
        formatted_date = claim_date.strftime('%Y-%m-%d')
        amountDSP = "${:,.2f}".format(amount)
        print(f"  {i}.       {formatted_date}    {amountDSP:>10s}")
    
    
    # Ask if the user wants to enter another customer
    Cont = input("Do you want to enter another customer? (Y/N): ").upper()
    if  Cont == 'N':
        break
