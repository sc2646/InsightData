# example of program that calculates the average degree of hashtags
import json
import datetime
import time
from collections import namedtuple
from collections import defaultdict

def featureTwo():
    tweet_dict={}
    f=open("../tweet_input/tweets.txt", "r")
    w=open("../tweet_output/ft2.txt","wb")
    i=0
    
    for line in f:
        #ignore lines like "{"limit": {"track":5,"timestamp_ms":"1446218985743"} }"
        if not line.startswith('{"l'):
            json_str=json.loads(line)
            created_at=json_str["created_at"].encode('ascii','ignore')
            hashtags=json_str["entities"]["hashtags"]
            
            ht=[]
            if (len(hashtags)!=0):
                for index in range (0,len(hashtags)):
                    ht.append(hashtags[index]["text"].encode('ascii','ignore'))
            else:
                ht=hashtags
            
            i=i+1
            
            FMT="%H:%M:%S"
            a=time.strptime(created_at[11:19],FMT)
            seconds=datetime.timedelta(hours=a.tm_hour, minutes=a.tm_min, seconds=a.tm_sec).seconds
            
            time_stamp=namedtuple("time_stamp",["month","day","second"])
            time_stamp_key=time_stamp(month=created_at[4:7],day=created_at[8:10],second=seconds)
            tweet_dict.setdefault(time_stamp_key,[]).append(ht)


# if(i==32):
#     break
# if a tweet only has 1 or zero node then there wont be any edge


#write cleaned text and timestamp to file
# w.write(text+" (timestamp:"+ created_at+")\n")

# w.write("\n")
# w.write(str(count)+" tweets contained unicode.")
print tweet_dict

if __name__ == "__main__":
    featureTwo()