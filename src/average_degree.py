# example of program that calculates the average degree of hashtags
import json
import datetime
import time
from collections import namedtuple
from collections import defaultdict
import collections

def featureTwo():
    tweet_dict={}
    f=open("../tweet_input/tweets.txt", "r")
    w=open("../tweet_output/ft2.txt","wb")

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

            FMT="%H:%M:%S"
            a=time.strptime(created_at[11:19],FMT)
            seconds=datetime.timedelta(hours=a.tm_hour, minutes=a.tm_min, seconds=a.tm_sec).seconds

            time_stamp=namedtuple("time_stamp",["month","day","second"])
            time_stamp_key=time_stamp(month=created_at[4:7],day=created_at[8:10],second=seconds)
            tweet_dict.setdefault(time_stamp_key,[]).append(ht)

    ordered_tweet_dict=collections.OrderedDict(sorted(tweet_dict.items()))
    cp_dict=ordered_tweet_dict


    for key in ordered_tweet_dict:
        original_graph={}
        original_graph=findingAllListInCurrentTimeStamp(ordered_tweet_dict,key,original_graph)
        new_list=[]
        for cp_key in cp_dict:
            new_graph={}
            if (key==cp_key):
                continue
            elif (key[0]==cp_key[0] and key[1]==cp_key[1]):
                if((1<=(cp_key[2]-key[2])<=60 )or (-60<=(cp_key[2]-key[2])<=-1) ):
                   # if yes, then make graph and calculate the edge and averageedge
                   new_graph=findingAllListInCurrentTimeStamp(cp_dict,cp_key,new_graph)
                   new_list.append(new_graph)

                else:
                    continue
            else:
                continue

        number_of_graph_in_new_list = len(new_list)
        new_dict= defaultdict(list)
        for key in original_graph.keys():
            new_dict[key].append(original_graph[key])
        # defaultdict(<type 'list'>, {'News': [['Trump', 'Election']], 'IfIEverGetToCabo': [['IfIEverGetToCabo']],
        # 'Trump': [['Election', 'News']], 'Election': [['News', 'Trump']]})

        for k in range (0, number_of_graph_in_new_list):
            for item in new_list[k].keys():
                new_dict[item].append(new_list[k][item])

        number_of_nodes_in_joined_graph = len(new_dict.keys())

        count=0
        for key in new_dict:
            l=len(new_dict[key])
            li=[]
            for x in range (0,l):
                if new_dict[key][x]==[key]:
                    count=count
                else:
                    li.extend(new_dict[key][x])

            t=list(set(li))
            count=count+len(t)

        if (number_of_nodes_in_joined_graph==0):
            w.write("0")
            w.write("\n")
        else:
            avg_degree=float(count)/number_of_nodes_in_joined_graph
            w.write(str(avg_degree))
            w.write("\n")




def findingAllListInCurrentTimeStamp(ordered_tweet_dict,key,graph):
    list_nodes_in_current_key=ordered_tweet_dict[key]
    number_of_nodes_in_list=len(list_nodes_in_current_key)
    list_of_current_nodes=[]

    for j in range (0, number_of_nodes_in_list):
        if not list_nodes_in_current_key[j]:
            continue
        else:
            list_of_current_nodes.append(list_nodes_in_current_key[j])

    new_list_of_current_nodes=[]

    if list_of_current_nodes:
        #get rid of empty lists in list
        for item in list_of_current_nodes:
            new_list_of_current_nodes.append([x for x in item if x])
        #get rid of empty lists
        new_list_of_current_nodes = [x for x in new_list_of_current_nodes if x]

        len_of_new_list_of_current_nodes=len(new_list_of_current_nodes)
        for n in range (0,len_of_new_list_of_current_nodes):
            for k in range (0, len(new_list_of_current_nodes[n])):
                if(len(new_list_of_current_nodes[n])>1):
                    graph.setdefault(new_list_of_current_nodes[n][k],[]).extend(new_list_of_current_nodes[n][k+1:])
                else:
                    graph.setdefault(new_list_of_current_nodes[n][k],[]).append(new_list_of_current_nodes[n][k])
                if(k>=1):
                    graph[new_list_of_current_nodes[n][k]].extend(new_list_of_current_nodes[n][:k])

    return graph


if __name__ == "__main__":
    featureTwo()