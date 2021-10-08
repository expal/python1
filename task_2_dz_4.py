from urllib.request import urlopen
from xml.etree import ElementTree as etree


def currency_rates():
    response = urlopen("https://www.cbr.ru/scripts/XML_daily.asp")
    tree = etree.parse(response)
    currency = tree.findtext('.//Valute[@ID="R01235"]/CharCode')
    currency1 = tree.findtext('.//Valute[@ID="R01239"]/CharCode')
    value = tree.findtext('.//Valute[@ID="R01239"]/Value')
    value1 = tree.findtext('.//Valute[@ID="R01235"]/Value')
    print(f'Валюта {currency} курс по отношению к рублю {value}')
    print(f'Валюта {currency1} курс по отношению к рублю {value1}')


if __name__ == '__main__':
    currency_rates()
