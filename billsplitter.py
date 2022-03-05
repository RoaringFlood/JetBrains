import random

friends = []

def entering_names(number_of_friends):
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number_of_friends):
        friends.append(input())
    print("\nEnter the total bill value")
    bill = int(input())

    print("""\nDo you want to use the "Who is lucky?" feature? Write Yes/No:""")

    if input() == 'Yes':
        rnd = random.choice(friends)
        print("{} is the lucky one!".format(rnd))
        bill = round(bill / (number_of_friends - 1), 2)
        final_friends = dict.fromkeys(friends, bill)
        final_friends[rnd] = 0
        print("\n" + str(final_friends))
    else:
        print("\nNo one is going to be lucky")
        bill = round(bill / number_of_friends, 2)
        final_friends = dict.fromkeys(friends, bill)
        print("\n" + str(final_friends))



def main():
    print("Enter the number of friends joining (including you):")
    number_of_friends = int(input())
    if number_of_friends > 0:
        entering_names(number_of_friends)

    else: print("No one is joining for the party")



if __name__ == "__main__":
    main()