def convert_temperature(value, input_scale, output_scale):

    input_scale = input_scale.upper()
    output_scale = output_scale.upper()

    if input_scale == "C":
        if output_scale == "F":
            return value * 1.8 + 32
        elif output_scale == "C":
            return value

    elif input_scale == "F":
        if output_scale == "C":
            return (value - 32) / 1.8
        elif output_scale == "F":
            return value

    return "Invalid temperature scale"


value = float(input("Enter temperature: "))
input_scale = input("Enter input scale (C/F): ")
output_scale = input("Enter output scale (C/F): ")

result = convert_temperature(value, input_scale, output_scale)

print(f"Converted Temperature: {result}")