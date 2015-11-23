# example of program that calculates the average degree of hashtags
import json
def featureTwo():
    f=open("../tweet_input/tweets.txt", "r")
    w=open("../tweet_output/ft2.txt","wb")
    count=0
    for line in f:
        #ignore lines like "{"limit": {"track":5,"timestamp_ms":"1446218985743"} }"
        if not line.startswith('{"l'):
            json_str=json.loads(line)
            created_at=json_str["created_at"]
            hashtags=json_str["entities"]["hashtags"]
            print created_at
            print hashtags
            break
            # check if the line has unicode
            # remove or replace escape characters
            # if(not text.encode('ascii','ignore').decode('ascii')== text):
            #     count=count+1
            #     text=text.encode('ascii','ignore').decode('ascii')
            # else:
            #     text=text.encode('ascii','ignore').decode('ascii')
            #write cleaned text and timestamp to file
            # w.write(text+" (timestamp:"+ created_at+")\n")

    # w.write("\n")
    # w.write(str(count)+" tweets contained unicode.")

if __name__ == "__main__":
    featureTwo()