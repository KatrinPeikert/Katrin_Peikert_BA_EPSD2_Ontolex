# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"

def replacer_cunei(tmp):

    x = tmp.replace("?", "\?")
    x = x.replace("@", "\!at\!")
    x = x.replace("(", "\(")
    x = x.replace(")", "\)")
    x = x.replace(" ", "_")
    return x

class Generate_Entries:
    """ Extracts the relevant data from an html-document """

    def __init__(self, data, language):
        """intiializing the data and the language of the entry (emesal or emegir)

            """
        self.data = data
        self.entry = []
        self.entry.append(language)

    def get_data(self):
        self.get_name()
        self.get_pos()
        self.get_instances()
        self.get_dif_language()
        self.get_senses_and_freq()
        self.get_general_freq()
        self.get_writing_alternative()
        self.get_prefixes()
        self.get_unique_name()
        return self.entry


    def get_name(self):
        """This Function extracts the entry-name from the title-triple of an entry from EPSD2"""
        try:
            x = self.data.body.div.div.h1.span.contents
            y = x[0]
            self.entry.append(y)
        except:
            y = " "
            self.entry.append(y)

    def get_pos(self):
        """ This Function extracts the PoS-Tag from the title-triple of an entry from EPSD2 """
        try:
            x = self.data.body.div.div.h1.find_all(attrs={"class":"pos"})[0].contents
            y= x[0].replace("(","")
            y = y.replace(")","")
            self.entry.append(y)
        except:
            y =" "
            self.entry.append(y)

    def get_instances(self):
        """ This Function extracts the frequency from the title-triple of an entry from EPSD2 """
        try:
            x = self.data.body.div.div.p.a.contents
            y = x[0].replace(" instances","")
            y = y.replace("instance","")
            self.entry.append(y)
        except:
            y = " "
            self.entry.append(y)

    def get_dif_language(self):
        """

        This Function extracts the trasnlations into akkadian and references
        to other entry from the EPSD2.
        """
        dif_languages = []
        l_akk = self.data.find_all(attrs={"class":"akk"})
        l_sux = self.data.find_all(attrs={"class":"equivs"})
        if l_akk != []:
            self.akk_list=[]
            self.akk_list =["akkadian"]
            for i in l_akk:
                self.akk_list.append(i.contents[0])
            dif_languages.append(self.akk_list)
        if l_sux != []:
            self.sux_list =["sumerian"]
            for i in l_sux:
                if i.find(attrs={"class":"sux"}) != None:
                    s = i.find(attrs={"class":"sux"}).contents[0]
                    self.sux_list.append(s)
            if len(self.sux_list) > 1:
                dif_languages.append(self.sux_list)
        self.entry.append(dif_languages)


    def find_pos_sense(self, ln):
        """This function checks whether a sense of an entry has an own PoS-Tag """
        pos = ""
        if ln.rfind('[') != -1 and ln.rfind(']') != -1:
            pos = ln[ln.rfind('[')+1 : ln.rfind(']')]
        return pos

    def get_senses_and_freq(self):
        """ This Function extracts the senses and their properties (frequencies, PoS) """
        freqs1 = self.data.find(attrs={ "id":"senses"}).find_all(attrs={"class":"icountu"})
        freqs2 = self.data.find(attrs={ "id":"senses"}).find_all(attrs={"class":"sense"})
        self.sense_list=[]
        if freqs1 != []:
            for l in freqs1:
                freq_dict= dict()
                sense=[]
                line = l.contents[1]
                name = line[0:line.rfind('(')]
                num = line[line.rfind('(')+1 : line.rfind('x')]
                pos = self.find_pos_sense(line)
                freq_dict["Frequency"]= int(num)

                sense.append(freq_dict)
                sense.append(name[0:name.rfind("[")])
                if pos != "":
                    sense.append(pos)
                self.sense_list.append(sense)
        if freqs2 != []:
            for s in freqs2:
                for l in s.contents:
                    if isinstance(l, str) and l != "\n":
                        freq_dict= dict()
                        sense=[]
                        freq_dict["Frequency"]= 0
                        pos = self.find_pos_sense(l)
                        sense.append(freq_dict)
                        if l.rfind("[") != -1:
                            sense.append(l[0:l.rfind("[")])
                        else:
                            sense.append(l)
                        if pos != "":
                            sense.append(pos)
                        self.sense_list.append(sense)
        self.entry.append(self.sense_list)


    def get_general_freq(self):
        """ This Function extracts the frequencies of the whole entry """
        freqs = self.data.find(attrs={ "id":"periods"}).find_all(attrs={"class":"icountu"})
        self.general_freq_dict= dict()
        for i in freqs:
            line = i.contents[0]
            name = line[0:line.rfind('(')]
            name = name.replace(" ", "")
            num = line[line.rfind('(')+1 : line.rfind('x')]
            self.general_freq_dict[name]= int(num)
        self.entry.append(self.general_freq_dict)

    def get_writing_alternative(self):
        """This funtion extracts all the different writing variants in latin script and in cuneiform """
        alts_c = []
        alts_l = []
        self.real_alts = []
        orths = self.data.find_all(attrs={"class":"orthindex"})
        for i in orths:
            ln = i.find_parent()
            if ln.find(attrs={"class":"cuneiform"}) != None:
                cunei = ln.find(attrs={"class":"cuneiform"}).contents
                if cunei == []:
                    alts_c.append(" ")
                else:
                    x = replacer_cunei(cunei[0])
                    alts_c.append(x)
                latn = ""
                w = ln.find(attrs={"class":"w"})
                if w != None:
                    for j in ln.find(attrs={"class":"w"}).contents:
                        if j.name =="span":
                            if j.find_all(attrs={"class":"sign"}) != []:
                                for el in j:
                                    if isinstance(el, str) :
                                        latn += el
                                    else:
                                        latn += el.contents[0]
                            else:
                                latn += j.contents[0]
                        elif j.name == "sup":
                            latn +='\''
                            latn += j.contents[0]
                            latn +='\''
                alts_l.append(latn)

            elif ln.find(attrs={"class":"cont"}) != None:
                form = ln.find(attrs={"class":"cont"}).contents
                if len(form) == 2:
                    freq = form[1].contents[0]
                    name = form[0]
                    num = freq[freq.rfind('(')+1 : freq.rfind('x')]
                    alt = []
                    alt.append({"Frequency":int(num)})
                    alt.append("")
                    alt.append(name)
                    self.real_alts.append(alt)
            else:
                cunei = ln.find(attrs={"class":"cuneiform"}).contents
                form = ln.find(attrs={"class":"cont"}).contents


        self.get_writing_alternative_freq()
        for i in range(0,len(alts_c)):
            tmp = []
            tmp.append(self.freq_list[i])
            tmp.append(alts_c[i])
            tmp.append(alts_l[i])
            self.real_alts.append(tmp)
        self.entry.append(self.real_alts)

    def get_writing_alternative_freq(self):
        """This function creates a List of the Frequencies of the different forms of an entry in various corpora"""
        self.freq_list=[]
        for i in self.data.find_all(attrs={"class":"ovindex"}):

            templ_dic = {"PC" :0, "ED IIIa":0, "ED IIIb":0, "Ebla":0,
                    "OAkk":0, "LAGII":0 ,"URIII":0, "OB":0, "Post-OB":0,
                    "(unknown)":0}
            x = i.find_parent().find_all(attrs={"class":"ovfreq"})
            count = 0
            for key in templ_dic:
                if x[count].contents != []:
                    templ_dic[key]= int(x[count].contents[0])
                count+= 1
            self.freq_list.append(templ_dic)
        return self.freq_list

    def get_prefixes(self):
        """This Function returns a List fo the Verbal Prefixes an entry might have."""
        prefixes = []
        prefix_class = self.data.find(attrs={"class":"morphs prefix"})
        if prefix_class != None:
            for prefix in prefix_class.find_all(attrs={"class":"icountu"}):
                prefixes.append(prefix.contents[0])
        self.entry.append(prefixes)

    def get_unique_name(self):
        """ This function extracts the unique ID-number from an entry"""
        try:
            x = self.data.body.div.find(attrs={"class":"summary-headword"}).contents[0].get('href')
            x = x[x.rfind(".x")+1:x.rfind(".html")]
            self.entry.append(x)

        except:
            print(self.data.body.div)
