# Author: Luis Mercado
# Date: 11/09/2024
# Description: Creates "Employee" class containing private variables for employee info
#              and a function that adds instances of Employee class to a dictionary


# define Employee class
class Employee:
    """
    Represents an employee with key identifying information
    """

    def __init__(self, name: str, ID_number: str, salary: int, email_address: str):
        """
        Creates an employee object with name, ID number, salary, and email address)
        """
        self._name: str = name
        self._ID_number: str = ID_number
        self._salary: int = salary
        self._email_address: str = email_address

    def get_name(self) -> str:
        """
        Returns employee name
        """
        return self._name
    
    def get_ID_number(self) -> str:
        """
        Returns employee ID number
        """
        return self._ID_number
    
    def get_salary(self) -> int:
        """
        Returns employee salary
        """
        return self._salary
    
    def get_email_address(self) -> str:
        """
        Returns employee email address
        """
        return self._email_address
    

# define make_employee_dict function
def make_employee_dict(name_list: list[str], ID_list: list[str], sal_list: list[int], email_list: list[str]) -> dict[str, Employee]:
    """
    Function that takes in lists of employee information, creates instances of the Employee class,
    and adds those objects to a dictionary whose keys are ID numbers and values are the whole employee object
    """

    # create starting empty dictionary
    emp_dict: dict[str, Employee] = {}

    # iteratively create Employee objects and add them to emp_dict
    for i in range(len(emp_ids)):
        emp: Employee = Employee(name_list[i], ID_list[i], sal_list[i], email_list[i])
        emp_dict[emp.get_ID_number()] = emp

    return emp_dict
    


# test code

emp_names: list[str] = ["Kyla", "Mandy", "Fin", "Hannah", "Arnie", "Kili"]
emp_ids: list[str] = ["1001", "1003", "1002", "1000", "666", "777"]
emp_sals: list[int] = [40, 8, 45, 150000, 2, 10]
emp_emails: list[str] = ["kyla@gmail.com", "mandy@outlook.com", "finnyboi@aol.com", "hannah@gmail.com", "poopyboy@hotmail.com", "kili@outlook.com"]

employee_dict: dict[str, Employee] = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
print(employee_dict["666"].get_salary())