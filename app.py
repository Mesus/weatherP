from flask import Flask, render_template
from weather import WeatherReport as wr
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather/<city>')
def weather(city):
    """Example endpoint returning a list of colors by palette
        This is using docstrings for specifications.
        ---
        parameters:
          - name: city
            in: path
            type: string
            enum: ['北京', '上海']
            required: true
            default: all
        definitions:
          Palette:
            type: object
            properties:
              palette_name:
                type: array
                items:
                  $ref: '#/definitions/City'
          Color:
            type: string
        responses:
          200:
            description: A list of weather (may be filtered by palette)
            schema:
              $ref: '#/definitions/Palette'
            examples:
              rgb: ['yesterday', 'today', 'tomorrow']
        """
    main_func = wr(city)
    city_code = main_func.get_city_code()
    print(city_code)
    if city_code:
        info = main_func.get_weather(city_code)
        return '<br>'.join(info)
    else:
        return "This city name is invalid, please re-enter."


@app.errorhandler(404)
def show_404_page(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def show_500_page(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, ssl_context='adhoc')
