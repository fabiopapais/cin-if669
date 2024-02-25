recipes = {
    'bobo de camarao': ('camarao', 'macaxeira', 'leite de coco', 'dende', 'tomate', 'cebola'),
    'tapioca de carne de sol': ('massa de tapioca', 'carne de sol', 'queijo coalho', 'tomate', 'cebola'),
    'carne de sol com macaxeira': ('carne de sol', 'macaxeira', 'manteiga'),
    'camarao na moranga': ('moranga', 'camarao', 'cebola', 'alho', 'tomate', 'pimentao', 'creme de leite', 'azeite', 'coentro')
}
ingredientsQuantity = {
    'tomate': 5,
    'cebola': 5,
    'coentro': 5,
    'manteiga': 5,
    'macaxeira': 5,
    'alho': 5,
    'pimentao': 5,
    'azeite': 5,
    'camarao': 5,
    'carne de sol': 5,
    'queijo coalho': 5,
    'massa de tapioca': 5,
    'leite de coco': 5,
    'dende': 5,
    'creme de leite': 5,
    'moranga': 5,
}
ingredientsPrices = {
    'tomate': 3.0,
    'cebola': 2.0,
    'coentro': 1.0,
    'manteiga': 5.5,
    'macaxeira': 3.0,
    'alho': 1.5,
    'pimentao': 2.0,
    'azeite': 15.0,
    'camarao': 30.0,
    'carne de sol': 30.0,
    'queijo coalho': 15.0,
    'massa de tapioca': 10.0,
    'leite de coco': 5.0,
    'dende': 15.0,
    'creme de leite': 4.0,
    'moranga': 10.0,
}
originalRecipes = ('bobo de camarao', 'tapioca de carne de sol', 'carne de sol com macaxeira', 'camarao na moranga')
balance = 30.0

def makeRecipe(recipeName):
    recipeProfit = 0
    deduction = 0
    for ingredient in recipes[recipeName]:
        if ingredientsQuantity[ingredient] < 1:
            deduction += buyIngredient(ingredient)
        recipeProfit += ingredientsPrices[ingredient]
        ingredientsQuantity[ingredient] -= 1
    # Checando se a receita foi adicionada durante o programa
    if recipeName not in originalRecipes:
        return (recipeProfit + 5) - deduction
    else:
        return recipeProfit - deduction

def buyIngredient(ingredientName):
    deduction = ingredientsPrices[ingredientName] * 4
    ingredientsQuantity[ingredientName] += 4
    return deduction

def createRecipe(recipeName):
    ingredients = {}
    for i in range(9):
        ingredients[input()] = ''
    recipes[recipeName] = tuple(ingredients.keys())
    return ingredients

soldRecipes = dict((recipe, 0) for recipe in originalRecipes)
notOriginalAskedRecipes = {}
while True:
    try:
        recipe = input()
        if recipe in recipes.keys():
            balance += makeRecipe(recipe)
            soldRecipes[recipe] += 1
            print(f'{recipe} saindo...')
        else:
            if recipe in notOriginalAskedRecipes.keys():
                if notOriginalAskedRecipes[recipe] == 2:
                    print(f'Atendendo demandas, {recipe} é a mais nova adição ao cardápio do Sabores de Recife.')
                    createRecipe(recipe)
                    soldRecipes[recipe] = 0
                else:
                    print(f'{recipe} ainda não é uma opção disponível.')
                    notOriginalAskedRecipes[recipe] += 1    
            else:
                print(f'{recipe} ainda não é uma opção disponível.')
                notOriginalAskedRecipes[recipe] = 1
    except EOFError:
        break

print("##### Fim do expediente #####")
print(f'O lucro obtido no dia de hoje foi de R${balance - 30:.2f}.')

# Pega a receita mais vendida.
mostSoldRecipe = ''
mostSoldValue = -1
for recipe in soldRecipes.keys():
    if soldRecipes[recipe] > mostSoldValue:
        mostSoldValue = soldRecipes[recipe]
        mostSoldRecipe = recipe

if mostSoldRecipe == 'bobo de camarao':
    print("O bom e tradicional Bobó de Camarão, líder em vendas, nunca será superado!")
else:
    print(f"{mostSoldRecipe.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário Bobó de Camarão.")