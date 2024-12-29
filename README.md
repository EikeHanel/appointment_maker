# Appointment-Maker (for Loans)  
#### Video Demo:  https://youtu.be/qhbv1Eznjf4
#### Description:

This project is a Python-based graphical user interface (GUI) application designed to manage loaned items and schedule appointments efficiently. The application allows users to input details such as names, companies, items loaned, and start and end dates. It provides several key features to enhance productivity and the workflow.

## Features:
### 1. Data Management:
Store and manage appointment details efficiently by saving them to a CSV file. This feature ensures that all appointment records are easily accessible, sortable, and editable for future reference. The CSV file acts as a centralized database, keeping track of critical details such as start and end dates, borrower names, associated companies, and loan descriptions.

### 2. File Generation:
Automatically create essential files for each appointment, including:

- A PDF summary that provides a clear and professional overview of the loan details, complete with the borrower’s information, loan duration, and a signature section.
- An ICS calendar file that integrates seamlessly with calendar applications, making it easier for users to schedule and track their appointments.
These files enhance organization and professionalism, offering users multiple formats to manage their appointments effectively.

### 3. Email Notifications:
Send timely email reminders to keep users informed about upcoming appointments. The email system includes the ability to attach the generated ICS calendar file for convenient integration into calendar applications. This ensures users never miss important loan deadlines and can easily manage their schedules with reminders delivered directly to their inbox.

### 4. Dynamic UI:
The graphical user interface (GUI) dynamically adjusts dropdown menus based on the selected month and year. This intelligent feature ensures users can only select valid dates, automatically accounting for month lengths and leap years. This makes date selection intuitive and error-free, improving overall user experience and minimizing mistakes in appointment scheduling.

### 5. Error Handling:
The application includes robust input validation and error messaging to ensure data accuracy. Users are alerted if inputs are missing, invalid, or out of expected ranges. This feature prevents the submission of incorrect or incomplete data, enhancing the reliability of records and the overall usability of the application.

### 6. `requirements.txt`
A requirements.txt file is included for effortless installation of all the necessary libraries and dependencies. With a simple command, users can set up the required environment to run the application, making it beginner-friendly and hassle-free. 

### 7. `.env` for Security
The .env file ensures secure management of sensitive information such as email credentials, SMTP server details, and recipient addresses. By storing these details in an environment file, the application minimizes the risk of exposing private information in the codebase. This approach adheres to best practices in software security, keeping critical data protected while simplifying configuration.

## Technologies Used:
- **Tkinter**: For the graphical user interface.
- **Python's calendar Module**: To calculate days of the month dynamically.
- **Self-Made Custom Modules**:
  
  These handler.py files were created to enhance code readability and maintainability. By separating distinct functionalities into individual modules, the codebase becomes more modular and easier to navigate. Additionally, this separation allows for more efficient testing and debugging of specific functions, facilitating quicker identification and resolution of issues.

  - **email_handler** for email functionality.
    - This module is designed to send emails with a specified subject, body, and an optional attachment using the SMTP protocol. The sender's email, recipient's email, and SMTP credentials are securely retrieved from environment variables, ensuring sensitive information is not hard-coded. The module supports attachments and validates the existence of files before attempting to send them. Comprehensive error handling ensures that issues such as missing attachments or SMTP connection errors are handled gracefully, providing meaningful feedback to the user.
  - **csv_handler** for data storage.
    - This module provides functionality to record loan details, such as start and end dates, borrower's name, associated company, and a description of the loaned item. It ensures that data is consistently appended to an existing CSV file or creates a new file if none exists. The module also automatically sorts entries by the start date for better organization. All data is stored in a structured format in the data/ directory, making it easily accessible for further processing or review.
  - **pdf_handler** for PDF generation.
    - This module creates professional-looking PDF documents that summarize the key details of a loan. It includes fields for the borrower's name, associated company, loan period, and description of the item. Signature lines for the borrower and lender are included for added validity. The module also supports adding a logo or image to the document if available. The PDFs are saved with descriptive filenames in the data/ directory, making them easy to locate and share.
  - **ics_handler** for calendar file creation.
    - This module generates ICS (iCalendar) files to represent loan events, enabling easy integration with calendar applications. Each event includes the loan's start and end dates, a description of the loaned item, and notifications set around the event's conclusion. By leveraging the ics library, the module ensures compatibility with major calendar tools. The ICS files are saved as appointment.ics for straightforward use and sharing.


This tool is ideal for businesses or individuals who need to track loans and appointments effectively while integrating reminders into their workflow.