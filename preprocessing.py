import csv
import json
import traceback

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from swiplserver import PrologMQI

from Pokemon import PokemonTeam

def process_pokemon_csv():
    with open('./resources/df_pokemon.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open('pokemons.pl', mode='w', encoding='utf-8') as plfile:
            for row in reader:
                name = row['Name']#.replace("'", "\\'")
                plfile.write(f"pokemon(\"{name}\").\n")
                type1 = row['Type1']
                type2 = row['Type2'] if row['Type2'] else 'null_type'
                # plfile.write(f"pokemon('{name}', '{type1}', '{type2}').\n")

def process_moves_csv():
    with open('./resources/df_moves.csv', mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open('moves.pl', mode='w', encoding='utf-8') as plfile:
            for row in reader:
                name = row['Name']#.replace("'", "\\'")
                move_type = row['Type']
                damage_class = row['Damage_class']
                plfile.write(f"move(\"{name}\").\n")
                # plfile.write(f"move('{name}', '{move_type}', '{damage_class}').\n")

def process_types_csv():
    with open('./resources/df_types.csv', mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open('types.pl', mode='w', encoding='utf-8') as plfile:
            for row in reader:
                name = row['Name']
                name = name[0].upper() + name[1:]
                plfile.write(f"type(\"{name}\").\n")

def getTypesList() -> list:
    path = './resources/'
    typesList = ['null_type']
    with open(path + 'df_types.csv', encoding='utf-8') as types:
        reader = csv.DictReader(types)
        for mtype in reader:
            mtype['Name'] = mtype['Name'][0].upper() + mtype['Name'][1:]
            typesList.append(mtype['Name'])
    types.close()
    return typesList[:-3] # togli i tipi Shadow, Uknown e Fairy

def getPokeMovesDict(typesList) -> dict:
    path = './resources/'
    movesDict = {}
    with open(path + 'df_moves.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # ============ PICCOLO PRE-PROCESSING DEI DATI ============
            if row['Name'] == 'Hidden Power':
                for mtype in typesList[1:]: # non si considera null_type
                    auxDic = row.copy()
                    auxDic['Name'] = row['Name'] + ' [' + mtype + ']'
                    auxDic['Type'] = mtype
                    movesDict[auxDic['Name']] = auxDic
            else: # ============ FINE PRE-PROCESSING DEI DATI =========
                movesDict[row['Name']] = row
    csvfile.close()
    return movesDict

def getPokeDict() -> dict:
    path = './resources/df_pokemon.csv'
    pokeDict = {}
    gen = 5
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['Generation']) <= gen:
                pokeDict[row['Name']] = row
    csvfile.close()
    return pokeDict

def getEffectivenessDict() -> dict:
    path = './resources/bridge_type_type_MOVE_EFFECTIVENESS_ON_POKEMON.csv'
    effectivenessDict = {}
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Atk. Move Type'] not in effectivenessDict:
                effectivenessDict[row['Atk. Move Type']] = {}
            effectivenessDict[row['Atk. Move Type']][row['Def. Pokemon Type']] = row['Damage Multiplier']
    csvfile.close()
    return effectivenessDict

def getNewFeatures(team):
    pokeDict = getPokeDict()
    input_teams, target_pks = team.getAllValidSubsets()
    X = []
    y = []
    for i in range(0, len(input_teams)):
        sample = [0] * len(pokeDict)
        for pk in input_teams[i]:
            sample[pk.getID()] += 1
        X.append(sample)
        y.append(target_pks[i].getType1() + ' ' + target_pks[i].getType2())
    return X, y

def getDefenceMultiplier(atktype, pk, effectivenessDict):
    # manca da tenere in considerazione anche le abilità tipo levitate su ground
    mult = 0
    pkType1 = pk.getType1()
    pkType2 = pk.getType2()
    if effectivenessDict[atktype][pkType1] == '2':
        mult -= 1
    if pkType2 != 'null_type' and effectivenessDict[atktype][pkType2] == '2':
        mult -= 1
    if effectivenessDict[atktype][pkType1] == '½':
        mult += 1
    if pkType2 != 'null_type' and effectivenessDict[atktype][pkType2] == '½':
        mult += 1
    if (pkType2 != 'null_type' and effectivenessDict[atktype][pkType2] == '0') or effectivenessDict[atktype][pkType1] == '0':
        mult = 1.5
    if mult < -1.5:
        mult += 0.5
    if mult > 1.5:
        mult -= 0.5
    return mult

def getAttackMultiplier(defType, pk, effectivenessDict):
    mult = 0
    for move in pk.getMoves():
        atkType = move.getType()
        if move.getDmgClass() != 'Status':
            if effectivenessDict[atkType][defType] == '2':
                if atkType == pk.getType1() or atkType == pk.getType2():
                    mult += 1
                mult += 1
    return mult

def getTeamCoverage(team, typesList, effectivenessDict, predict_type, subsets, coverageType):
    X = []
    y = []
    typesList = typesList[1:]
    if subsets:
        input_teams, target_pks = team.getAllValidSubsets()
    else:
        input_teams = [team.getTeam()[:-1]]
        target_pks = [team.getTeam()[-1]]
    for i, team in enumerate(input_teams):
        atkSample = {}
        defSample = {}
        for ptype in typesList:
            atkSample[ptype] = 0
            defSample[ptype] = 0
        for pk in team:
            for pType in typesList: # senza null_type
                defSample[pType] += getDefenceMultiplier(pType, pk, effectivenessDict)
                atkSample[pType] += getAttackMultiplier(pType, pk, effectivenessDict)
        if coverageType == 'attack':
            X.append([val for val in atkSample.values()])
        elif coverageType == 'defense':
            X.append([val for val in defSample.values()])
        else:
            X.append([val for val in defSample.values()] + [val for val in atkSample.values()])
        if predict_type == 'type2':
            y.append(target_pks[i].getType2()) # +' '+target_pks[i].getType2()
        elif predict_type == 'type1':
            y.append(target_pks[i].getType1()) # +' '+target_pks[i].getType2()
        else:
            y.append(target_pks[i].getType1()+' '+target_pks[i].getType2())
    return X, y

def getSamples(team):
    X = []
    y = []
    input_teams, target_pks = team.getAllValidSubsets()
    for i, team in enumerate(input_teams):
        sample = []
        for pk in team:
            sample.append(pk.getType1() + '_' + pk.getType2())

        for pk in team:
            for move in pk.getMoves():
                if move.getDmgClass() == '':
                    sample.append('null_type')
                else:
                    sample.append(move.getType())

        y.append(target_pks[i].getType1() + ' ' + target_pks[i].getType2())
        X.append(sample)
    return X, y

def getSingleTypeFrequencies(team, typesList, input_type, predict_type, subsets):
    X = []
    y = []
    feat_to_index = {}
    index = 0
    if input_type == 'both':
        for type1 in typesList[1:]: # senza null_type
            for type2 in typesList:
                if type1 != type2:
                    feat_to_index[type1 + ' ' + type2] = index
                    index += 1
        for mtype in typesList[1:]:
            feat_to_index[mtype + '_move'] = index
            index += 1
    else:
        for ptype in typesList:
            feat_to_index[ptype] = index
            index += 1
        for ptype in typesList:
            sample[ptype + '_move'] = index
            index += 1
        
    if subsets:
        input_teams, target_pks = team.getAllValidSubsets()
    else:
        input_teams = [team.getTeam()[:-1]]
        target_pks = [team.getTeam()[-1]]   
    for i, team in enumerate(input_teams):
        sample = [0] * index
        for pk in team:
            if input_type == 'both':
                sample[feat_to_index[pk.getType1() + ' ' + pk.getType2()]] += 1
            else:
                sample[feat_to_index[pk.getType1()]] += 1
                sample[feat_to_index[pk.getType2()]] += 1
            for move in pk.getMoves():
                if move.getDmgClass() != 'Status':
                    sample[feat_to_index[move.getType() + '_move']] += 1
        if predict_type == 'type2':
            # sample[target_pks[i].getType1()] += 1
            y.append(target_pks[i].getType2())
        elif predict_type == 'type1':
            y.append(target_pks[i].getType1())
        else:
            y.append(target_pks[i].getType1() + ' ' + target_pks[i].getType2())
        X.append(sample)
    return X, y

def filter(X, y, threshold):
    new_X = []
    new_y = []
    occurrences = {item: y.count(item) for item in y}
    for i, tar in enumerate(y):
        if occurrences[tar] > threshold:
            new_X.append(X[i])
            new_y.append(y[i])
    return new_X, new_y, occurrences


def getDataset(paths):
    types1_counter = {}
    types2_counter = {}
    both_types_counter = {}
    items = {}
    teams = []
    X = []
    y = []
    typesList = getTypesList()
    pokeDict = getPokeDict()
    movesDict = getPokeMovesDict(typesList)
    effectivenessDict = getEffectivenessDict()
    for type1 in typesList[1:]: #senza null_type
        for type2 in typesList:
            if type1 != type2:
                both_types_counter[type1 + ' ' + type2] = 0
    for key in typesList:
        types1_counter[key] = 0
        types2_counter[key] = 0
    count = 0
    all_teams = 0
    for path in paths:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            with PrologMQI() as mqi:
                with mqi.create_thread() as prolog_thread:
                    prolog_thread.query("consult('parser.pl').")
                    for team in data:
                        result = False

                        result = prolog_thread.query('parse_team("' + team["TeamString"] + '", ParsedTeam).')

                        if result:
                            new_team = PokemonTeam(result[0], pokeDict, movesDict)
                            teams.append(new_team)

                            for pk in new_team.getTeam():
                                if pk.getItem() in items:
                                    items[pk.getItem()] += 1
                                else:
                                    items[pk.getItem()] = 0
                                types2_counter[pk.getType2()] += 1
                                types1_counter[pk.getType1()] += 1
                                both_types_counter[pk.getType1()+' '+pk.getType2()] += 1

                            # new_X, new_y = getTeamCoverage(new_team, typesList, effectivenessDict, predict_type='both', subsets=True, coverageType='both')
                            new_X, new_y = getSingleTypeFrequencies(new_team, typesList, input_type='both', predict_type='both', subsets=True)
                            # add_X, add_y = getNewFeatures(new_team)
                            # new_X = [new_X[i] + add_X[i] for i in range(0, len(new_X))]
                            X += new_X
                            y += new_y
                        count += 1
                        print(count, end="\r")
        file.close()
        all_teams += len(data)

    X, y, occurrences = filter(X, y, 4)
    occurrences_mean = np.mean(list(occurrences.values()))
    occurences_median = np.median(list(occurrences.values()))
    occurrences_variance = np.var(list(occurrences.values()))

    # print("items: ", items)
    print(typesList)
    print("types1_counter: \n", sorted(types1_counter.values()))
    print("types2_counter: \n", sorted(types2_counter.values()))
    print("both_types_counter: \n", sorted(both_types_counter.values()))
    # print(occurrences)
    # print("Mean Target Occurrences: ", occurrences_mean)
    # print("Median Target Occurrences: ", occurences_median)
    # print("Variance Target Occurences: ", occurrences_variance)
    print("#(Data Teams): ", all_teams)
    print("#(Loaded Teams): ", len(teams))
    print("#(data_set): ", len(y))

    with open('./log_stats.txt', 'w', encoding='utf-8') as log_file:
        log_file.write("types1_counter: \n" + str(sorted(types1_counter.values())) + "\n")
        log_file.write("types2_counter: \n" + str(sorted(types2_counter.values())) + "\n")
        log_file.write("both_types_counter: \n" + str(sorted(both_types_counter.values())) + "\n")
        # log_file.write("Mean Occurrences: "+str(occurrences_mean)+'\n')
        # log_file.write("Median Occurrences: "+str(occurences_median)+'\n')
        # log_file.write("Variance Occurences: "+str(occurrences_variance)+'\n')
        log_file.write("#(Data Teams): " + str(all_teams) + "\n")
        log_file.write("#(Loaded Teams): " + str(len(teams)) + "\n")
        log_file.write("#(data_set): " + str(len(y)) + "\n")

    types1_counter.pop('null_type')

    df = pd.DataFrame.from_dict(types1_counter, orient='index', columns=['Occurrences'])
    df.sort_values('Occurrences', inplace=True)
    df.plot(kind='bar', legend=False, figsize=(8, 10), )
    plt.xlabel('Types1')
    plt.ylabel('Occurrences')
    plt.title('Types1 Target Distribution')
    plt.savefig('./stats plots/type1_distribution.png')

    df = pd.DataFrame.from_dict(types2_counter, orient='index', columns=['Occurrences'])
    df.sort_values('Occurrences', inplace=True)
    df.plot(kind='bar', legend=False, figsize=(8, 10))
    plt.xlabel('Type2')
    plt.ylabel('Occurrences')
    plt.title('Types2 Target Distribution')
    plt.savefig('./stats plots/type2_distribution.png')

    df = pd.DataFrame.from_dict(occurrences, orient='index', columns=['Occurrences'])
    df.sort_values('Occurrences', inplace=True)
    df.plot(kind='bar', legend=False, figsize=(100, 8))
    plt.xlabel('Both Types')
    plt.ylabel('Occurrences')
    plt.title('Both Types Target Distribution')
    plt.savefig('./stats plots/both_types_distribution.png')

    print(len(X[0]))

    return X, y

def getSimplifiedDataset(paths):
    teams = []
    X = []
    y = []
    typesList = getTypesList()
    pokeDict = getPokeDict()
    movesDict = getPokeMovesDict(typesList)
    effectivenessDict = getEffectivenessDict()
    count = 0
    all_teams = 0
    for path in paths:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            with PrologMQI() as mqi:
                with mqi.create_thread() as prolog_thread:
                    prolog_thread.query("consult('parser.pl').")
                    for team in data:
                        result = False

                        result = prolog_thread.query('parse_team("' + team["TeamString"] + '", ParsedTeam).')

                        if result:
                            new_team = PokemonTeam(result[0], pokeDict, movesDict)
                            teams.append(new_team)

                            new_X, new_y = getSamples(new_team)
                            X += new_X
                            y += new_y
                        count += 1
                        print(count, end="\r")
        file.close()
        all_teams += len(data)

    print("#(Data Teams): ", all_teams)
    print("#(Loaded Teams): ", len(teams))
    print("#(data_set): ", len(y))

    print(len(X[0]))

    return X, y

# X, y = getDataset(paths = ['./OU Teams/original/gen5ou.json'])
# X, y = getSimplifiedDataset(paths = ['./OU Teams/original/gen5ou.json'])
# print(X[0])
# process_pokemon_csv()
# process_moves_csv()
# process_types_csv()
