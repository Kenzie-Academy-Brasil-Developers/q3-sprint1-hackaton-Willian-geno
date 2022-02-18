hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_score(team_name, teams):
    index = 0;
    for item in teams:
        if item == team_name:
            return (f'A {team_name} ficou classificada em {index+1}')
        index +=1
    return (f'A time "{team_name}" não é um time da lista!')

