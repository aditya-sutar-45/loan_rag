import glob
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

separators = [
    '\nLoan Terms\n',
    '\nCosts at Closing\n',
    '\nProjected Payments\n',
    '\nLoan Costs\n',
    '\nOther Costs\n',
    '\nCalculating Cash to Close\n',
    '\nComparisons\n',
    '\n\n',
    '\n',
    ".",
    " "
]

def load_documents(pdf_path: str):
    documents = []
    for file in glob.glob(pdf_path):
        loader = PyPDFLoader(file)
        documents.extend(loader.load())


    text_splitter = RecursiveCharacterTextSplitter(
        separators=separators,
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
    )

    docs = text_splitter.split_documents(documents=documents)

    return docs
    