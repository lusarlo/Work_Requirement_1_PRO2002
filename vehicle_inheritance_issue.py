# class Vehicle:
#     def start_engine(self):
#         print("Engine started")

# class Bicycle(Vehicle):
#     def start_engine(self):
#         raise Exception("Bicycles do not have engines")


class Vehicle:
  def start_movement(self):
    print("Vehicle is moving")

class EnginedVehicle(Vehicle):
  def start_engine(self):
    print("Engine started")

class Bicycle(Vehicle):
  pass
