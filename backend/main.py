# Webserver
from flask import Flask, make_response
from flask_restx import Resource, Api
from flask_restx import reqparse
# BERT Model instantiation
from fitbert import FitBert
# RNN Model instantiation
from tensorflow import keras
# Import other files in this directory
import constructor as con
from preprocessor import preprocess
from bert import fill_in
from rnn_text_generator import text_generation

# Instantiate flask app and corresponding REST Api
app = Flask(__name__)
api = Api(app)

# Instantiate FitBERT
fb = FitBert(model_name="bert-large-uncased", disable_gpu=True)

# Instantiate RNN Models
model_1 = keras.models.load_model("./models/Shakespeare")
model_2 = keras.models.load_model("./models/Michael_Jackson")
model_3 = keras.models.load_model("./models/Maid_of_Honor")

# Globally save template stages to allow partial calls
template_text = ""
preprocessed_text = ""
current_options = {}

# --------------------------------------------------------------------------
# REST Endpoints for BERT requests

@api.route('/bert_wedding')
class Wedding(Resource):
    def get(self):
        # Bind vars to global
        global template_text
        global preprocessed_text
        global current_options

        # Parse arguments
        parser = reqparse.RequestParser()
        parser.add_argument('perspective', type=str, help='perspective', required=True)
        parser.add_argument('mood', type=str, help='mood', required=True)
        parser.add_argument('name1', type=str, help='groom')
        parser.add_argument('name2', type=str, help='bride')
        args = parser.parse_args()

        # Convert arguments to constructor parameters
        plural = (args["perspective"] == "many")
        # Call constructor
        template_text = con.wedding_constructor(plural, args["mood"], args["name1"], args["name2"])
        # Preprocess for BERT
        processed_result = preprocess(template_text, args["mood"])
        preprocessed_text = processed_result[0]
        current_options = processed_result[1]
        # Call BERT
        bert_result = fill_in(preprocessed_text, current_options, fb)
        text = bert_result[0]
        # update available options
        current_options = bert_result[1]

        # Build response with flask function, default http code is 200 (OK)
        response = make_response({"text": text})
        # Add header so Angular doesnt complain
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response



@api.route('/bert_birthday')
class Birthday(Resource):
    def get(self):
        # Bind vars to global
        global template_text
        global preprocessed_text
        global current_options

        # Parse arguments
        parser = reqparse.RequestParser()
        parser.add_argument('perspective', type=str, help='perspective', required=True)
        parser.add_argument('mood', type=str, help='mood', required=True)
        parser.add_argument('name1', type=str, help='name')
        parser.add_argument('age', type=int, help='age')
        args = parser.parse_args()

        # Convert arguments to constructor parameters
        plural = (args["perspective"] == "many")
        age = 0
        if args["age"] is not None:
            age = args["age"]
        # Call constructor
        template_text = con.birthday_constructor(plural, args["mood"], args["name1"], age)
        # Preprocess for BERT
        processed_result = preprocess(template_text, args["mood"])
        preprocessed_text = processed_result[0]
        current_options = processed_result[1]
        # Call BERT
        bert_result = fill_in(preprocessed_text, current_options, fb)
        text = bert_result[0]
        # update available options
        current_options = bert_result[1]

        # Build response with flask function, default http code is 200 (OK)
        response = make_response({"text": text})
        # Add header so Angular doesnt complain
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

@api.route('/bert_funeral')
class Funeral(Resource):
    def get(self):
        # Bind vars to global
        global template_text
        global preprocessed_text
        global current_options

        # Parse arguments
        parser = reqparse.RequestParser()
        parser.add_argument('perspective', type=str, help='perspective', required=True)
        parser.add_argument('mood', type=str, help='mood', required=True)
        parser.add_argument('gender', type=str, help='gender', required=True)
        parser.add_argument('name1', type=str, help='addressed')
        parser.add_argument('name2', type=str, help='deceased')
        args = parser.parse_args()

        # Convert arguments to constructor parameters
        plural = (args["perspective"] == "many")
        # Call constructor
        template_text = con.funeral_constructor(plural, args["mood"], args["name1"], args["name2"], args["gender"])
        # Preprocess for BERT
        processed_result = preprocess(template_text, args["mood"])
        preprocessed_text = processed_result[0]
        current_options = processed_result[1]
        # Call BERT
        bert_result = fill_in(preprocessed_text, current_options, fb)
        text = bert_result[0]
        # update available options
        current_options = bert_result[1]

        # Build response with flask function, default http code is 200 (OK)
        response = make_response({"text": text})
        # Add header so Angular doesnt complain
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

@api.route('/bert_valentines')
class Valentines(Resource):
    def get(self):
        # Bind vars to global
        global template_text
        global preprocessed_text
        global current_options

        # Parse arguments
        parser = reqparse.RequestParser()
        parser.add_argument('perspective', type=str, help='perspective', required=True)
        parser.add_argument('mood', type=str, help='mood', required=True)
        parser.add_argument('name1', type=str, help='name')
        args = parser.parse_args()

        # Convert arguments to constructor parameters
        plural = (args["perspective"] == "many")
        # Call constructor
        template_text = con.valentines_constructor(plural, args["mood"], args["name1"])
        # Preprocess for BERT
        processed_result = preprocess(template_text, args["mood"])
        preprocessed_text = processed_result[0]
        current_options = processed_result[1]
        # Call BERT
        bert_result = fill_in(preprocessed_text, current_options, fb)
        text = bert_result[0]
        # update available options
        current_options = bert_result[1]

        # Build response with flask function, default http code is 200 (OK)
        response = make_response({"text": text})
        # Add header so Angular doesnt complain
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

@api.route('/bert_retry')
class Retry(Resource):
    def get(self):
        # Bind vars to global
        global template_text
        global preprocessed_text
        global current_options

        # Call BERT with reduced options
        bert_result = fill_in(preprocessed_text, current_options, fb)
        text = bert_result[0]
        # update available options
        current_options = bert_result[1]

        # Check if any of the options is used up
        empty = False
        for key in current_options:
            if len(current_options[key]) == 0:
                empty = True
                break
        # Include a warning flag in response
        warn = ""
        if empty:
            warn = "EMPTY"

        # Build response with flask function, default http code is 200 (OK)
        response = make_response({"text": text, "warn": warn})
        # Add header so Angular doesnt complain
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

# --------------------------------------------------------------------------
# REST Endpoints for RNN requests

@api.route('/rnn_shakespeare')
class Shakespeare(Resource):
    def get(self):
        # Call RNN
        text = text_generation(model = model_1, index = 1)

        # Build response with flask function, default http code is 200 (OK)
        response = make_response({"text": text})
        # Add header so Angular doesnt complain
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

@api.route('/rnn_michaeljackson')
class MichaelJackson(Resource):
    def get(self):
        # Call RNN
        text = text_generation(model = model_2, index = 2)

        # Build response with flask function, default http code is 200 (OK)
        response = make_response({"text": text})
        # Add header so Angular doesnt complain
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

@api.route('/rnn_maidofhonor')
class MaidOfHonor(Resource):
    def get(self):
        # Parse arguments
        parser = reqparse.RequestParser()
        parser.add_argument('name1', type=str, help='groom')
        parser.add_argument('name2', type=str, help='bride')
        args = parser.parse_args()

        # Call RNN
        text = text_generation(model = model_3, index = 3)

        # replace generic names with specified ones if provided
        if args["name1"] is not None:
            text = text.replace("Todd", args["name1"])
            text = text.replace("Ben", args["name1"])
            text = text.replace("Mirko", args["name1"])
        if args["name2"] is not None:
            text = text.replace("Anna", args["name2"])
            text = text.replace("Dora", args["name2"])
            text = text.replace("Ele", args["name2"])
            text = text.replace("Tori", args["name2"])
        # remove surname
        text = text.replace("Smith", "")

        # Build response with flask function, default http code is 200 (OK)
        response = make_response({"text": text})
        # Add header so Angular doesnt complain
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

# --------------------------------------------------------------------------

if __name__ == '__main__':
    # Host on 0.0.0.0 (all local adresses), as localhost (loopback) will not be routed through docker
    app.run(host = '0.0.0.0', debug=False)
