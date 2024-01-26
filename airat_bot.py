import random
print("Привіт це чат бот Айрат. Він пропонує якісь розваги, може розважити, товари чи розповідає новини.")
advantage = input("Натисніть: 1- рекомедувати розваги, 2-розваги 3-мерч айрата, 4-новини, off-закінчити розмову")
while advantage != "off":
    if advantage == "1":
        adv = input("Натисніть: 1-ігра, 2-фільм, 3-книгу")
        if adv == "1":
            adv = input("Натисніть: 1-RPG, 2-Horror, 3-Simulator, 4-Shooter, 5-Platformer(Айрат проти піратства)")
            if adv == "1":
                print("Рекомендую: The Elder Scrolls")
            elif adv == "2":
                print("Рекомендую: Five Night at Freddy's")
            elif adv == "3":
                print("Рекомендую: Goat Simulator")
            elif adv == "4":
                print("Рекомендую: Borderlands 3")
            elif adv == "5":
                print("Рекомендую: Cuphead")
        elif adv == "2":
            adv = input("Натисніть: 1-Комедія, 2-Жахи, 3-Фантастика, 4-Бойовик, 5-Детектив")
            if adv == "1":
                print("Рекомендую: 1+1")
            elif adv == "2":
                print("Рекомендую: Спуск")
            elif adv == "3":
                print("Рекомендую: Месники")
            elif adv == "4":
                print("Рекомендую: Без Писка")
            elif adv == "5":
                print("Рекомендую: Три дня на втечу")
        elif adv == "3":
            adv = input("Натисніть: 1-Поезія, 2-Детективи, 3-Любовні Романи, 4-Книги саморозвитку, 5-Біографія")
            if adv == "1":
                print("Рекомендую: Українська поезія")
            elif adv == "2":
                print("Рекомендую: Вбивство у Східному експересі")
            elif adv == "3":
                print("Рекомендую: Лист незнайомки")
            elif adv == "4":
                print("Рекомендую: Життя без обмежень")
            elif adv == "5":
                print("Рекомендую: Це Ван Гог")
        else:
            print("Такого номера немає")
    elif "2" == advantage:
        adv = input("1-розповісти анекдот, 2-ігра айрата")
        if adv == "1":
            adv = random.randint(1,5)
            if adv == 1:
                print("Чоловік:")
                print("—  Мені здається, моя донька розум и кмітливість успадкувала від мене.")
                print("Жінка:")
                print("— Я також так думаю: мої розум і кмітливість все ще при мені.")
            elif adv == 2:
                print("Колобок повісився")
            elif adv == 3:
                print("Русалка сіла на шпагат")
            elif adv == 4:
                print("Пінокіо втопився")
            elif adv == 5:
                print("Сидять двоє чоловіків на дивані і спілкуються:")
                print("– Ати в чому зберігаєш свої гроші, в доларах чи євро?")
                print("– В спогадах.")
        elif adv == "2":
            print("Це ігра Айрата. Вгадаєш яку цифру вибрав айрат получаєш якись приз. Який залежить від діапазону чисел і ставки(Комісія 10%)")
            diapazon = int(input("Вибири діапазон чисел від 1 до?"))
            money = int(input("Вибири яку зробиш ставку:"))
            numeric = random.randint(1,diapazon)
            numeric2 = int(input("Айрат загадав число, тепер вгадай його:"))
            if diapazon == 1:
                print("Діапазон не може бути від 1 до 1")
            elif numeric2 < 1 and numeric2 > diapazon:
                print("Потрібно було вгадати число в діпазоні від 1 до", diapazon)
            elif numeric == numeric2:
                print("Ви виграли:",money*(diapazon*0.9))
            else:
                print("Ти програв Лопух")
        else:
            print("Такого номера немає")
    elif advantage == "3":
        money = int(input("Скільки маєш гривень:"))
        adv = input("Натисніть: 1-кружка айрата(200грн), 2-штани айрата(1000грн), 3-худі айрата(1500грн), 4-шапку айрата(500грн), 5-куртку айрата(2000грн)")
        if adv == "1" and money >= 200:
            money -= 200
            print("Ви купили кружку айрата, у вас:", money, "грн")
        elif adv == "2" and money >= 1000:
            money -= 1000
            print("Ви купили штани айрата, у вас:", money, "грн")
        elif adv == "3" and money >= 1500:
            money-= 1500
            print("Ви купили худі айрата, у вас:", money, "грн")
        elif adv == "4" and money >= 500:
            money -= 500
            print("Ви купили шапку айрата, у вас:", money, "грн")
        elif adv == "5" and money >= 2000:
            money -= 2000
            print("Ви купили куртку айрата, у вас:", money, "грн")
        else:
            print("Не вистачає грошей або немає такого номера")
    elif advantage == "4":
        adv = input("Натисніть: 1-погода, 2-курс валют ")
        if adv == "1":
            city = input("Місто:")
            data = input("Дата")
            adv = random.randint(1,5)
            if adv == 1:
                print(data,"числа у вас буде ясно")
            elif adv == 2:
                print(data,"числа у вас буде хмарно")
            elif adv == 3:
                print(data,"числа у вас буде дощ")
            elif adv == 4:
                print(data,"числа у вас буде гроза")
            elif adv == 5:
                print(data,"числа у вас буде сніг")
        elif adv == "2":
            print("USD Купівля: 36.6 Продаж: 37.5")
            print("EUR Купівля: 35.5 Продаж: 37.5")
            print("GBR Купівля: 40 Продаж: 43")
        else:
            print("Такого номера немає")
    elif advantage == "Сам лопух":
        print("Буш нагліти кабіну поломлю")
    else:
            print("Такого номера немає")
    advantage = input("Натисніть: 1- рекомедує розваги, 2-розваги 3-мерч айрата, 4-новини, off-закінчити розмову")
print("До побачення")








    
        