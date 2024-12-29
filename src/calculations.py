def calculate_annuity(payment, rate, periods, continuous=False):
    if continuous:
        return payment * ((1 - (1 + rate) ** -periods) / rate)
    else:
        return payment * ((1 - (1 + rate) ** -periods) / rate)

def calculate_mortgage(loan_amount, monthly_rate, total_months):
    return loan_amount * (monthly_rate * (1 + monthly_rate) ** total_months) / ((1 + monthly_rate) ** total_months - 1)

def estimate_retirement_balance(monthly_deposit, initial_capital, rate, months):
    balance = initial_capital
    for _ in range(months):
        balance = balance * (1 + rate) + monthly_deposit
    return balance

def time_to_double(rate):
    return 70 / rate

def solve_logarithmic(base, x):
    import math
    return math.log(x, base)

def to_scientific_notation(number):
    return "{:.2e}".format(number)

def from_scientific_notation(sci_str):
    return float(sci_str)

def main():
    while True:
        print("Financial Calculator")
        print("1. Calculate Annuity")
        print("2. Calculate Mortgage")
        print("3. Estimate Retirement Balance")
        print("4. Time to Double")
        print("5. Solve Logarithmic Equation")
        print("6. Convert to Scientific Notation")
        print("7. Convert from Scientific Notation")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            payment = float(input("Enter payment: "))
            rate = float(input("Enter rate: "))
            periods = int(input("Enter periods: "))
            continuous = input("Continuous growth? (y/n): ").lower() == 'y'
            print("Annuity:", calculate_annuity(payment, rate, periods, continuous))
        
        elif choice == '2':
            loan_amount = float(input("Enter loan amount: "))
            monthly_rate = float(input("Enter monthly rate: "))
            total_months = int(input("Enter total months: "))
            print("Monthly Mortgage Payment:", calculate_mortgage(loan_amount, monthly_rate, total_months))
        
        elif choice == '3':
            monthly_deposit = float(input("Enter monthly deposit: "))
            initial_capital = float(input("Enter initial capital: "))
            rate = float(input("Enter rate: "))
            months = int(input("Enter months: "))
            print("Estimated Retirement Balance:", estimate_retirement_balance(monthly_deposit, initial_capital, rate, months))
        
        elif choice == '4':
            rate = float(input("Enter rate: "))
            print("Time to Double:", time_to_double(rate))
        
        elif choice == '5':
            base = float(input("Enter base: "))
            x = float(input("Enter x: "))
            print("Logarithmic Solution:", solve_logarithmic(base, x))
        
        elif choice == '6':
            number = float(input("Enter number: "))
            print("Scientific Notation:", to_scientific_notation(number))
        
        elif choice == '7':
            sci_str = input("Enter scientific notation: ")
            print("Converted Number:", from_scientific_notation(sci_str))
        
        elif choice == '8':
            break
        
        else:
            print("Invalid choice. Please try again.")