import pandas as pd
import numpy as np
import json
import csv
import os

def main():

	#path to the JSON file and project repositories
	json_path = "Data/sstubsLarge"
	proj_dir = "Data/JavaProj/"

	filenames = os.listdir(proj_dir)
	#print(filenames)
	df = pd.read_json(json_path)

	d = df[df.projectName.isin(filenames)]
	d.to_csv(r"filteredTopProjectSStuBs.csv")
	#print(d)
	


if __name__=='__main__':
	main()
