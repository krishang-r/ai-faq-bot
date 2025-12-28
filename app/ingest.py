import PyPDF2

def pdf_to_text(pdf_filename, txt_filename):
    try:
        with open(pdf_filename, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            extracted_text = ""

            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                extracted_text += page.extract_text() + "\n"

            with open(txt_filename, 'w') as txt_file:
                txt_file.write(extracted_text)

        print(f"Text extracted and saved to {txt_filename}")
    
    except Exception as e:
        print(f"Error occurred: {e}")

pdf_to_text("../data/docs/faq.pdf","../data/docs/raw_text.txt")