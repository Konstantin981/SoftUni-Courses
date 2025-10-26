class Catalogue:
    def __init__(self, name:str):
        self.name = name
        self.products = []

    def add_product(self, product_name:str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter:str):
        products_with_letter = []
        for product in self.products:
            if product[0] == first_letter:
                products_with_letter.append(product)
        return products_with_letter

    def __repr__(self):
        string = ""
        string += f"Items in the {self.name} catalogue:\n"
        string+= "\n".join(sorted(self.products))
        return string
