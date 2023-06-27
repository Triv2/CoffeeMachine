money=0
def main(money):
  MENU = {
      "espresso": {
          "ingredients": {
              "water": 50,
              "coffee": 18,
          },
          "cost": 1.5,
      },
      "latte": {
          "ingredients": {
              "water": 200,
              "milk": 150,
              "coffee": 24,
          },
          "cost": 2.5,
      },
      "cappuccino": {
          "ingredients": {
              "water": 250,
              "milk": 100,
              "coffee": 24,
          },
          "cost": 3.0,
      }
  }

  #initial resources
  resources = {
      "water": 300,
      "milk": 200,
      "coffee": 100,
  }



  change=0

  #money values
  VALUE={
    "dollar":1,
    "quarter":0.25,
    "dime":0.1,
    "nickel":0.05,
    "penny":0.01
  }



  coffee_type= input("What type of coffee would you like? 'espresso', 'cappuccino' or 'latte': ").lower()
  
  
  if coffee_type == "report":
    print(f"{resources['water']}ml \n{resources['milk']}ml \n{resources['coffee']}g")
    print(f"Money: ${money:.2f}")
  elif coffee_type == "espresso" or coffee_type == "cappuccino" or coffee_type == "latte":
    # print("Please insert coins.")
    cost= MENU[coffee_type]["cost"]
    quarters=int(input("How many quarters? "))
    dimes=int(input("How many dimes? "))
    nickles=int(input("How many nickels? "))
    pennies=int(input("How many pennies? "))
    money_inserted=quarters*VALUE["quarter"] + dimes*VALUE["dime"] + nickles*VALUE["nickel"] + pennies*VALUE["penny"]
    if money_inserted >= cost:
      resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
      resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
      resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
      change += money_inserted - cost
      print(f"You inserted: ${money_inserted:.2f}.")
      print(f"The cost of a latte is: ${cost:.2f}.")
      print(f"Your change is: ${change:.2f}.")
      print(f"Here is your {coffee_type}")
    else:
      print("You don't have enough money.")
  else:
    print("Please insert a valid coffee type.")
  main(money)

main(money)   