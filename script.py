"""
A script based on python that automatically scrapes 
twitter remote gigs
"""
import twint, time, schedule, functools

def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        print('LOG: Job "%s" completed' % func.__name__)
        return result
    return wrapper

@with_logging
def get_tweet_data():

    c = twint.Config()
    c.Search = "Remote engineer OR Datascientist OR Developer"
    #c.Near = "Lagos"
    c.Limit = 2000
    c.Since = "2020-4-4"
    #c.Until = "2020-4-2"
    c.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet}"
    #c.Pandas = True
    #c.Pandas_clean = True
    c.Store_csv = True
    #c.Output = "Openings"
    c.Output = "Remote"

    twint.run.Search(c)
    
get_tweet_data()
schedule.every().day.at("15:45").do(get_tweet_data)

while True:
    schedule.run_pending()
    time.sleep(1)