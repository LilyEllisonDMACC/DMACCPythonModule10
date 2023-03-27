"""
Program: employee.py
Author: Lily Ellison
Last date modified: 03/27/2023

The purpose of this program is to create an employee class and display the information added to the instance of that employee.

"""


'''Employee Class'''
import datetime


class Employee:
    # Constructor
    def __init__(self, lname: str, fname: str, addr: str, phone_num: str, sal_tf: bool, start_d: datetime,
                 sal_amt: float):
        self.last_name = lname
        self.first_name = fname
        self.address = addr
        self.phone_number = phone_num
        self.salaried = sal_tf
        self.start_date = start_d
        self.salary = "{:,.2f}".format(sal_amt)
        #formatted salary int to include commas and add 2 decimal places

    def display(self):
        emp_info = self.__str__()
        return emp_info

    def get_salary_str(self):
        if self.salaried:
            salaried_str = "Salaried employee: $" + str(self.salary) + "/year"
        else:
            salaried_str = "Hourly employee: $" + str(self.salary) + "/hour"
        return salaried_str

    def __str__(self):

        return str(self.first_name + " " + self.last_name + "\n" + self.address + "\n" + self.get_salary_str() + "\nStart date: " + str(
            self.start_date))

    def __repr__(self):

        return "Employee(\"" +self.first_name + "\", \"" + self.last_name + "\", \"" + self.address + "\", " + str(self.salaried) + ", " + str(datetime.datetime(2019, 6, 28)) +", \"" + str(self.salary) + "\")"

# Driver
if __name__ =="__main__":
    date_info = datetime.datetime(2019, 6, 28)
    emp = Employee('Patel', 'Sasha', '123 Main Street \nUrban, Iowa', "", True, date_info,
               40000)  # call the construtor, needs to have a first and last name in parameter

    print(emp.display())  # display returns a str, so print the information

    del emp

    print("\n-OR-\n")

    emp = Employee('Patel', 'Sasha', '123 Main Street \nUrban, Iowa', "", False, date_info,
               7.25)  # call the construtor, needs to have a first and last name in parameter

    print(emp.display())  # display returns a str, so print the information

    print("\nrepr: " + repr(emp))

    del emp
