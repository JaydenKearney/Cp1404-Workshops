from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :) </h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)

@app.route('/convert_temp')
@app.route('/convert_temp/<temp>')
def convert_temp(temp=0):
    return str(convert_celcius_to_farenheit(temp))


def convert_celcius_to_farenheit(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit

if __name__ == '__main__':
    app.run()
