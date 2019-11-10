from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
testfilename = 'testset.pkl'

with open(testfilename, 'rb') as f:
    testset = pickle.load(f)

pred_table = {}

def process_testset():
    print("found {} items in testset".format(len(testset)))
    pred_table_filename = 'pred_table.pkl'
    for item in testset:
        uid = str(item[0])
        iid = str(item[1])
        rating = str(item[2])
        pred_table[uid+"_"+iid] = rating
    with open(pred_table_filename, 'wb') as f:
        print("saving pred_table to {}".format(pred_table_filename))
        pickle.dump(pred_table, f)
    return pred_table

pred_table = process_testset()

@app.route('/get_prediction')
def get_prediction():
    req_data = request.json
    print(req_data)
    uid = req_data["uid"]
    iid = req_data["iid"]
    key = str(uid)+"_"+str(iid)
    print("key: {}".format(key))
    resp={}
    if key in pred_table:
        resp["predicted_rating"] = pred_table[key]
    else:
        resp["predicted_rating"] = "not available"

    return jsonify(resp)


if __name__=='__main__':
    app.run("localhost", 5000)