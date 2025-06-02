class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def move(self):
        pass  # This will be overridden by child classes
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def move(self):
        return "🚗 Driving on the road"
    
    def honk(self):
        return "Beep! Beep!"

class Airplane(Vehicle):
    def __init__(self, brand, model, year, wingspan):
        super().__init__(brand, model, year)
        self.wingspan = wingspan
    
    def move(self):
        return "✈️ Flying in the sky"
    
    def take_off(self):
        return "Taking off from the runway"

class Boat(Vehicle):
    def __init__(self, brand, model, year, length):
        super().__init__(brand, model, year)
        self.length = length
    
    def move(self):
        return "⛵ Sailing on the water"
    
    def anchor(self):
        return "Dropping anchor"

# Example usage
def main():
    # Create different vehicles
    car = Car("Toyota", "Camry", 2023, 4)
    airplane = Airplane("Boeing", "747", 2022, 68.4)
    boat = Boat("Yamaha", "WaveRunner", 2023, 12)
    
    # Store vehicles in a list to demonstrate polymorphism
    vehicles = [car, airplane, boat]
    
    # Display information and movement for each vehicle
    for vehicle in vehicles:
        print(f"\nVehicle: {vehicle.display_info()}")
        print(f"Movement: {vehicle.move()}")
        
        # Demonstrate specific methods for each type
        if isinstance(vehicle, Car):
            print(f"Car specific: {vehicle.honk()}")
        elif isinstance(vehicle, Airplane):
            print(f"Airplane specific: {vehicle.take_off()}")
        elif isinstance(vehicle, Boat):
            print(f"Boat specific: {vehicle.anchor()}")

if __name__ == "__main__":
    main()
