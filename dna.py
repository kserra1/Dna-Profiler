import csv
from mailcap import findmatch
import re
import sys
def read_dna(dna_filename):
    with open(dna_filename,'r') as file:
        S=file.read()
    return S

def dna_length(dna_filename):
    dnaLength=len(read_dna(dna_filename))
    return dnaLength

def read_strs(strs_filename):
    with open(strs_filename) as data:
        stringContent=csv.DictReader(data)
        dnaListDict=[]
        for i in stringContent:
            csvDict={'name' : i['name'], 'AGAT':i['AGAT'], 'AATG': i['AATG'], 'TATC' :i ['TATC']}
            dnaListDict.append(csvDict)
        return dnaListDict

def get_strs(str_profile):

    newTuple=[(k,int(v))for k,v in str_profile.items()if k!='name']
                
    return newTuple

def longest_str_repeat_count(str_frag, dna_seq):
    index=0
    test=0
    res=0
    rangeTest=dna_seq[index:].find(str_frag)
    while(rangeTest!=-1):
        rangeTest=dna_seq[index:].find(str_frag)
        if rangeTest==0:
            test+=1
        else:
            res=max(res, test)
            test=1
        index+=rangeTest+len(str_frag)
    res=max(res, test)
    return res

def find_match(str_profile, dna_seq):
    profileRepeatAGAT=str_profile[0][1]
    profileRepeatAATG=str_profile[1][1]
    profileRepeatTATC=str_profile[2][1]
    dnaSeqAGAT=longest_str_repeat_count('AGAT', dna_seq)
    dnaSeqAATG=longest_str_repeat_count('AATG', dna_seq)
    dnaSeqTATC=longest_str_repeat_count('TATC', dna_seq)
    if profileRepeatAGAT==dnaSeqAGAT and profileRepeatAATG==dnaSeqAATG and profileRepeatTATC==dnaSeqTATC:
        return True
    else:
        return False

def dna_match(str_filename, dna_filename):
    totalData=read_strs(str_filename)
    strData=read_dna(dna_filename)
    testMatch=False
    index=0
    keepGoing=False
    while index<len(totalData) and (testMatch!=True):
        for l in totalData:
            newTuples=get_strs(l)
            for i in newTuples:
                testMatch=find_match(newTuples,strData)
                if testMatch==True:
                    keepGoing=True
                    return l['name']
        index+=1
        if testMatch==False and keepGoing==False:
            return 'No match'
            
       




if __name__ == '__main__':
    print(dna_match(sys.argv[1], sys.argv[2]))
    
  


    