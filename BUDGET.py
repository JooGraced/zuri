import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(2000, "initial deposit")
food.withdraw(56.15, "groceries")
food.withdraw(10.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
entertainment = budget.Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

main(module='test_module', exit=False)