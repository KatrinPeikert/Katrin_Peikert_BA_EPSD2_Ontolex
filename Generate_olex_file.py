# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"

import copy
from Header import setHeader, isHeaderSet
from LexicalEntry import *
from Forms import *
from Words import *
from Sense import *
from Lexicog import *

def generate_OLEX(documentName, wordList):
    """ 
    
    This function generates an Olex-file by callinf functions, wich print the
    Informations into a file. 
    """
    if not isHeaderSet(documentName):
    # setting the header
        setHeader(documentName)
    for lexWord in wordList:
    # going through every entry and printing it
        add_WordEntry(documentName,lexWord)
    print("finished")
    return

def add_WordEntry(documentName,lexWord):
    """This function prints all the different Informations into an olex file """
    sorted_by_sense_pos = []
    define_prefix(documentName, lexWord)
    if lexWord.sensesList:
    #sorting by PoS-tag in order to create the necessary Lexical Entries
        sorted_by_sense_pos = sort_senses(documentName, lexWord)
        for one_sense_pos in sorted_by_sense_pos:
            add_WordEntry_Sense(documentName, lexWord, one_sense_pos)
    else:
        # Printing the Lexical-entr base ant its references to the Senses, forms, translations etc.
        addLexicalEntry(documentName,lexWord)
    addForms(documentName,lexWord)

    if lexWord.translatableAsList:
        for word in lexWord.translatableAsList:
            add_translation(documentName, word)
    addLexicogEntry(documentName,lexWord, sorted_by_sense_pos)
    return


def add_WordEntry_Sense(documentName,lexWord, one_sense_pos):
    """
    
    If the senses have differnet PoS-tags, this function creates a LexicalEntry
    for every group of senses with the same PoS-tag and adds an entry into the 
    Lexicog entry.
    """
    lexWord_tmp = copy.copy(lexWord)
    lexWord_tmp.wordType = one_sense_pos[0]
    addLexicalEntry(documentName,lexWord_tmp, one_sense_pos)
    for one_sense in one_sense_pos[1:]:
        addLexicogSense(documentName, lexWord_tmp, one_sense)
    return


