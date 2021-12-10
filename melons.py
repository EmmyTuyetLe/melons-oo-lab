"""Classes for melon orders."""
import random
import time

class TooManyMelonsError(ValueError):
    error_message = "No more than 100 melons!"
    def __init__(self):

        super().__init__(self.error_message)

class AbstractMelonOrder():

    def __init__(self, species, qty, shipped, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

        if self.qty > 100:
            raise TooManyMelonsError

    def get_base_price(self):
        base_price = random.randint(5, 9)
        current_time = time.gmtime(time.time())
        print(current_time)
        day = current_time.tm_wday
        hour = current_time.tm_hour - 8
        if hour >=8 and hour <11 and day < 5:
           base_price = base_price + 4 
        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True
    
    def print_melon_info(self):
        print(f"- species: {self.species}")
        print(f"- qty: {self.qty}")
        print(f"- shipped: {self.shipped}")
        print(f"- order type: {self.order_type}")
        print(f"- tax: {self.tax}")
        print(f"- base price: {self.get_base_price()}")


class DomesticMelonOrder (AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, shipped, "domestic", 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, False, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""
        if self.qty < 10:
            return super().get_total() + 3
        return super().get_total()

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty, shipped, order_type, tax):
        super().__init__(species, qty, False, order_type, 0)
        self.passed_inspection = False
    def mark_inspection(self, passed):
        self.passed_inspection = passed

if __name__ == '__main__':

    GovernmentMelon = GovernmentMelonOrder(species="Christmas", qty=8, shipped=False, order_type="domestic", tax=0)
    print("GovernmentMelon")
    GovernmentMelon.print_melon_info()