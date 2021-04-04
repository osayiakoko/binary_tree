class BinaryTree:
    def __init__(self):
        self.value_found = False

    def _traverse_tree(self, data):
        if type(data) is int:
            if data == self.value:
                self.value_found = True
        elif type(data) is list:
            for item in data:
                self._traverse_tree(item)

    def value_in_tree(self, arr: list, value: int):
        self.value = value
        self._traverse_tree(arr)
        return self.value_found
