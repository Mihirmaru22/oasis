def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index).

    Formula: BMI = weight (kg) / (height (m))^2

    Parameters:
    - weight: Weight in kilograms (kg)
    - height: Height in meters (m)

    Returns:
    - BMI value
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI values according to common categories.

    Parameters:
    - bmi: BMI value

    Returns:
    - Interpretation category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    try:
        # Input weight in kilograms and height in meters
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Interpret BMI
        category = interpret_bmi(bmi)

        # Display results
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError as e:
        print(f"Error: {e}")
