import fitz  # PyMuPDF

class GLDecSearch:
    def __init__(self, pdf_path):
        # Path to your PDF file
        self.pdf_file = pdf_path
        # Open the PDF
        self.doc = fitz.open(self.pdf_file)

    def search(self):
    # Extract text from each page
        full_text = ""
        for page_num in range(self.doc.page_count):
            page = self.doc.load_page(page_num)
            full_text += page.get_text()

        # Print the extracted text to inspect it
        # print(full_text)

        # Apply regex as before
        import re
        patterns = [r"Bodily injury and property damage\s+\$(\d{1,3}(?:,\d{3})*)",
                    r"Damage to premises rented to you  Fire legal liability\s+\$(\d{1,3}(?:,\d{3})*)",
                    r"Medical expense payments\s+\$(\d{1,3}(?:,\d{3})*)",
                    r"Personal and advertising injury\s+\$(\d{1,3}(?:,\d{3})*)",

                    r"General aggregate\s+\$(\d{1,3}(?:,\d{3})*)",
                    r"Products  Completed operations aggregate\s+\$(\d{1,3}(?:,\d{3})*)",
                    ]
        values = []

        for i in range(0, len(patterns)):
            match = re.search(patterns[i], full_text)

            if match:
                dollar_value = match.group(1)
                print(f"Found Limit: ${dollar_value}")
                values.append(dollar_value)

            else:
                print("Bodily Injury and Property Damage Limit not found.")
                print(patterns[i])
                values.append("nothing found")

        policypattern = r"Q\d{2} \d{7}"

        # Search for the first occurrence of the pattern
        match = re.search(policypattern, full_text)

        # If a match is found, print it
        if match:
            print(f"Policy # {match.group()}")
            values.append(match.group())
        else:
            print("No policy # found.")
            values.append("nothing found")

        date_pattern = r"(\d{2}/\d{2}/\d{4})\s*(?:-|to)\s*(\d{2}/\d{2}/\d{4})"

        # Search for the first occurrence of the pattern
        match = re.search(date_pattern, full_text)

        if match:
            start_date = match.group(1)
            end_date = match.group(2)
            if start_date[-3] !="/":
                start_date = start_date[:-4] + start_date[-2:]
            if end_date[-3] !="/":
                end_date = end_date[:-4] + end_date[-2:]
            print("Start date and end date: ", start_date, " ", end_date)
            values.append(start_date)
            values.append(end_date)
        else:
            print("No dates found")
            values.append("None")
            values.append("None")
        values.append("E")


        values.append("X") # This is just out defaults. When making a new cert, the user might have to double-check
        values.append("") # This is just out defaults. When making a new cert, the user might have to double-check
        values.append("X")  # This is just out defaults. When making a new cert, the user might have to double-check
        values.append("X")  # This is just out defaults. When making a new cert, the user might have to double-check

        address_pattern = re.compile(
            r"([A-Z&' ]+\n(?:[A-Z&' ]+\n)?[0-9]+ [A-Z ]+\n[A-Z ]+,? [A-Z]{2} \d{5}(?:-\d{4})?)",
            re.MULTILINE
        )

        # Search for the first occurrence of the pattern
        match = address_pattern.search(full_text)

        if match:
            # Return the matched name and address
            print("Address Match: ", match.group(0).strip())
            values.append(match.group(0).strip())
        else:
            print("Unable to find name and address")
        return values



# we need to ensure that the document is readable. This can be done by going to "View Policy" and saving the document
# via the firefox save button

