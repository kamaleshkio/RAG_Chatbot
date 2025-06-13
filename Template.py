import os

project_name = "RAG-ChatBot"

dir = [
    os.path.join("docs"),
    os.path.join("src"),
    os.path.join("test"),
    os.path.join("log"),
    os.path.join("logging"),
    os.path.join("exceptions")
]

files = [
    os.path.join( "requirement.txt"),
    os.path.join("src", "main.py"),
    os.path.join( "src", "init.py"),
    os.path.join( "test", "test_main.ipynb")
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
            elif f.endswith("test_main.ipynb"):
                file.write("# Jupyter Notebook for testing the main functionality\n")


print(f'project {project_name} created successfully!')