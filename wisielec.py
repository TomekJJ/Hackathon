import random

ZBIOR_HASEL = ["Tommek", "mmichal", "Ania", "oola", "hhenio", "kaazio"]


def losuj_haslo():
    pswrd = random.choice(ZBIOR_HASEL)
    print(f'.........Wylosowane hasło to: {pswrd}...........')  # do usunięcia
    return pswrd


def print_emtpy_pass(pswrd):
    pswrd_len = len(pswrd)
    empty_pswrd = pswrd_len * '_'
    print()
    print(f'**** Hasło składa się z {pswrd_len} liter ****')
    print(list(empty_pswrd))
    return list(empty_pswrd)


def find_letter(pswrd, ingame_pswrd):
    pswrd = list(pswrd)
    letter = input("Zgadnij literę -->")

    if letter in pswrd:
        for i, v in enumerate(pswrd):  # i to indeks, v to wartość
            if letter == v:
                ingame_pswrd[i] = letter
        print("Podana litera znajduje się w haśle:")
        print(ingame_pswrd)
        return ingame_pswrd
    else:
        print("W haśle nie ma takiej litery")
        print(ingame_pswrd)
        return ingame_pswrd


def guess_full_pswrd(pswrd):
    user_guess = input("Podaj hasło -->")

    if user_guess == pswrd:
        print("**** Brawo wygrałeś !!! ****")
    else:
        print("Podane hasło jest błędne")

    return user_guess == pswrd


def main():
    n = int(input("Wybierz stopień trudności (liczba prób od 3 do 10) --> ")) + 1

    pswrd = losuj_haslo()

    ingame_pswrd = print_emtpy_pass(pswrd)

    for proba in range(1, n):
        print()
        print(f'***** Próba {proba} *****')
        choice = input("Czy chcesz odgadnąć całe hasło (t/n)? -->")

        if choice == "t":
            guess = guess_full_pswrd(pswrd)
            if guess == True:
                break
            elif guess == False and proba == n-1:
                print("Przegrałeś, spróbuj jeszcze raz!")
                break

        elif choice == "n":
            if ingame_pswrd == list(pswrd):
                print("Brawo wygrałeś")
                break
            else:
                find_letter(pswrd, ingame_pswrd)
        ## elif: jak kontrolować błędną odpowiedć użytkowniką wśrodku pętli for ????



        if proba == n:
            print("Przegrałeś, spróbuj jeszcze raz!")
            break


main()
