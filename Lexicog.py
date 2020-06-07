# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"

def define_prefix(documentName, lexWord):
    """This function creates the Link to the page from each entry and prints it. """
    prefix = "@prefix : <http://oracc.museum.upenn.edu/epsd2/cbd/sux/sux."
    prefix += lexWord.unique_name + ".html#> ."
    with open(documentName, 'a') as f:
        f.write(prefix)
        f.write("\n\n")

def addLexicogEntry(documentName, lexWord, sorted_by_sense_pos = []):
    """ 
    
    This function prints the lexicog entry, all it's lexical entries and the frequencies
    of the whole EPSD2-entry into an olex file. 
    """
    Lexicog = ""
    Lexicog += ":entry a lexicog:entry ; \n     rdfs:member "
    Lexicog += ":lex_" + lexWord.word + "_" + lexWord.wordType + "_" + lexWord.unique_name + ", "
    if sorted_by_sense_pos != []:
        for one_sense_pos in sorted_by_sense_pos[1:]:
                Lexicog += ":lex_" + lexWord.word + "_" + one_sense_pos[0] + "_" + lexWord.unique_name + ", "
    Lexicog = Lexicog[:len(Lexicog) - 2] + " .\n"

    frequencyRef = ""
    if lexWord.frequencyDict:
        for corpus,frequency in lexWord.frequencyDict.items():
            if frequency != 0:
                frequencyRef +='     frac:frequency [a e2model:' + corpus +'; rdf:value "' + str(frequency) +  '" ] ;\n'
        frequencyRef = frequencyRef[:len(frequencyRef) -2]

        Lexicog = Lexicog[:len(Lexicog) - 2] +";\n" + frequencyRef + " .\n"

    with open(documentName, 'a') as f:
        f.write(Lexicog)
        f.write("\n")
    return
