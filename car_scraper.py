import csv
import requests
from bs4 import BeautifulSoup


with open('car_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Mileage', 'Expert Rating', 'Consumer Rating'])
    for x in range(1, 26):
        start_url = 'https://www.kbb.com/car-finder/'
        if x == 1:
            middle_num = ''
        else:
            temp_num = x
            middle_num = str(temp_num)

        if x == 1:
            middle_url = ''
        else:
            middle_url = '/'
        end_url = '?mpg=over20&pricerange=0-30000&years=2018-2024'
        url = start_url + middle_num + middle_url + end_url
        response = requests.get(url, 1.0)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find('div', class_="css-a21061 e1qqueke1")
        counter = 0
        specounter = 0      
        for result in results:
            counter = counter + 1
            specifics = result.contents
            specounter = 0
            for specific in specifics:
                specounter = specounter + 1
                if specounter == 2 and counter != 2:
                    title = specific.text
                if specounter == 3 and counter != 2:
                    price = specific.find('div', class_='css-fpbjth e151py7u1')
                    my_price = price.text
                    my_price = my_price.replace('$', '')
                    my_price = my_price.replace(',', '')

                    mileages = specific.find('div', class_='css-14q4cew e19qstch13')
                    for child in mileages.descendants:
                        if 'MPG' in child.text and len(child.text) < 8 or 'N/A' in child.text:
                            mileage = child

                    my_mileage = mileage.text
                    my_mileage = my_mileage.replace('MPG', '')
                    my_mileage = my_mileage.replace(' ', '')

                    ratings = specific.find('div', class_='css-1ouitaz ex4y58i1')
                    expert_rating = ratings.contents[0]
                    my_expert = expert_rating.text
                    my_expert = my_expert.replace('Expert', '')
                    my_expert = my_expert.replace(' ', '')
                    my_expert = my_expert.replace('(', '')
                    my_expert = my_expert.replace(')', '')

                    consumer_rating = ratings.contents[1]
                    my_consumer = consumer_rating.text
                    my_consumer = my_consumer.replace('Consumer', '')
                    my_consumer = my_consumer.replace(' ', '')
                    my_consumer = my_consumer.replace('(', '')
                    my_consumer = my_consumer.replace(')', '')
                    writer.writerow([title, my_price, my_mileage, my_expert, my_consumer])

        new_results = soup.find('div', class_='css-8wywm8 e1qqueke1')
        if new_results is None:
            new_results = soup.find('div', class_="css-269gm9 e1qqueke1")
        counter = 0
        specounter = 0
        for result in new_results:
            counter = counter + 1
            specifics = result.contents
            specounter = 0
            for specific in specifics:
                specounter = specounter + 1
                if specounter == 2 and counter != 2:
                    title = specific.text
                if specounter == 3 and counter != 2:
                    price = specific.find('div', class_='css-fpbjth e151py7u1')
                    my_price = price.text
                    my_price = my_price.replace('$', '')
                    my_price = my_price.replace(',', '')

                    mileages = specific.find('div', class_='css-14q4cew e19qstch13')
                    for child in mileages.descendants:
                        if 'MPG' in child.text and len(child.text) < 8 or 'N/A' in child.text:
                            mileage = child


                    my_mileage = mileage.text
                    my_mileage = my_mileage.replace('MPG', '')
                    my_mileage = my_mileage.replace(' ', '')

                    ratings = specific.find('div', class_='css-1ouitaz ex4y58i1')
                    expert_rating = ratings.contents[0]
                    my_expert = expert_rating.text
                    my_expert = my_expert.replace('Expert', '')
                    my_expert = my_expert.replace(' ', '')
                    my_expert = my_expert.replace('(', '')
                    my_expert = my_expert.replace(')', '')

                    consumer_rating = ratings.contents[1]
                    my_consumer = consumer_rating.text
                    my_consumer = my_consumer.replace('Consumer', '')
                    my_consumer = my_consumer.replace(' ', '')
                    my_consumer = my_consumer.replace('(', '')
                    my_consumer = my_consumer.replace(')', '')
                    writer.writerow([title, my_price, my_mileage, my_expert, my_consumer])


