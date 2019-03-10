from datetime import timedelta, datetime


def get_time():
    currentDT = datetime.now()
    now = str(currentDT).split()[0]
    last_month = currentDT.month-1 if currentDT.month > 1 else 12
    last_month2 = now.split('-')
    last_month2[1] = str(0)+str(last_month)if last_month < 10 else last_month
    last_month = ('-'.join(str(x) for x in last_month2))
    return now, last_month


def get_time_week():
    currentDT = datetime.now()
    now = str(currentDT).split()[0]
    date_week_days_ago = datetime.now() - timedelta(days=7)
    one_week_ago = str(date_week_days_ago).split()[0]
    return now, one_week_ago


def proc_json(jsn_f):
    mag_list = []
    x_list = []
    y_list = []
    a = jsn_f.get("features")
    for i in a:
        b = i.get("properties")
        mag = b.get("mag")
        mag_list.append(str(mag))
        b = i.get("geometry")
        c = b.get("coordinates")
        x_list.append(c[0])
        y_list.append(c[1])
    js = list(zip(mag_list, y_list, x_list))
    return js
