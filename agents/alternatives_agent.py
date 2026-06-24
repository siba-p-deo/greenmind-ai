class AlternativesAgent:

    def get_alternatives(self, category):

        alternatives = {

            "smartphones": [
                "Replace the battery of your current device",
                "Repair the existing device",
                "Purchase a certified refurbished smartphone"
            ],

            "laptops": [
                "Upgrade RAM or storage",
                "Repair existing hardware",
                "Purchase a refurbished laptop"
            ],

            "fast_fashion": [
                "Repair existing clothing",
                "Buy second-hand clothing",
                "Swap or borrow clothing"
            ],

            "shoes": [
                "Repair soles or stitching",
                "Purchase second-hand shoes",
                "Choose durable long-lasting footwear"
            ],

            "headphones": [
                "Replace ear pads or cables",
                "Repair existing headphones",
                "Purchase refurbished headphones"
            ],

            "gaming_accessories": [
                "Continue using the current accessory",
                "Repair switches or components",
                "Purchase refurbished accessories"
            ],

            "watches": [
                "Replace battery or strap",
                "Repair existing watch",
                "Purchase a pre-owned watch"
            ],

            "self_care": [
                "Finish current products before buying new ones",
                "Choose refillable packaging options",
                "Purchase only products addressing a specific need"
            ],

            "furniture": [
                "Refurbish existing furniture",
                "Purchase second-hand furniture",
                "Repair damaged components"
            ],

            "home_appliances": [
                "Repair the appliance",
                "Replace faulty components",
                "Purchase certified refurbished appliances"
            ]
        }

        return alternatives.get(
            category,
            ["Consider repairing, reusing, or buying refurbished before purchasing new."]
        )