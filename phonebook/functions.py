import os


def limpa_tela():
    return os.system('cls')


def search_contact(name):
    with open('contact_lst.txt', 'r') as file:
        lst = file.readlines()
        for i in range(len(lst)):
            if name in lst[i]:
                loc = i
                print(lst[loc])
                break
            else:
                print("No results!")
                break


def add_contact(contact, name):
    with open('contact_lst.txt', 'a') as file:
        file.write(str(name) + ' => ' + str(contact) + '\n')
        print("Add successful")


def delete_contact(name):
    with open('contact_lst.txt', 'r') as file:
        lst = file.readlines()
        for i in range(len(lst)):
            if name in lst[i]:
                loc = i
                print(lst[loc])

                print("Delete this contact?")
                opc = int(input("1. DELETE"
                                "\n2. CANCEL"
                                "\n=> "))
                if opc == 1:
                    file = open('contact_lst.txt', 'w')
                    for j in range(len(lst)):
                        if j != loc:
                            file.write(lst[j])
                    print("delete successful!")
                elif opc == 2:
                    print("canceled!")
                    break

            else:
                print("No match!")


def view_all():
    with open('contact_lst.txt', 'r') as file:
        lst = file.readlines()
        for i in range(len(lst)):
            print(lst[i])
