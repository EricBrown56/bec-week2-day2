# Write a function that lets the user add items to a list, make sure you ask the user what they would like to add to the list and then add it to the list. Include a feature to remove items from the list. If the user would like to add another item to the list, call the function again. If the user would not like to add another item to the list, print a goodbye message.

def shopping_list_maker():
    shopping_list = []
    while True:
        item = input('What would you like to add to your shopping list? ')
        shopping_list.append(item)
        print(f'Great! You have added {item} to your shopping list!')
        add_another = input('Would you like to add another item to your shopping list? (yes/no) ')
        if add_another == 'no':
            break
        else:
            continue
    last_call = input('Before we print out your shopping list, would you like to remove any items? (yes/no) ')
    if last_call == 'yes':
                while True:
                    remove_item = input('What item would you like to remove? ')
                    shopping_list.remove(remove_item)
                    print(f'You have removed {remove_item} from your shopping list.')
                    remove_another = input('Would you like to remove another item? (yes/no) ')
                    if remove_another == 'no':
                        print('Thank you for creating your shopping list! Here is what you have added: ')
                        for item in shopping_list:
                            print(item)
                        break   
                    else:
                        continue
    else:
        print('Thank you for creating your shopping list! Here is what you have added: ')
        for item in shopping_list:
            print(item)
    print('\nHave a great day! And thank you for using the shopping list maker!')
        

print("Welcome to the shopping list maker!\n In just a few steps, you will have your shopping list ready to go!\n Let's get started!")

shopping_list_maker()