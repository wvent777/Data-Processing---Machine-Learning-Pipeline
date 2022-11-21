def load_data(file_name):
    dataset = []
    with open (file_name,'r') as data:
        csv_reader = reader(data)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset
file_name = 'pima-indians-diabetes.csv'
dataset = load_data(file_name)