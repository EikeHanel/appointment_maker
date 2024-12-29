import os
import pandas as pd
import datetime


def save_to_csv(start, end, d_name, d_firm, d_rent):
    """
        Adds a new appointment to a CSV file containing loan information.

        This function creates a new entry for the loan in the form of a dictionary
        and appends it to an existing CSV file, or creates a new CSV file if one
        does not already exist. The new entry includes the start and end dates,
        the name of the person the loan is from, the associated company (if provided),
        and the item being loaned. The CSV file is then sorted by the start date.

        Parameters:
        start (str): The start date of the loan in "DD/MM/YYYY" format.
        end (str): The end date of the loan in "DD/MM/YYYY" format.
        d_name (str): The name of the person the loan is from.
        d_firm (str): The name of the firm the loan is associated with (can be "NONE").
        d_rent (str): The description or amount of the loaned item.

        Returns:
        None: This function modifies the CSV file directly and does not return any value.
    """

    # Get the directory of the current script (main.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the path to the 'data' folder relative to the script
    data_folder = os.path.join(script_dir, 'data')

    # Check if the 'data' folder exists
    if not os.path.exists(data_folder):
        # If the folder doesn't exist, create it
        os.makedirs(data_folder)

    new_row = {
        "Start Date": datetime.datetime.strptime(start, "%d/%m/%Y"),
        "End Date": datetime.datetime.strptime(end, "%d/%m/%Y"),
        "Name": d_name,
        "Company": d_firm,
        "Item Loaned": d_rent
    }

    if os.path.exists("data/Loan_Data.csv"):
        df = pd.read_csv("data/Loan_Data.csv")
        df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
        new_row_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_row_df], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    df = df.sort_values(by='Start Date', ascending=True)
    df.to_csv("data/Loan_Data.csv", index=False)
