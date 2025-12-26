class Vehicle:
    def init(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    def init(self, make, model, fuel_type):
        super().init(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"


vehicle = Vehicle("lamborghini", "Countach")

car1 = Car("Honda", "Cr-v", "бензин")
car2 = Car("Tesla", "Cybertruck", "электричество")
car3 = Car("Ford", "F-250", "дизель")

print("Базовый класс Vehicle:")
print(vehicle.get_info())
print(car1.get_info())