hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_score(team_name, teams):
    index = 0;
    for item in teams:
        if item == team_name:
            return print(f'A {team_name} ficou classificada em {index+1}° lugar!')
        index +=1
    return print(f'A time "{team_name}" não é um time da lista!')


get_score( 'Team Liqued', hackathon_1)
get_score("Team Ateliware", hackathon_1)
get_score("Team Kenzie", hackathon_1)
get_score("Team Mirum", hackathon_3)