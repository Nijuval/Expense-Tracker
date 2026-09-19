import balance
from transaction_history import transaction_history , find_each_transactions,find_total_by_category
import data_load
import date_and_time
import write_operation
# import category


if __name__ == "__main__":
    exit = False
    data = data_load.import_data("data.json")
    while not exit:
        user_input = input("Options: \n1. Calculate balance\n2. Transaction history\n3. Total Expenses\n4. date and time\n5. category\n6. each category\n7. total by category \n8.add catergory \n8. exit\n Enter your choice: ")
        if user_input == "1":
            print("""\n--------""")
            print(balance.balance(data))
            print("""--------\n""")
        elif user_input == "2":
            print("""\n--------""")
            print(transaction_history(data))
            print("""--------\n""")
        elif user_input == "3":
            print(balance.total_expenses(data))
        elif user_input == "4":
             date=input("enter your date :")
             print(date_and_time.filter_by_date(data,date))
        elif user_input =="5":
             category=input("enter your category")
             print(category.filterd_by_category(data))
        elif user_input =="6":
            category=input("enter your category : ")
            print(find_each_transactions(data,category))
        elif user_input =="7":
            category=input("enter your category : ")
            print(find_total_by_category(data,category))
        elif user_input =="8":
            category=input("enter your category : ")
            print(write_operation.add_category("data.json",category))
        elif user_input == "9":
            exit = True
        else: 
            print("Invalid input. Please try again.")
    