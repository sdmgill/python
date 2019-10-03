class Employee():
    """Basic class for an employee"""
    def __init__(self, f_name, l_name, salary):
        """Initialize the arguments"""
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self,bump = 5000):
        """Give this man a raise!!"""
        self.salary += bump

    def show_employee_info(self):
        """Something,something, something...Dark Side"""
        employee_info = self.f_name.title() + ' ' + self.l_name.title() + " makes $" + str(self.salary) + " per year."
        print(employee_info)



empinfo = Employee('sean', 'gill', 100000)
empinfo.show_employee_info()
empinfo.give_raise(10000)
empinfo.show_employee_info()
empinfo.give_raise()
empinfo.show_employee_info()
