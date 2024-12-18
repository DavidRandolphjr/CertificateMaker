import fitz  # PyMuPDF
import os
import sys

class AutoDecSearch:
    def __init__(self, pdf_path):
        # Resolve the correct path for the PDF when running as an executable
        if getattr(sys, 'frozen', False):  # Check if the app is frozen (PyInstaller executable)
            bundle_dir = sys._MEIPASS
        else:
            bundle_dir = os.path.abspath(os.path.dirname(__file__))

        # Use the resolved path to open the PDF file
        self.pdf_file = os.path.join(bundle_dir, pdf_path)
        self.doc = fitz.open(self.pdf_file)

    def search(self):
        # Extract text from each page
        full_text = ""
        for page_num in range(self.doc.page_count):
            page = self.doc.load_page(page_num)
            full_text += page.get_text()

        # Apply regex to find desired patterns
        import re
        liabCoverage = r"BOD INJ & PROP DAMAGE \$(\d{1,4})"
        values = []

        match = re.findall(liabCoverage, full_text)

        if match:
            print(f"Found Limit: ${match}")
            if len(match) == 3:
                for i in match:
                    values.append(i[0] + "," + i[1:] + ",000")
                values.append("nothing")
            else:
                values.append("nothing")
                values.append("nothing")
                values.append("nothing")
                values.append(match[0])
        else:
            print("Bodily Injury and Property Damage Limit not found.")
            values.append("nothing found")

        # Regex pattern for policy number
        policypattern = r"Q\d{2}\s\d{6,}"
        match = re.search(policypattern, full_text)

        if match:
            print(f"Policy # {match.group()}")
            values.append(match.group())
        else:
            print("No policy # found.")
            values.append("nothing found")

        # Regex pattern for date
        date_pattern = r"(\d{2}/\d{2}/\d{2})\s*TO\s*(\d{2}/\d{2}/\d{2})"
        match = re.search(date_pattern, full_text)

        if match:
            start_date = match.group(1)
            end_date = match.group(2)
            if start_date[-3] != "/":
                start_date = start_date[:-4] + start_date[-2:]
            if end_date[-3] != "/":
                end_date = end_date[:-4] + end_date[-2:]
            print("Start date and end date: ", start_date, " ", end_date)
            values.append(start_date)
            values.append(end_date)
        else:
            print("No dates found")
            values.append("None")
            values.append("None")

        values.append("E")
        print("values = ", values)

        return values
