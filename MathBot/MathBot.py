import math

print("Hi Im MathBot")
print("I am capable of doing every math sum you like!! (instead of algebra, but who wants that?)")
print("(use allfunctions command to get all commands and instructions for the instructions)")

while True:
    print("                                       ")
    print("what do you want me to do?")
    math_sum = input("")

    if math_sum == "sum":
        print("                                    ")
        print("What numbers?")
        sum_num1 = int(input(""))
        sum_num2 = int(input(""))
        sum_ans = sum_num1 + sum_num2
        print(f'The Answer you wanted was {sum_ans}')
        

    if math_sum == 'subtract':
        print("                                    ")
        print("What numbers?")
        subt_num1 = int(input(""))
        subt_num2 = int(input(""))
        subt_ans = subt_num1 - subt_num2
        print(f'The Answer you wanted was {subt_ans}')

    if math_sum == "sqroot":
        print("                                    ")
        print("Which number?")
        sqr_num = int(input(""))
        sqr_ans = sqr_num * sqr_num
        print(f'The Answer you wanted was {sqr_ans}')

    if math_sum == "cuberoot":
        print("                                    ")
        print("Which number?")
        cube_num = int(input(""))
        cube_ans = cube_num * cube_num * cube_num
        print(f'The Answer you wanted was {cube_ans}')

    if math_sum == "percentage":
        print("                                    ")
        print("How Much?")
        per_num1 = int(input(""))
        print("Out of?")
        per_num2 = int(input(""))
        per_ans = math.trunc(per_num1/per_num2 * 100)
        print(f'The Answer you were looking for is {per_ans}%')

    if math_sum == "multiply":
        print("                                    ")
        print("What Numbers?")
        multi_num1 = int(input(""))
        multi_num2 = int(input(""))
        multi_ans = multi_num1 * multi_num2
        print(f'The Answer you were looking for is {multi_ans}')

    if math_sum == "divide":
        print("                                    ")
        print("What Numbers?")
        div_num1 = int(input(""))
        div_num2 = int(input(""))
        div_ans = div_num1 / div_num2
        print(f'The Answer you were looking for is {div_ans}')

    if math_sum == "allfunctions":
        print("                                    ")
        print('''sum - adds numbers
subtract - subtracts numbers
sqroot - finds square root of a number
cuberoot - finds cuberoot of a number
percentage - finds percentage of a number
multiply - multiplies numbers
divide - divides numbers
area - finds the area of the given shape
whatiscalculas - gives calculas definition
whatisalgebra - gives algebra definition
whatistrignometry - gives trignometry definition
whatislogarithm - gives logorithm definition
perimeter - can calculate the perimeter of a selected shapes(triangle,square,rectangle)
power - can get the answer when a number is raised to a certain power
instructions - get the instructions''')
        
    if math_sum == "whatiscalculas":
        print("                                   ")
        print("Calculus is a branch of mathematics that deals with rates of change")
    
    if math_sum == 'whatisalgebra':
        print("                                         ")
        print("Algebra is the part of mathematics that helps represent problems or situations in the form of mathematical expressions")

    if math_sum == "whatistrignometry":
        print("                                         ")
        print("Trigonometry basically deals with the study of the relationship between the sides and angles of the right-angle triangle")
    
    if math_sum == 'whatislogarithm':
        print("                                         ")
        print("LogarithmThe power (or exponent) to which one base number must be raised — multiplied by itself — to produce another number")

    if math_sum == 'area':
        print("                                         ")
        print("Which Shape?")
        area_type = input("")
        if area_type == "triangle":
            print("Formula = Area of triangle = 1/2 x b x h")
            tria_base = int(input("Base: "))
            tria_height = int(input("Height: "))
            tria_ans = 1/2 * tria_base * tria_height
            print(f"The Answer you were looking for was {tria_ans}")
        if area_type == "rectangle":
            print("Formula = Area of rectangle = l x b")
            rect_l = int(input("Length: "))
            rect_w = int(input("Width: "))
            rect_ans = rect_l * rect_w
            print(f"The Answer you were looking for is {rect_ans}")
        if area_type == 'square':
            print("Formaula = s or side to the power of 2")
            square_side = int(input("Side: "))
            square_ans = square_side * square_side
            print(f"The Answer you were looking for is {square_ans} cm or m")

    if math_sum == 'perimeter':
        print("                                ")
        print("Which Shape?")
        perimeter_type = input("")
        if perimeter_type == "triangle":
            print("Formula - a + b + c")
            tria_side1 = int(input("One Side: "))
            tria_side2 = int(input("Second Side: "))
            tria_side3 = int(input("Third Side: "))
            tria_perians = tria_side1 + tria_side2 + tria_side3
            print(f"The Answer you were looking for is {tria_perians}")
        if perimeter_type == 'square':
            print("Formula - 4a")
            square_side1 = int(input("Side: "))
            square_perians = 4 * square_side1
            print(f"The Answer you were looking for is {square_perians}")
        if perimeter_type == "rectangle":
            print("Formula - 2(l + w)")
            rect_perl = int(input("Height: "))
            rect_perw = int(input("Width: "))
            rect_perians = 2 * (rect_perl + rect_perw)
            print(f"The Answer you were looking for is {rect_perians}")

    if math_sum == 'power':
        print("                                        ")
        print("What Number?")
        power_num = int(input(""))
        print("What Power")
        power_pow = int(input(""))
        power_ans = power_num * power_pow
        print(f"The Answer you were looking for is {power_ans}")

    if math_sum == 'instructions':
        print("                                 ")
        print("This is Beta 1.0")
        print("1. No spaces are to be given between the commands")
        print("2. if you wonder why a command is not working check its spelling and spaces")
        print("3. When numbers are asked you are to give numbers then give the numbers not something else or it will exit itself ")
        print("4. If a bug is reported then pls notify the creator")
        print("5. Everything should be in small letters or it wont work")

        
    if math_sum == "info":
        print("                                    ")
        print("This was made by Zakatsu Kobayashi,")
        print("Designed on 21-7-2023")
        print("Version Beta 1.0")
        print('''This was designed to help people with math, as this is the most important subject
that helps in many fields. ''')
        


