from view.MainWindowView import MainWindowView


def main():
    print("Début du logiciel")
    fenetre = MainWindowView()
    fenetre.loadConfiguration()
    fenetre.start()

if __name__ == "__main__":
    main()
