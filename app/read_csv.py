import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        data = []
 #       data_population = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
#            population_dict = {header[i]: row[i] for i in [2, 5, 6, 7, 8, 9, 10, 11, 12]}
            data.append(country_dict)
#            data_population.append(population_dict)
        

        return data

if __name__ == '__main__':
    data = read_csv('data.csv')
    print(data[0])


