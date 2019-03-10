from flask import Flask, render_template, request
from func import get_time, proc_json, get_time_week
from api import call_api, api_url_all, api_url_point

app = Flask(__name__)

# end_date, start_date = get_time()
# jsn_f = call_api(api_url_all(start_date, end_date))
last_point = []


@app.route('/')
def index():
    end_date, start_date = get_time_week()
    jsn_f = call_api(api_url_all(start_date, end_date))
    data = proc_json(jsn_f)
    planes = []
    for i in data:
        planes.append(list(i))
        last_point.append(list(i))
    return render_template('earth.html', planes=planes, zoom=4, center=[33.1217, 47.6153])


@app.route('/cordinate_show', methods=['POST'])
def cordinate():
    end_date, start_date = get_time()
    data = request.form['cordinate']
    center = str(data).split(",")
    final = []
    for x in center:
        final.append(float(x))
    longitude = str(data).split(",")[1]
    latitude = str(data).split(",")[0]
    jsn_f = call_api(api_url_point(start_date, end_date, latitude, longitude))
    data = proc_json(jsn_f)
    planes = []
    for i in data:
        if float(i[0]) > 3:
            planes.append(list(i))
    return render_template('earth.html', planes=planes, zoom=6, center=final)


if __name__ == '__main__':
    app.run(debug=True)
