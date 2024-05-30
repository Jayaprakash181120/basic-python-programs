from datetime import *
presentday=datetime.now()
yesterday=presentday-timedelta(1)
tommorrow=presentday+timedelta(1)
print("yesterday=",yesterday.strftime('%d-%m-%y'))
print("presentday=",presentday.strftime('%d-%m-%y'))
print("tommorrow=",tommorrow.strftime('%d-%m-%y'))