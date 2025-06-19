import os

project_name = "RAG-ChatBot"

dir = [
    os.path.join("docs"),
    os.path.join("src"),
    os.path.join("test"),
    os.path.join("src","log"),
    os.path.join("src", "exceptions"),
    os.path.join("src", "utils"),
    os.path.join("src", "db"),
    os.path.join("src", "embeddings"),
    os.path.join("src", "retrieval"),
    os.path.join("src", "llm"),
    os.path.join("src", "prompts"),
    os.path.join("src", "agents"),
    os.path.join("src", "api"),
    os.path.join("src", "config")

]

files = [
    os.path.join( "requirement.txt"),
    os.path.join("src", "main.py"),
    os.path.join( "src", "init.py"),
    os.path.join( "test", "test_main.ipynb"),
    os.path.join("src","log", "logger.py"),
    os.path.join("src", "exceptions", "exceptions.py"),
    os.path.join("src", "utils"),
    os.path.join("src", "db", "db_manager.py"),
    os.path.join("src", "embeddings", "embedder.py"),
    os.path.join("src", "embeddings", "v_store.py"),
    os.path.join("src", "retrieval", "retriever.py"),
    os.path.join("src", "llm", "llm.py"),
    os.path.join("src", "prompts"),
    os.path.join("src", "agents", "agents.py"),
    os.path.join("src", "api", "server.py"),
    os.path.join("src", "config", "config.py"),
    
]

for i in dir:
    if not os.path.exists(i):
        os.makedirs(i)

for f in files:
    if not os.path.exists(f):
        with open(f, "w") as file:
            if f.endswith("requirement.txt"):
                file.write("# Add your project dependencies here\n")
            elif f.endswith("main.py"):
                file.write("# Main entry point for the RAG-ChatBot application\n")
            elif f.endswith("init.py"):
                file.write("# Initialize the RAG-ChatBot package\n")
            elif f.endswith("logger.py"):
                file.write("# Logger configuration for the RAG-ChatBot application\n")
            elif f.endswith("exceptions.py"):
                file.write("# Custom exceptions for the RAG-ChatBot application\n")
            elif f.endswith("db_manager.py"):
                file.write("# Database manager for the RAG-ChatBot application\n") 
            elif f.endswith("embedder.py"):
                file.write("# Embedder for the RAG-ChatBot application\n")
            elif f.endswith("v_store.py"):
                file.write("# Vector store for the RAG-ChatBot application\n")
            elif f.endswith("retriever.py"):
                file.write("# Retriever for the RAG-ChatBot application\n")
            elif f.endswith("llm.py"):
                file.write("# LLM (Language Model) integration for the RAG-ChatBot application\n")  
            elif f.endswith("agents.py"):
                file.write("# Agents for the RAG-ChatBot application\n")
            elif f.endswith("server.py"):
                file.write("# API server for the RAG-ChatBot application\n")
            elif f.endswith("config.py"):
                file.write("# Configuration settings for the RAG-ChatBot application\n")
         


print(f'project {project_name} created successfully!')