## CMPUT663 Project

This repository contains the _CMPUT663_ project works done titled as "**Which categories of Simple Stupid Bugs (SStuB) are missed by static analyzers?**". All scripts and dataset files are listed in specific directories. All the experiments are done on our local machines and publicly shared here.

<details open="open">
<summary>Table of Contents</summary>

- [Participants](#participants)
- [Task](#task)
- [Acknowledgement](#Acknowledgement)
- [Data Files] (#data)
- [Folders](#folders)
- [Report](#report)
- [Bibliography](#bibliography)

</details>

## Participants:

|Student name|  CCID  |
|------------|--------|
|Sakib Hasan |sakib2  |
|Nazmus Sakeef |sakeef|

## Task:
We anayzed the performances of the Static Analyzers like- _SonarQube_, _SpotBugs_ and _PMD_ on detecting simple stupid bugs from 100 Java and 100 maven porjects downloaded from the repository links available in the [ManySStuBs4j](https://datashare.ed.ac.uk/handle/10283/3424) dataset.

## Acknowledgement 

In accordance with the UofA Code of Student Behaviour, we acknowledge that  
- We have listed all external resources we consulted for this assignment.

Non-detailed oral discussion with others is permitted as long as any such discussion is summarized and acknowledged by all parties.

## Data Files
All of our data files are big in size which is beyond the accepted size limit of GitHub. The dataset files are stored here: [CMPUT663 G-Drive](https://drive.google.com/drive/folders/1g67LT82hwNFgQpElUPDzWO3tFeuA5E0N?usp=sharing) which is our dedicated drive for thisproject.

## Directories
The directory structure of the repository are as follows:

1. **BugsAdded_CodeFiles**: This directory contains the code files that we utilized for our manual scanner to scan. In these files, we manually integraetd some SStuBs for the specific pattern that our manual scanner will look for.
2. **NoBugs_CodeFiles**: This directory contains the code files that we collected where we manually integrated SStuBs. But these files are before adding bugs. If anyone wants, these files can be reued to implement newer template of bugs or number of bugs can even be increased.
3. ****

## Scripts and Code

The mining tool scripts and other filtering scripts can be found in this repository. This scripts are referenced from [ManySStuBs4J Homepage](https://zenodo.org/record/3653444#.YX18DJvF3Jx) and [mineSStuBs GitHub](https://github.com/mast-group/mineSStuBs).

## Execution steps

1. To run the mining, you have to download the datasets from the G-Drive above.
2. After that, you have to have the projects listed under topProjects.csv and 'topJavaMavenProjects.csv' file with the help of the scripts- [clone_top_repos.py](GHScripts/clone_top_repos.py) and [clone_top_maven_repos.py](GHScripts/clone_top_maven_repos.py).
3. For our experiment, we took 100 projects from Maven and Java respectively.
