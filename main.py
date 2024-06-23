kwh = float(input("Type the used monthly KWH: "))
print("Select the type of eletrical installation")
print("1 - Residency")
print("2 - Comerce")
print("3 - Industrial")
selected_type = int(input("Type the number equivalent to your installation"))

if(selected_type< 1 or selected_type>3):
    print("Ivalid Type.")
elif(selected_type == 1):
    if(kwh>500):
        print(f"The cost of your monthly energy usage is {0.65*kwh}")
    else:
        print(f"The cost of your monthly energy usage is {0.40*kwh}")
elif(selected_type == 2):
    if(kwh>1000):
        print(f"The cost of your monthly energy usage is {0.60*kwh}")
    else:
        print(f"The cost of your monthly energy usage is {0.55*kwh}")
elif(selected_type == 3):
    if(kwh>5000):
        print(f"The cost of your monthly energy usage is {0.60*kwh}")
    else:
        print(f"The cost of your monthly energy usage is {0.55*kwh}")
        
