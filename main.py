import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from email_handler import send_email
from csv_handler import save_to_csv
from pdf_handler import create_pdf
from ics_handler import create_ics_file
import calendar


MONTH = ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]
DAY = list(map(str, range(1, 32)))
YEAR = list(map(str, range(2024, 2031)))


# Function to handle OK button click
def on_ok():
    """
        Collects input data from form fields, saves the data to a CSV file, generates a PDF and ICS file,
        and sends a reminder email with an ICS file attachment.

        This function is triggered when the "OK" button is clicked. It retrieves user input from various form fields,
        constructs the start and end dates, and collects other details such as the name, firm, and item loaned.
        The function then:
        - Saves the data to a CSV file by calling the `save_to_csv` function.
        - Generates a PDF document using the `create_pdf` function.
        - Creates an ICS calendar file using the `create_ics_file` function.
        - Constructs the email subject and body, then sends the email with the ICS file attached using the `send_email` function.

        This function does not accept parameters nor return any values. It performs the actions of saving data, creating
        files, and sending an email directly.

        Side Effects:
        - Data is saved to a CSV file.
        - A PDF file and ICS file are generated.
        - An email with an ICS file attachment is sent to the recipient.

        Exceptions:
        - If an error occurs during the file generation or email sending process, an error message will be displayed.
    """

    # Check inputs
    if not name.get():  # Check if the name field is empty
        messagebox.showerror("Input Error", "The Name field is required.")
        return
    if not rent.get():  # Check if the name field is empty
        messagebox.showerror("Input Error", "The Item Loaned field is required.")
        return

    data_start_date = f"{day_start_var.get()}/{MONTH.index(month_start_var.get()) + 1:02d}/{year_start_var.get()}"
    data_end_date = f"{day_end_var.get()}/{MONTH.index(month_end_var.get()) + 1:02d}/{year_end_var.get()}"
    if data_start_date == data_end_date:
        result = messagebox.askyesno("Input Error", "The Start and End date are the same. "
                                                    "Do you want to continue?")
        if not result:
            return

    data_name = name.get()
    data_firm = firm.get() if firm.get() else "NONE"
    data_rent = rent.get()

    save_to_csv(start=data_start_date, end=data_end_date, d_name=data_name, d_firm=data_firm, d_rent=data_rent)
    create_pdf(start=data_start_date, end=data_end_date, d_name=data_name, d_firm=data_firm, d_rent=data_rent)
    create_ics_file(start=data_start_date, end=data_end_date, d_name=data_name, d_firm=data_firm, d_rent=data_rent)

    subject = f"Loan from: {data_name}"
    body = (f"Reminder:\n\n"
            f"Name: {data_name}\n"
            f"Loan: {data_rent}\n\n"
            f"Start: {data_start_date}\n"
            f"End: {data_end_date}")

    # Send email with the generated ICS file attached
    send_email(subject, body, "appointment.ics")


# Function to update the day dropdown based on the selected month and year
def update_days(day_var, month_var, year_var, day_combobox):
    """
        Updates the available days in a dropdown menu based on the selected month and year.

        This function is triggered when the month or year is changed. It retrieves the selected month and year,
        calculates the number of days in that month, and updates the day dropdown (combobox) with the valid days
        for that month and year. If the previously selected day is no longer valid (e.g., selecting February and
        the day is 30), it resets the day to the first valid day of the month.

        Parameters:
        - day_var (tkinter.StringVar): A variable holding the current selected day.
        - month_var (tkinter.StringVar): A variable holding the current selected month.
        - year_var (tkinter.StringVar): A variable holding the current selected year.
        - day_combobox (tkinter.Combobox): The combobox widget for selecting a day, which will be updated.

        Side Effects:
        - The 'values' attribute of `day_combobox` is updated to reflect the valid days for the selected month and year.
        - The selected day is updated if the previous selection is no longer valid.

        Exceptions:
        - If an error occurs during the process (e.g., invalid month or year), an error message is shown to the user.
    """

    try:
        # Get the currently selected month and year
        month_index = MONTH.index(month_var.get()) + 1
        year = int(year_var.get())

        # Determine the number of days in the month
        num_days = calendar.monthrange(year, month_index)[1]

        # Update the day dropdown with valid days
        valid_days = list(map(str, range(1, num_days + 1)))
        day_combobox['values'] = valid_days

        # Reset the day to a valid value if it's no longer valid
        if day_var.get() not in valid_days:
            day_var.set(valid_days[0])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def sync_end_date():
    """
        Syncs the end date to match the start date.

        This function updates the end date (month, day, and year) to match the currently selected start date.
        It ensures that the end date reflects the same values as the start date when the user chooses to sync them.

        Side Effects:
        - The `month_end_var`, `day_end_var`, and `year_end_var` variables are updated to match the values of
          `month_start_var`, `day_start_var`, and `year_start_var`, respectively.

        Exceptions:
        - If an error occurs during the synchronization process, an error message is shown to the user.
    """

    try:
        # Sync the end date to match the start date
        month_end_var.set(month_start_var.get())
        day_end_var.set(day_start_var.get())
        year_end_var.set(year_start_var.get())
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while syncing dates: {str(e)}")


# Create the main application window
root = tk.Tk()
root.title("Appointment Scheduler")

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Variables
month_start_var = tk.StringVar()
month_start_var.set(MONTH[0])
day_start_var = tk.StringVar()
day_start_var.set(DAY[0])
year_start_var = tk.StringVar()
year_start_var.set(YEAR[0])

month_end_var = tk.StringVar()
month_end_var.set(MONTH[0])
day_end_var = tk.StringVar()
day_end_var.set(DAY[0])
year_end_var = tk.StringVar()
year_end_var.set(YEAR[0])

# Start Date Widgets
tk.Label(root, text="Start Date:*").grid(row=1, column=0, padx=10, pady=10)
start_month_cb = ttk.Combobox(root, textvariable=month_start_var, values=MONTH, state="readonly")
start_month_cb.grid(row=1, column=1, padx=10, pady=10)
start_day_cb = ttk.Combobox(root, textvariable=day_start_var, values=DAY, state="readonly")
start_day_cb.grid(row=1, column=2, padx=10, pady=10)
start_year_cb = ttk.Combobox(root, textvariable=year_start_var, values=YEAR, state="readonly")
start_year_cb.grid(row=1, column=3, padx=10, pady=10)

# End Date Widgets
tk.Label(root, text="End Date:*").grid(row=2, column=0, padx=10, pady=10)
end_month_cb = ttk.Combobox(root, textvariable=month_end_var, values=MONTH, state="readonly")
end_month_cb.grid(row=2, column=1, padx=10, pady=10)
end_day_cb = ttk.Combobox(root, textvariable=day_end_var, values=DAY, state="readonly")
end_day_cb.grid(row=2, column=2, padx=10, pady=10)
end_year_cb = ttk.Combobox(root, textvariable=year_end_var, values=YEAR, state="readonly")
end_year_cb.grid(row=2, column=3, padx=10, pady=10)


# Traces
def setup_date_traces(day_var, month_var, year_var, day_cb):
    month_var.trace_add("write", lambda *args: update_days(day_var, month_var, year_var, day_cb))
    year_var.trace_add("write", lambda *args: update_days(day_var, month_var, year_var, day_cb))


setup_date_traces(day_start_var, month_start_var, year_start_var, start_day_cb)
setup_date_traces(day_end_var, month_end_var, year_end_var, end_day_cb)

month_start_var.trace_add("write", lambda *args: sync_end_date())
day_start_var.trace_add("write", lambda *args: sync_end_date())
year_start_var.trace_add("write", lambda *args: sync_end_date())


tk.Label(root, text="Name:* ").grid(row=3, column=0, padx=10, pady=10)
name = tk.Entry(root)
name.grid(row=3, column=1, columnspan=3, padx=10, pady=10, sticky="we")

tk.Label(root, text="Company:").grid(row=4, column=0, padx=10, pady=10)
firm = tk.Entry(root)
firm.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky="we")

tk.Label(root, text="Item Loaned:* ").grid(row=5, column=0, padx=10, pady=10)
rent = tk.Entry(root)
rent.grid(row=5, column=1, columnspan=3, padx=10, pady=10, sticky="we")

tk.Button(root, text="OK", command=on_ok).grid(row=6, column=0, columnspan=4, pady=20)

root.mainloop()
