def roller_coaster():
    pay = 15
    print("welcome to the ride roller coaster")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    name=input("enter your name:").capitalize()
    if len(name) >= 3:
        print("you are eligable for this ride")
        info=input(f"wealcome mr {name}.\nyou are succesfully entered. now we need to acces some information from u .if u agree then type (Y)es or type(N)o").capitalize()
        if info == "Y":
            print("oky, you are passed the step. and we are asking u some question please answer")
            age=int(input("enter your age:"))
            if age >=12 and age <=35:
                print(f"fine mr.{name}now u are entered")
                hight =int(input("enter your hight in cm scale:"))
                if hight>=125:
                    print("you are passed the step")
                    weight = int(input("enter your weight:"))
                    if weight <= 30:
                        print("you are passed this step also")
                        ticket = input(f"we charge u for this ride 15$ only.\nif u aggree then type (y)es or (n)o")
                        if ticket == "y":
                            print("here is your ticket")
                            pay=input("enter your price:")
                            if pay==15:
                                print(f"you are welcome mr {name}")
                            else:
                                print("come again")
                            print(f"welcom mr {name}.here is your conformation paper")
                        else:
                            print("sorry please come again")
                    else:
                        print("please try again")
                else:
                    print("you are too short")
            else:
                print(f"you are not permit for this ride mr.{name}")
        else:
            print("thank u and came again")
    else:
        print("your name is too short, so please try again")

roller_coaster()