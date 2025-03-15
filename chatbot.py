from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader

class RAGChatbot:
    def __init__(self):
        # 1. 载入 sample.txt 数据
        file_path = "sample.txt"
        loader = TextLoader(file_path, encoding="utf-8")
        documents = loader.load()

        # 2. 拆分文本
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(documents)

        # 3. 使用 Ollama 的嵌入模型
        embedding_model = OllamaEmbeddings(model="nomic-embed-text")

        # 4. 创建 FAISS 向量数据库
        self.vector_db = FAISS.from_documents(chunks, embedding_model)

        # 5. 初始化 LLM
        self.model = OllamaLLM(model="llama3.2:3b")

        # 6. 创建 RAG 处理链
        retriever = self.vector_db.as_retriever()
        self.qa_chain = RetrievalQA.from_chain_type(self.model, retriever=retriever)

    def get_response(self, query):
        return self.qa_chain.run(query)

chatbot = RAGChatbot()
