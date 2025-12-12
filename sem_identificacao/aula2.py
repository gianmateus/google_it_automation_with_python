import os
import csv

def create_file(filename):
    with open(filename, "w") as file:
        file.write("product,price,quantity\n")
        file.write("cell phone,699.99,10\n")
        file.write("laptop,999.99,5\n")
        file.write("tablet,399.99,7\n")
        file.write("smartwatch,199.99,15\n")
        file.write("headphones,149.99,20\n")


def contents_of_file(filename):
    return_string = ""

    create_file(filename)

    with open(filename) as file:
        reader = csv.DictReader(file)

        for row in reader:
            return_string += "a {} costs ${} and we have {} in stock\n".format(row["product"], row["price"], row["quantity"])
    return return_string


print(contents_of_file("products.csv"))