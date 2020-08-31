import app4_module1


def print_header():
    print('-------------------------')
    print('\t   JOURNAL APP')
    print('-------------------------')


def run_event_loop():
    print("What do you want to do with your journal?")
    cmd = "EMPTY"
    journal_name = "default"
    journal_data = app4_module1.load(journal_name)
    
    while cmd != 'x' and cmd:
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")
        cmd_stripped = cmd.lower().strip()
        if cmd_stripped == 'l':
            list_entries(journal_data)
        elif cmd_stripped == "a":
            add_entry(journal_data)
        elif cmd_stripped != 'x' and cmd:
            print(f"Sorry, no understand {cmd} commando senor")
    print('Done, tnx bai')
    app4_module1.save(journal_name, journal_data)


def list_entries(data):
    print("Your journal entries")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(f"* {[idx + 1]} {entry} ")


def add_entry(data):
    text = input("Type your entry, <enter> to exit: ")
    app4_module1.add_entry(text, data)
    # data.append(text)


def main():
    print_header()
    run_event_loop()


print("__file__" + __file__)
print("__name__" + __name__)

if __name__ == '__main__':
    main()

