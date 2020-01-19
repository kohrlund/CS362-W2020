import Dominion

def getBoxes(nV, mul):
    #Define box
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*mul
    box["Smithy"]=[Dominion.Smithy()]*mul
    box["Laboratory"]=[Dominion.Laboratory()]*mul
    box["Village"]=[Dominion.Village()]*mul
    box["Festival"]=[Dominion.Festival()]*mul
    box["Market"]=[Dominion.Market()]*mul
    box["Chancellor"]=[Dominion.Chancellor()]*mul
    box["Workshop"]=[Dominion.Workshop()]*mul
    box["Moneylender"]=[Dominion.Moneylender()]*mul
    box["Chapel"]=[Dominion.Chapel()]*mul
    box["Cellar"]=[Dominion.Cellar()]*mul
    box["Remodel"]=[Dominion.Remodel()]*mul
    box["Adventurer"]=[Dominion.Adventurer()]*mul
    box["Feast"]=[Dominion.Feast()]*mul
    box["Mine"]=[Dominion.Mine()]*mul
    box["Library"]=[Dominion.Library()]*mul
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*mul
    box["Council Room"]=[Dominion.Council_Room()]*mul
    box["Witch"]=[Dominion.Witch()]*mul
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*mul
    box["Militia"]=[Dominion.Militia()]*mul
    box["Spy"]=[Dominion.Spy()]*mul
    box["Thief"]=[Dominion.Thief()]*mul
    box["Throne Room"]=[Dominion.Throne_Room()]*mul
    return box


def getSupplyOrder():
    supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}
    return supply_order

def initSupply(supply, player_names, nV, nC):
    #The supply always has these cards
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC

def getNumVC(player_names):
    if len(player_names)>2:
        return 12
    else:
        return 8