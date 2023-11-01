class Vehicle:
    
    def __init__(self, VehicleID = "", Registration = "", DateOfRegistration = None, EngineSize = 0, PurchasePrice = 0.00):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00

MyCar = Vehicle()

MyCar.VehicleID = "asads"

MyCar2 = Vehicle(VehicleID = "asdasd23")
print(MyCar2.VehicleID)