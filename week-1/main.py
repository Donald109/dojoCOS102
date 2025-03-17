def simple_interest(principal, rate, time):
    """Calculate Simple Interest"""
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time, n=1):
    """Calculate Compound Interest"""
    amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    return amount - principal


def annuity_plan(payment, rate, time):
    """Calculate Annuity Plan Future Value"""
    rate = rate / 100
    return payment * (((1 + rate) ** time - 1) / rate)


if __name__ == "__main__":
    # User input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time period (in years): "))

    # Calculate Simple Interest
    si = simple_interest(principal, rate, time)
    print(f"Simple Interest: {si:.2f}")

    # Calculate Compound Interest (compounded annually by default)
    n = int(input("Enter number of times interest applied per year (default is 1): ") or 1)
    ci = compound_interest(principal, rate, time, n)
    print(f"Compound Interest: {ci:.2f}")

    # Calculate Annuity Plan Future Value
    annuity_payment = float(input("Enter the annuity payment per period: "))
    annuity_time = int(input("Enter the number of periods: "))
    annuity_value = annuity_plan(annuity_payment, rate, annuity_time)
    print(f"Annuity Future Value: {annuity_value:.2f}")
