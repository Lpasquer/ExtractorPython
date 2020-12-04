import os
import csv

def difference(csv_file_gt, csv_file_tc):
    with open(f'Ground_truth/{csv_file_gt}', 'r') as gt, open(f'Csv_to_check/{csv_file_tc}', 'r') as tc:
        ground_truth = gt.readlines()
        csv_to_check = tc.readlines()

    dircsv = './Result_ground_truth'
    if not os.path.exists(dircsv): #we check if the directory output exists
        os.mkdir(dircsv) #if not, we create one
    with open(f'Result_ground_truth/Result_{csv_file_tc}', 'w') as result:
        for line in csv_to_check:
            if line not in ground_truth:
                result.write(line) #if a line is different, put this line in result file


def Comparison_ground_truth():
    list_file_ground_truth = []
    list_file_to_check = []
    path = os.getcwd()
    for root, dirs, files in os.walk(path): #read of current directory
        for file in dirs:
            if file == "Ground_truth":
                for root, dirs, files in os.walk(file): #read directory "Ground_truth"
                    for file in files:
                        list_file_ground_truth.append(file)
            if file == "Csv_to_check":
                for root, dirs, files in os.walk(file): #read directory "Ground_truth"
                    for file in files:
                        list_file_to_check.append(file)

    for line, line2 in zip(list_file_ground_truth, list_file_to_check):
        difference(line, line2)

#this fonction will delete all empty file in Result_ground_truth 
#which means the extractor output csv file is equal to the ground truth
def purge(): 
    list_file_to_delete = []
    path = './Result_ground_truth'
    for root, dirs, files in os.walk(path): #read of current directory
        for file in files:
            with open(f'{path}/{file}', 'r') as f:
                if f.read() == "": #if file is empty, we will delete it
                    list_file_to_delete.append(file)

        for line in list_file_to_delete:
            os.remove(f'{path}/{line}') #delete all file empty

def run():
    Comparison_ground_truth()
    purge()

if __name__ == "__main__":
    run()
