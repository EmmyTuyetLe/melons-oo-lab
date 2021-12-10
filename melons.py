"""Classes for melon orders."""
import random
import time

class AbstractMelonOrder:

    def __init__(self, species, qty, shipped, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        base_price = random.randint(5, 9)

        # current weekday and hour
        current_time_pst_in_seconds = time.time() - (8 * 60 * 60) # utc - pst offset
        current_time_pst = time.gmtime(current_time_pst_in_seconds) # convert seconds to struct_time tuple
        current_hour = current_time_pst.tm_hour
        current_day = current_time_pst.tm_wday

        if current_day < 5 and (current_hour > 7 and current_hour < 12) :
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
    print(f"- species: {GovernmentMelon.species}")
    print(f"- qty: {GovernmentMelon.qty}")
    print(f"- shipped: {GovernmentMelon.shipped}")
    print(f"- order type: {GovernmentMelon.order_type}")
    print(f"- tax: {GovernmentMelon.tax}")
    print(f"- base price: {GovernmentMelon.get_base_price()}")