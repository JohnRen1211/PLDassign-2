print("Buying some fruits for a healthy body") 
amount_money = int(input("How much money do you have in wallet? "))
price_apple = int(input("How much is an apple? "))
maximum_apples = int(amount_money / price_apple)
remaining_money = float(amount_money - (maximum_apples * price_apple))
print(f"You can buy {maximum_apples} apples and your change is {remaining_money} pesos.") 