from globals import *
import sys, time, datetime
import elixir
import sqlalchemy as sql
from dbtables import *
  
def updateOne(feed):
  feed.update(forced=True)
  elixir.session.flush()  
  
# The feed updater (runs out-of-process)
def feedUpdater():
  import dbtables
  lastCheck=datetime.datetime(1970, 1, 1)
  while True:
    info("updater loop")
    now=datetime.datetime.now()
    period=config.getValue('options', 'defaultRefresh', 1800)
    cutoff=now-datetime.timedelta(0, 0, period)
    if (now-lastCheck).seconds>90: # Time to see if a feed needs updating
      # Feeds with custom check periods
      now_stamp=time.mktime(now.timetuple())
      for feed in dbtables.Feed.query.filter(sql.and_(dbtables.Feed.updateInterval<>-1, 
                            sql.func.strftime('%s', dbtables.Feed.lastUpdated)+\
                                                    dbtables.Feed.updateInterval*60<now_stamp)).\
                            filter(dbtables.Feed.xmlUrl<>None):
        try:
          feed.update()
          # feed.expire(expunge=False)
        except:
          pass
      # Feeds with default check period
      for feed in dbtables.Feed.query.filter(sql.and_(dbtables.Feed.updateInterval==-1, 
                                                      dbtables.Feed.lastUpdated < cutoff)).\
                                                      filter(dbtables.Feed.xmlUrl<>None):
        try:
          feed.update()
          # feed.expire(expunge=False)
        except:
          pass
      lastCheck=now
    time.sleep(2)

def main():
  initDB()
  elixir.metadata.bind.echo = True
  feedUpdater()
  

if __name__ == "__main__":
  main()