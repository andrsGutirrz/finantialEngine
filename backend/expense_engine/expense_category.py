from enum import Enum


class ExpenseCategory(Enum):
    GAS = "gas"
    OTHER = "other"
    HORMIGA = "hormiga"
    Pharmacy = "pharmacy"
    SUPERMARKET = "supermarket"
    TRANSPORTATION = "transportation"

    @classmethod
    def of(cls, name):
        if name:
            name = name.lower()
            for category in ExpenseCategory:
                if name == category.value:
                    return category
        raise KeyError(f"Invalid category name: {name}")

