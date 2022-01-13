#!/usr/bin/env python
# -*- coding: utf-8 -*-

def returnlist(originallist):
	finallist=[]
	for data in originallist:
		finallist.append(data%3)
	return finallist

test=returnlist([2,7,4,7,2,9,9])
print(test)