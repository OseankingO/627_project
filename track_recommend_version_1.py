directory_name = "./ee627a-2019fall"
testing_file_name = directory_name + "/testItem2.txt"
training_file_name = directory_name + "/trainItem2.txt"
track_relationship_file_name = directory_name + "/trackData2.txt"

testing_file = open(testing_file_name, "r")
track_relationship_file = open(track_relationship_file_name, "r")


def read_training_file(file_name):
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
    return res

def read_track_file(file_name):
    ftrackItem = open(file_name, 'r')

    dictrack = {}

    for line in ftrackItem:
        arr_track = line.strip().split('|')
        userID = arr_track[0]
        otherID=arr_track[1:]
        key, value=userID,otherID
        dictrack[key]=value
    return dictrack

def predict_rate(user_id, track_id, training_dict, track_dic):
    return 0


my_track = []
i = 0

# training_dict = read_training_file(training_file_name)
track_dic = read_track_file(track_relationship_file_name)

for line in testing_file:
    arr_test = line.strip().split('|')
    if len(arr_test) == 2:
        # if len(my_track) != 0:
        #     # print(user_id)
        #     # print(my_track)
        user_id = arr_test[0]
        my_track = []
    else:
        track_id = arr_test[0]
        my_track.append(track_id)
        # rate = predict_rate(user_id, track_id,)


