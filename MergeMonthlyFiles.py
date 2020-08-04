import os
import shutil
import glob
import pandas as pd



source = os.listdir("e:/Files/")
destination = "e:/AllFiles/"
copy files into one location
for root, dirs, files in os.walk('e:/Files/'):
    for file in files:
        path_file = os.path.join(root, file)
        shutil.copy2(path_file, 'e:/AllFiles/')  # change you destination dir
os.chdir("E:\AllFiles")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "BlueBikesData.csv", index=False, encoding='utf-8-sig')