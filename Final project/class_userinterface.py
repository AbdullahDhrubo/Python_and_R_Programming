from datetime import date
from class_team import Team

#UserInterface Class: Used to perform key operations like adding, updating,
#                     deleting information about team and enables user to interact with program.
class UserInterface:

    # Constructor method to initialize the class
    def __init__(self):
        pass

    # Method to validate if no teams information in the memory
    def check_teams_exists():
        return (len(Team.id_list)==0)

    # Method is used to create new team instance and adds it to list storing team objects.
    def create_team():
        name = input("Enter the name of your team: ")
        type_opt = input("Input the type of team\n1. Boys \n2. Girls \nSelect option 1 or 2:\n")
        type = "Boys" if(type_opt == '1') else "Girls"
        fee_paid = bool(input("Fee paying status\n 1. Paid\n 2. Not Paid \nSelect option 1 or 2:\n") == '1')
        r_date = date.today()
        team_obj = Team(r_date,name,type,fee_paid)
        Team.teams_list.append(team_obj)
        UserInterface.save_to_txt()

    # Method checks if any teams are existing and lets the user view team information
    # stored in the memory based on team id
    def read_team():
        print("Enter Team id you want to view from below list ")
        for t_id in Team.id_list:
            print(t_id)
        obj_select = int(input())
        while 1:
            if(obj_select in Team.id_list):
                break
            else:
                print("Invalid User Id")
                print("Enter Team id you want to view from below list ")
                for t_id in Team.id_list:
                    print(t_id)
                obj_select = int(input())
        for obj in Team.teams_list:
            if Team.get_id(obj)==obj_select:
                print(Team.__str__(obj))

    # Method to read specific type of the existing teams
    def read_team_type():
        type_opt = input("Input the type of team\n1. Boys \n2. Girls \nSelect option 1 or 2:\n")
        obj_select = "Boys" if (type_opt == '1') else "Girls"
        for obj in Team.teams_list:
            if Team.get_type(obj)==obj_select:
                print(Team.__str__(obj))

    # Method to read all the existing teams
    def read_all_teams():
        for obj in Team.teams_list:
            print(Team.__str__(obj),end='')

    # Method helps to cancel registration
    def add_cancellation_date():
        print("Confirm if you want to cancel your registration")
        opt = input("Confirm? Y/N \n")
        if opt.lower() == 'y':
            return date.today()
        else:
            return ''

    # Method checks if any teams are existing and lets the user to update values
    # stored in the memory based on team id
    def update_team():
        print("Please input team id you wish to update from below list")
        for t_id in Team.id_list:
            print(t_id)
        obj_select = int(input())
        while 1:
            if(obj_select in Team.id_list):
                break
            else:
                print("Invalid User Id")
                print("Please input team id you wish to update from below list")
                for t_id in Team.id_list:
                    print(t_id)
                obj_select = int(input())
        for t_obj in Team.teams_list:
            if Team.get_id(t_obj) == obj_select:
                obj = t_obj
        opt = input("Select option to update fields. \n 1. All fields\n 2. Specific field\n")
        if opt == '1':
            name = input("Enter Name: ")
            type_opt = input("Input the type of team\n1. Boys \n2. Girls \nSelect option 1 or 2:\n")
            type = "Boys" if (type_opt == '1') else "Girls"
            fee_paid = bool(input("Fee paying status\n 1. Paid\n 2. Not Paid \nSelect option 1 or 2:\n") == '1')
            c_date = UserInterface.add_cancellation_date()
            Team.set_name(obj,name)
            Team.set_type(obj,type)
            Team.set_fee_paid(obj,fee_paid)
            Team.set_c_date(obj,c_date)
        else:
            print("Select field you wish to update: \n 1. Name \n 2. Team Type \n 3. Fee Paying Status \n 4. Reg. Cancellation \n")
            upd_field = input()
            if upd_field == '1':
                name = input("Enter Name: ")
                Team.set_name(obj, name)
            elif upd_field == '2':
                type_opt = input("Input the type of team\n1. Boys \n2. Girls \nSelect option 1 or 2:\n")
                type = "Boys" if (type_opt == '1') else "Girls"
                Team.set_type(obj, type)
            elif upd_field == '3':
                fee_paid = bool(input("Fee paying status\n 1. Paid\n 2. Not Paid \nSelect option 1 or 2:\n") == '1')
                Team.set_fee_paid(obj, fee_paid)
            elif upd_field == '4':
                if(Team.get_c_date(obj)==''):
                    c_date = UserInterface.add_cancellation_date()
                    Team.set_c_date(obj, c_date)
                else:
                    print("Team already cancelled registration")
        UserInterface.save_to_txt()

    # Method checks if any teams are existing and lets the user delete teams
    # based on team id also updates team id list in of team class and object list in UI
    def delete_team():
        print("Please input team id you wish to delete from below list ")
        for t_id in Team.id_list:
            print(t_id)
        obj_select = int(input())
        while 1:
            if(obj_select in Team.id_list):
                break
            else:
                print("Invalid User Id")
                print("Please input team id you wish to delete from below list")
                for t_id in Team.id_list:
                    print(t_id)
                obj_select = int(input())
        ind = Team.id_list.index(obj_select)
        Team.id_list.remove(obj_select)
        Team.teams_list.remove(Team.teams_list[ind])
        print(f'\nTeam {obj_select} is deleted')
        UserInterface.save_to_txt()

    # Method helps to display number of teams created, percentage of teams paid the fees
    # Also displays no of teams cancelled the registration.
    def teams_details():
        num = len(Team.teams_list)
        print('\nNumber of teams currently available: ',num)
        cntr1,cntr2=0,0
        for obj in Team.teams_list:
            if Team.get_fee_paid(obj):
                cntr1+=1
            if(Team.get_c_date(obj) != ''):
                cntr2+=1
        print('Number of teams cancelled: ',cntr2)
        print(f'Overall percentage of Teams who paid fees: {round((cntr1*100/num),2)}%')

    # Method to save all the existing teams in the memory to a text file
    def save_to_txt():
        if len(Team.teams_list) != 0:
            file = open("HockeyTeams.txt", "w")
            for team in Team.teams_list:
                team_info = Team.get_team_info(team)
                file.write(team_info + '\n')
            print("\nTeams information is saved successfully!")
        else:
            print("\nNo team has registered!")

    # Method to load all the existing teams from the text file
    def load_from_txt():
        id_list = []
        try:
            file = open("HockeyTeams.txt", "r")
        except:
            print("Oops! File doesn't exist.")
            return None
        for team_obj in file:
            team_obj = team_obj.replace('\n', '')
            team_data = team_obj.split(',')
            Team_id = int(team_data[0])
            id_list.append(Team_id)
            rdt = team_data[1]
            year,month,day = map(int,rdt.split('-'))
            r_date = date(year,month,day)
            name = team_data[2]
            team_type = team_data[3]
            fee_paid = bool(team_data[4].lower() in ['true','t'])
            cdt=team_data[5]
            if cdt!='':
                year,month,day = map(int,cdt.split('-'))
                c_date = date(year,month,day)
            else:
                c_date = ''
            obj = Team(r_date, name, team_type, fee_paid, c_date)
            Team.set_id(obj, Team_id)
            Team.teams_list.append(obj)
        Team.id_list = id_list
        Team.cnt = max(Team.id_list)
        print("Successfully loaded the teams")

    # Exits completely from the program
    def exit_ui():
        while True:
            print("\nSelect an option to exit\n\n",
                  "1. Save & Exit\n",
                  "2. Exit without saving")
            opt = input("\nEnter your option: ")
            if opt == '1':
                UserInterface.save_to_txt()
                break
            elif opt == '2':
                break
            else:
                print('Invalid option')
        print("\nThanks for using Youth Hockey Cup Registration UI!")
        return 'exit'