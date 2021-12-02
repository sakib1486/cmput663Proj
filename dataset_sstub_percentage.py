import pandas as pd
import numpy as np
import json
import csv
import os


def sstubs_stat(df):
	#print(len(df))
	print(df.groupby(['bugType']).size())
	print(df.groupby(['bugType']).size()/len(df))



def main():

	#path to the JSON file and project repositories
	maven_json_path = "Data/sstubs"
	java_json_path = "Data/sstubsLarge"
	java_proj_dir = "/media/sakib/478407FA0B573D27/JavaProj/"

	df_maven = pd.read_json(maven_json_path)
	print(f'Maven Projects SStuBs statisitcs: \n')
	sstubs_stat(df_maven)

	d = pd.read_json(java_json_path)
	filenames = os.listdir(java_proj_dir)
	
	#filter for downloaded projects
	df_java = d[d.projectName.isin(filenames)]
	print(f'Java Projects SStuBs statisitcs: \n')
	sstubs_stat(df_java)
	
	


if __name__=='__main__':
	main()
