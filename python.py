class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employees.append(employee)

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def display_table(self):
        for emp in self.employees:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    table = EmployeeTable()

    table.add_employee("161E90", "Raman", 41, 56000)
    table.add_employee("161F91", "Himadri", 38, 67500)
    table.add_employee("161F99", "Jaya", 51, 82100)
    table.add_employee("171E20", "Tejas", 30, 55000)
    table.add_employee("171G30", "Ajay", 45, 44000)

    while True:
        print("Sort Options:")
        print("1. Sort by Age")
        print("2. Sort by Name")
        print("3. Sort by Salary")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            table.sort_by_age()
        elif choice == 2:
            table.sort_by_name()
        elif choice == 3:
            table.sort_by_salary()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        print("Sorted Employee Table:")
        table.display_table()
