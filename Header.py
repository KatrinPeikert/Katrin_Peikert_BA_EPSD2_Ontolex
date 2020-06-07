# -*- coding: utf-8 -*-
__author__ = "Katrin Peikert"

def setHeader(document):
    """

    This function simply has a string of all my Ontolex-prefixes and my Corpora-references
    and my PoS-definitions which are written into a document.
    """
    namespaces= \
        """@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
@prefix synsem: <http://www.w3.org/ns/lemon/synsem#> .
@prefix decomp: <http://www.w3.org/ns/lemon/decomp#> .
@prefix vartrans: <http://www.w3.org/ns/lemon/vartrans#> .
@prefix lime: <http://www.w3.org/ns/lemon/lime#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix owl: <http://www.w3.org/2002/07/owl#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix skos: <http://www.w3.org/2004/02/skos#>.
@prefix dbr: <http://dbpedia.org/resource/>.
@prefix dbo: <http://dbpedia.org/ontology/>.
@prefix void: <http://rdfs.org/ns/void#>.
@prefix lexinfo: <http://www.lexinfo.net/ontology/2.0/lexinfo#>.
@prefix semiotics: <http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl#>.
@prefix oils: <http://lemon-model.net/oils#>.
@prefix dct: <http://purl.org/dc/terms/>.
@prefix provo: <http://www.w3.org/ns/prov#>.
@prefix rdfs:	<http://www.w3.org/2000/01/rdf-schema#> .
@prefix lexicog: <http://www.w3.org/ns/lemon/lexicog#> .
@prefix frac: <http://www.w3.org/ns/lemon/frac#> .
@prefix e2model: <http://oracc.museum.upenn.edu/model/>.
@prefix epsd2: <http://oracc.museum.upenn.edu/epsd2/>.


e2model:Frequency rdfs:subClassOf frac:CorpusFrequency.
e2model:Frequency rdfs:subClassOf
 [ a owl:Restriction ;
   owl:onProperty dct:source ;
   owl:hasValue epsd2:pager ] .

e2model:Frequency_EDIIIa
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:ed3a ] .

e2model:Frequency_EDIIIb
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:ed3b ] .

e2model:Frequency_Ebla
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:ebla ] .

e2model:Frequency_OAKK
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:oakk ] .

e2model:Frequency_LAGII
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:lagash2 ] .

e2model:Frequency_UrIII
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:U3 ] .

e2model:Frequency_OB
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:oldbab ] .

e2model:Frequency_POB
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Post-OB ] .


e2model:Frequency_MdA
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Middle_Assyrian ] .


e2model:Frequency_MdB
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Middle_Babylonian ] .


e2model:Frequency_NeoA
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Neo-Assyrian ] .


e2model:Frequency_NeoB
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Neo-Babylonian ] .


e2model:Frequency_Pers
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Persian ] .


e2model:Frequency_Hel
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Hellenistic ] .


e2model:Frequency_Unct
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Uncertain ] .

e2model:Frequency_Unkw
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:unknown ] .

e2model:Frequency_PC
 rdfs:subClassOf e2model:Frequency;
 rdfs:subClassOf
   [ a owl:Restriction ;
     owl:onProperty dct:temporal ;
     owl:hasValue epsd2:Proto-Cuneiform ] .

e2model:pos
	rdfs:label "part of speech"@en;
	rdfs:comment "Describes the category of a word based on its grammatical and semantic properties, as used in EPSD2"@en .

e2model:DN a e2model:pos;
	rdfs:label "Divine Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:ON a e2model:pos;
	rdfs:label "Object Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:TN a e2model:pos;
	rdfs:label "Temple Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:SN a e2model:pos;
	rdfs:label "Settlement Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:WN a e2model:pos;
	rdfs:label "Watercourse Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:PN a e2model:pos;
	rdfs:label "Personal Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:GN a e2model:pos;
	rdfs:label "Geographical Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:MN a e2model:pos;
	rdfs:label "Month Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:RN a e2model:pos;
	rdfs:label "Royal Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:CN a e2model:pos;
	rdfs:label "Celestial Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:LN a e2model:pos;
	rdfs:label "Line Name (ancestral clan)"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:QN a e2model:pos;
	rdfs:label "Quarter Name (city area)"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:EN a e2model:pos;
	rdfs:label "Ethnos Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:FN a e2model:pos;
	rdfs:label "Field Name"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html".

e2model:V_i a e2model:pos;
	rdfs:label "intransitive Verb"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/sumerian/index.html".

e2model:V_t a e2model:pos;
	rdfs:label "transitive Verb"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/sumerian/index.html".

e2model:V a e2model:pos;
	rdfs:label "Verb"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:NU a e2model:pos;
	rdfs:label "number"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:AJ a e2model:pos;
	rdfs:label "adjective"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:J a e2model:pos;
	rdfs:label "interjection"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:CNJ a e2model:pos;
	rdfs:label "conjunction"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:AV a e2model:pos;
	rdfs:label "adverb"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:DP a e2model:pos;
	rdfs:label "demonstrative pronoun"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:QP a e2model:pos;
	rdfs:label "interrogative pronoun"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:RP a e2model:pos;
	rdfs:label "reflexive,reciprocal pronoun"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:PRP a e2model:pos;
	rdfs:label "preposition"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:IP a e2model:pos;
	rdfs:label "independent/anaphoric pronoun"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:N a e2model:pos;
	rdfs:label "noun"@en;
	skos:note "http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html".

e2model:U a e2model:pos;
	rdfs:label "unknown meaning"@en;
	skos:note "http://oracc.museum.upenn.edu/epsd2/".

e2model:O a e2model:pos;
	rdfs:label "No definition found"@en.

e2model:MA a e2model:pos;
	rdfs:label "No definition found"@en.
"""



    with open(document, 'w') as f:
        f.write(namespaces)
        f.write("\n\n")
#        f.write(partOfSpeech)
#        f.write("\n\n")
    return

def isHeaderSet(document):
    """This Function simply returns a False """
    return False
