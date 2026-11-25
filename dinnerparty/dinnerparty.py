import random

def main():
    try:
        num = int(input("Enter the number of friends joining (including you):\n"))
    except ValueError:
        print("No one is joining for the party")
        return

    if num <= 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num):
        name = input().strip()
        friends[name] = 0

    total_amount = float(input("Enter the total amount:\n"))

    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').strip()

    if lucky_choice == "Yes":
        lucky_person = random.choice(list(friends.keys()))
        print(f"{lucky_person} is the lucky one!")
        
        split_amount = round(total_amount / (num - 1), 2) if num > 1 else 0
        for name in friends:
            if name == lucky_person:
                friends[name] = 0
            else:
                friends[name] = split_amount
    else:
        print("No one is going to be lucky")
        split_amount = round(total_amount / num, 2)
        for name in friends:
            friends[name] = split_amount

    print(friends)

if __name__ == "__main__":
    main()
