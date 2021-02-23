from classes import Pizza, Ingredient


if __name__ == '__main__':
    # my_pizza = Pizza('Margherita', ['a', 'b', 'c'])
    # print(my_pizza)
    # print(my_pizza.name)
    # print(my_pizza.ingredients)

    # my_list = [my_pizza]
    # print(str(my_list))  # [Margherita]

    tomato_sauce = Ingredient('Tomato Sauce', 1, 0.5)
    basil = Ingredient('Basil', 1, 0)
    mozzarella = Ingredient('Mozzarella', 5, 1)
    ham = Ingredient('Ham', 7.5, 2)

    pizza_margherita_ingredients = [(tomato_sauce, 1.5), (mozzarella, 2.5), (basil, 4)]
    pizza_margherita = Pizza('Margherita', pizza_margherita_ingredients)
    # for ingredient in pizza_margherita.ingredients:
    #     print(type(ingredient), ingredient.name, ingredient.price, ingredient.quantity)
    print(pizza_margherita.price)
    pizza_margherita.bake()

    print()

    pizza_with_ham_ingredients = [(tomato_sauce, 1), (mozzarella, 2.5), (ham, 3)]
    pizza_with_ham = Pizza('Ham Pizza', pizza_with_ham_ingredients)
    # for ingredient in pizza_with_ham.ingredients:
    #     print(type(ingredient), ingredient.name, ingredient.price, ingredient.quantity)
    print(pizza_with_ham.price)
    pizza_with_ham.bake()

    # Polymorphism
    my_list = [pizza_margherita, pizza_with_ham, Dish()]
    for element in my_list:
        print(len(element))
