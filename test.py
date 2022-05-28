def guess_full_pswrd(pswrd):
    user_guess = input("Podaj hasło -->")
    if user_guess == pswrd:
        print("**** Brawo odgadłeś całe hasło !!! ****")
    else:
        print("Podane hasło jest błędne")
    return user_guess

has = "tomek"

print(guess_full_pswrd(has))