from ast import List
import re
import csv

class PokemonMove():

    def __init__(self, moveDict) -> None:
        self.name = moveDict['Name'] # sempre
        self.type = moveDict['Type'] # sempre
        if self.type == 'Fairy': # convertire i tipi Fairy nei tipi Normal della generazione 5
            self.type = 'Normal'
        # self.pp = int(moveDict['PP']) # sempre
        self.dmgClass = moveDict['Damage_class'] # sempre
        # self.effect = moveDict['Effect']
        # self.prob = moveDict['Prob. (%)']
        # self.power = moveDict['Power']
        # self.accurancy = moveDict['Acc.'] 

    def getDmgClass(self):
        return self.dmgClass

    def getType(self):
        return self.type

    def __str__(self) -> str:
        return self.name

class Pokemon():

    def __init__(self, build_dict, pokeDict, movesDict) -> None:
        args = build_dict['args']
        self.moves = []
        self.name = args[0]
        self.item = args[1]
        self.type1 = pokeDict[self.name]['Type1']
        self.type2 = pokeDict[self.name]['Type2']
        if self.type2 == '':
            self.type2 = 'null_type'
        for move in args[2]:
            self.moves.append(PokemonMove(movesDict[move]))
        # print(self.type1)
        # print(self.type2)

    def getType1(self) -> str:
        return self.type1
    
    def getType2(self) -> str:
        return self.type2

    def __str__(self) -> str:
        s = '$' + self.name + ' @ ' + self.item + '\n'
        # s += 'Ability: ' + self.ability + '\n'
        # s += 'Evs: ' + self.evs + '\n'
        # s += self.nature + '\n'
        # s += 'IVs: ' + self.ivs + '\n'
        for move in self.moves:
            s += '- ' + move.__str__() + '\n'
        return s + '$'

    def getMoves(self):
        return self.moves.copy()
    
    def getName(self) -> str:
        return self.name

    def getItem(self):
        return self.item
    
class PokemonTeam():

    def __init__(self, team_dict, pokeDict, movesDict) -> None:
        self.pokemons = []
        for build_dict in team_dict['ParsedTeam']:
            self.pokemons.append(Pokemon(build_dict, pokeDict, movesDict))
    
    def getPokemon(self, index) -> Pokemon:
        return self.pokemons[index]
    
    def getTeam(self):
        return self.pokemons.copy()
    
    def __str__(self) -> str:
        s = '$'
        for pk in self.pokemons:
            s += pk.__str__() + '\n'
        return s + '$'

    def getAllValidSubsets(self):
        input_teams = []
        target_pks = []
        target = 0
        for target in range(0, len(self.pokemons)):
            target_pks.append(self.pokemons[target])
            subset = []
            for pk in self.pokemons:
                if pk != self.pokemons[target]:
                    # print('0', end="")
                    subset.append(pk)
                # else:
                #     print('1', end="")
            # print()
            input_teams.append(subset)
        # print()
        # input()
        return input_teams, target_pks