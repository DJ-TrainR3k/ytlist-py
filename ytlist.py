import urllib.request
import json

i = 0 # Incremental boi for pages
j = 1 # Incremental boi for total
ID = "" # Initialize channel ID string variable
input = input('\nEnter channel ID or Username: ')
API_KEY = "" # Your API key here

if input.startswith("UC") and len(input) == 24: # valid channel id is str starting with UC and is 24 characters
    print("\nChannel ID Found!\n")
    ID = input # ProTip: Check what you are assigning to what...
else: # If not, run API call to get it from channel username
    print("\nUsername found, Attempting to convert to ID...\n")
    idconvert = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?key={}&forUsername={}&part=id".format(API_KEY, input)).read()
    id_json_data = json.loads(idconvert.decode('utf-8'))

    if not id_json_data["items"]: # Im gonna pretend I know why only this works and nothing else does...
        print("\nNo valid channel ID or username found! Try copying the channels' ID instead, some channels are weird with the API.")
        exit()
    elif id_json_data["items"] != "[]":
        print("Conversion Successful\n")
        ID = id_json_data["items"][0]["id"]

response = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={}&key={}".format(ID, API_KEY)).read()
json_data = json.loads(response.decode('utf-8'))

count = json_data["pageInfo"]["resultsPerPage"]
total = json_data["pageInfo"]["totalResults"]

if 'nextPageToken' in json_data: # Cheks to see if our request returned anything in the nextPageToken tag
    pageToken = json_data["nextPageToken"] # If so, set it as the next page token for subsiquent requests
else: # If nothing is returned, set the variable to be empty
    pageToken = ""

print("Saving Playlists...\n")
print("Total Playlists: " + str(total) + "\n")

if json_data["items"] == "[]" and input.startswith("UC") and len(input) == 24: # If valid channel ID but no user made playlists, json is empty ([])
    print("This User has no playlists!")
    exit()
f = open('playlists.txt', 'w', encoding='utf-8')
if total <= 5:
    while j <= total:
        print("Saving: " + json_data["items"][i]["snippet"]["title"])
        f.write("#" + json_data["items"][i]["snippet"]["title"] + "\n")
        f.write(json_data["items"][i]["id"] + "\n")
        #print("i = " + repr(i))
        #print("j = " + repr(j))
        #print(pageToken)
        i += 1
        j += 1
elif total > 5:
    while j <= total: # Checks the i variable to see if we have iterated through the max amount of items total
        if i == count: # This means that the loop has reached the end of the page
            # print("Next Page! \n")
            response = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={}&pageToken={}&key={}".format(ID, pageToken, API_KEY)).read()
            json_data = json.loads(response.decode('utf-8')) # Parse shite to json
            if j <= total - 5: # Ghetto fuckery for last page shenane
                pageToken = json_data["nextPageToken"]
            else:
                pageToken = ""
            i = 0
        elif i <= count and i < total:
            print("Saving: " + json_data["items"][i]["snippet"]["title"])
            f.write("#" + json_data["items"][i]["snippet"]["title"] + "\n")
            f.write(json_data["items"][i]["id"] + "\n")
            # print("i = " + repr(i))
            # print("j = " + repr(j))
            # print(pageToken)
            i += 1
            j += 1
    if j == total + 1:
        print("Done!")
