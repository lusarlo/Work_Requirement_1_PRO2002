# class OrderProcessor:
#     def create_order(self, order_type):
#         if order_type == "online":
#             return OnlineOrder()
#         elif order_type == "store":
#             return StoreOrder()
#         elif order_type == "phone":
#             return PhoneOrder()
#         else:
#             raise ValueError("Unknown order type")

# class OnlineOrder:
#     pass

# class StoreOrder:
#     pass

# class PhoneOrder:
#     pass

class OnlineOrder:
    pass    

class StoreOrder:
    pass

class PhoneOrder:
    pass

class OrderFactory:
  order_types = {
    "online": OnlineOrder,
    "store":  StoreOrder,
    "phone": PhoneOrder
  }

  @classmethod
  def create_order(cls, order_type):
    if order_type not in cls.order_types:
      raise ValueError("Unknown order type")
    
    return cls.order_types[order_type]()

