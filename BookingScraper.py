import requests
from bs4 import BeautifulSoup
from operator import attrgetter
from datetime import date, timedelta




def get_checkin_date():     # Funkcja do pobrania daty zameldowania
    while True:
        try:
            chekingDates = [date.today() + timedelta(days=i) for i in range(10)]  # Generujemy listę dat od dzisiaj do 10 dni w przód
            for index, dateItem in enumerate(chekingDates, start=1):
                print(f"{index}. {dateItem}")
            checkinDateIndex = input("Podaj datę zameldowania:")  # Pobieramy wybór użytkownika

            if 1 <= int(checkinDateIndex) <= len(chekingDates):  # Sprawdzamy, czy wybór jest poprawny
                checkinDate = chekingDates[int(checkinDateIndex) - 1]
            else:
                raise ValueError("Nieprawidłowy wybór")
            return checkinDate
        except ValueError as e:
            print(e)
            print("Proszę spróbować ponownie.\n")

def get_checkout_date(checkinDate): # Funkcja do pobrania daty wymeldowania
    while True:
        try:
            checkoutDates = [checkinDate + timedelta(days=i) for i in range(1, 10)]  # Generujemy listę dat od daty zameldowania do 9 dni w przód
            for index, dateItem in enumerate(checkoutDates, start=1):
                print(f"{index}. {dateItem}")
            checkoutDateIndex = input("Podaj datę wymeldowania:")  # Pobieramy wybór użytkownika

            if 1 <= int(checkoutDateIndex) <= len(checkoutDates):  # Sprawdzamy, czy wybór jest poprawny
                checkoutDate = checkoutDates[int(checkoutDateIndex) - 1]
            else:
                raise ValueError("Nieprawidłowy wybór")
            return checkoutDate
        except ValueError as e:
            print(e)
            print("Proszę spróbować ponownie.\n")

def trip_details(): # Funkcja do pobrania szczegółów podróży
    checkinDate = get_checkin_date()
    checkoutDate = get_checkout_date(checkinDate)
    while True:
        try:
            adultsGroup = input("Podaj liczbę dorosłych:")  # Pobieramy liczbę dorosłych
            if 1 <= int(adultsGroup):
                childrenGroup = input("Podaj liczbę dzieci (0 - 17 lat, max. 10):")  # Pobieramy liczbę dzieci
                if 0 <= int(childrenGroup) and 10 >= int(childrenGroup):
                    childrenGroupTotalAge = ['']  # Tworzymy pustą listę na wiek dzieci
                    for i in range(1, int(childrenGroup) + 1):
                        childrenGroupAge = input(f"Podaj wiek dziecka {i}: ")  # Pobieramy wiek każdego dziecka
                        if 0 <= int(childrenGroupAge) and 17 >= int(childrenGroupAge):
                            childrenGroupTotalAge.append(str(childrenGroupAge))  # Dodajemy wiek dziecka do listy
                        else:
                            raise ValueError("Nieprawidłowy wybór")
                    childrenGroupTotalAge = '&age='.join(childrenGroupTotalAge)  # Łączymy wieki dzieci w jednego stringa
                    print(childrenGroupTotalAge)
                else:
                    raise ValueError("Nieprawidłowy wybór")
            else:
                raise ValueError("Nieprawidłowy wybór")
            return adultsGroup, childrenGroup, checkinDate, checkoutDate, childrenGroupTotalAge  # Zwracamy wszystkie zebrane dane
        except ValueError as e:
            print(e)
            print("Proszę spróbować ponownie.\n")


# Ustalamy nagłówki, aby symulować żądanie przeglądarki
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, jak Gecko) Chrome/107.0.0.0 Safari/537.36"
}

def choose_city(adulsGroup, childrenGroup, checkinDate, checkoutDate, childrenGroupTotalAge):   # Funkcja do wyboru miasta
    cities = ['Kraków', 'Warszawa', 'Gdańsk']
    while True:
        try:
            for index, city in enumerate(cities, start=1):
                print(f"{index}. {city}")
            city_code = input("Wybierz miasto:")  # Pobieramy wybór użytkownika
            if city_code == '1':
                target_url = f"https://www.booking.com/searchresults.html?ss=Krakow%2C+Poland&ssne=Gdańsk&ssne_untouched=Gdańsk&label=gen173nr-1FCAEoggI46AdIM1gEaLYBiAEBmAExuAEHyAEN2AEB6AEB-AEJiAIBqAIDuAL0jbiyBsACAdICJDhjZmFlZmE1LWM2YmQtNDg1MS1iZWZjLTE1MDgzOTgyNjdhMtgCBuACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-510625&dest_type=city&checkin={checkinDate}&checkout={checkoutDate}&group_adults={adulsGroup}&no_rooms=1&group_children={childrenGroup}{childrenGroupTotalAge}"
            elif city_code == '2':
                target_url = f"https://www.booking.com/searchresults.html?ss=Warsaw&ssne=Warsaw&ssne_untouched=Warsaw&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaLYBiAEBmAExuAEHyAEN2AEB6AEB-AEJiAIBqAIDuAL0jbiyBsACAdICJDhjZmFlZmE1LWM2YmQtNDg1MS1iZWZjLTE1MDgzOTgyNjdhMtgCBuACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-534433&dest_type=city&checkin={checkinDate}&checkout={checkoutDate}&group_adults={adulsGroup}&no_rooms=1&group_children={childrenGroup}{childrenGroupTotalAge}"
            elif city_code == '3':
                target_url = f"https://www.booking.com/searchresults.html?ss=Gdańsk&ssne=Gdańsk&ssne_untouched=Gdańsk&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaLYBiAEBmAExuAEHyAEN2AEB6AEB-AEJiAIBqAIDuAL0jbiyBsACAdICJDhjZmFlZmE1LWM2YmQtNDg1MS1iZWZjLTE1MDgzOTgyNjdhMtgCBuACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-501400&dest_type=city&checkin={checkinDate}&checkout={checkoutDate}&group_adults={adulsGroup}&no_rooms=1&group_children={childrenGroup}{childrenGroupTotalAge}"
            else:
                raise ValueError("Nieprawidłowy wybór")
            return target_url  # Zwracamy wygenerowany URL z parametrami wyszukiwania
        except ValueError as e:
            print(e)
            print("Proszę spróbować ponownie.\n")


# Parsing funkcja
def scrape_hotels(target_url):
    response = requests.get(target_url, headers=headers)  # Wysyłamy żądanie do URL

    soup = BeautifulSoup(response.text, 'html.parser')  # Parsujemy otrzymaną stronę HTML
    if response.status_code == 200:  # Sprawdzamy, czy odpowiedź była pomyślna
        class Hotel: # Klasa do przechowywania informacji o hotelu
            def __init__(self, name, address, rating, room, description, price):
                self.name = name
                self.address = address
                self.rating = rating
                self.room = room
                self.description = description
                self.price = price

        # Tworzymy listę do przechowywania hoteli
        hotels_list = []

        # Wyciągamy informacje o każdym hotelu
        hotel_elements = soup.find_all("div", class_="c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 c6710787a4")
        for element in hotel_elements[:10]:  # Ograniczamy liczbę hoteli do 10
            name = element.find("div", class_="f6431b446c a15b38c233") # Wyciągamy nazwę hotelu
            name = name.text if name else "Brak danych"
            address = element.find("span", class_="aee5343fdb def9bc142a")  # Wyciągamy adres hotelu
            address = address.text if address else "Brak danych"
            rating = element.find("div", class_="a3b8729ab1 d86cee9b25")  # Wyciągamy ocenę hotelu
            rating = rating.text if rating else "Brak danych"
            room = element.find("h4", class_="abf093bdfe e8f7c070a7")  # Wyciągamy typ pokoju
            room = room.text if room else "Brak danych"
            description = element.find("div", class_="abf093bdfe f45d8e4c32")  # Wyciągamy opis hotelu
            description = description.text if description else "Brak danych"
            price = element.find("span", class_="f6431b446c fbfd7c1165 e84eb96b1f")  # Wyciągamy cenę i konwertujemy ją na liczbę całkowitą
            price = int(price.text[:-3].replace(',', '')) if price else 0

            hotel = Hotel(name, address, rating, room, description, price)  # Tworzymy obiekt hotelu
            hotels_list.append(hotel)  # Dodajemy hotel do listy

        def sort_hotels(hotels_list):   # Funkcja do sortowania hoteli
            sortWays = ['Cena', 'Nazwa', 'Ocena', 'Exit']  # Opcje sortowania
            for index, sortWay in enumerate(sortWays, start=1):
                print(f"{index}. {sortWay}")
            sortWay = input('Sortuj hotele według:')  # Pobieramy wybór użytkownika
            if sortWay == '1':
                hotels_list.sort(key=attrgetter('price'))  # Sortujemy hotele według ceny
                display_hotels(hotels_list)
            elif sortWay == '2':
                hotels_list.sort(key=attrgetter('name'))  # Sortujemy hotele według nazwy
                display_hotels(hotels_list)
            elif sortWay == '3':
                hotels_list.sort(key=attrgetter('rating'))  # Sortujemy hotele według oceny
                display_hotels(hotels_list)
            else:
                exit()

        def display_hotels(hotels_list):    # Funkcja do wyświetlania hoteli
            for x, hotel in enumerate(hotels_list):
                print("-" * 40)
                print(f"Hotel {x + 1}:")
                print(f"Nazwa: {hotel.name}")
                print(f"Adres: {hotel.address}")
                print(f"Ocena: {hotel.rating[:3]}")
                print(f"Typ: {hotel.room}")
                print(f"Cena ({hotel.description}): {hotel.price} zł")
                print("-" * 40)
            sort_hotels(hotels_list)  # Wywołujemy sortowanie po wyświetleniu

        display_hotels(hotels_list)  # Wyświetlamy hotele
        sort_hotels(hotels_list)  # Sortujemy hotele
    else:
        print("Error 404")  # Obsługa błędu

def main():     # Główna funkcja programu
    adultsGroup, childrenGroup, checkinDate, checkoutDate, childrenGroupTotalAge = trip_details()  # Pobieramy szczegóły podróży
    target_url = choose_city(adultsGroup, childrenGroup, checkinDate, checkoutDate, childrenGroupTotalAge)  # Wybieramy miasto i generujemy URL
    print("Poczekaj chwilę...")

    scrape_hotels(target_url)    # Parsujemy informacje o hotelach w wybranym mieście

if __name__ == '__main__':
    main()  # Uruchamiamy główną funkcję
