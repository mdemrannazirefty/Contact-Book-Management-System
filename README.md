# Contact Book Management System With Python
This is a Python-based Command Line Interface (CLI) application that allows users to manage their contact information efficiently. The system provides a wide range of features such as adding, viewing, removing, and searching contacts. It ensures that duplicate phone numbers cannot be added and provides proper error handling for user inputs.

The system saves all contact data into a CSV file and loads the data when the program starts. The user interface is interactive and easy to navigate, with options to manage your contacts, making it simple for anyone to use.

# Key Features
Add Contacts:

Add new contacts by entering details such as Name, Email, Phone Number, and Address.
Phone number uniqueness is enforced to ensure no duplicate contacts are added.
Prevent Duplicate Phone Numbers:

The system checks if the phone number already exists before adding a new contact. If the number exists, the system will prompt the user to use a different one.
View Contacts:

Display all saved contacts in an organized and user-friendly format. Users can see details such as Name, Email, Phone Number, and Address.
Save and Load Contacts:

All contacts are automatically saved to a CSV file on the system. Upon starting the application, the system will load previously saved contacts.
No data is lost between sessions.

Search for specific contacts using their name, email, or phone number. This allows users to quickly find the contact they are looking for.
Error Handling:

# Provides robust error handling for invalid inputs. For example:
- Ensures that the contact’s name is a string.
- Ensures that the phone number is an integer.
- If an invalid input is detected, the system will guide the user with a clear error message to help them correct it.

# Menu System
The application provides an interactive menu that lets users choose from different options. It includes options to:
- Add a contact
- Remove a contact
- View all contacts
- Search contacts
- Exit the application
- Data Storage
- Contacts are stored in a CSV file (Contact_List.csv) with fields for Name, Phone Number, Email, and Address.
- Upon starting the program, all existing contacts are loaded from the CSV file into the system.

# Technologies Used
Python 3.x: Core programming language used for the implementation.
CSV: For storing and retrieving contact information in a text-based format.

# Conclusion
This Contact Book Management System is a simple and effective CLI application that can be extended further with additional features like editing contacts, sorting, or even integrating with other platforms. It's a great project to practice Python basics and file handling.
