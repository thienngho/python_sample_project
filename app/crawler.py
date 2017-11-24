import requests
import json
from bs4 import BeautifulSoup

def crawler(url, model_type):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = {}
    data[model_type] = []

    temps = [t for t in soup.find_all(class_='rt')]

    for t in temps:
        item = {}        
        model = t.find(class_='rt-h').get_text().split()
        item['Year'] = model[0]
        item['Model'] = ' '.join(model[1:])
        item['Summary'] = t.find(class_='description').get_text()

        data[model_type].append(item)
    return data

if __name__ == '__main__':
    url1 = "http://www.nydailynews.com/autos/types/sports-car"
    model_type1 = "sport"
    res_data1 = crawler(url1, model_type1)

    with open('data/'+model_type1+'.json', 'w') as outfile1:
        json.dump(res_data1, outfile1)

    url2 = "http://www.nydailynews.com/autos/types/truck"
    model_type2 = "truck"
    res_data2 = crawler(url2, model_type2)

    with open('data/'+model_type2+'.json', 'w') as outfile2:
        json.dump(res_data2, outfile2)
