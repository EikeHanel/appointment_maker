import datetime
from ics import Calendar, Event


def create_ics_file(start, end, d_name, d_firm, d_rent):
    """
    Create an ICS calendar event for a loan and save it to a file.

    This function generates an ICS file with a calendar event that represents
    the loan period. The event includes a description, start and end time
    based on the provided start and end dates, and sets notifications for the
    event. The ICS file is saved with the name "appointment.ics".

    Parameters:
    start (str): The start date of the loan in "DD/MM/YYYY" format.
    end (str): The end date of the loan in "DD/MM/YYYY" format.
    d_name (str): The name of the person the loan is from.
    d_firm (str): The name of the firm the loan is associated with (can be "NONE").
    d_rent (str): The amount or description of the loan.

    Returns:
    None: This function does not return any value. It creates and writes an ICS file.
    """

    # Convert the end date to datetime object
    event_end = datetime.datetime.strptime(end, "%d/%m/%Y")

    # Set notifications based on event end time
    notification_start = event_end.replace(hour=7, minute=0, second=0)
    notification_end = event_end.replace(hour=9, minute=0, second=0)

    # Format the start and end dates for display
    start_formatted = datetime.datetime.strptime(start, "%d/%m/%Y").strftime("%d/%m/%Y")
    end_formatted = event_end.strftime("%d/%m/%Y")

    # Create the calendar and event
    c = Calendar()
    e = Event()
    e.name = f"Loan: {d_rent}, from {d_name} ({d_firm}) ends today."
    e.description = f"Loan Period: {start_formatted} - {end_formatted}"
    e.begin = notification_start
    e.end = notification_end

    # Add event to calendar
    c.events.add(e)

    # Save ICS file
    with open("appointment.ics", "w") as f:
        f.writelines(c)
