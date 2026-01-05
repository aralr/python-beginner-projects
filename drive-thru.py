def welcome():
    print("""
🍔 Welcome to Hamburguesas Doña Chuy 🍔
Please choose an item number:

1. 🍔 Cheeseburger
2. 🍟 Fries
3. 🥤 Soda
4. 🍦 Ice Cream
5. 🍪 Cookie
""")
 

def get_item(choice):
    menu = {
        1: '🍔 Cheeseburger',
        2: '🍟 Fries',
        3: '🥤 Soda',
        4: '🍦 Ice Cream',
        5: '🍪 Cookie'
    }

    return menu.get(choice, '❌ Invalid item')

welcome()

choice = int(input('What would you like to order? (1–5): '))
item = get_item(choice)

print(f'You ordered: {item}. Enjoy your {item}')
