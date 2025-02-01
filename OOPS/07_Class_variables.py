"""
  Class Variables - Any variables defined at the class level is called Class Variables
  Instance Variables -Any varaiables defined at the with in the method are called ad Instance Variables

  Always prepend Instance varaiables with self so that they can be accesseed with in or outside class defination
  Class variables hould be definde with clas name
"""

class Employee():
    emp_count = 0#class variables
    emp_id    = 0#class variables

    def __init__(self,name,salary=15000):
        print("\n New Employee Joined")
        self.employee_name = name
        self.salary = salary
        Employee.emp_count += 1 #class variables defined with name of class

    def Total_Employees_count(self):
        print(f"Total employess count(before)    :",{Employee.emp_count})

        # Employee.emp_count+= 1
        self.emp_count += 1
        print(f"self.emp_count  :{self.emp_count}")
        print(f"Total Employees count(After)    :",{Employee.emp_count})
    
    def __del__(self):
         pass

if __name__ == "__main__":
    empl_1 = Employee("Brook",50000)
    print(vars(empl_1))
    empl_1.Total_Employees_count()

    empl_2 = Employee("Ross",12000)
    print(vars(empl_2))
    empl_2.Total_Employees_count()

    empl_3 = Employee("Bradon",2000)
    print(vars(empl_3))
    empl_3.Total_Employees_count()

    del empl_1

    empl_4 = Employee("Joss",120000)
    print(vars(empl_4))
    empl_4.Total_Employees_count()
"""
OUTPUT - If we TAKE !!!-- self.emp_count += 1
        print(f"self.emp_count  :{self.emp_count}")--!!!
 New Employee Joined
{'employee_name': 'Brook', 'salary': 50000}
Total employess count(before)    : {1}
self.emp_count  :2
Total Employees count(After)    : {1}

 New Employee Joined
{'employee_name': 'Ross', 'salary': 12000}
Total employess count(before)    : {2}
self.emp_count  :3
Total Employees count(After)    : {2}

 New Employee Joined
{'employee_name': 'Bradon', 'salary': 2000}
Total employess count(before)    : {3}
self.emp_count  :4
Total Employees count(After)    : {3}

 New Employee Joined
{'employee_name': 'Joss', 'salary': 120000}
Total employess count(before)    : {4}
self.emp_count  :5
Total Employees count(After)    : {4}
"""



"""

OUTPUT - If we TAKE !!!--Employee.emp_count+= 1 --!!!
New Employee Joined
{'employee_name': 'Brook', 'salary': 50000}
Total employess count(before)    : {1}
Total Employees count(After)    : {2}

 New Employee Joined
{'employee_name': 'Ross', 'salary': 12000}
Total employess count(before)    : {3}
Total Employees count(After)    : {4}

 New Employee Joined
{'employee_name': 'Bradon', 'salary': 2000}
Total employess count(before)    : {5}
Total Employees count(After)    : {6}

 New Employee Joined
{'employee_name': 'Joss', 'salary': 120000}
Total employess count(before)    : {7}
Total Employees count(After)    : {8}
"""