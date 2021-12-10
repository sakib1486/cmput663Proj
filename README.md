## CMPUT663 Project

This repository contains the _CMPUT663_ project works done titled as "**Which categories of Simple Stupid Bugs (SStuB) are missed by static analyzers?**". All scripts and dataset files are listed in specific directories. All the experiments are done on our local machines and publicly shared here.

<details open="open">
<summary>Table of Contents</summary>

- [Participants](#participants)
- [Task](#task)
- [Acknowledgement](#Acknowledgement)
- [Data] (#data)
- [Directories](#directories)
- [Execution] (#execution)
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

## Data
All of our data files are big in size which is beyond the accepted size limit of GitHub. The dataset files are stored here: [CMPUT663 G-Drive](https://drive.google.com/drive/folders/1g67LT82hwNFgQpElUPDzWO3tFeuA5E0N?usp=sharing) which is our dedicated drive for thisproject. For analysis, one has to download the necessary data files.

## Directories
The directory structure of the repository are as follows:

1. **BugsAdded_CodeFiles**: This directory contains the code files that we utilized for our manual scanner to scan. In these files, we manually integraetd some SStuBs for the specific pattern that our manual scanner will look for.
2. **NoBugs_CodeFiles**: This directory contains the code files that we collected where we manually integrated SStuBs. But these files are before adding bugs. If anyone wants, these files can be reued to implement newer template of bugs or number of bugs can even be increased.
3. **ImplementedScripts**: This directory contains the scripts that we implemented for our analysis. The execution instructions for these scripts are described later.
4. **ScriptsForDataCollection**: This directory contains the original scripts from the [_ManySStuBs4j_](https://github.com/mast-group/mineSStuBs) dataset's official GitHub repository. We used these scripts to download the projects that were used for static analysis through the analyzer tools.
5. **ScannedReports**: These directories contain the scanned reports in _.csv_ formats. There are four files here. 
  - [MethodsArgumentsCheck.csv](ScannedReports/MethodsArgumentsCheck.csv) contains the reports of our manual scanner on the code files that are available in [here](BugsAdded_CodeFiles/)
  - [SonarQube_Rerport.csv](ScannedReports/SonarQube_Report.csv) contains the SonarQube scan reports on our selected projects from Maven and Java.
  - [spotbugs_bugs_java.csv](ScannedReports/spotbugs_bugs_java.csv) contains the SpotBugs scan reports on our selected Java projects.
  - [spotbugs_bugs_maven.csv](ScannedReports/spotbugs_bugs_maven.csv) contains the SpotBugs scan reports on our selected Maven projects.


## Execution

1. To run the mining, you have to download the datasets from the [G-Drive](https://drive.google.com/drive/folders/1g67LT82hwNFgQpElUPDzWO3tFeuA5E0N?usp=sharing).
2. After that, you have to have the projects listed under topProjects.csv and 'topJavaMavenProjects.csv' file with the help of the scripts- [clone_top_repos.py](Scripts For Data Collection/clone_top_repos.py) and [clone_top_maven_repos.py](Scripts For Data Collection/clone_top_maven_repos.py). We can choose any number of projects
3. For our experiment, we took 100 projects from Maven and Java respectively. The next step is to scan the projects wtih the static analyzers of anyone's choice, and filtering out the desired SStuBs' patterns to analyze. The execution steps for the static analyzers that we used can be achieved here- [SonarQube](https://github.com/SonarSource/sonarqube), [SpotBugs](https://github.com/spotbugs/spotbugs), and [PMD](https://pmd.github.io/).
4. **Manuak Scanning**: To manually scan a Java file for the two templates of SStuBs named "_Same Function More Args_" and "_Same Function Less Args_" can be achieved by running the folowing command-

`python3 ImplementedScripts/manualScanner.py`

This scanner can only analyze one single file at a time. The scanner is not optimized yet, thus the path to the file that one wants to scan has to be manually edited in the [Scanner](ImplementedScripts/manualScanner.py) file.




