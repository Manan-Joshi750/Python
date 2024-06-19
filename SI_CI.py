# Simple interest and Compound interest.
try:
    principal_amount = float(input("Enter the principal amount: "))
    rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
    time = float(input("Enter the time (in years): "))

    simple_interest = (principal_amount * rate_of_interest * time) / 100
    compound_interest = principal_amount * (1 + rate_of_interest / 100) ** time - principal_amount

    print(f"\nPrincipal Amount: {principal_amount}")
    print(f"Rate of Interest: {rate_of_interest}%")
    print(f"Time: {time} years\n")

    print(f"Simple Interest: {simple_interest}")
    print(f"Compound Interest: {compound_interest}")

except ValueError:
    print("Error: Please enter valid numeric values.")
