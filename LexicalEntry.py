# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"

from Words import LexWord
from Sense import replacer_sense
from Forms import replace_form


def addSense_entry(lexWord, one_pos):
    """ This function creates a string, which includes all the different senses od the entry, with the same PoS-tag"""
    senseRef = ""
    for sense in one_pos[1:]:
        senseRef += "     ontolex:sense :" +lexWord.word + "_sense_" + replacer_sense(sense.definition) +" ;\n"
    if senseRef != "":
        senseRef = senseRef[:len(senseRef) -2]
        senseRef += "."

    return senseRef

def addLexicalEntry(documentName, lexWord, one_sense_pos = []):
    """

    This function prints the entry-definition, the references to senses, forms and the translations
    into Akkadian, the references to another EPSD2-entry and the Verbal prefixes into an
    olex-file.
    """

    #entry-definition:
    lexRef = ":lex_" + lexWord.word + "_" + lexWord.wordType + "_" + lexWord.unique_name + " a ontolex:LexicalEntry;\n"

    if lexWord.wordType:
        lexInfo = "     lexinfo:partOfSpeech e2model:" + lexWord.wordType +" ;\n"
    else:
        lexInfo = ""
    #canonical-form:
    canonicalFormRef = "     ontolex:canonicalForm :form_"  + lexWord.word +  "_" +lexWord.unique_name + " ;\n"

    otherFormRef = ""

    #If this word has a Sense, it calls addSense_entry to create the string for printing
    senseRef = ""
    if one_sense_pos != []:
        senseRef = addSense_entry(lexWord, one_sense_pos)

    #References to different forms
    if lexWord.otherFormsList:
        otherFormRef += "     ontolex:otherForm"
        num = 1
        for otherForm in lexWord.otherFormsList:
            otherFormRef += " :form_" + replace_form(otherForm.word)
            if otherForm.transliteration and otherForm.transliteration.word != "" and otherForm.transliteration.word != " ":
                otherFormRef += "_" + otherForm.transliteration.word
            otherFormRef +=  "_" + lexWord.unique_name
            otherFormRef += ", "
            num += 1
        otherFormRef = otherFormRef[:len(otherFormRef) - 2]
        otherFormRef += " ;\n"

    if otherFormRef:
        otherFormRef = otherFormRef[:len(otherFormRef) - 2]
        otherFormRef += "."
    else:
        canonicalFormRef = canonicalFormRef[:len(canonicalFormRef) - 2]
        canonicalFormRef += "."

    translationRef = ""
    if lexWord.translatableAsList:
        translationRef += "     vartrans:translatableAs"
        for translation in lexWord.translatableAsList:
            translationRef += " :lex_" + translation.word + ","
        translationRef = translationRef[:len(translationRef) - 1]
        translationRef += " ." #" ;\n"

    referenceRef = ""
    if lexWord.reference:
        referenceRef += "     skos:note "
        for reference in lexWord.reference:
            referenceRef += " \"refers to EPSD2-Entry " + str(reference) +"\" ,\n"
        referenceRef = referenceRef[:len(referenceRef) - 2]
        referenceRef += " ."


    morphologyRef = ""
    if lexWord.prefixes:
        morphologyRef += "     e2model:VerbalPrefixes"
        for prefix in lexWord.prefixes:
            morphologyRef += " \"" + prefix + "\","
        morphologyRef = morphologyRef[:len(morphologyRef) - 1]
        morphologyRef += " ." #" ;\n"

    lexEntry = lexRef + lexInfo + canonicalFormRef + otherFormRef


    if senseRef:
        lexEntry = lexEntry[:len(lexEntry) - 1]
        lexEntry += ";\n"
        lexEntry += senseRef

    if translationRef:
        lexEntry = lexEntry[:len(lexEntry) - 1]
        lexEntry += ";\n"
        lexEntry += translationRef

    if referenceRef:
        lexEntry = lexEntry[:len(lexEntry) - 1]
        lexEntry += ";\n"
        lexEntry += referenceRef

    if morphologyRef:
        lexEntry = lexEntry[:len(lexEntry) - 1]
        lexEntry += ";\n"
        lexEntry += morphologyRef

    with open(documentName, 'a') as f:
        f.write(lexEntry)
        f.write("\n\n")
    return
