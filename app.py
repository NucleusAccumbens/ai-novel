
import json
import openai 

with open('story_points.json') as json_file: 
    data1 = json.load(json_file) 

with open('expositions.json') as json_file: 
    data2 = json.load(json_file) 

with open('reactions.json') as json_file: 
    data3 = json.load(json_file) 

with open('actions.json') as json_file: 
    data4 = json.load(json_file) 

with open('choice.json') as json_file: 
    data5 = json.load(json_file) 


story = data2["exposotions"][0]["body"]
story_points = data1["storyPoints"]

reactions = data3["reactions"]
actions = data4["actions"]
choice = data5["choice"]

def analize_story_point(pointId):
    if pointId == 0:
        print("\nChoose the mood of the main character:\n" +
                "0 - fear\n" +
                "1 - sadness\n" +
                "2 - rage\n" +
                "3 - joy\n\n")
        return input()
    if pointId == 1:    
        print("\nChoose an event:\n1 - the appearance of a new character,\n2 - an unexpected gift\n\n")
        return input()
    if pointId == 4:
        print("\nWhat did the heroine choose?\n0 - first option,\n1 - second option")
        return input()       

openai.api_key = "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"

i = 0

while i < 8:
    
    storytwist = analize_story_point(i)
    gpt_commad = story_points[i]["body"]

    if i == 0:
        print(story)
        gpt_commad+=reactions[int(storytwist)]["body"]
    if i == 1:
        gpt_commad+=reactions[int(storytwist)]["body"]
    if i == 3:
        gpt_commad+=actions[0]["body"]
    if i == 4:
        gpt_commad+=choice[int(storytwist)]["body"]
    
    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=story+gpt_commad, 
        temperature=0, 
        max_tokens=450)
    i+=1
    print("\n" + response["choices"][0]["text"])
    story+=response["choices"][0]["text"]


