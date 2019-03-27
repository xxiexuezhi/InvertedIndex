# this program is to search based on a inverted_index file named result


import string


inverted={}

f=open("result","r")
for line in f:
	line=line.strip()
	word,docID = line.split("\t")
	IDlst=docID.split(',')
	inverted[word]=IDlst

def search(inverted, query):
    """
    """
    result=[]
    if query in inverted:
        result=inverted[query]
    return result



def find_and (lst1,lst2):
    if lst1==[] or lst2==[]:
	return []
    return list(set(lst1).intersection(lst2))


def find_or (lst1,lst2):
    new_lst= lst1+lst2
    return new_lst




def boolean_search(inverted,q_str):
    q_str=q_str.translate(None, string.punctuation)
    q_lst=q_str.split()
    c_res=[]
    i=0
    while i<len(q_lst):
        if q_lst[i]=='and' and i+1<len(q_lst):
            c_res=find_and(c_res,search(inverted,q_lst[i+1]))
            i+=1
        if q_lst[i]=='or' and i+1 <len(q_lst):
            c_res=find_or(c_res,search(inverted,q_lst[i+1]))
            i+=1
        if i==0:
            c_res=search(inverted,q_lst[i])
        i+=1
	c_res=list(set(c_res))
    return c_res


def main():
	q_str=raw_input("please input the query: \n")
	print (boolean_search(inverted,q_str))

main()
