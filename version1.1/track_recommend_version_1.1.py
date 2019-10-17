"""
version 1.0
in this version, the weights of each item are the same
which means the user rates for album, artist and genre have same weight
final rate = the sum of every exist rate / amount of exist rate

submit date: 16 Oct 2019, 19:47
submit score: 0.79683
"""
import csv

directory_name = "../ee627a-2019fall"
testing_file_name = directory_name + "/testItem2.txt"
training_file_name = directory_name + "/trainItem2.txt"
track_relationship_file_name = directory_name + "/trackData2.txt"
output_file_name = "output.csv"

testing_file = open(testing_file_name, "r")


def read_training_file(file_name):
    print("Reading the training file ...")
    file = open(file_name, "r")
    res = {}
    my_rate = {}
    count = 0
    for line in file:
        arr_test = line.strip().split("\t")
        if len(arr_test) == 1:
            arr_test = arr_test[0].split('|')
            user_id = arr_test[0]
            count = int(arr_test[1])
        elif len(arr_test) == 2:
            my_rate[arr_test[0]] = arr_test[1]
            count = count - 1
            if count == 0:
                res[user_id] = my_rate
                my_rate = {}
    print("Training file reading completed!")
    return res


def read_track_file(file_name):
    print("Reading the track file ...")
    ftrackItem = open(file_name, 'r')

    dictrack = {}

    for line in ftrackItem:
        arr_track = line.strip().split('|')
        userID = arr_track[0]
        otherID = arr_track[1:]
        key, value = userID, otherID
        dictrack[key] = value
    print("Track file reading completed!")
    return dictrack


def predict_rate(user_id, track_id, training_dict, track_dict):
    check_list = track_dict.get(track_id)
    score_dict = training_dict.get(user_id)
    count = 0
    res = 0
    kind = 0    # 0 for album, 1 for artist, 2 and more than 2 for genre
    just_genre = False
    for id in check_list:
        score = score_dict.get(id)
        if kind < 2:
            if score != None:
                if kind == 0:
                    count = count + 0.5
                    res = res + int(score) * 0.5
                else:
                    count = count + 0.3
                    res = res + int(score) * 0.3
        else:
            if kind == 2 and count == 0:
                just_genre = True
            if score != None:
                count = count + 0.1
                res = res + int(score) * 0.1
        kind = kind + 1
    if count == 0:
        return 0
    res = res / count
    if just_genre:
        return res / 2
    return res


def predict_recommendation(my_track):
    rates = list(my_track.values())
    tracks = list(my_track.keys())
    rates.sort(reverse=True)
    for item in tracks:
        r = my_track.get(item)
        i = rates.index(r)
        rates[i] = item
    return rates


my_track = {}
result = [["TrackID", "Predictor"]]
count = 0

training_dict = read_training_file(training_file_name)
track_dict = read_track_file(track_relationship_file_name)

print("Start to predict rating ...")
for line in testing_file:
    arr_test = line.strip().split('|')
    if len(arr_test) == 2:
        user_id = arr_test[0]
        count = int(arr_test[1])
    else:
        track_id = arr_test[0]
        rate = predict_rate(user_id, track_id, training_dict, track_dict)
        # print("userid: " + user_id + " track_id: " + track_id + " rate: " + str(rate))
        my_track[track_id] = rate
        count = count - 1
        if count == 0:
            my_track_recommendation = predict_recommendation(my_track)
            for i in range(6):
                if i < 3:
                    result.append([user_id + "_" + my_track_recommendation[i], 1])
                else:
                    result.append([user_id + "_" + my_track_recommendation[i], 0])
            my_track = {}
print("Predict rating completed!")

print("Start to write down the prediction ...")
with open(output_file_name, "w") as output_file:
    writer = csv.writer(output_file)
    for item in result:
        writer.writerow(item)
print("Processing completed!")

