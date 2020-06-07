# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"


import re
import os
import io
from bs4 import BeautifulSoup
import Generate_entries_from_html as ge
from Generate_olex_file import *

# The input_path describes the path where the EPSD2-files are saved
input_path = "/home/user/Documents/"


def change_corpus_names(dict):
    """ Changing the Names of the Corpora from the EPSD2 to my own definitions """
    new_dict = {}
    for epsd2_name in dict.keys():
        if epsd2_name =='EarlyDynasticIIIa' or epsd2_name == "ED IIIa":
            new_dict["Frequency_EDIIIa"] = dict[epsd2_name]

        elif epsd2_name =='EarlyDynasticIIIb' or epsd2_name == "ED IIIb":
            new_dict["Frequency_EDIIIb"] = dict[epsd2_name]

        elif epsd2_name == "Ebla":
            new_dict["Frequency_Ebla"] = dict[epsd2_name]

        elif epsd2_name == "Post-OB":
            new_dict["Frequency_POB"] = dict[epsd2_name]

        elif epsd2_name =='MiddleBabylonian':
            new_dict["Frequency_MdB"] = dict[epsd2_name]

        elif epsd2_name =='Neo-Assyrian':
            new_dict["Frequency_NeoA"] = dict[epsd2_name]

        elif epsd2_name == 'Neo-Babylonian':
            new_dict["Frequency_NeoB"] = dict[epsd2_name]

        elif epsd2_name =='Persian':
            new_dict["Frequency_Pers"] = dict[epsd2_name]

        elif epsd2_name =='Hellenistic':
            new_dict["Frequency_Hel"] = dict[epsd2_name]

        elif epsd2_name =='OldAkkadian' or epsd2_name == "OAkk":
            new_dict["Frequency_OAKK"] = dict[epsd2_name]

        elif epsd2_name =='LagashII' or epsd2_name == "LAGII":
            new_dict["Frequency_LAGII"] = dict[epsd2_name]

        elif epsd2_name =='UrIII' or epsd2_name == "URIII":
            new_dict["Frequency_UrIII"] = dict[epsd2_name]

        elif epsd2_name =='OldBabylonian' or  epsd2_name == "OB":
            new_dict["Frequency_OB"] = dict[epsd2_name]

        elif epsd2_name =='MiddleAssyrian':
            new_dict["Frequency_MdA"] = dict[epsd2_name]

        elif epsd2_name == 'unknown' or epsd2_name == '(unknown)':
            new_dict["Frequency_Unkw"] = dict[epsd2_name]

        elif epsd2_name == 'uncertain' or epsd2_name == 'Uncertain' :
            new_dict["Frequency_Unct"] = dict[epsd2_name]

        elif epsd2_name == 'Archaic' or epsd2_name == "PC":
            new_dict["Frequency_PC"] = dict[epsd2_name]
        else:
            new_dict[epsd2_name] = dict[epsd2_name]
    return new_dict

class Transformator:
    """

    Takes the raw data, which was extracted from the html-documents and changes
    them into the Word- and Entry-classes, which i defined for my Ontolex-model,
    and returns the information in a specific order.
    """

    def __init__(self, entry):
        self.entry = entry
        self.extract_data(entry)
        self.send_data()

    def send_data(self):
        return self.word

    def extract_data(self, entry):
        self.extract_simple_data(entry)
        self.senses_list_add_pos()
        self.get_canonical_info()
        self.get_otherForms()
        self.get_translateables_and_references()
        return self.finished_transformation()

    def extract_simple_data(self, entry):
        self.tmp_word = replacer(entry[1].replace(" ", "_"))
        self.tmp_writing_language = entry[0]
        self.tmp_wordType = entry[2].replace("/", "_")
        self.tmp_FrequencyDict= change_corpus_names(entry[6])
        self.tmp_otherFormsList = entry[7]
        self.tmp_translateableAsList = entry[4]
        self.tmp_sensesList = entry[5]
        self.tmp_prefixes = entry[8]
        self.tmp_unique_name = entry[9]

    def senses_list_add_pos(self):
        """

        This function checks if a sense has already a  PoS-Tag .
        If not, it adds the PoS-tag of the entry.
        """
        tmp = []
        for i in self.tmp_sensesList:
            if len(i) == 2:
                i.append(self.tmp_wordType)
            tmp.append(WordSense(change_corpus_names(i[0]),i[1],i[2].replace("/", "_")))
        self.tmp_sensesList = tmp


    def get_canonical_info(self):
        self.tmp_canonicalFrequencyDict = change_corpus_names({'PC': 0,
        'ED IIIa': 0, 'ED IIIb': 0, 'Ebla': 0, 'OAkk': 0, 'LAGII': 0,
        'URIII': 0, 'OB': 0, 'Post-OB': 0, '(unknown)': 0})
        self.tmp_transliteration = WordForm( " ", "cuneiform")
        for form in self.tmp_otherFormsList:
            if form[2] == self.tmp_word:
                self.tmp_canonicalFrequencyDict = change_corpus_names(form[0])
                self.tmp_transliteration = WordForm(form[1], "cuneiform")
                self.tmp_otherFormsList.remove(form)
                break

    def get_otherForms(self):
        tmp = []
        for form in self.tmp_otherFormsList:
            tmp.append(WordForm(replacer(form[2]), "latin", frequencyDict =
            change_corpus_names(form[0]) ,
            transliteration = WordForm(form[1], "cuneiform")))
        self.tmp_otherFormsList = tmp

    def get_translateables_and_references(self):
        """

        This function sorts the akkadian translations and the references to other
        emegir-words from the EPSD2
        """
        tmp = []
        reference = []
        for trans in self.tmp_translateableAsList:
            lang = trans[0]
            for i in range(1,len(trans)):
                if lang == "akkadian":
                    x = trans[i].replace(" ", "_")
                    tmp.append(LexWord(replacer(x), lang))
                elif lang == "sumerian":
                    reference.append(trans[i])


        self.tmp_translateableAsList = tmp
        self.tmp_reference = reference

    def finished_transformation(self):
        """ This function creates an object from the class LexWord """
        self.word = LexWord(self.tmp_word, self.tmp_writing_language,
        wordType=self.tmp_wordType, sensesList=self.tmp_sensesList,
        frequencyDict=self.tmp_FrequencyDict,
        canonicalFrequencyDict=self.tmp_canonicalFrequencyDict,
        otherFormsList=self.tmp_otherFormsList,
        transliteration=self.tmp_transliteration,
        translatableAsList = self.tmp_translateableAsList,
        prefixes = self.tmp_prefixes,
        unique_name = self.tmp_unique_name,
        reference = self.tmp_reference)




# mint_olaf: /home/kp/Documents

# on toshi: C:/Users/Katrin Peikert/Documents/Uni/Bachelorarbeit_Ling/Meine BA
# on mint @work: /home/user/Documents/testing



def replacer(tmp):
    """

    This function adds \\ to  all the signs, which are not accepted by Turtle
    """
    for i in "~.-!$&'()*+,;=/?#@":
        x = "\\"  + i
        tmp = tmp.replace(i, x)
    tmp = tmp.replace("%", "__")
    tmp = tmp.replace("’", "\_")
    tmp = tmp.replace("{", "\(")
    tmp = tmp.replace("}", "\)")
    tmp = tmp.replace("×", "x")
    tmp = tmp.replace("[", "\(")
    tmp = tmp.replace("]", "\)")
    tmp = tmp.replace("|", "_")
    return tmp

def start_e2model():
    """
    starts my Program by getting the needed information from every html-document
    in a folder transforming it into my own format, and adding it to a list. This
    list will then be printed into a .olex file. It also gives out the html-files,
    where an error occured
    """
    transformed_entries = []
    error_documents = []
    error_number = 0
    print("start_e2model")

    with os.scandir(input_path) as entries:
        for entry in entries:
            if str(entry.name).endswith('.html'):
                if "emesal" in str(entry.name):
                    language = "sux-emesal"
                else:
                    language = "sumerian"
                    with open(entry, encoding="utf-8") as cur_entry:
                        data = BeautifulSoup(cur_entry, "html.parser")
                        x = ge.Generate_Entries(data, language)
                        try:
                            y = x.get_data()
                            transformed_entries.append(Transformator(y).send_data())
                        except:
                            error_documents.append(entry.name)
                            error_number += 1
                    cur_entry.close()
    print("error", error_documents)
    print(error_number)

    generate_OLEX("EPSD_in_Ontolex.olex", transformed_entries)


# Starting the process

start_e2model()
