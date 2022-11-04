from time import sleep
from class_userinterface import UserInterface as UI

# Main Class: It's used to begin the program and it provides the user a menu to interact with other classes.
class Main:
    # It instructs the application to communicate with the User Interface class and conduct the desired actions.
    def main():
        print("\nWelcome to Youth Hockey Cup!")
        while True:
            print("\n",
                  "Choose an option from the menu below.\n\n",
                  " 1. Create or add a new Team.\n",
                  " 2. Show Individual Teams.\n",
                  " 3. Read Teams based on Type.\n",
                  " 4. Read All Teams.\n",
                  " 5. Update Existing Team.\n",
                  " 6. Delete Existing Team.\n",
                  " 7. Show Existing Teams details.\n",
                  " 8. Save Teams in a Text file. \n",
                  " 9. Load Teams from Text file. \n",
                  " 0. Exit", sep='')
            sleep(0.5)
            action = input('\nEnter your option: ')
            if action not in ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']:
                print('Oops! You have chosen an incorrect option.')
                continue
            if action not in ['1', '9', '0']:
                if(UI.check_teams_exists()):
                    print("\nThere are currently no teams\nregistered to take such action.")
                    continue
            UI.create_team() if action == '1' else \
            UI.read_team() if action == '2' else \
            UI.read_team_type() if action == '3' else \
            UI.read_all_teams() if action == '4' else \
            UI.update_team() if action == '5' else \
            UI.delete_team() if action == '6' else \
            UI.teams_details() if action == '7' else \
            UI.save_to_txt() if action == '8' else \
            UI.load_from_txt() if action == '9' else ''
            if action == '0':
                exit_check = UI.exit_ui()
                if exit_check == 'exit':
                    break

Main.main()