class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def fare(self):
        return self.capacity * 100  

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        additional_charge = base_fare * 0.1 
        return base_fare + additional_charge

school_bus = Bus("School Bus", 50)
print(f"Total Bus Fare: {school_bus.fare()}")
