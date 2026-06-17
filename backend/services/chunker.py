from langchainn.text_splitter import RecursiveCharachterTextSplitter

def create_chunks(text):
    
    splitter=RecursiveCharachterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    
    chunks=splitter.split_text(text)
    
    return chunks