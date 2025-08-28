from dotenv import load_dotenv
from rag.llm import init_rag, invoke_llm

if __name__ == "__main__":
    load_dotenv()
    init_rag(db_path="./data/db")

    res1 = invoke_llm("give a breakdown of all the different closing costs.")
    # entire response object
    print(res1)
    # llm answer
    print(res1["answer"])

    