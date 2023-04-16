from flask import Flask , render_template, jsonify, request
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods= ['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            carat=float(request.form.get('carat')), #to convert requested string data from html form page into float
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),   #no need to do convert because already in str cast
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )

    final_new_data = data.get_data_as_dataframe() #converting custome data into Dataframe
    predict_pipeline= PredictPipeline()
    pred= predict_pipeline.predict(final_new_data)

    result = round(pred[0],2)
    return render_template('result.html', final_result = result)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)



