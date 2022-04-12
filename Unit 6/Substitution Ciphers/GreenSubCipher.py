from math import log
import random
import sys
from tqdm import tqdm

POPULATION_SIZE = 750 # the number of strategies in each generation
NUM_CLONES = 1 # the number of precisely cloned strategies retained from each generation to the next
TOURNAMENT_SIZE = 40 # how many strategies selected for each tournament
TOURNAMENT_WIN_PROBABILITY = .75 # the probability with which the best strategy in a tournament is selected
CROSSOVER_LOCATIONS = 5 # how many exact letters from parent 1 are copied to the child in the same locations
MUTATION_RATE = .2 # the chance that a child experiences a mutation after being generated

real_alphabet = 'ETAOINSHRDLCUMWFGYPBVKXJQZ'

toDecode = '''PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG
GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNG
HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR
BEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ-
SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAF
NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG
UNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL
VAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR
NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL
PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT.
GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ
NF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ
FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRA
NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER
VAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFR
QBAG FUBJ GURZ GB LBHE PYNFFRF YRG GURZ RKCREVRAPR GUR
NPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR
NER BCRA FBHEPR GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAF
NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVSL
GUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF
HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE
PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ
BS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR.
SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE
ZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR
BHE CEVAPVCYRF CNTR.'''
if len(toDecode) < 840: 
    N = 3
else:
    N = 4

print("Parameters used:")
print("N =", N)
print("Population info:")
print("\tPopulation size =", POPULATION_SIZE)
print("\tNum clones per gen =", NUM_CLONES)
print("\tCrossover locations =", CROSSOVER_LOCATIONS)
print("\tMutation rate =", MUTATION_RATE)
print("Tournament info:")
print("\tTourney size =", TOURNAMENT_SIZE)
print("\tTourney win rate =", TOURNAMENT_WIN_PROBABILITY)


ngrams = dict()
with open('ngrams.txt') as f:
    ngrams = {line.split()[0] : line.split()[1] for line in f}

def encode(message, cipher_alphabet):
    cipher = dict()
    for index, letter in enumerate(real_alphabet):
        cipher[letter] = cipher_alphabet[index]
    message = message.upper()
    encoded = ""
    for letter in message:
        if letter in real_alphabet:
            encoded += cipher[letter]
        else:
            encoded += letter
    return encoded

def decode(message, cipher_alphabet):
    cipher = dict()
    for index, letter in enumerate(cipher_alphabet):
        cipher[letter] = real_alphabet[index]
    message = message.upper()
    decoded = ""
    for letter in message:
        if letter in real_alphabet:
            try:
                decoded += cipher[letter]
            except:
                print(cipher_alphabet, "error")
                decoded += cipher[letter]
        else:
            decoded += letter
    return decoded

def fitness(n, encoded_block, cipher_alphabet):
    encoded_block = decode(encoded_block, cipher_alphabet)
    log_sum = 0
    for index, char in enumerate(encoded_block):
        ngram = encoded_block[index: index + n]
        if (len(ngram) == n) and (ngram in ngrams):
            log_sum += log(int(ngrams[ngram]), 2)
    return log_sum

def swap_random_alphabet(alphabet):
    alphabet = [letter for letter in alphabet]
    random_letter_1 = random.randrange(0, 26) # swapped letter 1 
    random_letter_2 = random.randrange(0, 26) # swapped letter 2
    temp = alphabet[random_letter_1]
    alphabet[random_letter_1] = alphabet[random_letter_2]
    alphabet[random_letter_2] = temp
    return ''.join(alphabet)    

def hill_climber(encoded_block, chosen_alphabet, n):
    current_fitness = fitness(n, encoded_block, chosen_alphabet)
    i = 0
    while True:
        new_alphabet = swap_random_alphabet(chosen_alphabet)
        new_fitness = fitness(n, encoded_block, new_alphabet)
        if new_fitness > current_fitness:
            encoded_block = decode(encoded_block, new_alphabet)
            current_fitness = new_fitness
            chosen_alphabet = new_alphabet
            print(encoded_block, current_fitness)
            

def generate_random_alphabet():
    check = [letter for letter in real_alphabet]
    new_alpha = ""
    while check:
        choice = random.choice(check)
        check.remove(choice)
        new_alpha += choice
    return new_alpha

def generate_initial_population():
    population = []
    while len(population) < POPULATION_SIZE:
        toBeAdded = generate_random_alphabet()
        if toBeAdded not in population:
            population.append(toBeAdded)
    return rank_population(population)

def rank_population(population):
    strat_to_fitness = dict()
    for strategy in population:
        strat_to_fitness[strategy] = fitness(N, toDecode, strategy)
    ranked = sorted(strat_to_fitness.items(), key = lambda kv : (kv[1], kv[0]))
    return ranked[::-1]


def breed(parent1, parent2):
    child = ['' for i in range(26)]
    parent1 = [letter for letter in parent1]
    parent2 = [letter for letter in parent2]
    crossovers = []
    while len(crossovers) < CROSSOVER_LOCATIONS:
        potential = random.randrange(0, 26)
        if potential not in crossovers:
            crossovers.append(potential)
    for crossover in crossovers:
        try:
            child[crossover] = parent1[crossover]
        except:
            print(child, parent1, parent2)
    for letter in parent2:
        if letter not in child:
            index = child.index('')
            child[index] = letter
    return ''.join(child)

def create_child(current_population):
    full_tourney = []
    while len(full_tourney) < (TOURNAMENT_SIZE * 2):
        toAdd = random.choice(current_population)
        if toAdd not in full_tourney:
            full_tourney.append(toAdd)
    tourney1 = full_tourney[:TOURNAMENT_SIZE]
    tourney2 = full_tourney[TOURNAMENT_SIZE:]
    tourney1.sort(key=lambda x:x[1])
    tourney2.sort(key=lambda x:x[1])
    tourney1 = tourney1[::-1]
    tourney2 = tourney2[::-1]
    parent1 = 0
    parent2 = 0
    for element in tourney1:
        if random.random() <= TOURNAMENT_WIN_PROBABILITY:
            parent1 = element[0]
            break
    for element in tourney2:
        if random.random() <= TOURNAMENT_WIN_PROBABILITY:
            parent2 = element[0]
            break
    if parent1 == 0:
        parent1 = tourney1[0][0]
    if parent2 == 0:
        parent2 = tourney2[0][0]
    child = breed(parent1, parent2)
    if random.random() < MUTATION_RATE:
        child = swap_random_alphabet(child)
    return child


population = generate_initial_population()
for i in tqdm(range(500)):
    decode(toDecode, population[0][0])
    fitness(4, toDecode, population[0][0])
    new_generation = []
    for clone in range(NUM_CLONES):
        new_generation.append(population[clone][0])
    while len(new_generation) < POPULATION_SIZE:
        child = create_child(population)
        if child not in new_generation:
            new_generation.append(child)
    population = rank_population(new_generation)
