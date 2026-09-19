def transaction_history(data: dict) -> list[dict[str, any]]:
    """
        This function takes a data dictionary as input and returns the transaction history.
        The transaction history is a list of dictionaries containing the details of each transaction.
        
        Parameters:
        data (dict): A dictionary containing income and expenses.
        
        Returns:
        List[dict]: A list of dictionaries containing the transaction history.
    """

    transaction_histories = []
    for expense in data["expenses"]:
        transaction = {
            "desctiption": expense["description"],
            "amount": expense["amount"],
        }
        transaction_histories.append(transaction)
    return transaction_histories


def find_each_transactions(data: dict,category: str,) ->int:
    """
        This function takes a data dictionary as input and returns the number of transactions in each category.
        The transaction is a list of dictionaries containing the details of each transaction.
        
        Parameters:
        data (dict): A dictionary containing income and expenses.
        category(str):A str containing category
        Returns:
        int: A number denoting number of transactions in a given category.
    """
    total=0
    for expense in data["expenses"]:
        if expense["category"]==category:
            total+=1
    
    return total


def find_total_by_category(data: dict,category:str)->int:
        """
        This function takes a data dictionary as input and returns the number of transactions in each category.
        The transaction is a list of dictionaries containing the details of each transaction.
        
        Parameters:
        data (dict): A dictionary containing income and expenses.
        category(str):A str containing category
        Returns:
        int: A number denoting number of transactions in a given category.
    """
        total=0
        for expense in data["expenses"]:
             if expense["category"]==category:
                total+=expense["amount"]
        return total



def find_most_expensive_caterory(data:dict)->int:
    """
        This function takes a data dictionary as input and returns the number of transactions in each category.
        The transaction is a list of dictionaries containing the details of each transaction.
        
        Parameters:
        data (dict): A dictionary containing income and expenses.
        category(str):A str containing category
        Returns:
        int: A number denoting number of transactions in a given category.
    """
    initiziling={}
    for expense in data["expenses"]:
        find_total_by_category
        
    return total