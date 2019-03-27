#! /usr/bin/python

from sys import stdin
import re

index = {}

for line in stdin:
	line=line.strip()
        word, docID = line.split('\t')

        index.setdefault(word, [])
	if docID not in index[word]:
		index[word].append(docID)

for key in index:
	print '%s\t%s' %(key, ','.join(map(str,index[key])))
	
#print index

#        for posting in postings.split(','):
 #               doc_id, count = posting.split(':')
 #               count = int(count)
#
 #               index[word].setdefault(doc_id, 0)
 #               index[word][doc_id] += count

#for word in index:
 #       postings_list = ["%s:%d" % (doc_id, index[word][doc_id])
  #                       for doc_id in index[word]]

   #     postings = ','.join(postings_list)
    #    print('%s\t%s' % (word, postings))
