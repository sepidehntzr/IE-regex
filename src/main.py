import copy
from itertools import count
import re
import argparse
import glob
import csv

## Positional Command-line Arguments

parser = argparse.ArgumentParser("Search for date expressions in news texts")
parser.add_argument("input_path", help="Path to the data directory")
parser.add_argument("output_path",help="Path to the output CSV file")
args = parser.parse_args()
"the day afte ..."
# simple_date_pattern1 = "(?:[Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]gust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember),\s*[0-9]{0,4}"
# print(re.match(r"[1-9][0-9]{0,3}","2034"))
month = r"([Jj]an\.|[Jj]anuary|[Ff]eb\.|[Ff]ebruary|[Mm]arch|[Aa]pril|[M]ay|[Jj]une|[Jj]uly|[Aa]ug\.|[Aa]gust|[Ss]ep\.|[Ss]eptember|[Oo]ct\.|[Oo]ctober|[Nn]ov\.|[Nn]ovember|[Dd]ec\.|[Dd]ecember)"
year = r"([1-9][0-9]{3})"
relative_year_month_week = r"((?:[Nn]ext|[Ll]ast|[Tt]his|[Tt]hese)\s+(?:([Mm]onday|[Tt]uesday|[Ww]ednesday|[Tt]hursday|[Ff]riday|[Ss]aturday|[Ss]unday)|days?|[Ww]eekday|[Ww]eekend|[Ww]eek|month|year|decade|century|millennium))"
month_relative_year= r"(([Jj]an\.|[Jj]anuary|[Ff]eb\.|[Ff]ebruary|[Mm]arch|[Aa]pril|[M]ay|[Jj]une|[Jj]uly|[Aa]ug\.|[Aa]gust|[Ss]ep\.|[Ss]eptember|[Oo]ct\.|[Oo]ctober|[Nn]ov\.|[Nn]ovember|[Dd]ec\.|[Dd]ecember)\s+(?:[Nn]ext|[Ll]ast|[Tt]his)\s+year)"
dayofweek= "([Mm]onday|[Tt]uesday|[Ww]ednesday|[Tt]hursday|[Ff]riday|[Ss]aturday|[Ss]unday)"
part_of_relative_year_month_week = r"((?:[Ee]arly|[Ll]ate|[Ll]ater)(?:[Nn]ext|[Tt]his)\s+(?:day|[Ww]eekend|[Ww]eek|month|year|decade|century|millennium))"
day_month = r"((?:(?:[1-2][0-9]?)|(?:3[0-1])|(?:[0-9]))\s+(?:[Jj]an\.|[Jj]anuary|[Ff]eb\.|[Ff]ebruary|[Mm]arch|[Aa]pril|[M]ay|[Jj]une|[Jj]uly|[Aa]ug\.|[Aa]gust|[Ss]ep\.|[Ss]eptember|[Oo]ct\.|[Oo]ctober|[Nn]ov\.|[Nn]ovember|[Dd]ec\.|[Dd]ecember))"
month_year = r"((?:[Jj]an\.|[Jj]anuary|[Ff]eb\.|[Ff]ebruary|[Mm]arch|[Aa]pril|[M]ay|[Jj]une|[Jj]uly|[Aa]ug\.|[Aa]gust|[Ss]ep\.|[Ss]eptember|[Oo]ct\.|[Oo]ctober|[Nn]ov\.|[Nn]ovember|[Dd]ec\.|[Dd]ecember)\s+[1-9][0-9]{0,3})"
day_month_year = r"((?:(?:[1-2][0-9]?)|(?:3[0-1])|(?:[0-9]))\s+([Jj]an\.|[Jj]anuary|[Ff]eb\.|[Ff]ebruary|[Mm]arch|[Aa]pril|[M]ay|[Jj]une|[Jj]uly|[Aa]ug\.|[Aa]gust|[Ss]ep\.|[Ss]eptember|[Oo]ct\.|[Oo]ctober|[Nn]ov\.|[Nn]ovember|[Dd]ec\.|[Dd]ecember)\s+([1-9][0-9]{0,3}))"
decade = r"([Tt]he\s+[1-9][0-9]{1,3}s)"
patterns = [day_month_year,month_relative_year,part_of_relative_year_month_week,relative_year_month_week,day_month,month_year,decade,dayofweek,month,year]
simple_date_pattern12 = None
simple_date_pattern13 = None
deictic_date_pattern1 = None
deictic_date_pattern2 = None
deictic_date_pattern3 = None
deictic_date_pattern4 = None
deictic_date_pattern5 = None
deictic_date_pattern6 = None
deictic_date_pattern7 = None
deictic_date_pattern8 = None
deictic_date_pattern9 = None
deictic_date_pattern10 = None

def write_to_csv(data):
    f = open(args.output_path,"a")
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

def text_to_smaller_chunks(text):
    sentences=[]
    for match in re.finditer("((?:[^\.\s]+\.?[^\.]+)+[\.\?!]+\s+)",text):
        sentences.append((match.group(), match.start()))
        #print("match", count, match.group(), "start index", match.start())
    return sentences

def search_for_date(text):
    pass
    
def read_input_file(input_path):
        f = open(input_path,"r")
        text = f.read()
        f.close()
        return text
        

    

for single_input_path in glob.glob(args.input_path+"/*"):
        text = read_input_file("data/dev/1003.txt")
        save_month_in_date_expression_index = []
        save_year_in_date_expression_index = []
        save_week_in_date_expression_index = []
        print("shg")
        sentences =text_to_smaller_chunks(text)
        print("dsf")
        for sentence in sentences:
            temp_sentence = copy.deepcopy(sentence[0])
            for pattern in patterns:

                for match in re.finditer(pattern,temp_sentence):
                    print((match.group(), match.start()+sentence[1]))
                    temp_sentence=temp_sentence.replace (match.group(), len(match.group())*"#",1)
                    print("hi")
            
                 

            
        break


