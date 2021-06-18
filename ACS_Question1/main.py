from flask import Flask
import conversions
app = Flask(__name__)

@app.route("/speech2words/<string:speech>", methods=['GET'])
def speech2words(speech):
    converted_word = conversions.conversion_speech_to_word(speech)
    return converted_word

if __name__ == '__main__':
    app.run(debug=True)