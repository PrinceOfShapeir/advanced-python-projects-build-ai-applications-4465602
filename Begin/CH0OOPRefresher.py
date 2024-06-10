class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is running!")

car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")

print(f"I have a {car1.make} {car1.model}.")
print(f"I also own a {car2.make} {car2.model}.")\

car1.start_engine()
car2.start_engine()

#test = "abc"
#print(f"{test}")

##hilariously I needed to edit the supplied file names because pylint threw a fit