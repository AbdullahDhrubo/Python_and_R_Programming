#Team Class : Used for creating team instances based on the schema defined in team class
class Team:
    fee = 500  # the fee that each team must pay to participate in the event
    cnt = 0 # initializing the counter for generating team id
    id_list = []
    teams_list = []

    # Constructor method used to define required attributes
    def __init__(self, r_date, name, type, fee_paid, c_date=''):
        Team.cnt += 1 #Method used for incremental operation of the counter value used for generating ID
        self.__id = Team.cnt  # a unique value for each object created
        self.__r_date = r_date  # date, when team was created
        self.__name = name  # name of team
        self.__type = type  # whether the team is for girls or boys
        self.__fee_paid = fee_paid  # if fee has been paid or not to participate in the event
        self.__c_date = c_date # if a team decides to cancel participation
        Team.id_list.append(Team.cnt)

    # Method used to update team id while loading from text file
    def set_id(self, tid):
        self.__id = tid

    # Method used to update team registration date while loading from text file
    def set_r_date(self, rdt):
        self.__r_date = rdt

    # Method enables user to update team name
    def set_name(self,name):
        self.__name = name

    # Method enables user to get a date of registration cancellation
    def set_c_date(self, c_date):
        self.__c_date = c_date

    # Method enables user to update team type
    def set_type(self, type):
        self.__type = type

    # Method enables user to update team type
    def set_fee_paid(self, fee_paid):
        self.__fee_paid = fee_paid

    # Method enables user to fetch team id
    def get_id(self):
        return self.__id

    # Method enables user to fetch team registration date
    def get_r_date(self):
        return self.__r_date

    # Method enables user to fetch team name
    def get_name(self):
        return self.__name

    # Method enables user to fetch team type
    def get_type(self):
        return self.__type

    # Method enables user to fetch team registration fee paid status
    def get_fee_paid(self):
        return self.__fee_paid

    # Method enables user to fetch team registration cancellation
    def get_c_date(self):
        return self.__c_date

    # Method enables user to fetch team info
    def get_team_info(self):
        team_data = (str(self.__id) + ',' + str(self.__r_date) + ',' + \
                     str(self.__name) + ',' + self.__type + ',' + str(self.__fee_paid) + \
                     ',' + str(self.__c_date))
        return team_data

    # Method enables user to print teams information
    def __str__(self):
        if (self.__c_date != ''):
            c_date = ("Cancelled on\t\t:" + str(self.__c_date)+'\n')
        else:
            c_date = ''

        team_info = "\nTeam Id \t\t\t:" + str(self.__id) + \
                    "\nRegistered on \t\t:" + str(self.__r_date) + \
                    "\nName of Team \t\t:" + self.__name + \
                    "\nType of Team \t\t:" + self.__type + \
                    "\nFee Status \t\t\t:" + str(self.__fee_paid) + '\n' + c_date

        return team_info
