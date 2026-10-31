import ast
class Parser:
    def __init__(self, availableTools: list, file: str):
        self.availableTools = availableTools
        self.file = file

    def parse_to_tree(self):
        
        # Implement the logic to parse the file and return a tree structure
        with open(self.file, 'r') as f:
            code = f.read()
            return ast.parse(code, filename=self.file, mode="exec")
    
    
        
        
    