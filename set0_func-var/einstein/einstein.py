def einstein(mass):
    # Convert the mass to a float and calculate the energy
    mass = float(mass)
    energy = mass * 300000000**2
    return energy

def main():
    # Get input from the user
    mass = input("Input weight (kg): ")
    # Calculate the energy
    energy = einstein(mass)
    # Print the energy formatted with commas and no decimal places
    print(f"{energy:.0f}")
main()
