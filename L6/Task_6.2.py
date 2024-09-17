sec_in_day = 86400
sec_in_hour = 3600
sec_in_minute = 60
number = int(input('Введіть число від 0 до 8640000 : '))
days = number // sec_in_day
hours = (number - (days * sec_in_day)) // sec_in_hour
minutes = (number - (days * sec_in_day) - (hours * sec_in_hour)) // sec_in_minute
seconds = number % sec_in_minute
if 0 <= number <= 8640000:
    days = str(days).zfill(2)
    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)
    text = 'днів'
    if days.endswith('1') and days != '11':
        text = 'день'
    elif days.endswith('2') or days.endswith('3') or days.endswith('4'):
        text = 'дні'
    date_format = "{} {}, {}:{}:{}".format(days, text, hours, minutes, seconds)
    print(date_format)
else:
    print('Невірне число !')
