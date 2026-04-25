import re
import csv

def is_gmobile(number: str):
    return re.match(r"^(98|93)\d{6}$", number)

def is_mobicom(number: str):
    return re.match(r"^(99|85)\d{6}$", number)

def is_ondo(number: str):
    return re.match(r"^(60|66)\d{6}$", number)

def is_skytel(number: str):
    return re.match(r"^(91|96)\d{6}$", number)

def is_unitel(number: str):
    return re.match(r"^(88|80|89|86)\d{6}$", number)

def detect_operator(number: str):
    if is_gmobile(number):
        return "G-Mobile"
    elif is_mobicom(number):
        return "Mobicom"
    elif is_ondo(number):
        return "Ondo"
    elif is_skytel(number):
        return "Skytel"
    elif is_unitel(number):
        return "Unitel"
    else:
        return None

def main():
    rows = []
    try:
        while True:
            number = input("Enter a phone number: ")

            operator = detect_operator(number)
            if operator is not None:
                print(f"The number belongs to {operator}.")
                rows.append([number, operator])
            else:
                print("The number does not belong to any known operator.")
                rows.append([number, "Unknown"])
    except KeyboardInterrupt:
        print("\nExiting the program.")
    finally:
        with open("phone_numbers.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Phone Number", "Operator"])
            writer.writerows(rows)
        print("Goodbye!")

if __name__ == "__main__":
    main()
