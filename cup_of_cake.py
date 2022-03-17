

def get_recipe_price(prices, optionals=[], **ingredients):
    total = 0

    for i in ingredients.items():
        if i[0] not in optionals:
            total += (float(i[1]) / 100) * prices[i[0]]
    print(total)


if __name__ == '__main__':
    get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300, milk=100)
