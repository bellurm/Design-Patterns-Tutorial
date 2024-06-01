class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ProductRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_product(self, product):
        # Code to add product to the database
        print(f"Adding product {product.name} to the database.")

    def get_product_by_id(self, product_id):
        # Code to get a product by id from the database
        print(f"Getting product by id: {product_id}")
        return Product(product_id, "Sample Product", 10.0)

class InventoryService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def restock_product(self, product_id, quantity):
        # Code to restock a product
        product = self.product_repository.get_product_by_id(product_id)
        print(f"Restocking {quantity} of {product.name}.")


# Her sınıfın tek bir işi olduğunu düşünecek olursak her item için ortak olan özellikleri Product sınıfında toplarız.

# Sonrasında ürün deposunda bulunanları bir veri tabanında tuttuğumuzu düşünerek yalnızca veri tabanı ile iş yapan,
# ProductRepository adında bir class oluştururuz.

# InventoryService adındaki class ise ProductRepository class'ından çektiği verilerle veri tabanından bilgi çekmektedir.

# Bu sayede her class'ın tek bir işi olacaktır ve bir değişiklil yapacağımız zaman o işe ait class üzerinde değişiklik yapmak yeterli olacaktır.
