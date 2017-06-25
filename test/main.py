from flask import Flask, request, jsonify
from predict import predict
import subprocess

app = Flask(__name__)

@app.route('/')
@app.route('/senti', methods=['POST'])

def getSenti():
    res_obj = {}
    print "In getSenti"

    if request.method == 'GET':
        res_obj['desc'] = "Get request"
        res_obj['msg'] = "Please Give a POST request with the Tweet"
    else:
        tweet = request.form['tweet']
        print "Got a POST request"
        print "Tweet received {}".format(tweet)

        #write to input.txt
        #FIXME - disk I/O not preferred in an API
        with open("input.txt", "w+") as inp_file:
            print>>inp_file, tweet
        # FIXME - again a disk I/O 
        subprocess.check_call(["./run.sh", "input.txt"])
        # FIXME - predict also uses disk I/O
        results = predict()
        res_obj['desc'] = "Tweet count - {}".format(len(results))
        res_obj['msg'] = "OK"
        res_obj['sentiment'] = results[0]

    return jsonify(res_obj)


if __name__ == "__main__":
    app.run(debug=True)
