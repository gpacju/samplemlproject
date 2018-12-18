from flask import Flask, request 
from flask_restful import Resource, Api 
import pickle 

app = Flask(__name__) 

api = Api(app) 


def classify(petal_len, petal_wd, sepal_len, sepal_wd): 
    species = ['Iris-Setosa', 'Iris-Versicolour', 'Iris-Virginica']
    with open('models/iris_classifier_model.pk', 'rb') as model_file: 
        model = pickle.load(model_file) 

    species_class = int(model.predict([[petal_len, petal_wd, sepal_len, sepal_wd]])[0])
    return species[species_class]


class IrisPredict(Resource): 

    def get(self): 
        sl = float(request.args.get('sl'))
        sw = float(request.args.get('sw'))
        pl = float(request.args.get('pl'))
        pw = float(request.args.get('pw'))


        result = classify(sl, sw, pl, pw) 

        return {'sepal_length':sl,
                'sepal_width':sw,
                'petal_length':pl,
                'petal_width':pw,
                'species':result} 


api.add_resource(IrisPredict, '/classify/')
