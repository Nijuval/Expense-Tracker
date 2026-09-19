def filter_by_date(data,date: dict) ->list[dict[str, any]]:

    """
        This function takes a data dictionary as input and returns the filter_by_date
        The transaction history is a list of dictionaries containing the details of each transaction.
        
        Parameters:
        data (dict): A dictionary containing income and expenses.
        
        Returns:
        List[dict]: A list of dictionaries containing the filter_by_date
    """
    total=0
    for expense in data["expenses"]:
        if expense["date"]==date:
            total += expense["amount"]
    return total