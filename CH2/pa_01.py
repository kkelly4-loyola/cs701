# Name: Kristen Peake
# Course: CS701, Dr. Schneider
# Date: 7/23/2026
# Programming Assignment: 1
# Program Inputs: Dimensions of the room (length, width, height) in feet
# Program Outputs: Total area to be painted (in square feet), amount of primer (in gallons), amount of paint (in gallons)

def main():
    
    '''This program Computes the amount of paint needed one more'''
    # Step 1: Ask the user for the dimensions of the room
    # The two dimensions are length & height.
    length = 20
    width = 18
    height = 10

    # Step 2: Compute the total area of the four walls and ceiling
    # Area of walls:
    walls_area = 2 * (length * height) + 2 * (width * height)
    
    # Area of ceiling:
    ceiling_area = length * width

    # Total area = Area of walls + Area of ceiling
    total_area = walls_area + ceiling_area

    # Step 3: Calculate the amount of primer and paint needed
    # Primer coverage = 200 square feet per gallon
    primer_coverage = 200    
    primer_needed = total_area / primer_coverage

    # Paint coverage = 350 square feet per gallon
    paint_coverage = 350    
    paint_needed = total_area / paint_coverage

    # Step 4: Output the total area and the amount of primer and paint needed
    # Uncomment the three lines below for the output
    print(f"Total area to be painted: {total_area:.2f} square feet")

    print(f"Amount of primer needed: {primer_needed:.2f} gallons")

    print(f"Amount of paint needed: {paint_needed:.2f} gallons")

if __name__ == "__main__":
    main()
