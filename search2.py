#loading the inverted_index to the program 
import pickle
fileObject=open("Inverted_index",'rb')
inverted = pickle.load(fileObject)



_STOP_WORDS = frozenset([
"and", "but", "is", "the", "to"])





def word_split(text):
    """
    Split a text in words. Returns a list of 
    (word, positions) location is a list of position of the word.
    """
    word_list = []
    wcurrent = []
    windex = None
    o_w_list=text.split()
    for i in range (len(o_w_list)):
        word_list.append((i,o_w_list[i]))
    
    return word_list


def words_normalize(words):
    """
    Do a normalization precess on words. In this case is just a to lower(),
    """
    normalized_words = []
    for word in words:
        wnormalized = word.lower()
        normalized_words.append((wnormalized))
    return normalized_words





def words_cleanup(words):
    """
    Remove words stopwords.
    """
    cleaned_words = []
    for word in words:
        if word in _STOP_WORDS:
            continue
        cleaned_words.append((word))
    return cleaned_words






def search(inverted, query):
#     """
#     Returns a set of documents id that contains all the words in your query.
#     """
    result = {}
    if query in inverted.keys():
        result[query]=inverted[query]
    return result


# Update the list of positions by deleting the common id.
def delete_id (dic,common_id):
    for key in dic.keys():
        for i in list(dic[key].keys()):
            if i in common_id:
                dic[key].pop(i)
    return dic

#return the list of positions inside a dic
def find_id (dic):
    res=[]
    for key in dic:
        res.extend(list(dic[key].keys()))
    return res

#find the list of id doesnot belongs to lst1 or lst2
def find_delete_id(lst1,lst2):
    return list(set(lst1) ^ set(lst2))



import copy
def boolean_search(inverted_new,q_str):
    q_lst=q_str.split()
    q_lst=words_normalize(q_lst)
    c_res={}
    i=0
    inverted=copy.deepcopy(inverted_new)
    while i<len(q_lst):
        if q_lst[i]=='and' and i+1<len(q_lst):
            s_next=search(inverted,q_lst[i+1])
            if s_next=={} or c_res=={}:
                for key in c_res:
                    c_res[key]={}
                c_res[q_lst[i+1]]={}
                i+=1
            else:
                id1=find_id(c_res)
                id2=find_id(s_next)
                d_id=find_delete_id(id1,id2)
                delete_id(c_res,d_id)
                delete_id(s_next,d_id)
                c_res[q_lst[i+1]]=s_next[q_lst[i+1]]
                i+=1
        if q_lst[i]=='or':
            s_then=search(inverted_new,q_lst[i+1])
            c_res[q_lst[i+1]]=s_then[q_lst[i+1]]
            i+=1
        if i==0:
            c_res=search(inverted,q_lst[i])
        i+=1
    print (c_res)    
    return c_res

def main():
    q_str = str(input("Please a query or a boolean query:   \n"))
    q_str=''.join([i for i in q_str if not i.isdigit()])
    boolean_search(inverted,q_str)

main()
