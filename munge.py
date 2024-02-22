import os
# Define file paths for the input raw data and the output clean data
filepathn = os.path.join('data', 'netflix_data.csv')
file_obj = open(filepathn,'r')

filepathc = os.path.join('data', 'clean_data.csv')
new_file = open(filepathc,'w')


def edit(line):
    new_list = []
    new_line = ""

    # working with titles that have "," 
    if line[0] == '"':

        quotations_count = 0 
        for i in line:
            if i == '"':
                quotations_count += 1
        
        # points with no commas in title will have 4 commas throughout lime
        # split successful and there are no issues with ',' in the title
        if quotations_count == 4:

            title_str = '' 
            new_line += '"'
            index = 2   # counter variable to record where the title ends

            for i in line[1::]:
                index += 1
                if i != '"':
                    title_str += i
                    new_line += i 
                else: 
                    title_str += i
                    new_list += [title_str]
                    new_line += i + ","
                    break

        # titles with '""' and no commas
        else:
            title_str = '' 
            new_line += '"'
            index = 1   # counter variable to record where the title ends
            for i in line[1::]:
                index += 1
                if i != ",":
                    title_str += i
                else:
                    break
            
            new_line += title_str + ','


    else:
        title_str = ''
        index = 0 
        for char in line: 
            index += 1
            if char != ',':
                title_str  += char
                new_line += char
            else:   # title is complete, now add to new_list 
                new_list += [title_str]
                new_line += ","
                break
    
    # adding column to determine if title is a TV show (not all TV shows can be identified)
    
    for keyword in ["Season","Temporada"]:
        if title_str.find(keyword) != -1:
            new_line += 'Yes,'
            series = True
            break
        else:
            series = False

    
    if series == False:
        new_line += 'NaN,'

        
    split_str = line[index:].strip().split(",")

    for i in [0,1]:
        if i == 0:
            new_line += split_str[i]+','

        elif i == 1:
            date = split_str[i]
            # handling missing data 
            if date == "":
                new_line += "NaN,"
            else:
                year = date[0:4]
                new_line += year+','
    

    # creating new viewership measurement
    value = ""
    for i in range(2,len(split_str)):
        for char in split_str[i]:
            if char.isnumeric():
                value += char


    value_div_by1M = int(value)/1000000
    new_list += [str(float(value_div_by1M))]
    new_line += str(float(value_div_by1M))

    return new_line
 



# skip irrelevant lines 
for i in range(6):
    line = file_obj.readline()

# write columns titles and replace "release date" for "release year" and "release month"
columns = line[1::].strip()
columns= columns.split(',')


new_file.write("Title,TV Show,Available Globally?,Premiere Year,Hours Viewed (in 1M units)"+'\n')


# iterating through each line containing streaming data for each title
for line in file_obj:
        # discarding intial ',' char -- irrelevant
    line = line[1::]

    new_file.write(str(edit(line))+'\n')
