from flask import Flask, render_template, request,url_for
import joblib
# import mysql.connector
import pandas as pd


model = joblib.load("bike_price_model.lb")
app = Flask(__name__)

# def get_ab_connection():
#     try:
#         conn = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             password = "",
#             database = "bike"
#         )
#         return conn
#     except mysql.connector.Error as err:
#         print(f"Error connecting to my sql:{err}")
#         return none

@app.route('/')
def home():
    return render_template('index.html')

@app.route ("/project")
def project():
    return render_template('project.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

# @app.route('/history',method=["GET","POST"])
# def history():
#     brand_name_filter = request.form.get(
#         "bround_name_filter",None)
#     historical_data =[]

    # if conn:
    #     cursor = conn.cursor(dictionary = True)
    #     try:
    #         if brand_name_filter:
    #             query = "SELECT * FROM bike_prediction WHRE brand_name_ = %s"
    #             cursor.exceute(query,(brand_name_filter,))
    #         else:
    #             query = "SELECT * FROM bike_prediction"
    #             cursor.execute(query)

    #         historical_data = cursor.fetchall()
    #     except mysql.connector.Error as err:
    #         print(f"Error fetching data from mysql:{err}")
    #     finally:
    #         cursor.close()
    #         conn.close()

    #         return render_template('history.html', historical_data = historical_data)
        

# predition route'

@app.route('/predict',methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            brand_name = int(request.form.get("brand_name"))
            owner_name = int(request.form["owner"])
            age_bike = int(request.form["age"])
            power_bike =int( request.form["power"])
            kms_driven_bike =int(request.form["kms_driven"])

            bike_numbers = {{'TVS': 0,
                                'Royal Enfield': 1,
                                'Triumph': 2,
                                'Yamaha': 3,
                                'Honda': 4,
                                'Hero': 5,
                                'Bajaj': 6,
                                'Suzuki': 7,
                                'Benelli': 8,
                                'KTM': 9,
                                'Mahindra': 10,
                                'Kawasaki': 11,
                                'Ducati': 12,
                                'Hyosung': 13,
                                'Harley-Davidson': 14,
                                'Jawa': 15,
                                'BMW': 16,
                                'Indian': 17,
                                'Rajdoot': 18,
                                'LML': 19,
                                'Yezdi': 20,
                                'MV': 21,
                                'Ideal': 22}}
                                
            bike_name_encoded = bike_numbers.get(brand_name,-1)
            input_data = [[bike_name_encoded,
                    kms_driven_bike,
                    age_bike,
                    power_bike]]
            prediction = model.predict(input_data)[0]
            prediction = round(prediction,2)

    # conn = get_ab_connection()
    # if conn:
    #     cursor = conn.cursor()
    #     query = "INSERT INTO bike_prediction ( owner_name,brand_name,kms_drive,age_bike,power_bike,bike_preiction) VALUES (%s,%s,%s,%s,%s)"
    #     user_data = (owner_name,brand_name,kms_driven_bike,age_bike,prediction)
    #     cursor.execute(query,user_data)
    #     conn.commit()
    #     cursor.close()
    #     conn.close()

    #     return render_template("project.html",prediction=prediction)
    
        except Exception as e:
            print(e)


if __name__ == '_main_':
        app.run(debug= True,host='0.0.0.0', port = 2525)