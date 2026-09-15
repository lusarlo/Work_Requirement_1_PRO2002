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

## Vehicle Inheritance Issue