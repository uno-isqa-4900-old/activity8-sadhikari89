# defining Customer as class
class Customer:

# defining the functions with customer attributes inside
    def __init__(self, cust_id=0, first_name="",last_name="",company_name="",address="",city="",state="",zip=""):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

# importing CSV file that stores data
import csv

file_name = "customers.csv"

# defining get_customers function that returns list of Customer objects
def get_customers(self):
    customers = []
    with open(file_name, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            customers.append(customer)
    return customers

def display_title():
    print("Customer Viewer Application")
    print()


def viewer():
    customers = get_customers(Customer)
    # get input from customer
    customerid = int(input("Enter customer ID:  "))
    print()

    # creating loops until they enter a valid customer ID
    if customerid >=101 and customerid <= 600:
        customer = customers[customerid-100]
        print(customer.first_name +" "+ customer.last_name)
        if customer.company_name == "":
            pass
        else:
            print(customer.company_name)
        print(customer.address)
        print(customer.city + ", " + customer.state, customer.zip)
        print()
    else:
        print("No customer with that specified ID.")
        print()


def main2():
    # know whether users wants to continue or leave
    choice = input("Continue (y/n): ")
    if choice == "y":
        print()
        viewer()
        main2()
    elif choice == "n":
        print("Bye!")
    else:
        print("Invalid input. Enter either y or n")
        main2()


def main1():
    display_title()
    viewer()
    main2()
# calling the main function
if __name__ == "__main__":
    main1()

