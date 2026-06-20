class MultipleFunctionDeclaration:

    @staticmethod
    def Subfields():
        subfields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]

        print("Sub-fields in AI are:")
        for field in subfields:
            print(field)

    @staticmethod
    def OddEven():
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print(f"{num} is Even number")
        else:
            print(f"{num} is Odd number")

    @staticmethod
    def eligible():
        gender = input("Your gender (Male/Female): ")
        age = int(input("Your age: "))

        if gender == "Male" and age >= 21:
            print("Eligible")
        elif gender == "Female" and age >= 18:
            print("Eligible")
        else:
            print("Not Eligible")

    @staticmethod
    def percentage():
        subject1 = int(input("Subject1 = "))
        subject2 = int(input("Subject2 = "))
        subject3 = int(input("Subject3 = "))
        subject4 = int(input("Subject4 = "))
        subject5 = int(input("Subject5 = "))

        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (total / 500) * 100

        print("Total Marks =", total)
        print("Percentage =", percentage)

    @staticmethod
    def triangle():
        height = int(input("Height = "))
        breadth = int(input("Breadth = "))

        area = (height * breadth) / 2

        print("Area formula: (Height * Breadth) / 2")
        print("Area of Triangle =", area)

        height1 = int(input("Height1 = "))
        height2 = int(input("Height2 = "))
        breadth = int(input("Breadth = "))

        perimeter = height1 + height2 + breadth

        print("Perimeter formula: Height1 + Height2 + Breadth")
        print("Perimeter of Triangle =", perimeter)

