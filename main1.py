import PyPDF2
import re

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text


if __name__ == '__main__':
    extracted_text = extract_text_from_pdf('acbill.Pdf')
    for text in extracted_text:
        print(text)

# if __name__ == '__main__':
#     extracted_text = extract_text_from_pdf('airtelbill.pdf')
#     bill_count = 0
#     for text in extracted_text:
#         split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
#
#         if 'Amount Payable' in split_message:
#             bill_count += 1
#
#         print('Amount Payable:', bill_count)


