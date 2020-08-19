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
	import json

	app = Flask(__name__)

	model = pickle.load(open('model.pkl','rb'))

	api = Api(app)

	class prediccion(Resource):
		def get(self,archivo):

			df = pd.read_csv('datosprueba/'+archivo)
			x = np.array(df[["Rh F (mm)","Rv F (mm)","Astig F (D)","Asph. Q F","Rh B (mm)","Rv B (mm)","K2 B (D)","Astig B (D)","Asph. Q B","Pachy Apex","Pachy Min","ISV","IVA","IHA","IHD","K1 (D)","K2 (D)","Astig","RPI Max","K max","I-S","AC Depth","Ecc Sup","Ecc Inf","Cor.Vol.","KPD","Ecc (Front)","Ecc (Back)","Sag. Height Mean [µm]","ACD Apex"]])

			prediccion = model.predict(x[0:1])
			resultado = prediccion.tolist()

			clasificacion = ''
			data = {}
			data['reglas0'] = []
			data['reglas1'] = []
			data['reglas2'] = []
			data['resultado'] = []

			if resultado[0] == 0:
				clasificacion = 'Forme Fruste'
				data['resultado'].append({
					'clasificacion':clasificacion
					})
				data['reglas0'].append({
				    'parametro': 'Sag. Height Mean [um]',
				    'condicion': '<=',
				    'valor': 1468})
				data['reglas0'].append({
				    'parametro': 'Rh F(mm)',
				    'condicion': '>',
				    'valor': 8.03})
				data['reglas0'].append({
				    'parametro': 'K1 (D)',
				    'condicion': '<=',
				    'valor': 41.9})
				data['reglas0'].append({
				    'parametro': 'Pachy Min',
				    'condicion': '>',
				    'valor': 546})
				
				data['reglas1'].append({
				    'parametro': 'Rh F (mm)',
				    'condicion': '>',
				    'valor': 8.03})
				data['reglas1'].append({
				    'parametro': 'K1 (D)',
				    'condicion': '<=',
				    'valor': 41.9})
				data['reglas1'].append({
				    'parametro': 'K Max',
				    'condicion': '<=',
				    'valor': 44.98})
				data['reglas1'].append({
				    'parametro': 'Rh B(mm)',
				    'condicion': '>',
				    'valor': 6.59})

				data['reglas2'].append({
				    'parametro': 'Rh F (mm)',
				    'condicion': '>',
				    'valor': 8.03})
				data['reglas2'].append({
				    'parametro': 'K1 (D)',
				    'condicion': '<=',
				    'valor': 41.9})
				data['reglas2'].append({
				    'parametro': 'Pachy Min',
				    'condicion': '>',
				    'valor': 546})
				data['reglas2'].append({
				    'parametro': 'Rh B(mm)',
				    'condicion': '>',
				    'valor': 6.59})
			elif resultado[0] == 1:
				clasificacion = 'Queratocono'
				data['resultado'].append({
					'clasificacion':clasificacion
					})
				data['reglas0'].append({
				    'parametro': 'Sag. Height Mean [Um]',
				    'condicion': '>',
				    'valor': 1578})
				data['reglas0'].append({
				    'parametro': 'Rh F (mm)',
				    'condicion': '<=',
				    'valor': 7.52})
				data['reglas0'].append({
				    'parametro': 'Pachy Min',
				    'condicion': '<=',
				    'valor': 478})
				data['reglas0'].append({
				    'parametro': 'K max',
				    'condicion': '>',
				    'valor': 51.45})
				data['reglas0'].append({
				    'parametro': 'Pachy Apex',
				    'condicion': '<=',
				    'valor': 486})
				data['reglas0'].append({
				    'parametro': 'K1 (D)',
				    'condicion': '>',
				    'valor': 44.6})	
				data['reglas0'].append({
				    'parametro': 'ISV',
				    'condicion': '>',
				    'valor': 61})
				data['reglas0'].append({
				    'parametro': 'IHD',
				    'condicion': '>',
				    'valor': 59})
				data['reglas0'].append({
				    'parametro': 'RPI Max',
				    'condicion': '>',
				    'valor': 2.43})
				data['reglas0'].append({
				    'parametro': 'IVA',
				    'condicion': '>',
				    'valor': 0.54})

				data['reglas1'].append({
				    'parametro': 'Sag. Height Mean [Um]',
				    'condicion': '>',
				    'valor': 1578})
				data['reglas1'].append({
				    'parametro': 'Rh F (mm)',
				    'condicion': '<=',
				    'valor': 7.52})
				data['reglas1'].append({
				    'parametro': 'Pachy Min',
				    'condicion': '<=',
				    'valor': 478})
				data['reglas1'].append({
				    'parametro': 'K max',
				    'condicion': '>',
				    'valor': 51.45})
				data['reglas1'].append({
				    'parametro': 'Pachy Apex',
				    'condicion': '<=',
				    'valor': 486})
				data['reglas1'].append({
				    'parametro': 'K1 (D)',
				    'condicion': '>',
				    'valor': 44.6})	
				data['reglas1'].append({
				    'parametro': 'ISV',
				    'condicion': '>',
				    'valor': 61})
				data['reglas1'].append({
				    'parametro': 'IHD',
				    'condicion': '>',
				    'valor': 59})
				data['reglas1'].append({
				    'parametro': 'RPI Max',
				    'condicion': '>',
				    'valor': 2.43})
				data['reglas1'].append({
				    'parametro': 'K2 (D)',
				    'condicion': '>',
				    'valor': 48.4})

				data['reglas2'].append({
				    'parametro': 'Sag. Height Mean [Um]',
				    'condicion': '>',
				    'valor': 1578})
				data['reglas2'].append({
				    'parametro': 'Rh F (mm)',
				    'condicion': '<=',
				    'valor': 7.52})
				data['reglas2'].append({
				    'parametro': 'K2 (D)',
				    'condicion': '>',
				    'valor': 48.4})
				data['reglas2'].append({
				    'parametro': 'K max',
				    'condicion': '>',
				    'valor': 51.45})
				data['reglas2'].append({
				    'parametro': 'I-S',
				    'condicion': '>',
				    'valor': 3.34})
				data['reglas2'].append({
				    'parametro': 'K1 (D)',
				    'condicion': '>',
				    'valor': 44.6})	
				data['reglas2'].append({
				    'parametro': 'ISV',
				    'condicion': '>',
				    'valor': 61})
				data['reglas2'].append({
				    'parametro': 'IHD',
				    'condicion': '>',
				    'valor': 59})
				data['reglas2'].append({
				    'parametro': 'RPI Max',
				    'condicion': '>',
				    'valor': 2.43})
				data['reglas2'].append({
				    'parametro': 'IVA',
				    'condicion': '>',
				    'valor': 0.54})
			elif resultado[0] == 2:
				clasificacion = 'Subclinico'
				data['resultado'].append({
					'clasificacion':clasificacion
					})
				data['reglas0'].append({
				    'parametro': 'Pachy Min',
				    'condicion': '<=',
				    'valor': 478})
				data['reglas0'].append({
				    'parametro': 'Pachy Apex',
				    'condicion': '<=',
				    'valor': 486})
				data['reglas0'].append({
				    'parametro': 'Sag. Height Mean [um]',
				    'condicion': '<=',
				    'valor': 1578,
				    'condicion2': '>',
				    'valor2': 1513})

				data['reglas1'].append({
				    'parametro': 'Pachy Min',
				    'condicion': '<=',
				    'valor': 478})
				data['reglas1'].append({
				    'parametro': 'Sag. Height Mean [um]',
				    'condicion': '<=',
				    'valor': 1578,
				    'condicion2': '>',
				    'valor2': 1513})
				data['reglas1'].append({
				    'parametro': 'Cor. Vol',
				    'condicion': '<=',
				    'valor': 58.1})
			elif resultado[0] == 3:
				clasificacion = 'Ojo sano'
				data['resultado'].append({
					'clasificacion':clasificacion
					})
			return data


	api.add_resource(prediccion,'/prediccion/<archivo>')

	if __name__ == '__main__':
		app.run(debug=True)
