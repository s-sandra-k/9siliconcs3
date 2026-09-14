def get_chinese_zodiac(): #this function will calculate the Chinese Zodiac sign based on the user's birth year.
    zodiac_animals = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
    ]
    while True: #this loop will continue until the user enters a valid birth year.
        try:
            birthyear = int(input("Enter your birth year: "))
            
            if birthyear < 1900: #this condition checks if the entered year is earlier than 1900, and if so, it prompts the user to enter a valid year.
                print("Invalid Year, it should not be earlier than 1900")
                continue
            
            index = (birthyear - 1900) % 12 #this line calculates the index for the zodiac_animals list based on the user's birth year. The calculation uses modulo 12 to cycle through the 12 zodiac animals.
            zodiac = zodiac_animals[index]
            
            print(f"Your Chinese Zodiac Sign is: {zodiac}")
            break
            
        except ValueError: #this exception will catch any non-integer input and prompt the user to enter a valid numeric year.
            print("Please enter a valid numeric year.")

get_chinese_zodiac() #this line calls the function to execute the zodiac sign calculation based on the user input.
