import re
from datetime import time, timedelta
from pathlib import Path

import PyPDF2
import requests
from bs4 import BeautifulSoup
import pprint


class BusQuery:
    def __init__(self):
        print("BusQuery created...")
        self.name = "Metarch"

    def run_works_manages_to_read_pdf(self):
        """
        Test with PyPDF2, works but the output needs a lot of work to get info we need out of it.
        Returns: None

        """
        print(f"{self.name} starting run function")

        # Path
        path_to_pdf = Path.cwd() / "metarch/ressources/express_1_Hiver_19_20.pdf"
        print("The file with path {} was found : {}".format(path_to_pdf, Path.is_file(path_to_pdf)))
        print("#######################################################################################################")

        pdf_file_obj = open(str(path_to_pdf), "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

        print(f"there are {pdf_reader.numPages} pages in this document")

        page_obj = pdf_reader.getPage(0)
        first_page_text = page_obj.extractText()
        print(first_page_text)

    def run(self):
        """
        Test with
        Returns:

        """
        print(f"{self.name} starting run function")

        # # page = url_buses_destinations(259)
        # page = url_bus_horaire()
        #
        # print("we are querying this page: ", page)
        # response = requests.get(page)
        # # res is a dict
        # res = response.json()
        # pprint.pprint(res)
        #
        # print(format_results(res))

        # find_bus_1_next_schedule()
        # new_test_local()
        # new_test_ligne_1_online_vers_saint_germain()
        new_test_ligne_10_online_vers_saint_germain()

        # for todo_item in page.json():
        #     print('{} {}'.format(todo_item['id'], todo_item['summary']))

        # soup = BeautifulSoup(page.content, "html.parser")
        # results = soup.find(id="main-content")
        # results = soup.find(id="ixxi-horaire-result")
        # results = soup.find(id="challenge-form")
        # print(results)

        # response = urllib.request.urlopen(url)
        # html = response.read()
        # text = html.decode()
        # print(text)


def find_bus_1_next_schedule():
    # url = "https://www.transdev-idf.com/horaires-ligne-1/ancienne-mairie-vers-gare-de-versailles-chantiers-gare-routiere/012-EXPR1-50012165-591361744"

    url = "https://www.transdev-idf.com/horaires-ligne-1/ancienne-mairie-vers-rue-thiers/012-EXPR1-50012166-50012309"

    local_path = Path.cwd() / "metarch/ressources/ligne_1.html"
    print("local path is ", local_path)

    page_data = Path.open(local_path)
    soup = BeautifulSoup(page_data, "html.parser")

    # page_data = requests.get(url, "html")
    # print(page_data.content)
    # soup = BeautifulSoup(page_data.content, "html.parser")

    for item in soup.findAll('div', {"class": "schedule-line"}):
        print(item)

    # print("we are querying this page: ", page)
    # response = requests.get(page)
    # res = response.json()
    # pprint.pprint(res)


def new_test_local():
    local_path = Path.cwd() / "metarch/ressources/ligne_1.html"
    with open(str(local_path), "r") as f:
        content = f.read()
        soup = BeautifulSoup(content, "lxml")

        time_schedules = []
        for item in soup.findAll('div', {"class": "schedule-line"}):
            # print(item.content)
            # print(type(item))
            # print(item.text)
            # text_draft = "05 h\n        \n                   46\n                01\n"
            text_draft = str(item.text)

            # here find all integers in text
            temp = re.findall(r'\d+', text_draft)
            res = list(map(int, temp))
            #
            print(res)

            first_time = time(5, 0, 0)

            _hour = res[0]
            for elem in res[1:]:
                t = time(_hour, elem, 0)
                time_schedules.append(t)
                # print(t)

            # for elem in (str.split(text_draft)):
            #     print("elem: ", elem)
            #     for sub_elem in str.split(elem):
            #         print(sub_elem)
            #         print(type(sub_elem))

            # print(str.split(text_draft))
            # numbers = [int(s) for s in str.split(text_draft) if s.isdigit()]
            # print(numbers)
            print("#########################################")

        # test if for example, current_time = 8h30, what is the next bus
        # current_time = time(8, 30, 0)
        current_time = time(9, 30, 0)
        # current_time = time(12, 28, 0)
        # current_time = time(0, 2, 0)

        next_bus_schedule = find_next_bus_1(current_time, time_schedules)


def find_next_bus_1(current_time: time, time_schedules: list):
    for t in time_schedules:
        # the first iteration when the time schedule is > ie incoming, return that time
        if t > current_time:
            delta_minutes = t.minute - current_time.minute
            print(f"current time being: {current_time}, the next bus is : {t}, in {delta_minutes} mins")
            return t


def new_test_ligne_1_online_vers_saint_germain():
    """
    This function fetches ligne 10 schedule.
    Returns:

    """
    url = "https://www.transdev-idf.com/horaires-ligne-1/ancienne-mairie-vers-rue-thiers/012-EXPR1-50012166-50012309"
    # NET REQUEST
    page_data = requests.get(url, "html")
    print("A NET REQUEST HAPPENED")

    soup = BeautifulSoup(page_data.content, "html.parser")
    print(soup.findAll('div', {"class": "schedule-line"}))
    for item in soup.findAll('div', {"class": "schedule-line"}):
        text_draft = str(item.text)

        # here
        temp = re.findall(r'\d+', text_draft)
        res = list(map(int, temp))
        print(res)
        # break


def new_test_ligne_10_online_vers_saint_germain():
    """
    This function fetches ligne 10 schedule.
    Returns:

    """
    url = "https://www.transdev-idf.com/horaires-ligne-10/square-de-versailles-vers-rue-thiers/012-ESF-50012500-50012310"
    # NET REQUEST
    page_data = requests.get(url, "html")
    print("A NET REQUEST HAPPENED")

    soup = BeautifulSoup(page_data.content, "html.parser")
    i = 0
    for item in soup.findAll("div", {"class": "schedule"}):
        text_draft = str(item.text)
        # this is a str with all data # to be processed ex: \n\n06 h\n\n\n     25\n
        # print(text_draft)

        "If i split this way, every nombre pair is the hours and impair the minutes in the hour."
        hours_and_minutes_array_data = text_draft.split(sep="\n\n\n")
        pprint.pprint(hours_and_minutes_array_data)
        final_res = []
        for i, elem in enumerate(hours_and_minutes_array_data):
            print("i = ", i)

            # this filters only numbers
            temp_data = re.findall(r'\d+', elem)
            filtered_numbers = list(map(int, temp_data))

            if i % 2 == 0:
                final_res.append(list(filtered_numbers))
            else:
                for numb in filtered_numbers:
                    final_res[-1].append(numb)

        # ADD THIS LEVEL WE HAVE OUR STRUCTURE
        """
        [[6, 25, 51],
         [7, 10, 20, 30, 38, 48, 55],
         [8, 7, 16, 23, 33, 39, 48, 59],
         [9, 6, 16, 26, 36, 51],
         [10, 0, 23, 49]
        ]
        """
        pprint.pprint(final_res)



        # print(final_res)
        # here
        # temp = re.findall(r'\d+', text_draft)
        # print("temps =", temp)
        # res = list(map(int, temp))
        # print(res)

        extract_clean_schedule_from_text_weird_pattern(text_draft)


def extract_clean_schedule_from_text_weird_pattern(arg_text: str):
    wanted_res = None
    for line in arg_text.split():
        pass


def format_results(result: dict):
    bus_hours = []
    res = result["result"]["schedules"]
    for bus in res:
        bus_hours.append(bus["message"])

    print("all the upcoming buses are : ", bus_hours)
    print(res)

    first_bus = [int(s) for s in str.split(bus_hours[0]) if s.isdigit()][0]
    second_bus = [int(s) for s in str.split(bus_hours[1]) if s.isdigit()][0]

    return f"\nLes prochains bus 259 pour Saint Germain en Laye sont dans {first_bus} et {second_bus}\n"


def url_buses_destinations(bus_number: int):
    url = "https://api-ratp.pierre-grimaud.fr/v4/"
    return url + "destinations/buses/" + str(bus_number)


def url_bus_horaire():
    return "https://api-ratp.pierre-grimaud.fr/v4/schedules/buses/259/jaures/A"


def save_fo_file(page_content):
    """
    The techniq i used to parse transdev files were with requests.get(), it gets you a page. Then print in console
    page.content, and put it in a file
    Returns:

    """
    pass
    # file_path = Path
    # file = open(file)




