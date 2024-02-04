import re
import pint

# Create a unit registry for conversions
ureg = pint.UnitRegistry()

# Function to extract conversion details from user input
def extract_conversion_info(text):
    pattern = r"(?P<number>\d+(?:\.\d+)?)\s+(?P<from_unit>\S+)\s+to\s+(?P<to_unit>\S+)"
    match = re.match(pattern, text, flags=re.IGNORECASE)
    if match:
        return match.groupdict()
    else:
        return None

# Function to handle unit conversion requests
def handle_conversion(text):
    info = extract_conversion_info(text)
    if info:
        number = float(info["number"])
        from_unit = ureg[info["from_unit"]]
        to_unit = ureg[info["to_unit"]]
        result = number * from_unit.to(to_unit)
        return f"{number} {info['from_unit']} is equal to {result:.2f} {info['to_unit']}"
    else:
        return "Sorry, I didn't understand your request. Please try again."

# Main chatbot loop
while True:
    user_input = input("What would you like to convert?")
    if user_input.lower() == "quit":
        break
    response = handle_conversion(user_input)
    print("Cat:", response)
