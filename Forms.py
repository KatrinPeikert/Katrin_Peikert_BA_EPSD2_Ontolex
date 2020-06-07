# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"


from Words import LexWord

def replace_form(tmp):
    for i in tmp:
        if not(i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"):
            tmp = tmp.replace(i, "_")
    return tmp



def addForms(documentName, lexWord):
    """ This function calls the functions for canonical Forms and Other Forms. """
    addCanonicalForm(documentName, lexWord)
    num = 1
    for otherForm in lexWord.otherFormsList:
        addOtherForm(documentName, otherForm, lexWord.unique_name)
        num += 1
    return

def addCanonicalForm(documentName, lexWord):
    """ This function writes the Definition of an canonical form into an olex file. """
    formRef = ":form_" + replace_form(lexWord.word) + "_" + lexWord.unique_name + " a ontolex:Form;\n"

    writtenRepRef = "     ontolex:writtenRep \""
    writtenRepRef += lexWord.word + "\"" + lexWord.writingLanguage

    if lexWord.transliteration.word != " " and lexWord.transliteration.word != "" :
        writtenRepRef += ", \"" + lexWord.transliteration.word + "\"" + lexWord.transliteration.writingLanguage
    writtenRepRef += " ."

    frequencyRef = ""
    if lexWord.canonicalFrequencyDict:
        frequencyRef = "\n"
        for corpus,frequency in lexWord.canonicalFrequencyDict.items():
            if frequency != 0:
                frequencyRef +='     frac:frequency [a e2model:' + corpus +'; rdf:value "' + str(frequency) +  '" ] ;\n'
        frequencyRef = frequencyRef[:len(frequencyRef) -2]
        frequencyRef += "."
    formEntry = formRef + writtenRepRef
    if frequencyRef != ".":
        formEntry = formEntry[:len(formEntry) -1]
        formEntry += "; "
        formEntry += frequencyRef

    with open(documentName, 'a') as f:
        f.write(formEntry)
        f.write("\n\n")
    return


def addOtherForm(documentName, word, unique):
    """ This function writes the definiiton of a form, its written forms (in cuneiform and latin script) and its frequencies. """
    formRef = ":form_" + replace_form(word.word)
    if word.transliteration and word.transliteration.word != "" and word.transliteration.word != " ":
        formRef += "_" + word.transliteration.word
    formRef += "_" + unique

    formRef += " a ontolex:Form;\n"

    writtenRepRef = "     ontolex:writtenRep \""
    writtenRepRef += word.word + "\"" + word.writingLanguage

    if word.transliteration and word.transliteration.word != "":
        writtenRepRef += ", \"" + word.transliteration.word + "\"" + word.transliteration.writingLanguage
    writtenRepRef += " ."

    frequencyRef = ""
    if word.frequencyDict:
        frequencyRef = "\n"
        for corpus,frequency in word.frequencyDict.items():
            if frequency != 0:
                frequencyRef +='     frac:frequency [a e2model:' + corpus +'; rdf:value "' + str(frequency) +  '" ] ;\n'
        frequencyRef = frequencyRef[:len(frequencyRef) -2]
        frequencyRef += "."
    formEntry = formRef + writtenRepRef
    if frequencyRef != ".":
        formEntry = formEntry[:len(formEntry) -1]
        formEntry += ";"
        formEntry += frequencyRef

    with open(documentName, 'a') as f:
        f.write(formEntry)
        f.write("\n\n")
    return

def add_translation( documentName, word):
    """This function writes the translation into Akkadian."""
    transref = ":lex_" + word.word +" a ontolex:LexicalEntry;\n"
    formref = "     ontolex:canonicalForm :form_" + word.word + " .\n \n"
    repref = ":form_" + word.word +" a ontolex:Form;\n"
    writtenRepRef = "     ontolex:writtenRep \""
    writtenRepRef += word.word + "\"" + word.writingLanguage  + " ."
    translateEntry = transref + formref + repref + writtenRepRef
    with open(documentName, 'a') as f:
        f.write(translateEntry)
        f.write("\n\n")
    return
