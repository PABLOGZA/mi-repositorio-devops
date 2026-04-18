from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello_world():
    return '¡Pipeline CI/CD funcionando con Docker y LocalStack!'

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)