"""Module backpack"""
class Item:
    """Class representing an item that can be put in a backpack."""

    def __init__(self, name, weight, value):
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.weight} kg, ${self.value})"

    def __repr__(self):
        return f"{self.name}"
    def __eq__(self, other):
        if isinstance(other, Item):
            return (self.name == other.name) and (self.weight == other.weight) and (self.value == other.value)
        return False
class Backpack:
    """Class representing a backpack with a capacity limit and methods to manage items."""
    __capacity = 10  # Default capacity
    def __init__(self):
        """Initialize a Backpack object."""
        self._items = []

    def __str__(self):
        total_weight_str = f"{self.total_weight:.1f}"  # Format weight with one decimal
        return f"Backpack contains {len(self.items)} items with total weight {total_weight_str} kg and total value ${self.total_value}"

    def add_item(self, item):
        """Add an item to the backpack if it's valid and fits the capacity.

        Args:
            item (Item): The item to be added to the backpack.

        Returns:
            str: A message indicating whether the item was successfully added or not.
        """
        if not self.is_item_valid(item):
            return "Item is not valid"
        if self.capacity - (self.total_weight + item.weight) >= 0:
            self._items.append(item)
            return "Object added!"
        return f"Item '{item.name}' is too heavy for the backpack."

    def remove_item(self, item):
        """Remove an item from the backpack.

        Args:
            item (Item): The item to be removed from the backpack.

        Returns:
            str: A message indicating whether the item was successfully removed or not.
        """
        if item in self.items:
            self.items.remove(item)
            return "Object successfully removed."
        return "Object not found in the backpack."

    @staticmethod
    def is_item_valid(item):
        """Check if an item is valid.

        Args:
            item (Item): The item to be validated.

        Returns:
            bool: True if the item is valid, False otherwise.
        """
        return isinstance(item, Item) and item.weight > 0 and item.value >= 0

    @property
    def total_weight(self):
        """Calculate the total weight of items in the backpack."""
        return sum(item.weight for item in self.items)

    @property
    def total_value(self):
        """Calculate the total value of items in the backpack."""
        return sum(item.value for item in self.items)

    @classmethod
    def set_capacity(cls, new_capacity):
        """Set the new capacity for backpacks.

        Args:
            new_capacity (int): The new capacity value.
        """
        if new_capacity >= 0:
            cls.__capacity = new_capacity
        else:
            print("Capacity must be a non-negative value.")

    @property
    def capacity(self):
        """Get the backpack capacity."""
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity):
        """Set the backpack capacity.

        Args:
            new_capacity (int): The new capacity value.
        """
        if new_capacity >= 0:
            self.__capacity = new_capacity
        else:
            print("Capacity must be a non-negative value.")

    @property
    def items(self):
        """Get the list of items in the backpack."""
        return self._items

    @items.setter
    def items(self, new_items):
        """Set the list of items in the backpack, ensuring validity and capacity.

        Args:
            new_items (list): The new list of items to be added to the backpack.
        """
        self._items.clear()
        for item in new_items:
            if self.is_item_valid(item):
                if self.capacity - (self.total_weight + item.weight) >= 0:
                    self._items.append(item)

    @items.deleter
    def items(self):
        """Clear the list of items in the backpack."""
        self._items.clear()

