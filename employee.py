"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_wage * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."


class SalaryEmployeeWithBonus(Employee):
    def __init__(self, name, monthly_salary, bonus):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def get_pay(self):
        return self.monthly_salary + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class HourlyEmployeeWithBonus(Employee):
    def __init__(self, name, hourly_wage, hours_worked, bonus):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus

    def get_pay(self):
        return (self.hourly_wage * self.hours_worked) + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."


class SalaryEmployeeWithCommission(Employee):
    def __init__(self, name, monthly_salary, commission_per_contract, contracts_landed):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.commission_per_contract = commission_per_contract
        self.contracts_landed = contracts_landed

    def get_pay(self):
        return self.monthly_salary + (self.commission_per_contract * self.contracts_landed)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."


class HourlyEmployeeWithCommission(Employee):
    def __init__(self, name, hourly_wage, hours_worked, commission_per_contract, contracts_landed):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.commission_per_contract = commission_per_contract
        self.contracts_landed = contracts_landed

    def get_pay(self):
        return (self.hourly_wage * self.hours_worked) + (self.commission_per_contract * self.contracts_landed)

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = SalaryEmployeeWithCommission('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = HourlyEmployeeWithCommission('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = SalaryEmployeeWithBonus('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = HourlyEmployeeWithBonus('Ariel', 30, 120, 600)