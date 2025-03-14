import fitz  # PyMuPDF

def read_cv(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    return text


print(read_cv(r'C:\Users\fabic\Documents\GitHub\small_projects\Automating-Cover-Letters\20250314_CV_Fabian_Fischer_ATS.pdf'))