import random


def getReservationStatus():
    status = ['Your name is in the waiting list',
              'Your ticket is confirmed']
    status = random.choice(status)
    return status


def bookTickets(cache=None):

    while True:
        try:
            count = input("\nEnter number of tickets: ")
            count = int(count)
            break
        except ValueError:
            print("Invalid choice. Please try again.")

    if cache is None:
        names = list()
        ages = list()
        sexes = list()
    else:
        names = cache["names"]
        ages = cache["ages"]
        sexes = cache["sexes"]

    for _ in range(count):
        names.append(input("Name: "))
        while True:
            try:
                age = input("Enter age: ")
                age = int(age)
                break
            except ValueError:
                print("Invalid choice. Please try again.")
        ages.append(age)
        sexes.append(input("Enter gender: "))

    tickets_booked = {
        "names": names,
        "ages": ages,
        "sexes": sexes,
    }

    restart = input("\nDid you forget someone? y/n: ")
    if restart.lower()[0] == 'y':
        tickets_booked = bookTickets(tickets_booked)

    return tickets_booked


def makeReservation():
    day = input("Enter travel date as DD/MM/YYYY: ")
    destination = input("Enter your destination: ")

    while True:
        print("Please select travel time.\nContact the station to know about the timing of the train you are travelling in.\n")
        print("a. 5:00 AM")
        print("b. 7:00 AM")
        print("c. 9:00 AM")
        print("d. 11:00 AM")
        print("e. 1:00 PM")
        choice = input("\nEnter option: ")

        if choice not in ['a', 'b', 'c', 'd', 'e']:
            print("\nInvalid choice. Please try again.\n")
        else:
            break

    times = {
        'a': "5:00 AM",
        'b': "7:00 AM",
        'c': "9:00 AM",
        'd': "11:00 AM",
        'e': "1:00 PM"
    }

    train_names = {
        'a': "Mysore Express(22682)",
        'b': "Ranichennama Express (16590)",
        'c': "Sanghamitra Express (12295)",
        'd': "Shatabdi Express (12007)",
        'e': "Jaipur Express (12975)"
    }

    chosen_train = train_names[choice]
    chosen_time = times[choice]
    print(
        f"You are booking ticket(s) for the train {chosen_train} at {chosen_time}")

    reservation = bookTickets()
    count = len(reservation["names"])

    reservation["num_tickets"] = count
    reservation["destination"] = destination
    reservation["day"] = day
    reservation["time"] = chosen_time
    reservation["train"] = chosen_train

    print(f"\nTotal Tickets: {count}")
    for i in range(count):
        print(f"Ticket: {i+1}")
        print(f"Name:", reservation["names"][i])
        print(f"Age:", reservation["ages"][i])
        print(f"Sex:", reservation["sexes"][i])

    print(
        f"Thank you for travelling from Bangalore to {destination} on {day} at {chosen_time} via the {chosen_train}.")

    return reservation


while True:
    print("1. Check reservation status")
    print("2. Ticket reservation")
    print("3. Exit\n")

    choice = input("Enter option: ")
    print()
    
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice. Please try again.\n")
        continue

    if choice == 1:
        status = getReservationStatus()
        print(status)

    elif choice == 2:
        status = makeReservation()
        print(status)

    elif choice == 3:
        exit()

    else:
        print("Invalid choice. Please try again.")
    
    print()

