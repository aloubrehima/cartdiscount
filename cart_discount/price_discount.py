def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):

    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.

    if no discount will be taken, return 0

    what is appropriate if function is called with
    """
    if len(item_prices) >= 3:
        cheapest_item = min(item_prices)
        return cheapest_item
    else:
        return 0  # No discount if there are three or fewer discount

if __name__ == '__main__':
    main()