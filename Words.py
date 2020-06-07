# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"

class WordForm:
    """

    This class describes the different properties of a Word and is mostly used
    for Forms and the translations into Akkadian in my model.
    """

    def __init__(self, word, writingLanguage, frequencyDict = {},
    transliteration = ""):
        self.word = word
        self.writingLanguage = self.getWritingLangueString(writingLanguage)
        self.transliteration = transliteration
        self.frequencyDict = frequencyDict

    def getWritingLangueString(self, writingLanguage):
        """This function replaces the Information about the Language with an ISO693 or ISO 15924 form. """
        if writingLanguage == "latin" or writingLanguage == "sumerian":
            result = "@sux-Latn"
        elif writingLanguage == "cuneiform":
            result = "@sux-Xsux"
        elif writingLanguage == "en-gb":
            result = "@en-GB"
        elif writingLanguage == "en-us":
            result = "@en-US"
        elif writingLanguage == "de":
            result = "@de"
        elif writingLanguage == "fr":
            result = "@fr"
        elif writingLanguage == "akkadian":
            result = "@akk"
        elif writingLanguage == "sux-emesal":
            result = "@sux-emesal"
        else:
            result = "@en"
        return result

class LexWord(WordForm):
    """

    This Class inherits the properties from the general Word class and extends
    them. It is used for the Lexical Entries.
    """

    def __init__(self, word, writingLanguage, wordType = "",
    sensesList= [],frequencyDict={}, canonicalFrequencyDict={},
    transliteration = "", otherFormsList = [],
    translatableAsList = [], prefixes = [], unique_name = "", reference = []):
        WordForm.__init__(self,word, writingLanguage, frequencyDict, transliteration)
        self.wordType = wordType
        self.otherFormsList = otherFormsList
        self.sensesList = sensesList
        self.canonicalFrequencyDict = canonicalFrequencyDict
        self.translatableAsList = translatableAsList
        self.prefixes = prefixes
        self.unique_name = unique_name
        self.reference = reference
        return
