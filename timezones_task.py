import pytz, datetime

# for country in pytz.country_names:
#     print(country, pytz.country_names[country], pytz.country_timezones.get(country))

timezone_dict = {
    'AD': ('Andorra', 'Europe/Andorra'),
    'AE': ('United Arab Emirates', 'Asia/Dubai'),
    'AF': ('Afghanistan', 'Asia/Kabul'),
    'AG': ('Antigua & Barbuda', 'America/Antigua'),
    'AI': ('Andorra', 'America/Anguilla'),
    'AL': ('Albania', 'Europe/Tirane'),
    'AM': ('Armenia', 'Asia/Yerevan')
}

for key in timezone_dict:
    print(key, timezone_dict[key])

print('Please enter a two-letter code of the country to choose the timezone')
print('(or "q" to quit)')

while True:
    country_code = input()

    if country_code == 'q':
        break
    if country_code in timezone_dict.keys():
        timezone = pytz.timezone(timezone_dict[country_code][1])
        print('Local time is {}'.format(datetime.datetime.now(tz=timezone)))
        print('UTC time is {}'.format(datetime.datetime.utcnow()))




