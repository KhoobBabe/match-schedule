from tabulate import tabulate
import math
import random

#this function generates the schedule
def match_sched(teams_list):
    #the original teams list is copied
    y = teams_list.copy()
    s = len(y)
    q = int(s/2)
    sched_list = []
    for i in range(q):
        match_sc = []
        #team 1 is chosen up randomly by the program and removed from the copied list
        z = random.choice(y)
        x = y.index(z)
        team_1 = y.pop(x)
        # team 2 is chosen up randomly by the program and removed from the copied list
        a = random.choice(y)
        b = y.index(a)
        team_2 = y.pop(b)

        #a table is generated which shows the stats of the two teams
        headers = [f"MATCH {i+1}", "WIN RATE", "WIN CHANCE"]
        o = [team_1['Name'], team_1['Win Rate'], round((float(team_1['Win Rate'])/(float(team_1['Win Rate'])+float(team_2['Win Rate'])))*100, 1)]
        c = [team_2['Name'], team_2['Win Rate'], round((float(team_2['Win Rate'])/(float(team_1['Win Rate'])+float(team_2['Win Rate'])))*100, 1)]
        table = [o , c]
        print(tabulate(table, headers, tablefmt = "pretty"))
        print()
        #the two teams are kept in a list
        match_sc.append(team_1)
        match_sc.append(team_2)
        #the list is kept in a bigger list
        sched_list.append(match_sc)
        print()
    return sched_list

#this function shows the team details in a table manner
def team_details(teams_list):
    headers = ["Name", "Matches Played", "Matches Won", "Matches Lost", "Win Rate"]
    details = []
    for i in range(len(teams_list)):
        team_detail = [teams_list[i]['Name'], teams_list[i]["Matches Played"], teams_list[i]["Match Won"], teams_list[i]["Match Lost"], teams_list[i]["Win Rate"]]
        details.append(team_detail)
    print(tabulate(details, headers, tablefmt = "pretty"))
    print()

#this function allows the user to enter the resul6ts of each round
def ent_res(sched_list):
    print("ENTER THE RESULTS OF THIS RESULT")
    print()
    win_list = []
    lose_list = []
    for i in range(len(sched_list)):
        #asks the user to input the result of each match
        print(f"IN MATCH {i+1}")
        print()
        print(sched_list[i][0]['Name'], "vs", sched_list[i][1]['Name'])
        win = input("Who won the match: ")
        if win == sched_list[i][0]['Name']:
            win_list.append(sched_list[i][0])
            lose_list.append(sched_list[i][1])

        elif win == sched_list[i][1]['Name']:
            win_list.append(sched_list[i][1])
            lose_list.append(sched_list[i][0])
        print()

    #if there is only one team left it will be declared as the winner
    if len(win_list) == 1:
        print("Team", win_list[0]['Name'], "is the winner ( /^ω^)/♪♪")
        print()
    else:
        return win_list


def ent_details():
    # these functions checks if the number of teams is a power of two
    def Log2(teams):
        return (math.log10(teams) / math.log10(2))

    def isPowerOfTwo(teams):
        return (math.ceil(Log2(teams)) == math.floor(Log2(teams)))

    # number of teams entered which are the power of 2
    teams = int(input("Enter even number of teams: "))

    #checks if the enterd number is teh power of two
    while teams != 0:
        if(isPowerOfTwo(teams)):
            print()
            break
        else:
            print("Enter the number which is a power of 2")
            teams = int(input("Enter even number of teams: "))
    print()
    #initial teams list is kept empty like the brain
    teams_list = []
    for i in range(teams):
        #info about each team is saved in a separate dictionary for each team
        team_info = {}
        team_info["Name"] = input("write the name of the team: ")
        team_info["Matches Played"] = int(input("how many matches have been played by the team: "))
        mw = team_info["Match Won"] = int(input("how many matches have been won: "))
        ml = team_info["Match Lost"] = int(input("how many matches have been lost: "))
        team_info["Win Rate"] = round((mw/(mw + ml))*100, 1)
        print()
        #all the teams info is saved in a list
        teams_list.append(team_info)
    return teams_list

#CODE STARTS FROM HERE
#options are given about what would you like to do with info provided
opt = ""
while opt != 0:
    print("choose from the options:-")
    print("a. enter teams deatails")
    print("b. generate match schedule")
    print("c. show team details")
    print("d. enter result of a round")
    print("e. exit program")

    opt = input("Enter the option: ")
    print()
    if opt == "a":
        teams_list = ent_details()
    elif opt == "b":
        sched_list = match_sched(teams_list)
    elif opt == "c":
        team_details(teams_list)
    elif opt == "d":
       teams_list = ent_res(sched_list)
    elif opt == 'e':
        print("program closed")
        break
              
            

