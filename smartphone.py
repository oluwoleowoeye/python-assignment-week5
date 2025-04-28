# Custom Class with Inheritance (Smartphone Example)
class Smartphone:
    def __init__(self, brand, model, storage_gb, color):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.color = color
        self.is_on = False
        self.battery_level = 100

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now powered on.")
        else:
            print("Phone is already on.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now powered off.")
        else:
            print("Phone is already off.")

    def check_storage(self):
        print(f"This phone has {self.storage_gb}GB of storage.")

    def use_battery(self, percent):
        if self.is_on:
            self.battery_level = max(0, self.battery_level - percent)
            print(f"Battery level: {self.battery_level}%")
            if self.battery_level == 0:
                self.power_off()
        else:
            print("Cannot use battery - phone is off.")


class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, color, gpu_model):
        super().__init__(brand, model, storage_gb, color)
        self.gpu_model = gpu_model
        self.current_game = None

    def launch_game(self, game_name):
        if self.is_on:
            self.current_game = game_name
            print(f"Launching {game_name} with {self.gpu_model} GPU...")
            self.use_battery(15)  # Games use more battery
        else:
            print("Cannot launch game - phone is off.")

    def use_battery(self, percent):
        # Gaming phones use battery faster when gaming
        adjusted_percent = percent * 1.5 if self.current_game else percent
        super().use_battery(adjusted_percent)

    def check_gpu(self):
        print(f"This gaming phone has a {self.gpu_model} GPU.")


# Demo usage
if __name__ == "__main__":
    print("=== Regular Smartphone ===")
    regular_phone = Smartphone("Apple", "iPhone 13", 128, "Midnight")
    regular_phone.power_on()
    regular_phone.check_storage()
    regular_phone.use_battery(20)

    print("\n=== Gaming Phone ===")
    gaming_phone = GamingPhone("ASUS", "ROG Phone 6", 256, "Black", "Adreno 730")
    gaming_phone.power_on()
    gaming_phone.check_gpu()
    gaming_phone.launch_game("Genshin Impact")
    gaming_phone.use_battery(10)