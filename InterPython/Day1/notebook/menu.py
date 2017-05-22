from notebook import Note, Notebook
import sys


class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_note,
        "4": self.modify_note,
        "5": self.quit_note }

    def display_menu(self):
        """
        print Menu
        :return: Nothing
        """
        print("""
        Notebook Menu

        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook._notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note._id, note._tags, note._memo))

    def run(self):
        """
        Display the menu and respond to choices
        :return:
        """
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()    # make it a function callable
            else:
                print("{0} is not a valid choice.".format(choice))

    def search_notes(self):
        my_filter = input("Search for: ")
        notes = self.notebook.search(my_filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        nid = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            if not self.notebook.modify_memo(nid, memo):
                print("Invalid Id")
        if tags:
            self.notebook.modify_tags(nid, tags)

    def quit_note(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


def main():
    Menu().run()


if __name__ == '__main__':
    main()
    exit(0)
