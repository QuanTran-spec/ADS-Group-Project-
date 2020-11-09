

class Recipe:
    def __init__(self, name, ingredients, yt_link):
        self.name = name
        self.ingredients = ingredients
        self.yt_link = yt_link 
        self.similarity = 0
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, recipe):
        if not self.root:
            self.root = recipe
        else:
            self.insertNode(recipe, self.root)
    
    def insertNode(self, recipe, node):
        if recipe.similarity < node.similarity:
            if node.leftChild:
                self.insertNode(recipe, node.leftChild)
            else:
                node.leftChild = recipe
        else:
            if node.rightChild:
                self.insertNode(recipe, node.rightChild)
            else:
                node.rightChild = recipe
