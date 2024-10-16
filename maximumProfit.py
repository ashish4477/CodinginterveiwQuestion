def max_profit(prices):
    if len(prices) < 2:
        return 0  # Need at least two prices to calculate profit

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # Calculate profit if we sell at the current price
        profit = price - min_price
        # Update the max profit if current profit is higher
        max_profit = max(max_profit, profit)
        # Update the min_price to the lowest encountered so far
        min_price = min(min_price, price)

    return max_profit

# Test the function with the given prices
prices = [6, 3, 5, 8, 10, 1, 9]
max_profit_value = max_profit(prices)
max_profit_value
