# Sahiti Kota and Tanmai Kalisipudi
# 12/13/2021

import sys

textFile = sys.argv[1]
minimumLength = int(sys.argv[2])
if len(sys.argv) == 4:
    word = sys.argv[3].upper()
    originalWord = sys.argv[3].upper()
else:
    word = ''
    originalWord = ''

words = set()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
completeWords = set()

with open(textFile) as f:
    lineList = [line.strip().upper().split() for line in f]
    for lineNum in range(0, len(lineList)):
        if "".join(lineList[lineNum]).isalpha() == True and len("".join(lineList[lineNum])) >= minimumLength:
            currentWord = "".join(lineList[lineNum])
            currentChar = 1
            while currentChar < len(currentWord) + 1:
                words.add(currentWord[0:currentChar])
                currentChar += 1
            completeWords.add(currentWord)

def possibleNextMoves(currentWord):
    possibleNextWords = []
    if currentWord == '':
        for letter in alphabet:
            possibleNextWords.append((letter, letter))
    # if game in progress
    else:
        for letter in alphabet:
            newWord = currentWord + letter
            if newWord in words:
                possibleNextWords.append((newWord, letter))
    return possibleNextWords

def gameIsOver(word):
    if word in completeWords:
        return True
    return False

def currentPlayer(word):
    if (len(word) - len(originalWord)) % 2 == 0:
        return "H"
    else:
        return "C"

def score(word, player):
    if player == "H":
        return 1
    else:
        return -1

def minStep(word):
    if gameIsOver(word):
        return score(word, currentPlayer(word))
    results = []
    for nextWord, move in possibleNextMoves(word):
        results.append(maxStep(nextWord))
    return min(results)

def maxStep(word):
    if gameIsOver(word):
        return score(word, currentPlayer(word))
    results = []
    for nextWord, move in possibleNextMoves(word):
        results.append(minStep(nextWord))
    return max(results)

def minMove(word):
    results = []
    for nextWord, move in possibleNextMoves(word):
        results.append((maxStep(nextWord), move))
    minimum, move = min(results)
    moves = []
    for step, move in results:
        if step == minimum and minimum < 1:
            moves.append(move)
    return moves

def maxMove(word):
    results = []
    for nextWord, move in possibleNextMoves(word):
        results.append((minStep(nextWord), move))
    maximum, move = max(results)
    moves = []
    for step, move in results:
        if step == maximum and maximum > -1:
            moves.append(move)
    return moves

if len(maxMove(word)) == 0:
    print("Next player will lose!")
else:
    print("Next player can guarantee victory by playing any of these letters:", maxMove(word))