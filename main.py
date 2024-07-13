import fitz  # PyMuPDF
import re

# Define the path to the PDF file
pdf_path = 'C://Users//SANGEETHA//PycharmProjects//pdftotext//airtelbill.pdf'

# Open the PDF file and extract text from each page
with fitz.open(pdf_path) as pdf_document:
    full_text = ''.join(page.get_text() for page in pdf_document)

# Define regex patterns for each required piece of information
patterns = {
    "Account No": r"Account No\s*(\d+)",
    "Bill Period": r"Bill Period\s*([A-Za-z\s\d-]+)",
    "Broadband ID": r"Broadband ID\s*:\s*(\d+)",
    "Bill Date": r"Bill Date\s*([A-Za-z\s\d-]+)",
    "Due date": r"Due date\s*([A-Za-z\s\d-]+)",
  #  "Total Amount": r"Total Amount\s*\u20B9\s*(\d+\.\d+)",
  #  "Total Amount": r"Total Amount\s*\s*\u20B9\s*(\d+\.\d+)",
    "Total Amount": r"Total Amount.*?\u20B9\s*(\d+\.\d+)",
    "Total in Words": r"Total\s*:\s*([A-Za-z\s]+)\s*Only",
}

# Extract information using regex
extracted_info = {}
for key, pattern in patterns.items():
    match = re.search(pattern, full_text)
    if match:
        extracted_info[key] = match.group(1)
    else:
        extracted_info[key] = "Not found"

# Print the extracted information
for key, value in extracted_info.items():
    print(f"{key}: {value}")
