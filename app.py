from flask import Flask 
from flask import flash
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import numpy as np 
import pandas as pd 
from flask import jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
import pickle 


app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

app.secret_key = "diagnosticoQueratocono"
app.config['MYSQL_HOST'] = 'bv8xv3gi0rnln7uikpvy-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'us5ow3hmh4ksah0n'
app.config['MYSQL_PASSWORD'] = '31EQWftwDQCVQNy7Vduk'
app.config['MYSQL_DB'] = 'bv8xv3gi0rnln7uikpvy'

api = Api(app)
mysql = MySQL(app)

class prediccion(Resource):
	def get(self,dni):
		cur = mysql.connection.cursor()
		cur.callproc("obtener_archivo",[dni])
		archivo = cur.fetchone()
		cur.close()

		df = pd.read_csv('datosprueba/'+archivo[0])
		x = np.array(df[["Rh F (mm)","Rv F (mm)","Astig F (D)","Asph. Q F","Rh B (mm)","Rv B (mm)","K2 B (D)","Astig B (D)","Asph. Q B","Pachy Apex","Pachy Min","ISV","IVA","IHA","IHD","K1 (D)","K2 (D)","Astig","RPI Max","K max","I-S","AC Depth","Ecc Sup","Ecc Inf","Cor.Vol.","KPD","Ecc (Front)","Ecc (Back)","Sag. Height Mean [µm]","ACD Apex"]])

		prediccion = model.predict(x[0:1])
		resultado = prediccion.tolist()

		return {"Resultado": resultado}


api.add_resource(prediccion,'/prediccion/<dni>')

if __name__ == '__main__':
	app.run(debug=True)