# Work Requirement 1 - PRO2002
The task is to analyze these examples and refactor them to improve structure, readability, and maintainability. Where appropriate, apply simple design patterns (e.g. Strategy or Factory), but only when they clearly improve the design.

## User Manager Mixed Responsabilities
The User Manager class handled many concerns at once: creating a user, saving user information, sending a welcome email and generating a user report. 
I decided to refactor this example following the Single Responsibility Principle, therefore I created different classes for each responsability. 
- User: creates the user.
- UserSaver: saves user information in database.
- EmailSender: send welcome email to user.
- UserReport: generate report to user.

By keeping responsibilities separate, the system is easier to understand, extend, and maintain.

## Order Creation Conditional Logic
The original OrderProcessor used if/else statements to decide which order class should be created for each order type. This made the creation logic harder to read and meant that another conditional branch had to be added when a new order type was needed.
I decided to refactor this example using the Factory pattern, therefore I moved the object creation responsibility into a separate class.
- OnlineOrder: represents an order made online.
- StoreOrder: represents an order made in a store.
- PhoneOrder: represents an order made by phone.
- OrderFactory: creates the correct order object based on the order type.

By separating object creation from the order classes, the code is easier to read and maintain. New order types can be added by updating the factory mapping instead of adding more if/else statements, and unsupported types are handled with a ValueError.

## Vehicle Inheritance Issue
The original Vehicle class included a start_engine method, even though not all vehicles have an engine. This caused a problem when Bicycle inherited from Vehicle because it had to raise an exception when start_engine was called.
I decided to refactor this example following the Liskov Substitution Principle, therefore I moved the engine-specific behavior into a separate subclass.
- Vehicle: provides movement behavior shared by all vehicles.
- EnginedVehicle: provides the start_engine behavior for vehicles with engines.
- Bicycle: inherits movement behavior without inheriting an engine method it cannot support.

By separating the movement and engine behavior, each subclass can be safely used with its parent class. The design is easier to extend to other vehicles without engine and avoids exceptions caused by unsupported behavior.
