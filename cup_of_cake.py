import functools


def get_recipe_price(prices, optionals=[], **ingredients):
    """

    :param prices: dictionary of prices and products
    :param optionals: optional ingredients to canceling
    :param ingredients: to pick up
    :return: total sum of products
    """
    total = 0
    PRICE = 1
    PRODUCT = 0
    for product in ingredients.items():
        if product[0] not in optionals:
            total += (float(product[PRICE]) / 100) * prices[product[PRODUCT]]
    return total


if __name__ == '__main__':
    print(get_recipe_price({}))
