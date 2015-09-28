*#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import sys, os, csv

boms = ["../Thinkpad/Cube/PCB/Principale/Principale--1-6.csv", 
		"../Thinkpad/Cube/PCB/Sinks/Sinks--1-6.csv", 
		"../Thinkpad/Cube/PCB/Connectique/PCB_Connectique_1-6.csv", 
		"../Thinkpad/Cube/PCB/TFT/PCB_TFT_1-6.csv", 
		"../Thinkpad/Cube/PCB/SupportPlans/Support-Plans--1.6.csv", 
		"../Thinkpad/Cube/PCB/SupportColonnes/Support-Colonnes--1.6.csv"]

def groupby(key, csvFile):
	reader = csv.reader(open(csvFile), delimiter=',')
	result = {}
	attrs = reader.next()

	for row in reader:
		if len(row) > 6:
			rkey = (row[attrs.index(key[0])], row[attrs.index(key[1])])
			result[rkey] = int(row[attrs.index(" Quantity")])

	return result

def merge(dic1, dic2):
	dic = dic1
	
	for k2 in dic2:
		if k2 in dic:
			dic[k2] += dic2[k2]
		else:
			dic[k2] = dic2[k2]
	
	return dic
	
if __name__ == "__main__":
	res = {}
	for bom in boms:
		res = merge(res, groupby((" Manufacturer"," Reference"),bom))
	print "Manufacturer,Reference,Number"
	for k in res:
		print k[0],",", k[1], ",", res[k]
