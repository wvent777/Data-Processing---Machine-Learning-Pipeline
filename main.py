# Project-1 - Basic Steps for processing data
import csv
import collections

# 1.1 Loading Data
# This function will load the data from
# a csv file to a dictionary with the column names as keys
abalonepath = 'abalone.data'
abaloneheader = ['Sex', 'Length', 'Diameter', 'Height', 'Whole Weight', 'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings']


def load_data(path, header):
    # Data is going to be loaded into a dictionary
    # a temporary file will be created to write the column names in the first row
    with open('temp_file.csv', 'w', newline='') as tempfile:
        writer = csv.writer(tempfile, delimiter=",")
        writer.writerow(header)
        # afterwards the data will be open and be written into the temporary file
        with open(path, 'r') as data:
            reader = csv.reader(data)
            writer.writerows(reader)
    tempfile.close()

    # using a default dictionary so no key errors are raised
    dictionary = collections.defaultdict(list)

    with open('temp_file.csv', 'r', encoding='utf8') as file:
        reader2 = csv.DictReader(file)
        for row in reader2:
            for key, value in row.items():
                dictionary[key].append(value)
    return dictionary  # returns the dictionary dataset


abalone_dataset = load_data(abalonepath, abaloneheader)


# print(dataset['Sex'])

# Converts lists within dictionary to float, otherwise values stay as strings
# If a value cannot be converted to a float then it will be ignored 
def floatconvert(dataset):
    for key in dataset.keys():  # iterates through all of the keys in dictionary
        float_list = []
        for index in dataset[key]:  # goes through each value of list
            try:
                float_list.append(float(index))  # if it is possible it will convert it to a float
            except ValueError:  # if it is not possible it will ignore and continue
                float_list.append(index)
                continue
            dataset[key] = float_list
    return dataset


#floatconvert(abalone_dataset)
#print(abalone_dataset)

# Converts lists within dictionary to integer, otherwise values stay as strings
# If a value cannot be converted to a integer then it will be ignored
def integerconvert(dataset):
    for key in dataset.keys():  # iterates through all of the keys in dictionary
        integer_list = []
        for index in dataset[key]:  # goes through each value of list
            try:
                integer_list.append(int(index))  # if possible it will convert value to an integer
            except ValueError:  # if not possible it will ignore it and continue
                integer_list.append(index)
                continue
            dataset[key] = integer_list
    return dataset

# 1.2 Handling Missing Values
breastpath = 'breast-cancer-wisconsin.data'
breastheader = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion',
                'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']

print ('This is the breast data')
breast_dataset = load_data(breastpath, breastheader)

floatconvert(breast_dataset)
#print(breast_dataset["Bare Nuclei"])
# This will impute missing value with the mean of the column
def impute_missing(dataset):  #not the whole dictionary, just the specific column that is being looked at
    mean_list = []  # empty list to add the numbers that are floats
    for index in dataset:
        if isinstance(index,float) == True:  # if i is a float then it will append to the list
            mean_list.append(index)
        else:   # if it is not then it will be skipped
            continue

    average = sum(mean_list)/len(mean_list)  # the average is now calculated

    new_list = []
    for index in dataset:
        if isinstance(index, float) == True:    # if it a float it will append to new list
            new_list.append(index)
        else:
            new_list.append(average)    # if it is not a float it will be replaced with the average calculated earlier
    return new_list

breast_dataset["Bare Nuclei"] = impute_missing(breast_dataset["Bare Nuclei"])
print('this is testing it out')
print(breast_dataset["Bare Nuclei"])

# 1.3 Handling Categorical Data

# a. Ordinal Data
# Order Matters (ex. education levels)
def ordinal_encode(dataset, value_map):
    new_dataset = {}
    for key, value in dataset.items():
        lst = list(map(value_map.get, value))
        new_dataset[key] = lst
    return new_dataset

# b. Nominal data
# One-Hot Encoding
def nominal_encode(data, categories):
    mapping = {}
    for index in range(len(categories)):
        mapping[categories[index]] = index
    one_hot = []
    #print(mapping)

    for value in data:
        data = one_hot
        array = [0]*len(categories)
        array[mapping[value]] = 1
        one_hot.append(array)
    #print(data)
    return data
#Totalsex = ['M','F','I']
#abalone_dataset['Sex'] = nominal_encode(abalone_dataset['Sex'], Totalsex)
#print(abalone_dataset['Sex'])

# 1.4 Discretization
def discretize(ds, bins=int, distype=int):
    maxval = max(ds)
    #print(maxval)

    minval = min(ds)
    #print(minval)
    size = len(ds)
    # equal width discretization
    # good for outliers
    if distype == 0:
        # width is width of each interval
        width = (maxval - minval) / size
        widtharr = []
        # print(width)
        for i in range(0, bins + 1):
            widtharr = widtharr + [minval + width * i]
        # print("widtharray", widtharr)
        res = []
        for i in range(0, bins):
            group = []
            for x in ds:
                if widtharr[i] <= x <= widtharr[i + 1]:
                    group += [x]
            res +=[group]
        return res
    # equal-frequency discretization
    # not good for outliers
    elif distype == 1:
        depth = int(size / bins)
        out = []
        for i in range(0, bins):
            res = []
            for j in range(i * depth, (i + 1) * depth):
                if j > size:
                    break
                res = res + [ds[j]]
            out += [res]
        return out
    else:
        print('Type is not a 0 (equal width discretization) or 1 (equal frequency discretization)')


# 1.5 Standardization


# 1.6 Cross Validation

# 1.7 Evaluation Metrics

# 1.8 Learning Algorithms




