import csv
import requests
from bs4 import BeautifulSoup


with open('car_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Mileage', 'Expert Rating', 'Consumer Rating'])
    for x in range(1, 82):
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
        end_url = '?pricerange=0-30000&years=2012-2024'
        url = start_url + middle_num + middle_url + end_url
        response = requests.get(url)
        #print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        results = soup.find('div', class_="css-a21061 e1qqueke1")
        counter = 0
        specounter = 0
        
        for result in results:
            print(counter)
            # print("Results:", result)
            # print("NEWLINE")
            counter = counter + 1
            specifics = result.contents
            specounter = 0
            for specific in specifics:
                specounter = specounter + 1
                print("counter:", specounter)
                print("NEWLINE")
                print(specific)
                print("EARLYCOUNTER:", counter)
                if specounter == 2 and counter != 2:
                    title = specific.text
                    print("TITLE:", title)
                if specounter == 3 and counter != 2:
                    price = specific.find('div', class_='css-fpbjth e151py7u1')
                    my_price = price.text
                    my_price = my_price.replace('$', '')
                    my_price = my_price.replace(',', '')
                    print("PRICE:", my_price)

                    mileages = specific.find('div', class_='css-14q4cew e19qstch13')
                    for child in mileages.descendants:
                        if 'MPG' in child.text and len(child.text) < 8:
                            mileage = child

                    my_mileage = mileage.text
                    my_mileage = my_mileage.replace('MPG', '')
                    my_mileage = my_mileage.replace(' ', '')
                    print("MILEAGE:", my_mileage)

                    # mpg = specific.find('div', class_="css-fpbjth e151py7u1")

                    ratings = specific.find('div', class_='css-1ouitaz ex4y58i1')
                    expert_rating = ratings.contents[0]
                    my_expert = expert_rating.text
                    my_expert = my_expert.replace('Expert', '')
                    my_expert = my_expert.replace(' ', '')
                    print("EXPERT RATING:", my_expert)

                    consumer_rating = ratings.contents[1]
                    my_consumer = consumer_rating.text
                    my_consumer = my_consumer.replace('Consumer', '')
                    my_consumer = my_consumer.replace(' ', '')
                    print("CONSUMER RATING:", my_consumer)
                    writer.writerow([title, my_price, my_mileage, my_expert, my_consumer])

        new_results = soup.find('div', class_='css-8wywm8 e1qqueke1')
        counter = 0
        specounter = 0
        for result in new_results:
            print(counter)
            # print("Results:", result)
            # print("NEWLINE")
            counter = counter + 1
            specifics = result.contents
            specounter = 0
            for specific in specifics:
                specounter = specounter + 1
                print("counter:", specounter)
                print("NEWLINE")
                print(specific)
                print("EARLYCOUNTER:", counter)
                if specounter == 2 and counter != 2:
                    title = specific.text
                    print("TITLE:", title)
                if specounter == 3 and counter != 2:
                    price = specific.find('div', class_='css-fpbjth e151py7u1')
                    my_price = price.text
                    my_price = my_price.replace('$', '')
                    my_price = my_price.replace(',', '')
                    print("PRICE:", my_price)

                    mileages = specific.find('div', class_='css-14q4cew e19qstch13')
                    for child in mileages.descendants:
                        if 'MPG' in child.text and len(child.text) < 8 or 'N/A' in child.text:
                            mileage = child


                    my_mileage = mileage.text
                    my_mileage = my_mileage.replace('MPG', '')
                    my_mileage = my_mileage.replace(' ', '')
                    print("MILEAGE:", my_mileage)

                    # mpg = specific.find('div', class_="css-fpbjth e151py7u1")

                    ratings = specific.find('div', class_='css-1ouitaz ex4y58i1')
                    expert_rating = ratings.contents[0]
                    my_expert = expert_rating.text
                    my_expert = my_expert.replace('Expert', '')
                    my_expert = my_expert.replace(' ', '')
                    print("EXPERT RATING:", my_expert)

                    consumer_rating = ratings.contents[1]
                    my_consumer = consumer_rating.text
                    my_consumer = my_consumer.replace('Consumer', '')
                    my_consumer = my_consumer.replace(' ', '')
                    print("CONSUMER RATING:", my_consumer)
                    writer.writerow([title, my_price, my_mileage, my_expert, my_consumer])
    # print(my_title)
    # print(my_price)
    # print(my_mileage)
    # print(my_expert)
    # print(my_consumer)


