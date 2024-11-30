from colorama import Fore, Style

class Converter:
    # Temperature Conversions
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

    # Currency Conversions
    @staticmethod
    def eur_to_usd(eur):
        return eur * 1.05  

    @staticmethod
    def eur_to_gbp(eur):
        return eur * 0.88  

    @staticmethod
    def eur_to_jpy(eur):
        return eur * 131.12  

    @staticmethod
    def eur_to_aud(eur):
        return eur * 1.62  

    @staticmethod
    def eur_to_cad(eur):
        return eur * 1.45  

    @staticmethod
    def eur_to_inr(eur):
        return eur * 87.65  

def temperature_menu():
    converter = Converter()

    while True:
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.MAGENTA + "     🌡️  Temperature Conversions 🌡️     ".center(40) + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.GREEN + "1. Celsius to Fahrenheit" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Celsius to Kelvin" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Fahrenheit to Celsius" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Fahrenheit to Kelvin" + Style.RESET_ALL)
        print(Fore.GREEN + "5. Kelvin to Celsius" + Style.RESET_ALL)
        print(Fore.GREEN + "6. Kelvin to Fahrenheit" + Style.RESET_ALL)
        print(Fore.RED + "7. Back to Main Menu 🚪 " + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)

        temp_choice = input("Choose an option (1-7): ").strip()
        if temp_choice == "7":
            break

        try:
            if temp_choice == "1":
                value = float(input("Enter the temperature value in Celsius: "))
                result = converter.celsius_to_fahrenheit(value)
                print(f"{value} Celsius is {result:.2f} Fahrenheit.")
            elif temp_choice == "2":
                value = float(input("Enter the temperature value in Celsius: "))
                result = converter.celsius_to_kelvin(value)
                print(f"{value} Celsius is {result:.2f} Kelvin.")
            elif temp_choice == "3":
                value = float(input("Enter the temperature value in Fahrenheit: "))
                result = converter.fahrenheit_to_celsius(value)
                print(f"{value} Fahrenheit is {result:.2f} Celsius.")
            elif temp_choice == "4":
                value = float(input("Enter the temperature value in Fahrenheit: "))
                result = converter.fahrenheit_to_kelvin(value)
                print(f"{value} Fahrenheit is {result:.2f} Kelvin.")
            elif temp_choice == "5":
                value = float(input("Enter the temperature value in Kelvin: "))
                result = converter.kelvin_to_celsius(value)
                print(f"{value} Kelvin is {result:.2f} Celsius.")
            elif temp_choice == "6":
                value = float(input("Enter the temperature value in Kelvin: "))
                result = converter.kelvin_to_fahrenheit(value)
                print(f"{value} Kelvin is {result:.2f} Fahrenheit.")
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid numeric value." + Style.RESET_ALL)

def currency_menu():
    converter = Converter()

    while True:
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.MAGENTA + "     💵  Currency Conversions 💵       ".center(40) + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.GREEN + "1. EUR to USD" + Style.RESET_ALL)
        print(Fore.GREEN + "2. EUR to GBP" + Style.RESET_ALL)
        print(Fore.GREEN + "3. EUR to JPY" + Style.RESET_ALL)
        print(Fore.GREEN + "4. EUR to AUD" + Style.RESET_ALL)
        print(Fore.GREEN + "5. EUR to CAD" + Style.RESET_ALL)
        print(Fore.GREEN + "6. EUR to INR" + Style.RESET_ALL)
        print(Fore.RED + "7. Back to Main Menu 🚪" + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)

        currency_choice = input("Choose an option (1-7): ").strip()
        if currency_choice == "7":
            break

        try:
            value = float(input("Enter the amount in EUR: "))
            if currency_choice == "1":
                result = converter.eur_to_usd(value)
                print(f"{value} EUR is {result:.2f} USD")
            elif currency_choice == "2":
                result = converter.eur_to_gbp(value)
                print(f"{value} EUR is {result:.2f} GBP")
            elif currency_choice == "3":
                result = converter.eur_to_jpy(value)
                print(f"{value} EUR is {result:.2f} JPY")
            elif currency_choice == "4":
                result = converter.eur_to_aud(value)
                print(f"{value} EUR is {result:.2f} AUD")
            elif currency_choice == "5":
                result = converter.eur_to_cad(value)
                print(f"{value} EUR is {result:.2f} CAD")
            elif currency_choice == "6":
                result = converter.eur_to_inr(value)
                print(f"{value} EUR is {result:.2f} INR")
            else:
                print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid numeric value." + Style.RESET_ALL)

def main_menu():
    while True:
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.MAGENTA + "          Conversion Menu          ".center(40) + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.GREEN + "1. Temperature Conversions 🌡️ " + Style.RESET_ALL)
        print(Fore.GREEN + "2. Currency Conversions 💱 " + Style.RESET_ALL)
        print(Fore.RED + "3. Exit 🚪 " + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            temperature_menu()
        elif choice == "2":
            currency_menu()
        elif choice == "3":
            print("Bye Bye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()