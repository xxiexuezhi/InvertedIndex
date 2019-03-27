#This program is desgiend for structured data, assignment 2. Inverted index. 
#The purpose of this program is to build up an inverted index for any word docuemnt.


_STOP_WORDS = frozenset([
    'and','but','is','the','to'])

def word_split(text):
    """
    Split a text in words. Returns a list of element that (word, positions) position is the position of the word.
    """
    word_list = []
    wcurrent = []
    windex = None
    o_w_list=text.split()
    for i in range (len(o_w_list)):
        word_list.append((i+1,o_w_list[i]))
    
    return word_list


def words_cleanup(words):
    """
    Remove the stopwords.
    """
    cleaned_words = []
    for index, word in words:
        if  word in _STOP_WORDS:
            continue
        cleaned_words.append((index, word))
    return cleaned_words

def words_normalize(words):
    """
    Do a normalization precess on words. In this case is just a to lower(),
    """
    normalized_words = []
    for index, word in words:
        wnormalized = word.lower()
        normalized_words.append((index, wnormalized))
    return normalized_words

import re
import string
def word_index(text):
    """
    Removing numbers and symbols.
    It calls word split, normalize and cleanup.
    """
    translator = str.maketrans( ".", ",", string.punctuation)
    text=text.translate(translator)
    text=''.join(i for i in text if not i.isdigit())
    text=re.sub(r'([^\s\w]|_)+','',text)
    words = word_split(text)
    words = words_normalize(words)
    words = words_cleanup(words)
    return words

def inverted_index(text):
    """
    Create an Inverted-Index of the text document.
        {word:[positions]}
    """
    inverted = {}

    for index, word in word_index(text):
        locations = inverted.setdefault(word, [])
        locations.append(index)

    return inverted

def inverted_index_add(inverted, doc_id, doc_index):
    """
    Add Invertd-Index doc_index of the document doc_id to the 
    Multi-Document Inverted-Index (inverted), 
    using doc_id as document identifier.
        {word:{doc_id:[locations]}}
    """
    for word, locations in doc_index.items():
        indices = inverted.setdefault(word, {})
        indices[doc_id] = locations
    return inverted

my_documents = {}

import sys
for n in sys.argv[1:]:
    input=open(n,"r")
    my_documents[n] =input.read().replace('\n',' ')
#print (my_documents)

if __name__ == '__main__':
     # Build Inverted-Index for documents
    inverted = {}
    for doc_id, text in my_documents.items():
        doc_index = inverted_index(text)
        inverted_index_add(inverted, doc_id, doc_index)
    print(inverted) 
    
    
    import pickle
    fileObject=open("Inverted_index",'wb')
    pickle.dump(inverted,fileObject)
