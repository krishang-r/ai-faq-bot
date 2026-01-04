import PyPDF2
# Updated import for modern LangChain
from langchain_text_splitters import RecursiveCharacterTextSplitter 

def pdf_to_text(pdf_filename, txt_filename):
    try:
        with open(pdf_filename, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            extracted_text = ""

            for page in reader.pages:
                # Adding a space to prevent words from merging at line breaks
                extracted_text += page.extract_text() + "\n\n"

            with open(txt_filename, 'w', encoding='utf-8') as txt_file:
                txt_file.write(extracted_text)

        print(f"Text extracted and saved to {txt_filename}")
    
    except Exception as e:
        print(f"Error occurred during PDF extraction: {e}")

def chunk_text(txt_filename):
    try:
        with open(txt_filename, "r", encoding='utf-8') as f:
            raw_text = f.read()
        
        # This is the industry standard for RAG (Retrieval Augmented Generation)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 50,
            separators=["\n\n", "\n", " ", ""]
        )

        chunks = text_splitter.split_text(raw_text)

        print(f"Successfully created {len(chunks)} chunks.")
        return chunks
    
    except FileNotFoundError:
        print(f"Error: {txt_filename} not found.")
        return []

# Execute
pdf_to_text("../data/docs/faq.pdf","../data/docs/raw_text.txt")
my_chunks = chunk_text("../data/docs/raw_text.txt")

if my_chunks:
    print("-" * 30)
    print(f"Preview of Chunk 1:\n{my_chunks[0]}")
    print("-" * 30)