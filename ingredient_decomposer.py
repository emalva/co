#Practice Exercise: Substring Ingredient Decomposer
#Task Description
#
#You are given:
#ingredients: a list of strings that are basic ingredients.
#recipes: a list of recipe objects, each with "name" and "ingredients" (some may be concatenations like "eggflour").
#
#You must:
#Determine whether each recipe can be formed entirely from available ingredients.
#For each recipe ingredient (like "eggflour"), decompose it into the list of matched ingredients.
#Return only recipes that can be fully formed, with their detailed breakdown.

def solution(ingredients, recipes):
    available = set(ingredients)
    results = []

    # Recursive decomposition using memoization
    def decompose(word, memo={}):
        if word in memo:
            return memo[word]
        if word in available:
            memo[word] = [word]
            return [word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in available:
                rest = decompose(suffix, memo)
                if rest:
                    memo[word] = [prefix] + rest
                    return memo[word]
        memo[word] = None
        return None

    for recipe in recipes:
        matched_map = {}
        all_match = True
        for ing in recipe["ingredients"]:
            parts = decompose(ing)
            if parts:
                matched_map[ing] = parts
            else:
                all_match = False
                break
        if all_match:
            results.append({"name": recipe["name"], "matched": matched_map})

    return results


# Example Test
ingredients = ["egg", "flour", "milk", "sugar"]

recipes = [
    {"name": "Simple Cake", "ingredients": ["eggflour", "milk", "sugar"]},
    {"name": "Omelette", "ingredients": ["eggcheese"]},
    {"name": "Sweet Mix", "ingredients": ["flourmilk", "sugar"]},
    {"name": "Impossible Pie", "ingredients": ["eggbutter"]}
]

print(solution(ingredients, recipes))
