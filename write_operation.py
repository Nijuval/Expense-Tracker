import data_load
def add_category(path,category):
    data= data_load.import_data(path)
    data["categories"].append(category)
    data_load.write_data(data,path)