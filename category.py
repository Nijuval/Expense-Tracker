# def filterd_by_category(data,category: dict) -> list[dict[str, any]]:

#     """
#         This function takes a data dictionary as input and returns the filterd_by_category
#         The transaction history is a list of dictionaries containing the details of each transaction.
        
#         Parameters:
#         data (dict): A dictionary containing income and expenses.
        
#         Returns:
#         List[dict]: A list of dictionaries containing the filterd_by_category
#     """
#     for expense in data["expenses"]:
#         if expense["catergory"]==category:
#             total += expense["amount"]
#     return total