# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"


import Generate_olex_file

class WordSense:
    """

    This class defines sense-objects with 4 properties: Frequency, the corpus,
    their definition and their PoS-tag .
    """

    def __init__(self, frequencyDict, definition, partOfSpeech =  ""):
        if len(frequencyDict) > 1:
            print("error too many corpus for sense")
        if len(frequencyDict) < 1:
            print("no corpus for sense")
        tmp = []
        for i in frequencyDict.keys():
            tmp.append(i)
        corpus = tmp[0]
        frequency = frequencyDict[corpus]
        self.corpus = corpus
        self.frequency = frequency
        self.definition = definition
        self.partOfSpeech = partOfSpeech

def replacer_sense(tmp):
    """

    This function adds \\ to  all  signs, which are not accepted by Turtle.
    [ and ] are replaced by \\\( and \\\). A Space is replaced by _.
    """
    for i in "~.-!$&()*+,;=/?#@":
        x = "\\"  + i
        tmp = tmp.replace(i, x)
    tmp = tmp.replace("⟦", "\(")
    tmp = tmp.replace("⟧", "\)")
    if tmp[0] == " ":
        tmp = tmp[1:]
    if tmp[-1] == " ":
        tmp = tmp[:-1]
    tmp = tmp.replace("%", "__")
    tmp = tmp.replace(" ", "_")
    tmp = tmp.replace("[", "\(")
    tmp = tmp.replace("]", "\)")
    tmp = tmp.replace("{", "\(")
    tmp = tmp.replace("}", "\)")
    tmp = tmp.replace("`", "\-")
    tmp = tmp.replace("'", "\-")
    tmp = tmp.replace("’", "\-")
    return tmp

def addLexicogSense(documentName, lexWord, sense):
    """This function prints a Sense-onject with a definition, the word itself, and its frequency. """
    senseRef = ":" + lexWord.word + "_sense_" + replacer_sense(sense.definition) + " a ontolex:LexicalSense;\n"
    skosRef = '     skos:definition "' + sense.definition +  '" ;\n'
    if sense.frequency != 0:
        frequencyRef =   '     frac:frequency [a e2model:' + sense.corpus +'; rdf:value "' + str(sense.frequency) +  '" ] .'
        senseEntry = senseRef + skosRef + frequencyRef + "\n"
    else:
        senseEntry = senseRef + skosRef[:-2] + ".\n"

    with open(documentName, 'a') as f:
        f.write(senseEntry)
        f.write("\n")
    return

def sort_senses(documentName, lexWord):
    """This function sorts the different senses by their PoS-tags. """
    sense_sorted_by_pos = []
    sense_sorted_by_pos.append([lexWord.wordType])
    if lexWord.sensesList:
        for sense in lexWord.sensesList:
            new_pos = []
            added = False
            for one_pos in sense_sorted_by_pos:
                if sense.partOfSpeech == one_pos[0]:
                    one_pos.append(sense)
                    added = True
            if not(added):
                new_pos.append(sense.partOfSpeech)
                new_pos.append(sense)
                sense_sorted_by_pos.append(new_pos)
    return(sense_sorted_by_pos)
