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
The original OrderProcessor used if/else statements to decide which order class should be created for each order type. This makes the creation logic harder to read and means that another conditional branch must be added when a new order type is needed.

I refactored this example using a simple Factory pattern. The OrderFactory creates the correct order object. A dictionary maps each order type to its class, and the create_order method uses that mapping to create the object. It also checks whether the order type is supported and raises a ValueError when it is not.

This improves the design by:
- Removing the repeated if/else statements.
- Making the code easier to read and maintain.
- Making it easier to add another order type by updating only the factory.

## Vehicle Inheritance Issue