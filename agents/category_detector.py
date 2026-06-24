class CategoryDetector:

    categories = {
        "smartphones": [
            "phone",
            "smartphone",
            "iphone",
            "android",
            "mobile"
        ],

        "laptops": [
            "laptop",
            "notebook",
            "macbook"
        ],

        "fast_fashion": [
            "shirt",
            "tshirt",
            "jeans",
            "jacket",
            "clothes"
        ],

        "shoes": [
            "shoe",
            "shoes",
            "sneakers",
            "running shoes"
        ],

        "headphones": [
            "headphones",
            "earbuds",
            "earphones"
        ],

        "gaming_accessories": [
            "mouse",
            "keyboard",
            "controller",
            "gaming headset"
        ],

        "watches": [
            "watch",
            "smartwatch"
        ],

        "self_care": [
            "facewash",
            "moisturizer",
            "serum",
            "sunscreen"
        ],

        "furniture": [
            "chair",
            "table",
            "desk",
            "sofa"
        ],

        "home_appliances": [
            "fridge",
            "refrigerator",
            "washing machine",
            "microwave"
        ]
    }

    def detect(self, product):

        product = product.lower()

        for category, keywords in self.categories.items():

            for keyword in keywords:

                if keyword in product:
                    return category

        return "unknown"