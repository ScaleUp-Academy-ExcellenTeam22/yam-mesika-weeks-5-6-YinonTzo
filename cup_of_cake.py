def get_recipe_price(prices: dict, optionals: list = None, **ingredients: int) -> float:
    """
    :param prices: Dictionary of prices and products.
    :param optionals: Optional list ingredients to canceling.
    :param ingredients: To pick up.
    :return: Total sum of products.
    """
    if optionals is None:
        optionals = []

    total = 0
    for product, amount in ingredients.items():
        if product not in optionals:
            total += ((float(amount) / 100) * prices[product])
    return total


if __name__ == '__main__':
    print(get_recipe_price({}))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
