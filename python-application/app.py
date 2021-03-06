from flask import Flask
import epsagon

epsagon.init(
    token='set your token here',
    app_name='pipeline-azure-aks',
    metadata_only=False
)

app = Flask(__name__)
epsagon.flask_wrapper(app)

@app.route('/')
def hello():
    return "Stay inside, stay safe and keep social distancing."

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    app.run(host='0.0.0.0') 
