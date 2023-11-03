import pickle

class Vehicle:
    
    def __init__(self, VehicleID = "", Registration = "", DateOfRegistration = None, EngineSize = 0, PurchasePrice = 0.00):
        self.VehicleID = VehicleID
        self.Registration = Registration
        self.DateOfRegistration = DateOfRegistration
        self.EngineSize = EngineSize
        self.PurchasePrice = PurchasePrice
    
    def output(self):
        print(f"VehicleID: {self.VehicleID}")
        print(f"Registration: {self.Registration}")
        print(f"DateOfRegistration: {self.DateOfRegistration}")
        print(f"EngineSize: {self.EngineSize}")
        print(f"PurchasePrice: {self.PurchasePrice}")

MyCar = Vehicle()

MyCar.VehicleID = "00100101"
MyCar.Registration = "PYT009"
MyCar.DateOfRegistration = "23/11/2023"
MyCar.EngineSize = 2500
MyCar.PurchasePrice = 21000.00

MyCar.output()

#####################
## Sequential File ##
#####################

Cars = [Vehicle() for i in range(100)]

CarFile = open("Cars.dat", "wb")
for item in range(100):
    pickle.dump(Cars[item], CarFile)
CarFile.close()


CarFile = open("Cars.dat", "rb")
Car = []
for _ in range(100):
    Car.append(pickle.load(CarFile))
CarFile.close()

#################
## Random File ##
#################

JoWee = Vehicle()
JoWee.VehicleID = "asdasdq"

CarFile = open("JoWee.dat", "wb")
Address = hash(JoWee.VehicleID)
CarFile.seek(Address)
pickle.dump(JoWee, CarFile)
CarFile.close()


CarFile = open("JoWee.dat", "rb")
Address = hash(JoWee.VehicleID)
CarFile.seek(Address)
JoWee = pickle.load(CarFile)
CarFile.close()