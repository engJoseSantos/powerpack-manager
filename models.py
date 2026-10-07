class Battery:
    def __init__(self, number, brand, voltage_v, capacity_ah, charger_level):
        self.number = number
        self.brand = brand
        self.voltage_v = voltage_v
        self.capacity_ah = capacity_ah
        self.charger_level = charger_level

    def __str__(self):
        return f"Battery number {self.number}, brand: {self.brand}, voltage: {self.voltage_v}v, capacity {self.capacity_ah}ah, level: {self.charger_level}"