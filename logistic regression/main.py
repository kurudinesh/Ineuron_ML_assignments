
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            input = [1]
            for k in request.form:
                print(k)
                if k == 'occ' or k == 'occ_husband':
                    val = int(request.form[k])
                    for i in range(2,7):
                        if i == val:
                            input.append(1)
                        else:
                            input.append(0)
                else:
                    input.append(float(request.form[k]))
            # val1=float(request.form['crim'])
            # val2 = float(request.form['zn'])
            # val3 = float(request.form['lstat'])
            # val4 = float(request.form['rm'])
            filename = 'logreg_model.sav'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            print("input=",input)
            prediction=loaded_model.predict([input])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)
	# app.run(debug=True) # running the app