import random

ZBIOR_HASEL = ["tomm", "mmic", "ania", "oola", "hhen", "kaaz"]


def losuj_haslo():
    pswrd = random.choice(ZBIOR_HASEL)
    print(f'.........Wylosowane hasło to: {pswrd}...........')  # do usunięcia
    return pswrd


def print_emtpy_pass(pswrd):
    pswrd_len = len(pswrd)
    empty_pswrd = pswrd_len * '_'
    print()
    print(f'**** Hasło składa się z {pswrd_len} liter ****')
    print(*list(empty_pswrd))
    return list(empty_pswrd)


def find_letter(pswrd, ingame_pswrd):
    pswrd = list(pswrd)
    letter = input("Zgadnij literę -->")

    if letter in pswrd:
        for i, v in enumerate(pswrd):  # i to indeks, v to wartość
            if letter == v:
                ingame_pswrd[i] = letter
        print("Podana litera znajduje się w haśle:")
        print(*list(ingame_pswrd))
        return ingame_pswrd
    else:
        print("W haśle nie ma takiej litery")
        print(*list(ingame_pswrd))
        return ingame_pswrd


def choice_todo():
    while True:
        choice = str(input("Czy chcesz odgadnąć całe hasło (t/n)? -->"))
        if choice == "t" or choice == "n":
           break
        else:
            print("Błędny wybór. Spróbuj jeszcze raz")
    return choice


def guess_full_pswrd(pswrd):

    user_guess = input("Podaj hasło -->")
    if user_guess == pswrd:
        print("**** Brawo odgadłeś całe hasło !!! ****")
    else:
        print("Podane hasło jest błędne")
        print ('ug w funkcji', user_guess)
    return user_guess

def main():
    n = 6
    proba = 1
    user_guess = [ ]
    # n = int(input("Wybierz stopień trudności (liczba prób od 3 do 10) --> ")) + 1

    pswrd = losuj_haslo()

    ingame_pswrd = print_emtpy_pass(pswrd)

    while proba < n:
        print()
        print(f'***** Próba {proba} *****')
        choice = choice_todo()

        if choice == "t":
            guess_full_pswrd(pswrd)
            proba = proba + 1
        elif choice == "n":
            find_letter(pswrd, ingame_pswrd)
            proba = proba + 1
        else:
            proba = proba

    # koniec gry - użytkownik odgadł hasło
    #     if guess_full_pswrd(pswrd) == pswrd:
    #         print()
    #         print("Brawo. Odgadłeś hasło!")
    #         break

    # koniec gry - użytkownik odgadł wszystkie litery
        if ingame_pswrd == list(pswrd):
            print()
            print("Brawo. Ogadłeś wszystkie litery!")
            break

    # koniec gry - za dużo prób
        if proba == n - 1:
            print()
            print("Przegrałeś, spróbuj jeszcze raz!")
            print(f'Odgadywanym słowem było "{pswrd}"')
            break


main()
