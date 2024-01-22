def convert_subscribers_count(subscribers_count_str):
  subscribers_count_str = subscribers_count_str.replace('\xa0', ' ').replace(" подписчиков", "")
  if "тыс." in subscribers_count_str:
    subscribers_count = int(float(subscribers_count_str.replace(" тыс.", "").replace(",", ".")) * 1000)
  elif "млн" in subscribers_count_str:
    subscribers_count = int(float(subscribers_count_str.replace(" млн", "").replace(",", ".")) * 1000000)
  else:
    subscribers_count = int(subscribers_count_str.replace(",", ""))
  return subscribers_count