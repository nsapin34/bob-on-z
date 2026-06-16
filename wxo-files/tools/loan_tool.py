from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool()
def monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    """
    Calculate the fixed monthly payment for a loan using mortgage-style amortization.
    
    This function computes the monthly payment amount for a loan with a fixed interest
    rate and term, using the standard amortization formula with monthly compounding.
    
    Args:
        principal: Total loan amount in currency units (must be positive).
        annual_rate: Annual interest rate as a percentage (e.g., 4.5 for 4.5%).
                    Must be non-negative.
        years: Loan duration in years (must be positive integer).
    
    Returns:
        The fixed monthly payment amount, rounded to 2 decimal places.
    
    Raises:
        ValueError: If principal is negative or zero, years is non-positive,
                   or annual_rate is negative.
    
    Examples:
        >>> monthly_payment(200000, 4.5, 30)
        1013.37
        >>> monthly_payment(100000, 0, 10)
        833.33
    """
    # Validate inputs
    if principal <= 0:
        raise ValueError(f"Principal must be positive, got {principal}")
    
    if years <= 0:
        raise ValueError(f"Years must be positive, got {years}")
    
    if annual_rate < 0:
        raise ValueError(f"Annual rate must be non-negative, got {annual_rate}")
    
    # Handle zero interest rate case
    if annual_rate == 0:
        # Simple division: total amount / number of months
        monthly_pmt = principal / (years * 12)
        return round(monthly_pmt, 2)
    
    # Convert annual rate from percentage to decimal and calculate monthly rate
    monthly_rate = (annual_rate / 100) / 12
    
    # Calculate total number of payments
    num_payments = years * 12
    
    # Apply standard amortization formula:
    # M = P * [r(1+r)^n] / [(1+r)^n - 1]
    # where:
    #   M = monthly payment
    #   P = principal
    #   r = monthly interest rate
    #   n = number of payments
    
    numerator = monthly_rate * ((1 + monthly_rate) ** num_payments)
    denominator = ((1 + monthly_rate) ** num_payments) - 1
    
    monthly_pmt = principal * (numerator / denominator)
    
    return round(monthly_pmt, 2)

# Made with Bob
