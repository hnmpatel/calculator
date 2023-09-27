import math


def calculate_emi(principal_amount, interest_rate, tenure_of_loan):
    """Calculates the EMI for a given principal amount, interest rate and tenure of loan.

    Args:
        principal_amount: The principal amount of the loan.
        interest_rate: The interest rate of the loan.
        tenure_of_loan: The tenure of the loan in months.

    Returns:
        The EMI for the given loan.
    """

    # Calculate the number of EMI payments.
    emi_count = tenure_of_loan * 12

    mir = interest_rate / 1200

    # Calculate the EMI.
    emi = (
        principal_amount * mir * math.pow(1 + mir, emi_count)
    ) / (math.pow(1 + mir, emi_count) - 1)
    return emi
