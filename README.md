<p align="center">
  <img width="400" height="400" src="https://user-images.githubusercontent.com/66196840/218777586-a365a5b2-b8ed-4f17-b067-2afd41e33958.png">
</p>

# <p align="center">Validify</p>

A python script that dynamically performs URL validation and auto-correction using multi-processing and regex.

## Key Features
- Multiprocessing: By spawning the desired number of processes, the script significantly speeds up program execution.
- Auto-correction: By utilising regex and HTTP status codes, the script attempts to auto-correct the URLs.
- Manual-correction: The script allows user to auto-correct URLs manually.

## How To Use
To clone and run this application, you'll need Git and Python3 installed on your computer. From your command line:
1. Activate the virtual environment
```
source bin/acitvate
```

2. Clone this respository
```
git clone https://github.com/theamankumarsingh/data-cleanup.git
```

3. Go into the repository
```
cd data-cleanup
```

4. Install the requirements
```
pip3 install -r requirements.txt
```

5. Run the script
```
python3 main.py (<number of threads>)
```
