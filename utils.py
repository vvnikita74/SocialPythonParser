import re


def convert_subscribers_count(subscribers_count_str):
  subscribers_count_str = subscribers_count_str.replace('\xa0', ' ').replace(" подписчиков", "")
  if "тыс." in subscribers_count_str:
    subscribers_count = int(float(subscribers_count_str.replace(" тыс.", "").replace(",", ".")) * 1000)
  elif "млн" in subscribers_count_str:
    subscribers_count = int(float(subscribers_count_str.replace(" млн", "").replace(",", ".")) * 1000000)
  else:
    subscribers_count = int(subscribers_count_str.replace(",", ""))
  return subscribers_count


def convert_subscribers_count_it(subscribers_count_str):
  
  match = re.search(r'Подписчики: (\d+(\.\d+)?)([MK]?)', subscribers_count_str)
  if match:

    value = float(match.group(1))
    unit = match.group(3)

    if unit == 'M':
      followers_count = int(value * 1e6)
    elif unit == 'K':
      followers_count = int(value * 1e3)
    else:
      followers_count = int(value)
  return followers_count