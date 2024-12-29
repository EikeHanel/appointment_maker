import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


def create_pdf(start, end, d_name, d_firm, d_rent):
    """
        Creates a PDF document with loan details and saves it as a file.

        This function generates a PDF containing the loan details, including the
        name of the person the loan is from, the associated company, the loan period,
        and the item loaned. It also includes two signature lines for validation.
        An image (e.g., logo) is added to the PDF if the file exists. The PDF is saved
        as "_document.pdf".

        Parameters:
        start (str): The start date of the loan in "DD/MM/YYYY" format.
        end (str): The end date of the loan in "DD/MM/YYYY" format.
        d_name (str): The name of the person the loan is from.
        d_firm (str): The name of the firm the loan is associated with (can be "NONE").
        d_rent (str): The description or amount of the loaned item.

        Returns:
        None: This function generates and saves a PDF file directly with the loan details.
    """

    pdf_path = f"data/{d_name}_{d_rent}_loan.pdf"
    font_path = os.path.join(os.getcwd(), 'Open_Sans', 'OpenSans_font.ttf')
    image_path = "placeholder.jpg"
    pdf_canvas = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    pdfmetrics.registerFont(TTFont('Open_Sans', font_path))

    image_width = 2.5 * inch
    image_height = 1.5 * inch
    pdf_canvas.drawImage(image_path, (width - image_width) / 2, height - image_height - inch, width=image_width,
                         height=image_height)
    y_position = height - image_height - 2 * inch

    pdf_canvas.setFont("Open_Sans", 12)
    pdf_canvas.setFillColor(colors.black)

    label_x = 1 * inch
    data_x = 3 * inch

    pdf_canvas.drawString(label_x, y_position, "Name:")
    pdf_canvas.drawString(data_x, y_position, d_name)
    y_position -= 0.3 * inch
    pdf_canvas.drawString(label_x, y_position, "Company:")
    pdf_canvas.drawString(data_x, y_position, d_firm)
    y_position -= 0.3 * inch
    pdf_canvas.drawString(label_x, y_position, "Period:")
    pdf_canvas.drawString(data_x, y_position, f"{start} - {end}")
    y_position -= 0.3 * inch
    pdf_canvas.drawString(label_x, y_position, "Loan:")
    pdf_canvas.drawString(data_x, y_position, d_rent)
    y_position -= 1 * inch
    pdf_canvas.drawString(1 * inch, y_position, "Authorized Signature:")
    line_start_x = 3.5 * inch
    line_end_x = 7.5 * inch
    pdf_canvas.line(line_start_x, y_position, line_end_x, y_position)
    y_position -= 1 * inch
    pdf_canvas.drawString(1 * inch, y_position, "Recipient's Signature:")
    pdf_canvas.line(line_start_x, y_position, line_end_x, y_position)

    pdf_canvas.showPage()
    pdf_canvas.save()
