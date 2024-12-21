import datetime
import pytz

def get_24h_window():
    nyc_now = datetime.datetime.now(pytz.timezone('America/New_York'))

    # Yesterday to today 6pm NYC time
    nyc_end_time = nyc_now.replace(hour=18, minute=0, second=0, microsecond=0)
    nyc_start_time = nyc_end_time - datetime.timedelta(days=1)

    utc_end_time = nyc_end_time.astimezone(pytz.utc).isoformat().replace('+00:00', 'Z')
    utc_start_time = nyc_start_time.astimezone(pytz.utc).isoformat().replace('+00:00', 'Z')

    # utc_end_time = str(nyc_end_time.astimezone(pytz.utc).timestamp())
    # utc_start_time = str(nyc_start_time.astimezone(pytz.utc).timestamp())

    return utc_start_time, utc_end_time
