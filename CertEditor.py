import os
import time
import fitz  # PyMuPDF
import subprocess
import os
import sys

class Certify:

    def __init__(self):
        # Check if running from a bundled executable (PyInstaller)
        if hasattr(sys, '_MEIPASS'):
            # If running as a PyInstaller executable, use the bundled resource
            self.pdf_template = os.path.join(sys._MEIPASS, 'Certificate Template.pdf')
        else:
            # Otherwise, assume the template is in the same directory as the script
            self.pdf_template = os.path.join(os.getcwd(), 'Certificate Template.pdf')

    def fill_form(self, entries, name):
        print("printing entries: ")
        for i in entries:
            print(i)
        agency = "THE RANDOLPH INS AGY INC\n1151 S TROOPER RD\nNORRISTOWN, PA 19403"

        # Create a new PDF from the template
        doc = fitz.open(self.pdf_template)
        page = doc[0]  # Assuming we're only working with the first page

        # Define positions for each entry (x, y) - adjust these values based on your PDF layout
        positions = [

            (100, 120),  # Position for Agency Address

            (100, 180),  # Position Name and Address of Insured
            (325, 120),  # Position for Agent Number
            (525, 49),  # Position for Description of Operations

            (40, 595),  # Position for Certificate Holder Name and Address
            (80, 715),  # Position for PDF Name


            (465, 270),  # Position for GL Each Occurrence
            (465, 281),  # Position for GL Fire Damage
            (465, 293),  # Position for GL Med EXP
            (465, 305),  # Position for GL Personal & ADV. Injury
            (465, 317),  # Position for GL General Aggregate
            (465, 329),  # Position for GL General Aggregate
            (160, 270),  # Position for GL General Aggregate
            (267, 270),  # Position for GL General Aggregate
            (323, 270),  # Position for GL General Aggregate
            (20, 270),  # Position for GL General Aggregate

            (45, 278),  # Position for GL General Aggregate
            (60, 290),  # Position for GL General Aggregate
            (115, 290),  # Position for GL General Aggregate
            (45, 338),  # Position for GL General Aggregate
            (81, 338),  # Position for GL General Aggregate
            (122, 338),  # Position for GL General Aggregate
            (465, 360),  # Position forAL bod inj ep
            (465, 375),  # Position for bod inj ea
            (465, 388),  # Position for AL prop dam
            (465, 410),  # Position for AL Bodily Inj and prop dam combined
            (160, 360),  # Position for AL Policy #
            (267, 360),  # Position for AL Start Date
            (323, 360),  # Position for AL End Date
            (20, 350),  # Position for AL CO LTR
            (45, 360),  # Position for AL Any Auto
            (45, 373),  # Position for AL Owned
            (45, 387),  # Position for AL Hired
            (45, 400),  # Position for AL Non-Owned
            (45, 413),  # Position for AL Garage
            (465, 427),  # Position for EL Each Occurrence
            (465, 438),  # Position for EL Aggregate
            (160, 427),  # Position for EL Policy #
            (267, 427),  # Position for EL Start Date
            (323, 427),  # Position for EL End Date
            (20, 427),  # Position for EL CO LTR
            (45, 437),  # Position for EL End Date
            (45, 461),  # Position for EL End Date
            (465, 493),  # Position for WC Accident Each Accident
            (465, 504),  # Position for WC Disease Policy Limit
            (465, 516),  # Position for WC Disease Each Employee
            (160, 487),  # Position for WC Policy #
            (267, 487),  # Position for WC Start Date
            (323, 487),  # Position for WC End Date
            (20, 487),  # Position for EL CO LTR
            (410, 538),  # Position for other description
            (60, 538),  # Position for other Policy #
            (160, 538),  # Position for other Policy #
            (267, 538),  # Position for WC Start Date
            (323, 538),  # Position for WC End Date
            (20, 532)  # Position for other CO LTR

        ]

        # Write agency address at the first position
        page.insert_text(positions[0], agency, fontsize=11)

        # Populate the PDF with entries based on the defined positions
        for i in range(len(entries)):
            if i < len(positions) - 1:  # Check to ensure we don't go out of bounds
                page.insert_text(positions[i + 1], entries[i], fontsize=11)

        # Save the modified PDF with a new name
        pdf_name = os.path.join(os.getcwd(), name + ".pdf")
        doc.save(pdf_name)
        doc.close()

        # Get the absolute path to the PDF
        pdf_path = os.path.abspath(pdf_name)

        # Open the PDF in the default viewer
        import subprocess

        if os.name == 'nt':  # Windows
            subprocess.Popen([pdf_path], shell=True)
        elif os.name == 'posix':  # macOS and Linux
            os.system(f"open {pdf_path}")

        # Allow time for the PDF viewer to open the file before deletion
        time.sleep(2)  # Adjust time if necessary

        # Delete the PDF after viewing
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
