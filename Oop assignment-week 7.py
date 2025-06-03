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

# Assignment 1: Smartphone Class Hierarchy
class Smartphone:
    def __init__(self, brand, model, storage_gb, color):
        self._brand = brand  # Encapsulated attribute
        self._model = model
        self._storage_gb = storage_gb
        self._color = color
        self._battery_level = 100
        self._is_powered_on = False
    
    def power_on(self):
        if not self._is_powered_on:
            self._is_powered_on = True
            return f"{self._brand} {self._model} is powering on..."
        return "Phone is already on"
    
    def power_off(self):
        if self._is_powered_on:
            self._is_powered_on = False
            return f"{self._brand} {self._model} is powering off..."
        return "Phone is already off"
    
    def charge(self, percentage):
        if 0 <= percentage <= 100:
            self._battery_level = min(100, self._battery_level + percentage)
            return f"Battery level: {self._battery_level}%"
        return "Invalid charging percentage"
    
    def get_info(self):
        return f"{self._brand} {self._model} ({self._color}, {self._storage_gb}GB)"

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, color, gpu_model):
        super().__init__(brand, model, storage_gb, color)
        self._gpu_model = gpu_model
        self._game_mode = False
    
    def enable_game_mode(self):
        self._game_mode = True
        return "Game mode enabled - Performance optimized for gaming"
    
    def disable_game_mode(self):
        self._game_mode = False
        return "Game mode disabled"
    
    def get_info(self):
        return f"{super().get_info()} - Gaming Edition with {self._gpu_model}"

class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, color, camera_mp):
        super().__init__(brand, model, storage_gb, color)
        self._camera_mp = camera_mp
        self._flash_enabled = False
    
    def enable_flash(self):
        self._flash_enabled = True
        return "Camera flash enabled"
    
    def disable_flash(self):
        self._flash_enabled = False
        return "Camera flash disabled"
    
    def take_photo(self):
        if self._is_powered_on:
            return f"📸 Taking photo with {self._camera_mp}MP camera"
        return "Cannot take photo - phone is powered off"
    
    def get_info(self):
        return f"{super().get_info()} - Camera Edition with {self._camera_mp}MP camera"

def demonstrate_smartphones():
    print("\n=== Smartphone Demonstration ===")
    
    # Create different types of smartphones
    gaming_phone = GamingPhone("ASUS", "ROG Phone", 512, "Black", "Snapdragon 8 Gen 2")
    camera_phone = CameraPhone("Sony", "Xperia", 256, "Silver", 48)
    
    # Store phones in a list to demonstrate polymorphism
    phones = [gaming_phone, camera_phone]
    
    # Demonstrate functionality for each phone
    for phone in phones:
        print(f"\nPhone: {phone.get_info()}")
        print(phone.power_on())
        
        if isinstance(phone, GamingPhone):
            print(phone.enable_game_mode())
        elif isinstance(phone, CameraPhone):
            print(phone.enable_flash())
            print(phone.take_photo())
        
        print(phone.charge(30))
        print(phone.power_off())

if __name__ == "__main__":
    main()  # Run the vehicle demonstration
    demonstrate_smartphones()  # Run the smartphone demonstration
