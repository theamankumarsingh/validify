<p align="center">
  <img width="400" height="400" src="https://user-images.githubusercontent.com/66196840/218777586-a365a5b2-b8ed-4f17-b067-2afd41e33958.png">
</p>

# <p align="center">Validify</p>

A python script that dynamically performs URL validation in a database and auto-correction using multi-processing and regex.

## Key Features
- Multiprocessing: By spawning the desired number of processes, the script significantly speeds up program execution.
- Auto-correction: By utilising regex and HTTP status codes, the script attempts to auto-correct the URLs.
- Manual-correction: The script allows user to auto-correct URLs manually.

## How To Use
To clone and run this application, you'll need Git and Python3 installed on your computer. From your command line:

1. Clone this respository
```
git clone https://github.com/theamankumarsingh/validify.git
```

2. Go into the repository
```
cd validify
```

3. Create python's virtual environment
```
python3 -m venv .
```

4. Activate the virtual environment
```
source bin/acitvate
```

5. Install the requirements
```
pip3 install -r requirements.txt
```


6. Run the script
```
python3 main.py <Workbook file name (.xlsx)> <number of threads> <operating mode(optional)>
```

## Operating Modes
This script has an auto fix and a manual fix mode, as well as testing (checking) mode. These can be enabled/disabled by using operation codes:

0: auto fix is on, manual fix is off, testing is off

1: auto fix is on, manual fix is on, testing is off

2: auto fix is on, manual fix is off, testing is on

3: auto fix is on, manual fix is on, testing is on


If operating code is not specified or any number other than mentioned is specified, the script defaults to code 0.

## Note
1. Make sure that the workbook's location is in the repository itself.
2. Workbook's entries are in the format as follows:

|Name|Address|Telephone|Email ID|WebURL|
|----|-------|---------|--------|------|
|Entry1|||||
|Entry2|||||
etc.

The workbook should include the headings as well.

## Application
This script can be used to filter database of people with their details (name, address, telephone, email, URL) to ensure that data with only valid URLs remain.

## Sample Screenshot
![Sample](0.png "A sample screenshot showing script in action")