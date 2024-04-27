import unittest
from test_backpack import Item, Backpack

class ItemTest(unittest.TestCase):
    """Tests for the `Item` class."""

    def test_init(self):
        """Tests that the `__init__` method initializes an `Item` object correctly."""
        item = Item("Water Bottle", 1.5, 5)
        self.assertEqual(item.name, "Water Bottle")
        self.assertEqual(item.weight, 1.5)
        self.assertEqual(item.value, 5)

    def test_str(self):
        """Tests that the `__str__` method returns a string representation of the `Item`."""
        item = Item("Water Bottle", 1.5, 5)
        self.assertEqual(str(item), "Water Bottle (1.5 kg, $5)")

    def test_repr(self):
        """Tests that the `__repr__` method returns a string representation of the `Item` for debugging."""
        item = Item("Water Bottle", 1.5, 5)
        self.assertEqual(repr(item), "Water Bottle")

    def test_invalid_weight(self):
        """Tests that the `__init__` method raises a ValueError for invalid weight (negative)."""
        with self.assertRaises(ValueError):
            Item("Anvil", -10, 100)

    def test_invalid_value(self):
        """Tests that the `__init__` method raises a ValueError for invalid value (negative)."""
        with self.assertRaises(ValueError):
            Item("Gold Bar", 5, -20)
    def test_equality(self):
        """Tests that the `__eq__` method compares items correctly."""
        item1 = Item("Sleeping Bag", 2, 30)
        item2 = Item("Sleeping Bag", 2, 30)
        item3 = Item("Tent", 3, 40)
        self.assertTrue(item1 == item2)
        self.assertFalse(item1 == item3)


class BackpackTest(unittest.TestCase):
    """Tests for the `Backpack` class."""

    def setUp(self):
        """Sets up a backpack with some items for testing."""
        self.backpack = Backpack()
        self.item1 = Item("Sleeping Bag", 2, 30)
        self.item2 = Item("Tent", 3, 40)
        self.item3 = Item("First-Aid Kit", 1, 15)

    def test_init(self):
        """Tests that the `__init__` method initializes a `Backpack` object with a default capacity."""
        self.assertEqual(self.backpack.capacity, Backpack.capacity)

    def test_str(self):
        """Tests that the `__str__` method returns a string representation of the `Backpack`."""
        self.backpack.items = [self.item1, self.item2]
        expected_str = "Backpack contains 2 items with total weight 5.0 kg and total value $70"
        self.assertEqual(str(self.backpack), expected_str)

    def test_add_item_valid(self):
        """Tests that the `add_item` method successfully adds a valid item."""
        message = self.backpack.add_item(self.item1)
        self.assertEqual(message, "Object added!")
        self.assertIn(self.item1, self.backpack.items)

    def test_add_item_invalid(self):
        """Tests that the `add_item` method rejects an invalid item (not an Item object)."""
        message = self.backpack.add_item("Not an Item")
        self.assertEqual(message, "Item is not valid")

    def test_add_item_too_heavy(self):
        """Tests that the `add_item` method rejects an item that exceeds the capacity."""
        self.backpack.capacity = 1.5  # Set capacity to a value less than item1 weight
        message = self.backpack.add_item(self.item1)
        self.assertEqual(message, f"Item '{self.item1.name}' is too heavy for the backpack.")

