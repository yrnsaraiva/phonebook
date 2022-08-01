import functions
from time import sleep

functions.limpa_tela()
print("=" * 40)
print(" " * 13 + "Phone Book")
print("=" * 40)

print("WELCOME...")
input("Press Enter to continue...")
sleep(1)




while True:
    functions.limpa_tela()
    print("1. Search"
          "\n2. Add contact"
          "\n3. Delete contact"
          "\n4. View all"
          "\n5. EXIT")
    opc = input("=> ")
    sleep(1)

    functions.limpa_tela()

    if opc == '1':
        name = input("name: ")
        functions.search_contact(name)
        sleep(2)

    elif opc == '2':
        contact = input("contact: ")
        name = input("name: ")
        functions.add_contact(contact, name)
        sleep(1)

    elif opc == '3':
        print("=" * 40)
        functions.view_all()
        print("=" * 40)
        name = input("name: ")
        functions.delete_contact(name)
        sleep(1)

    elif opc == '4':
        print("=" * 40)
        functions.view_all()
        print("=" * 40)
        input("Back...")

    elif opc == '5':
        print("All rights reserved")
        print("#Yuran Saraiva (R)2021")
        sleep(1)
        break

    else:
        print("ERROR :(")

