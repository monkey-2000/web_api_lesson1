import requests


def main():
    cyties = ['London', 'svo', 'Череповец']
    lang = 'ru'
    units = 'm'
    url_template = 'https://wttr.in/{city}?lang={lang}&{units}&n'
    for city in cyties:
        url = url_template.format(city=city, lang=lang, units=units)
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
