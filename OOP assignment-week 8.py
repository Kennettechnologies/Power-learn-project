class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self._name = name  # Encapsulated attribute
        self._secret_identity = secret_identity
        self._power_level = power_level
        self._is_active = False
        self._energy = 100
    
    def activate_powers(self):
        if not self._is_active:
            self._is_active = True
            return f"{self._name} is now active and ready for action!"
        return f"{self._name} is already active"
    
    def deactivate_powers(self):
        if self._is_active:
            self._is_active = False
            return f"{self._name} has returned to civilian life"
        return f"{self._name} is already in civilian form"
    
    def use_power(self):
        if self._is_active and self._energy > 0:
            self._energy -= 10
            return f"{self._name} uses their power! Energy remaining: {self._energy}%"
        return "Cannot use power - either not active or out of energy"
    
    def get_info(self):
        return f"Superhero: {self._name} (Power Level: {self._power_level})"

class FlyingHero(Superhero):
    def __init__(self, name, secret_identity, power_level, max_altitude):
        super().__init__(name, secret_identity, power_level)
        self._max_altitude = max_altitude
        self._is_flying = False
    
    def fly(self):
        if self._is_active:
            self._is_flying = True
            return f"🦸 {self._name} is flying at {self._max_altitude} feet!"
        return "Cannot fly - powers not activated"
    
    def land(self):
        if self._is_flying:
            self._is_flying = False
            return f"{self._name} has landed safely"
        return "Already on the ground"
    
    def get_info(self):
        return f"{super().get_info()} - Flying Hero (Max Altitude: {self._max_altitude}ft)"

class TechHero(Superhero):
    def __init__(self, name, secret_identity, power_level, tech_level):
        super().__init__(name, secret_identity, power_level)
        self._tech_level = tech_level
        self._gadgets = []
    
    def add_gadget(self, gadget):
        self._gadgets.append(gadget)
        return f"Added {gadget} to {self._name}'s arsenal"
    
    def use_gadget(self, gadget):
        if gadget in self._gadgets and self._is_active:
            return f"🦸 {self._name} uses {gadget}!"
        return f"Cannot use {gadget} - either not in arsenal or powers not activated"
    
    def get_info(self):
        return f"{super().get_info()} - Tech Hero (Tech Level: {self._tech_level})"

def demonstrate_superheroes():
    print("\n=== Superhero Demonstration ===")
    
    # Create different types of superheroes
    flying_hero = FlyingHero("Sky Guardian", "John Smith", 85, 10000)
    tech_hero = TechHero("Tech Master", "Sarah Johnson", 90, "Advanced")
    
    # Store heroes in a list to demonstrate polymorphism
    heroes = [flying_hero, tech_hero]
    
    # Demonstrate functionality for each hero
    for hero in heroes:
        print(f"\nHero: {hero.get_info()}")
        print(hero.activate_powers())
        
        if isinstance(hero, FlyingHero):
            print(hero.fly())
            print(hero.use_power())
            print(hero.land())
        elif isinstance(hero, TechHero):
            print(hero.add_gadget("Grappling Hook"))
            print(hero.add_gadget("Smoke Bombs"))
            print(hero.use_gadget("Grappling Hook"))
            print(hero.use_power())
        
        print(hero.deactivate_powers())

if __name__ == "__main__":
    demonstrate_superheroes()
