#creating tweets dictionary
def generateTweets(no_of_tweets):

    tweet_dict = {}
    for i in range(no_of_tweets):
        tweets_list = input().split()
        name = tweets_list[0]
        tweet_value = tweets_list[1]

        if name in tweet_dict.keys():
            tweet_dict[name].append(tweet_value)
        elif name not in tweet_dict.keys():
            tweet_dict[name] = [tweet_value] 

    return tweet_dict

#calculating maximum tweets and highest tweeter
def maxTweets(tweet_dict):
    maximum = 0
    tweet_dict_keys = list(tweet_dict.keys())
    tweet_dict_values = list(tweet_dict.values())
    maximum = len(tweet_dict_values[0])


    highest_tweeter = {}
    for key, value in tweet_dict.items():
        if maximum < len(value):
            maximum = len(value)
            highest_tweeter[key] = maximum
        elif maximum == len(value):
            highest_tweeter[key] = maximum
        else:
            continue
            
    return highest_tweeter      #return a dictionary of highest tweeters and their highest tweet counts


if __name__ == '__main__':
    test_cases = int(input('Enter number of test cases: '))     #number of test cases entered by the user
    Highest_Tweeters = {}
    for i in range(test_cases):
        no_of_tweets = int(input('Enter number of tweets: '))   #number of tweets entered by the user
        user_tweets = generateTweets(no_of_tweets)             #creating tweets dictionary
        maximum = maxTweets(user_tweets)                        #calculating maximum tweets and highest tweeter
        for key, value in maximum.items():
            Highest_Tweeters[key] = value
    for key, value in sorted(Highest_Tweeters.items()):
        print(key, value)