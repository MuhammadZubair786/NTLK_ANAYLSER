import nltk

list1 = [

'''The French data protection authority ('CNIL') announced, on 15 February 2021, its call for General Data Protection Regulation (Regulation (EU) 2016/679)Â ('GDPR') sandbox projects in the field of digital health. In particular, CNIL noted that its aim isÂ to give enhanced support to the projects that stand out in terms of data protection in the realm of digital health, as well as highlightedÂ that a 'sandbox' cannot lead to a temporary lifting of regulatory constraints under the GDPR. The call for projects is open until 2 April 2021.
You can read the announcement, only available in French, 
 ''' ,
''' The Hong Kong Monetary Authority ('HKMA') announced, on 28 Dec 2018, that it had fined JPMorgan Chase Bank, National Association, Hong Kong BranchÂ HKD 12.5 million (approx. â‚¬1.39 million) for violating Sections 19(2) and 19(3) of Schedule 2 of the Anti-Money Laundering and Counter-Terrorist Financing ('AML/CTF') Ordinance. In particular, the HKMA noted that JPMorgan Hong Kong had failedÂ to establish and maintain effective procedures for identifying and handling wire transfers and for the purposes of carrying out its duties concerning customer due diligence and continuous monitoring of business relationships.
HKMA has ordered JPMorgan Hong Kong to submit an independent report assessing whether its remedial measures were sufficient to address the violations identified.
You can read the press releaseÂ 
Â 
 ''' ,
'''The Italian data protection authority ('Garante') published, on 25Â November 2021, its decision in case No. 407,Â in which it imposed a fine of â‚¬50,000Â on A.O.R.N. Antonio Cardarelli, a hospital within the national system for specialised hospitals, for its violation of Articles 5(1)(a), 5(1)(c), 6, and 9 of theÂ General Data Protection Regulation (Regulation (EU) 2016/679) ('GDPR'), following its processing of personal data in the absence of a suitable legal basis.Â 
Background to the case
In particular, the GaranteÂ stated that the 'Transparent Administration' section ofÂ the hospital'sÂ institutional website had various downloadable documents containing personal data, including, among other things, contact details, tax codes, addresses, and sensitive personal data on health. In this regard, the Garante specified that the aforementioned personal dataÂ was usedÂ inÂ merit ranking in relation to the competition for recruitment of new staff to be employed in light of the Coronavirus and had been disseminated by the hospital under the mistaken belief of pursuing transparency in their actions. In doing so, the Guarante noted thatÂ the hospital did not take into account the current regulatory framework and the indications provided by the Garante to all public entities.
Findings of the Garante
Notably, the Garante found that the hospital, in disseminatingÂ personal data on its websiteÂ in the form of downloadable documents, had processed personal data unlawfully in the absence of a valid legal basis, thus violatingÂ the general principles of processing personal data under Articles 5 and 6 of the GDPR and inÂ contravention ofÂ the provisions relating to theÂ processing of sensitive personal data in Article 9 of the GDPR.
Outcomes
Ultimately, the Garante fined the company â‚¬50,000 and in assessing theÂ quantity of the fine to be imposed, consideredÂ the following factors:
You can read the decision, only available in Italian, 
''',
'''The Italian data protection authority ('Garante') issued, on 27 January 2022, its decision in Case No. 23, in which it imposed a fine of â‚¬40,000 on T.S.M. s.r.l., for violations of Articles 13, 15, and 21 of the General Data Protection Regulation (Regulation (EU) 2016/679) ('GDPR'), and Articles 157 and 166(2) of the Personal Data Protection Code, Containing Provisions to Adapt the National Legislation to General Data Protection Regulation ('the Code'), following a complaint submitted by an individual.
Background to the decision
In particular, the Garante stated that, according to the complaint, in order to participate in a professional training course, the complainant had been requested by the organisers to fill some forms, which, however, were in the name of T.S.M.. In addition, the Garante noted that the complainant had requested the organisers to provide explanations on the same, following which the complainant decided to submit to T.S.M. a request for the exercise of the right of access, the right to erasure, and the right to object. Subsequently, the Garante outlined that T.S.M. had confirmed to the complainant the deletion of their personal data from its archives, without providing the complainant with the information required under Article 15 of the GDPR and without ensuring that it had taken note of the complainant's objection to future processing.
Further to this, the Garante highlighted that T.S.M. had repeatedly failed to respond to requests for information and comments sent by the Garante, following which the Garante hadÂ initiatedÂ the procedure for the adoption of enforcement actions.
Findings of the Garante
Further to the above, based on the elements emerged in the course of the investigation, the Garante found that the forms in questions had required the complainant to attach a copy of their identity document and health card, but did not contain any information on the processing of personal data nor did they clarify the relationship between T.S.M. and the course organisers. Therefore, the Garante held that T.S.M. was in violation of Article 13 of the GDPR, as it had failed to clarify its role and the scope of the processing of personal data. In addition, the Garante deemed T.S.M. in breach of Articles 15 and 21 of the GDPR, having provided incomplete information to the complainant in response to their request for the exercise of their rights, thus making it impossible for the same to exercise those rights and depriving them of control over their personal data.
Notably, the Garante also found T.S.M. in breach of Articles 157 and 166(2) of the Code, for failure to respond to the requests for information and documents submitted by the Garante, thus hindering the investigation.
Given the above, the Garante imposed a fine and, in quantifying the same, the Garante considered, among other things, the repetitive nature of the omissive conduct of T.S.M. towards the Garante's requests, the duration of the violation of the complainant's rights, and the general lack of cooperation during the investigation.
In addition, the Garante:
Outcomes
In conclusion, the Garante imposed the aforementioned fine, warning, prohibition, and orders, and highlighted that T.S.M. may, within 30 days, lodge an appeal before the judicial authority.
You can read the decision, only available in Italian, 
''',

]
get_country_list=[

''' France: CNIL calls for sandbox GDPR digital health project''',
''' Hong Kong: HKMA fines JP Morgan Hong Kong HKD 12.5M for AML/CTF violations''',
''' Italy: Garante fines Antonio Cardarelli Hospital â‚¬50,000 for processing personal data without legal basis''',
''' Italy: Garante fines T.S.M. â‚¬40,000 for violation of data subject rights and failure to cooperate during investigation''',
''' Italy: Garante fines Villa Masi â‚¬1,000 for failure to provide notice of use of CCTV cameras''',
''' Romania: ANSPDCP fines Banca Transilvania â‚¬100,000 for inadequate security measures''',
''' Romania: ANSPDCP fines Viva CreditÂ RON 9,680 for inadequate response to erasure request''',
''' Romania: ANSPDCP sanctions Owners Association Bl and orders corrective measures for GDPR breaches relating to CCTV''',
''' Spain: AEPD fines Comercial Vigobrandy â‚¬1,500 for providing inadequate information in relation to CCTV surveillance''',
''' Turkey: KVKK fines electronic sales service provider TRY 200,000 for failing to take technical and administrative measures to ensure data security''',
''' UK: FCA fines IBUK over Â£1M for failing to report suspicious transactions''',
''' UK: Taskforce report calls for new data protection framework to replace UK GDPR''',]
index_main=-1
for i in list1:
    text = nltk.word_tokenize(i)
    pos_tagged = nltk.pos_tag(text,tagset='universal')
    chk =""
    extra_noun =[]
    extra_verb =[]
    extra_adj=[]

    for j in pos_tagged:
        if(j[1]=="ADJ"):
            if(len(j[0])>5):
                extra_adj.append(j[0])
    
    
    for j in pos_tagged:
        if(j[1]=="NOUN"):
            if(len(j[0])>5):
                extra_noun.append(j[0])

    

    for j in pos_tagged:
        if(j[1]=="VERB"):
            if(len(j[0])>5):
                extra_verb.append(j[0])
                
    for j in pos_tagged:
        
        art_no =""
        count_name =""
        org_name = ""

        action_data =""
        highlighted=""
        particular_data=""
        organization_name ="no company name"

        
        

        
        try:
            if(j[1]=="VERB"):
                index_main+=1
                
                try:
                    cnty_index = get_country_list[index_main].index(":")
                    country_name = get_country_list[index_main][0:cnty_index]
                    count_name=country_name
                    #print(count_name )
                    
                except:
                    count_name="No Country"

                try :
                    org_ind = get_country_list[index_main].index("fines")
                    org_name = get_country_list[index_main][org_ind+6:org_ind+25]
                    organization_name= org_name
                    #print(org_name)

                except:
                    try:
                        org_ind= i.index("fines")
                        org_name = i[org_ind:org_ind+15]
                        organization_name=org_name
                        #print(organization_name)
                    except:
                        a=0
                        #3print("Not get company")
                        
                        
                         

                    
                try:
                    ch_id = i.index("Article")
                    ch_of_article_id = i.index("of",ch_id)
                    art = i[ch_id: ch_of_article_id]
                    art_no=art
                    
                except:
                    art_no=""
                    

                try:
                    highligh= i.index("highlighted")
                    highlight =i[highligh:i.index(",",highligh)]
                    
                    
                except:
                    highlight="no highlight"
                    

                try:
                    particular = i.index("In particular")
                    particular_data = i[particular:i.index(".",particular)]
                    
                    
                   
                except:
                    particular_data= "no particular"
                    

                get_index = i.index(chk)

                if(get_index ==0):
                    org_name = chk
                    
                    
                else:
                    
                    name = i[0:get_index+1]
                    org_name=name
            
                start_index1 = i.index(", on")

                start_index2 = i.index(",",start_index1+1)

                main_date = i[start_index1+4:start_index2]
                list1 =[]

                if(art_no==""):
                    print("\n")
                    print(f"Application Status :",j[0])
                    print("Date :", main_date)
                    print("Org name :",org_name)
                    print("Country :",count_name)
                    print("No Article ")
                    
                    
                    print("Extra Noun:",extra_noun)
                    print("Extra Verb : ",extra_verb)
                    print("extra adj:",extra_adj)
                    print("highlight : ",highlight)
                    print("particular : ",particular_data)
                    print("COMPANY NAME :",organization_name)
                    print("*******************")
                 
                    
                  
                else:
                    print("\n")
                    
                    print("Application Status :",j[0])
                    print("Date :",main_date)
                    print("Org name :",org_name)
                    print("Country :",count_name)
                    print("Article No :",art_no)
                    
                   
                    print("Extra Noun:",extra_noun)
                    print("Extra Verb : ",extra_verb)
                    print("extra adj:",extra_adj)
                    print("highlight : ",highlight)
                    print("particular : ",particular_data)
                    print("COMPANY NAME :",organization_name)
                    print("*******************")

                
                

                


                break
                  
            else:    
                chk =j[0]
                
            
            
            
        except:
            print("no data")
        
