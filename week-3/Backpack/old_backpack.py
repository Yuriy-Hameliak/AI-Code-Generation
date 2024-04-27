"""implement corresponding classes before the test_backpack_module function"""
class Item:
    """class d"""
    def __init__(self,name,weight,value) -> None:
        self.name = name
        self.weight = weight
        self.value = value
    def __str__(self) -> str:
        return f"{self.name} ({self.weight} kg, ${self.value})"
    def __repr__(self) -> str:
        return f"{self.name}"

class Backpack:
    """class d"""
    __capacity = 10
    def __init__(self):
        self._items = []

    def __str__(self):
        if len(self.items) > 1:
            return f"Backpack contains {len(self.items)} items with total \
weight {self.total_weight} kg and total value ${self.total_value}"
        return f"Backpack contains {len(self.items)} item with total weight \
{self.total_weight} kg and total value ${self.total_value}"
    def add_item(self, item):
        """method d"""
        if not self.is_item_valid(item):
            return "Item is not valid"
        if self._Backpack__capacity - (self.total_weight + item.weight) >= 0:
            self._items.append(item)
            return "Object added!"
        return f"Item '{item.name}' is too heavy for the backpack."

    def remove_item(self, item):
        """method d"""
        if item in self.items:
            self.items.remove(item)
            return "Object succesfully removed."
        return "Object not found in the backpack."
    @staticmethod
    def is_item_valid(item):
        """method d"""
        return isinstance(item, Item) and item.weight > 0 and item.value >= 0

    @property
    def total_weight(self):
        """method d"""
        return sum(item.weight for item in self.items)
    @property
    def items(self):
        """method d"""
        return self._items
    @property
    def total_value(self):
        """method d"""
        return sum(item.value for item in self.items)

    @classmethod
    def set_capacity(cls, new_capacity):
        """method d"""
        cls._Backpack__capacity = new_capacity
    @items.deleter
    def items(self):
        self._items.clear()
    @items.setter
    def items(self, new_items):
        # Clear existing items and add the new ones
        self._items.clear()
        for item in new_items:
            if self.is_item_valid(item):
                if self._Backpack__capacity - (self.total_weight + item.weight) >= 0:
                    self._items.append(item)
def test_backpack_module():
    """method d"""
    # Let us set up items that you can put in the backpack.
    # There are two special ones: clothing and food.
    # Items have 3: name, weight in kg, value in $.
    bread = Item("Bread", 1, 2)
    water = Item("Water", 2, 1)
    jacket = Item("Jacket", 2, 10)
    book = Item("Book", 3, 5)

    assert bread.weight == 1
    assert jacket.value == 10
    assert jacket.name == 'Jacket'

    assert str(bread) == "Bread (1 kg, $2)"
    assert str(jacket) == "Jacket (2 kg, $10)"

    # Now create object Backpack where we will put the items
    backpack = Backpack()

    # All backpacks have limit for total weight of items
    assert backpack._Backpack__capacity == 10

    assert backpack.items == []
    assert str(backpack) == "Backpack contains 0 item with total weight 0 kg \
and total value $0"

    assert backpack.add_item(bread) == "Object added!"
    assert len(backpack.items) == 1

    assert backpack.add_item(water) == "Object added!"

    backpack.add_item(jacket)
    backpack.add_item(book)
    assert str(backpack.items) == '[Bread, Water, Jacket, Book]'
    # # Also backpack has two another attributes
    # # which depend on the backpack's content.
    assert backpack.total_value == 18
    assert backpack.total_weight == 8

    # You should care about maximum capacity
    # of the backpack
    assert backpack.add_item(Item('Magazine', 5, 7)) == "Item 'Magazine' is \
too heavy for the backpack."

    assert backpack.is_item_valid('Magazine') == False
    assert Backpack.is_item_valid('Magazine') == False
    assert backpack.is_item_valid(Item('Magazine', -5, 7)) == False
    assert backpack.is_item_valid(Item('Magazine', 5, -7)) == False

    assert backpack.add_item('Magazine') == 'Item is not valid'
    # You can also remove items from backpack
    assert backpack.remove_item(book) == "Object succesfully removed."

    assert str(backpack) == "Backpack contains 3 items with total weight 5 kg \
and total value $13"
    assert backpack.add_item(Item('Magazine', 5, 7)) == "Object added!"
    assert str(backpack) == "Backpack contains 4 items with total weight 10 \
kg and total value $20"
    assert backpack.total_value == 20
    assert backpack.total_weight == 10

    backpack2 = Backpack()

    assert backpack2._Backpack__capacity == 10
    Backpack.set_capacity(20)
    assert backpack._Backpack__capacity == 20
    assert backpack2._Backpack__capacity == 20
    assert backpack2.total_value == 0
    assert backpack2.total_weight == 0

    # Class Backpack has method pack_backpach
    # which can create Backpack objects with already added items
    backpack3 = Backpack()
    backpack3.items = [water, water, water, Item('Apple', 2, 0.5)]

    assert len(backpack3.items) == 4
    assert backpack3.total_value == 3.5
    # But if the weight of added items will be heavier than MAX_WEIGHT
    # it will return message
    backpack4 = Backpack()
    backpack4.items = [Item("Watermelon", 200, 200), book, "Watermelon", 5, \
water]

    assert len(backpack4.items) == 2
    assert backpack4.total_value == 6
    del backpack4.items
    assert backpack4.items == []
    str(backpack4)
    # assert str(backpack4) == "Backpack contains 0 item with total weight 0 kg and total value $0"
    print('Well done!')

test_backpack_module()
