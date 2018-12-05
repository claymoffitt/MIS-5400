from random import seed
from random import random
from random import randint
from random import shuffle
import random



Team1 = "Alabama"
Team2 = "Fresno_State"
Team1_name = "Alabama"
Team2_name = "Fresno State"
print(Team1_name)
print(Team2_name)

Reg_Predicted_Factor = .9
Reg_Random_Factor = .9
Team1_AdjPFpg = 43.7
Team1_AdjPApg = 15.5
Team2_AdjPFpg = 30.7
Team2_AdjPApg = 26.9
Team1_Projected_PF = (Team1_AdjPFpg+(Team2_AdjPApg-28))
Team2_Projected_PF = (Team2_AdjPFpg+(Team1_AdjPApg-28))
print(Team1_Projected_PF)
print(Team2_Projected_PF)

seed(random)

x = [i for i in range(-99,100)]
shuffle(x)
print(x)
for _ in range(2):
	rand_factor_1 = (random.choice(x))/100
print(rand_factor_1)
Team1_Reg_PF = max(int((Team1_Projected_PF/Reg_Predicted_Factor) + ((Team1_Projected_PF*rand_factor_1)/Reg_Random_Factor)), 0)
Team2_Reg_PF = max(int((Team2_Projected_PF/Reg_Predicted_Factor) + ((Team2_Projected_PF*rand_factor_1)/Reg_Random_Factor)), 0)
print(Team1_name, Team1_Reg_PF)
print(Team2_name, Team2_Reg_PF)