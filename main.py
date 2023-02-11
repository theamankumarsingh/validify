import multiprocessing
import sys
import openpyxl
import preparation
import subprocess
import numpy as np

def launch_script_with_terminal(wb_name):
    subprocess.Popen(["gnome-terminal","--","python3","script.py",wb_name])

if len(sys.argv) < 3:
    print("Usage: python3 script.py <workbook_name> <processes>")
    sys.exit(1)
else:
    workbook_name=sys.argv[1]
process=int(sys.argv[2])
if process < 1:
    print("Error: process count must be greater than 0")
    sys.exit(1)
workbook_ext=".xlsx"
if workbook_name[-5:] == ".xlsx":
    workbook_name=workbook_name[:-5]

#read sheet from workbook
print("Preparing file "+workbook_name+workbook_ext+" for execution ...")
try:
    wb=openpyxl.load_workbook(workbook_name+workbook_ext)
except Exception as exception:
    print("Error: "+type(exception).__name__+" while reading workbook from file "+workbook_name+workbook_ext)
    sys.exit(1)
sheet=wb['Sheet1']

dataset,data_dict=preparation.prepare(sheet,duplicates=False)
dataset_t = np.array_split(dataset, process)

processes=[]
for i in range(process):
    dataset_n=list(dataset_t[i])
    wb_new = openpyxl.Workbook()
    sheet_new = wb_new['Sheet']
    sheet_new['A1']="Name"
    sheet_new['B1']="Register Number"
    sheet_new['C1']="Mobile Number"
    sheet_new['D1']="Email-Id"
    sheet_new['E1']="WebURL"
    for row in range(1,len(dataset_n)+1):
        sheet_new['A'+str(row+1)]=dataset_n[row-1][1]
        sheet_new['B'+str(row+1)]=dataset_n[row-1][2]
        sheet_new['C'+str(row+1)]=dataset_n[row-1][3]
        sheet_new['D'+str(row+1)]=dataset_n[row-1][4]
        sheet_new['E'+str(row+1)]=dataset_n[row-1][5]
    wb_new.save(workbook_name+str(i)+workbook_ext)
    processes.append(multiprocessing.Process(target=launch_script_with_terminal,args=(workbook_name+str(i),)))

#start all processes
print("Starting all processes ("+str(process)+") ...")
for p in processes:
    p.start()
input("Please wait for completion, then press enter to exit ...")
sys.exit(0)