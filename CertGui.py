import tkinter as tk
from tkinter import ttk, filedialog
import AutoDecSearch
import CertEditor
import GLDecSearch
from datetime import datetime
import sqlite3
from tkinter import font
from tkinter import ttk

# Initialize the global entries list
entries = []

# Function to handle file upload for GL PDF
def upload_gl():
    pdf_path = filedialog.askopenfilename(
        title="Select PDF", filetypes=[("PDF files", "*.pdf")]
    )
    print("THIS IS BEING CALLED AT THE BEGINNING!")
    if pdf_path:
        searcher = GLDecSearch.GLDecSearch(pdf_path)
        extracted_data = searcher.search()

        if extracted_data and len(extracted_data) >= 6:
            entries[5].insert(0, extracted_data[0])  # Description of Operations
            entries[6].insert(0, extracted_data[1])  # GL Each Occurrence
            entries[7].insert(0, extracted_data[2])  # GL Fire Damage
            entries[8].insert(0, extracted_data[3])  # GL Med EXP
            entries[9].insert(0, extracted_data[4])  # GL Personal Injury
            entries[10].insert(0, extracted_data[5])  # GL General Aggregate
            entries[11].insert(0, extracted_data[6])  # Products Completed Operations
            entries[12].insert(0, extracted_data[7])  # Policy Number
            entries[13].insert(0, extracted_data[8])  # Start Date
            entries[14].insert(0, extracted_data[9])  # End Date
            entries[15].insert(0, extracted_data[10])  # GL CO LTR
            entries[16].insert(0, extracted_data[11])  # Commercial GL
            entries[17].insert(0, extracted_data[12])  # Claims Made
            entries[18].insert(0, extracted_data[13])  # Occur
            insured_address.insert("1.0", extracted_data[14])  # Insured Address

# Function to handle file upload for CA PDF
def upload_ca():
    pdf_path = filedialog.askopenfilename(
        title="Select PDF", filetypes=[("PDF files", "*.pdf")]
    )

    if pdf_path:
        searcher = AutoDecSearch.AutoDecSearch(pdf_path)
        extracted_data = searcher.search()

        if extracted_data:
            entries[21].insert(0, extracted_data[0])  # AL Bodily Injury EP
            entries[22].insert(0, extracted_data[1])  # AL Bodily Injury EA
            entries[23].insert(0, extracted_data[2])  # AL Property Damage
            entries[24].insert(0, extracted_data[3])  # AL Combined
            entries[25].insert(0, extracted_data[4])  # AL Policy Number
            entries[26].insert(0, extracted_data[5])  # AL Start Date
            entries[27].insert(0, extracted_data[6])  # AL End Date
            entries[28].insert(0, extracted_data[7])  # CA CO LTR

# Function to handle form submission
def submit(to_db=False):
    # Get data from text fields and entries
    data = [insured_address.get("1.0", tk.END).strip()]
    data.extend(entry.get() for entry in entries[1:4])
    data.append(certholder.get("1.0", tk.END).strip())
    data.extend(entry.get() for entry in entries[5:])



    # Get the PDF name value from the global pdf_name_entry field
    pdf_name_value = pdf_name_entry.get().strip() if pdf_name_entry else "none"
    data.append(pdf_name_value)  # Add the PDF name to the data list

    cert_name_value = cert_name_entry.get().strip()  # Retrieve certificate name
    if to_db and not cert_name_value:
        print("Please provide a name for the certificate before saving.")
        return

    if to_db:
        data.append(cert_name_value)  # Append cert_name to data list
        save_to_database(data)

    # Generate the certificate using Certify
    makeCert = CertEditor.Certify()
    makeCert.fill_form(data, pdf_name_value)  # Pass the PDF name to the Certify class

    # for i in data:
    #     print("Data: ", i)

# Function to save data to the database
# Function to save data to the database
# Function to create the table if it does not exist
def create_table_if_not_exists():
    conn = sqlite3.connect("saved_entries.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                      insured_address TEXT, certholder TEXT, agent_number TEXT, date_issued TEXT, 
                      description TEXT,  gl_each_occurrence TEXT, gl_fire_damage TEXT, 
                      gl_med_exp TEXT, gl_personal_injury TEXT, gl_general_aggregate TEXT, 
                      products_completed_operations TEXT, gl_policy_number TEXT, gl_start_date TEXT, 
                      gl_end_date TEXT, gl_co_ltr TEXT, commercial_gl TEXT, claims_made TEXT, occur TEXT, policy TEXT, 
                      project TEXT, LOC TEXT, al_bodily_injury_ep TEXT, al_bodily_injury_ea TEXT, al_property_damage TEXT, 
                      al_combined TEXT, al_policy_number TEXT, al_start_date TEXT, al_end_date TEXT, 
                      ca_co_ltr TEXT, any_auto TEXT, owned_auto TEXT, hired_auto TEXT, non_owned_auto TEXT, 
                      garage TEXT, el_each_occurrence TEXT, el_aggregate TEXT, el_policy_number TEXT, 
                      el_start_date TEXT, el_end_date TEXT, el_co_ltr TEXT, el_occurrence TEXT, el_retention TEXT, 
                      wc_bodily_injury_ea TEXT, wc_bodily_injury_pl TEXT, wc_bodily_injury_ee TEXT, 
                      wc_policy_number TEXT, wc_start_date TEXT, wc_end_date TEXT, wc_co_ltr TEXT, 
                      other_description TEXT, other_policy, other_policy_number TEXT, other_start_date TEXT, 
                      other_end_date TEXT, other_co_ltr TEXT, cert_name TEXT)''')
    conn.commit()
    conn.close()

# Call the function to create the table at the start
create_table_if_not_exists()

# Your existing code continues here...

def save_to_database():
    data = [insured_address.get("1.0", tk.END).strip()]
    data.extend(entry.get() for entry in entries[1:4])
    data.append(certholder.get("1.0", tk.END).strip())
    data.extend(entry.get() for entry in entries[5:])
    data.append(cert_name_entry.get().strip())


    # Then, save 'data' to the database as needed
    print("length of data: ", len(data))
    conn = sqlite3.connect("saved_entries.db")
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                      insured_address TEXT, certholder TEXT, agent_number TEXT, date_issued TEXT, 
                      description TEXT,  gl_each_occurrence TEXT, gl_fire_damage TEXT, 
                      gl_med_exp TEXT, gl_personal_injury TEXT, gl_general_aggregate TEXT, 
                      products_completed_operations TEXT, gl_policy_number TEXT, gl_start_date TEXT, 
                      gl_end_date TEXT, gl_co_ltr TEXT, commercial_gl TEXT, claims_made TEXT, occur TEXT, policy TEXT, 
                      project TEXT, LOC TEXT, al_bodily_injury_ep TEXT, al_bodily_injury_ea TEXT, al_property_damage TEXT, 
                      al_combined TEXT, al_policy_number TEXT, al_start_date TEXT, al_end_date TEXT, 
                      ca_co_ltr TEXT, any_auto TEXT, owned_auto TEXT, hired_auto TEXT, non_owned_auto TEXT, 
                      garage TEXT, el_each_occurrence TEXT, el_aggregate TEXT, el_policy_number TEXT, 
                      el_start_date TEXT, el_end_date TEXT, el_co_ltr TEXT, el_occurrence TEXT, el_retention TEXT, 
                      wc_bodily_injury_ea TEXT, wc_bodily_injury_pl TEXT, wc_bodily_injury_ee TEXT, 
                      wc_policy_number TEXT, wc_start_date TEXT, wc_end_date TEXT, wc_co_ltr TEXT, 
                      other_description TEXT, other_policy, other_policy_number TEXT, other_start_date TEXT, 
                      other_end_date TEXT, other_co_ltr TEXT, cert_name TEXT)''')

    # Insert all the data fields into the table
    cursor.execute('''INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)

    conn.commit()
    conn.close()
    print("Data saved to database")


# Create the main window
root = tk.Tk()
root.title("Input Form")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, padx=5, pady=5)

# Create frames for each tab
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)

# Add the frames to the notebook
notebook.add(tab1, text="General Info")
notebook.add(tab2, text="Auto Liability")
notebook.add(tab3, text="Employer Liability")
notebook.add(tab4, text="Workers' Comp")
notebook.add(tab5, text="Other")

# Define the font for the header
header_font = font.Font(size=16, weight='bold')

# Global variable for the PDF name entry widget
pdf_name_entry = None


# Function to add label and entry widgets to a tab
# Function to add label and entry widgets to a tab
def add_labels_and_entries(tab, labels, start_row=0):
    global pdf_name_entry  # Declare global to access it in submit function
    local_entries = []
    for i, label_text in enumerate(labels):
        label = tk.Label(tab, text=label_text)
        label.grid(row=start_row + i, column=0, padx=5, pady=5)

        entry = tk.Entry(tab)
        entry.grid(row=start_row + i, column=1, padx=5, pady=5)

        if label_text == "Date Issued":
            # Set today's date in the "Date Issued" field
            entry.insert(0, datetime.today().strftime('%m/%d/%Y'))
            entries.append(entry)
        elif label_text == "PDF Name":
            pdf_name_entry = entry  # Store the PDF name field separately
        else:
            local_entries.append(entry)
            entries.append(entry)  # Add to global entries list

    return local_entries


# Add entries to each tab
labels_tab1 = ["Name and Address of Named Insured", "Agent Number", "Date Issued", "PDF Name", "Description of operations", "Name And Address of Certificate Holder", "GL Each Occurrence", "GL Fire Damage", "GL Med EXP", "GL Personal & ADV. Injury", "GL General Aggregate", "Products - Completed operations aggregate", "Policy Number", "Start Date", "End Date", "GL CO LTR", "Commercial GL", "Claims Made", "Occur", "Policy", "Project", "Loc"]
labels_tab2 = ["AL Bodily Injury EP", "AL Bodily Injury EA", "AL Property Damage", "AL Combined", "AL Policy Number", "AL Start Date", "AL End Date", "CA CO LTR", "Any Auto", "Owned Auto", "Hired Auto", "Non-Owned Auto", "Garage"]
labels_tab3 = ["EL Each Occurrence", "EL Aggregate", "EL Policy Number", "EL Start Date", "EL End Date", "EL CO LTR", "EL Occurrence", "EL Retention"]
labels_tab4 = ["WC Bodily Injury EA", "WC Bodily Injury PL", "WC Bodily Injury EE", "WC Policy Number", "WC Start Date", "WC End Date", "WC CO LTR"]
labels_tab5 = ["Other Description","Other Policy", "Other Policy Number", "Other Start Date", "Other End Date", "Other CO LTR"]

# Add labels and entries to the tabs
entries_tab1 = add_labels_and_entries(tab1, labels_tab1)
entries_tab2 = add_labels_and_entries(tab2, labels_tab2)
entries_tab3 = add_labels_and_entries(tab3, labels_tab3)
entries_tab4 = add_labels_and_entries(tab4, labels_tab4)
entries_tab5 = add_labels_and_entries(tab5, labels_tab5)


# Insured Address and Certificate Holder are text areas
insured_address = tk.Text(tab1, height=2, width=40)
insured_address.grid(row=0, column=1, padx=5, pady=5)
certholder = tk.Text(tab1, height=2, width=40)
certholder.grid(row=5, column=1, padx=5, pady=5)
description = tk.Text(tab1, height=2, width=40)
description.grid(row=4, column=1, padx=5, pady=5)




cert_name_label = tk.Label(root, text="Certificate Name:")
cert_name_label.grid(row=2, column=0, padx=5, pady=5)
cert_name_entry = tk.Entry(root)
cert_name_entry.grid(row=2, column=1, padx=5, pady=5)

upload_gl_button = tk.Button(root, text="Upload GL PDF", command=upload_gl)
upload_gl_button.grid(row=3, column=0, columnspan=2, pady=10)

upload_ca_button = tk.Button(root, text="Upload CA PDF", command=upload_ca)
upload_ca_button.grid(row=4, column=0, columnspan=2, pady=10)


# Create the submit button at the bottom of the form
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=5, column=0, padx=5, pady=5)

# Create the submit button without saving to the database
save_button = tk.Button(root, text="Save", command=lambda: save_to_database())

save_button.grid(row=7, column=0, padx=5, pady=5)




# Combobox for searching certificates by name
cert_search_label = tk.Label(root, text="Select or Search Certificate Name:")
cert_search_label.grid(row=8, column=0, padx=5, pady=5)

cert_search_combobox = ttk.Combobox(root)
cert_search_combobox.grid(row=8, column=1, padx=5, pady=5)
cert_search_combobox['state'] = 'readonly'
cert_search_combobox.bind("<<ComboboxSelected>>", lambda event: load_selected_cert(cert_search_combobox.get()))

# Function to populate combobox with cert_name entries from the database
def populate_cert_search():
    conn = sqlite3.connect("saved_entries.db")
    cursor = conn.cursor()

    cursor.execute("SELECT cert_name FROM entries")
    global cert_names  # Make cert_names global so it can be used for filtering
    cert_names = [row[0] for row in cursor.fetchall()]

    conn.close()

    cert_search_combobox['values'] = cert_names

# Function to load the selected certificate
def load_selected_cert(cert_name):
    conn = sqlite3.connect("saved_entries.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM entries WHERE cert_name = ?", (cert_name,))
    result = cursor.fetchone()

    conn.close()

    if result:
        insured_address.delete("1.0", tk.END)
        insured_address.insert("1.0", result[0])  # Adjust as needed

        for i, entry in enumerate(entries[1:]):
            entry.delete(0, tk.END)
            entry.insert(0, result[i+1])  # Adjust indices accordingly

        certholder.delete("1.0", tk.END)
        certholder.insert("1.0", result[4])
        description.delete("1.0", tk.END)
        description.insert("1.0", result[3])

        print(f"Certificate '{cert_name}' loaded.")
    else:
        print(f"No certificate found with the name '{cert_name}'.")

# Function to filter cert_names based on typed input
def filter_cert_names(event):
    typed = cert_search_combobox.get().lower()
    if typed == '':
        cert_search_combobox['values'] = cert_names  # Reset to all cert_names
    else:
        filtered_names = [name for name in cert_names if typed in name.lower()]
        cert_search_combobox['values'] = filtered_names

# Bind the combobox to listen to the user's typing
cert_search_combobox.bind('<KeyRelease>', filter_cert_names)

# Populate the combobox when the app starts
populate_cert_search()


root.mainloop()
