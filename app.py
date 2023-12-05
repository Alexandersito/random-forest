from flask import Flask, jsonify, request
import joblib
import sklearn


app= Flask(__name__)

@app.route("/")
def home():
    return 'La pagina esta funcionando bien'

@app.route("/predecir", methods=["POST"])
def predecir():
    json=request.get_json(force=True)
    medidas=json['Medidas']
    clf=joblib.load('random_forest_model.pkl')
    prediccion=clf.predict(medidas)
    return 'El valor de la produccion es: {0}\n\n'.format(prediccion)

if __name__ == '__main__':
    app.run()



#curl -d "{\"Medidas\":[[15,3,147]]}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predecir

#curl -d "{\"Medidas\":[[15.2,3.3,147.1]]}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predecir