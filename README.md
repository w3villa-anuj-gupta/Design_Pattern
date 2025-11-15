# Design Patterns Demo: Office System

This project demonstrates the implementation of three fundamental design patterns (Singleton, Factory, and Observer) in a simple office system. The application models an office environment where employees can be created and notified of important announcements.

## Design Patterns Used

### 1. Singleton Pattern - `OfficeConfig`
- Ensures a single, global instance manages system-wide settings
- Provides centralized control over office configuration
- Used for managing office hours and location settings

### 2. Factory Pattern - `EmployeeFactory`
- Provides a unified interface for creating different types of employees
- Encapsulates object creation logic
- Makes it easy to add new employee types without modifying existing code

### 3. Observer Pattern - `AnnouncementService`
- Implements a publish-subscribe mechanism for office announcements
- Allows employees to receive updates automatically
- Decouples the announcement sender from the receivers

### Flowchart

```
[Start]
  |
  v
[Get OfficeConfig (Singleton)]
  |
  v
[EmployeeFactory creates Employees]
  |
  v
[Register Employees as Observers to AnnouncementService]
  |
  v
[AnnouncementService sends an announcement]
  |
  v
[Employees receive notification]
  |
  v
[End]
```


## File Structure

- `main.py` - Main application code demonstrating the patterns
- `singleton.py` - Implementation of the Singleton pattern (OfficeConfig)
- `factory.py` - Implementation of the Factory pattern (EmployeeFactory)
- `observer.py` - Implementation of the Observer pattern (AnnouncementService)

## Running the Application

1. Ensure you have Python installed
2. Run the application:
   ```bash
   python main.py
   ```

## Design Pattern Comparison

| Pattern     | Purpose | Example Used | Project Role |
|-------------|---------|--------------|--------------|
| Singleton   | Single instance shared system-wide | OfficeConfig | Office-wide settings |
| Factory     | Centralized object creation | EmployeeFactory | Employee creation |
| Observer    | Publish–subscribe notification system | AnnouncementService | Office announcements to employees |
