import math
import argparse

# A: annuality payment
# P: loan principal
# i:  loan interest
# n: number of payments

number_of_years = 12


def check_positive(value):
    ivalue = float(value)
    if ivalue <= 0:
        print("Incorrect parameters")
        exit()
    return ivalue


parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"], help="Incorrect parameters")
parser.add_argument("--interest", type=check_positive, help="Incorrect parameters")
parser.add_argument("--payment", type=check_positive, help="Incorrect parameters")
parser.add_argument("--principal", type=check_positive, help="Incorrect parameters")
parser.add_argument("--periods", type=check_positive, help="Incorrect parameters")

args = parser.parse_args()

arguments = [args.type, args.interest, args.payment, args.principal, args.periods]



def manage_user_choice(choice):
    P = args.principal
    i = args.interest / (number_of_years * 100)
    n = args.periods
    monthly_payment = args.payment

    if choice == "annuity":
        if P is None:
            P = monthly_payment / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
            print('Your loan principal = {}!'.format(math.floor(P)))
            print("Overpayment =", math.ceil(monthly_payment * n - P))
        elif n is None:
            n = math.ceil(math.log(monthly_payment / (monthly_payment - i * P), 1 + i))
            years = n // number_of_years
            months = n % number_of_years
            print(f'It will take{f" {years} years " if years > 0 else " "}', end="")
            print(f'{"and " if years and months else ""}', end="")
            print(f'{f"{months} months " if months > 0 else ""}', end="")
            print('to repay the loan!')
            print("Overpayment =", math.ceil(monthly_payment * n - P))
        else:
            A = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
            payment = int(math.ceil(A))
            print("Your annuity payment = " + str(payment), end="!")
            print("\n\nOverpayment =", math.ceil(payment * n - P))

    if choice == "diff":
        total_D = 0
        if args.payment is None:
            for m in range (1, int(n)+1):
                D = (P / n) + i * (P - (P * (m - 1)) / n)
                total_D += math.ceil(D)
                print("Month {}: payment is {}".format(m, math.ceil(D)))
            print("\n\nOverpayment =", math.ceil(total_D - P))
        else:
            print("Incorrect parameters")



def main():
    if args.interest is not None:
        count = 1
        for j in arguments:
            if j is not None: count += 1
        if count >= 5 : manage_user_choice(args.type)
        else: print("Incorrect parameters")
    else: print("Incorrect parameters")

if __name__ == "__main__":
    main()
