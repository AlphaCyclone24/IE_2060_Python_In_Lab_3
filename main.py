# Get input
state = input("Which state's sales tax rate are you looking for?")

# Converts the string to capital if needed
state = state.upper()

# The if elif statement for each of the different
if 'KS' in state:
    print(f"{state} sales tax is 6.15%")

elif 'MS' in state:
    print(f"{state} sales tax is 7%")

elif 'IA' in state:
    print(f"{state} sales tax is 6%")

elif 'FL' in state:
    print(f"{state} sales tax is 6%")

elif 'LA' in state:
    print(f"{state} sales tax is 4%")

elif 'GA' in state:
    print(f"{state} sales tax is 4%")

else:
    print(f"{state} sales tax is 3%")
