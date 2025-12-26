class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Имя сострудника: {self.name}, id сотрудника: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} руководит проектами в отделе {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание по специализации: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        return "\n".join(emp.get_info() for emp in self.team)


emp_1 = Employee("Егор", "001")
print(emp_1.get_info())

emp_2 = Manager("Костя", "002", "Продажи")
print(emp_2.get_info())
print(emp_2.manage_project())

tech_emp_1 = Technician("Аля", "003", "Сети")
print(tech_emp_1.get_info())
print(tech_emp_1.perform_maintenance())

tech_emp_2 = TechManager("Тимур", "004", "ИТ", "Системы")
print(tech_emp_2.get_info())
print(tech_emp_2.manage_project())
print(tech_emp_2.perform_maintenance())


tech_emp_2.add_employee(tech_emp_2)
tech_emp_2.add_employee(emp_1)
tech_emp_2.add_employee(emp_2)
tech_emp_2.add_employee(tech_emp_1)
print("Информация о команде TechManager's :")
print(tech_emp_2.get_team_info())