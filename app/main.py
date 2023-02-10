import utils
import read_csv
import charts



def run():
    data = read_csv.read_csv('data.csv')
    
    que_ver = input('quieres ver la poblaion_mundial o un_pais ')
    if que_ver == 'un_pais':
        country = input('type country =>')
 
        result = utils.population_by_country(data, country)

        if len(result) > 0:
            country = result[0]
            labels, values = utils.get_population(country)
            print(labels, values)
            charts.show_chart(labels, values, tipo='bar')
    elif que_ver == 'poblaion_mundial':
        labels, values = utils.country_percentage(data)
        charts.show_chart(labels, values, tipo='pie')



if __name__ == '__main__':
    run()