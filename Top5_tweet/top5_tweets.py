# Open the file and store it in f
with open('twitter_data.txt', 'r', encoding='utf8') as twitter_file:
    # initialize an empty dictionary to keep track of hashtag counts
    hashtags = {}

    # open the file with tweets and loop over each line
    for line in twitter_file:
        # split the line into words
        words = line.split()

        # loop over each word and check if it starts with a '#'
        for word in words:
            if word.startswith('#'):
                # convert the hashtag to lowercase
                hashtag = word.lower()

                # check if the hashtag is already in the dictionary
                if hashtag in hashtags:
                # if it is, increment the count
                    hashtags[hashtag] += 1
                else:
                    # if it's not, add it to the dictionary with a count of 1
                    hashtags[hashtag] = 1

# print the top 5 hashtags
for hashtag, count in sorted(hashtags.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{hashtag}: {count}")
