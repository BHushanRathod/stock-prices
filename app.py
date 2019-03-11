
import datetime
from pandas_datareader import data as pdr
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/data')
def line():

    global cmpny_name
    try:
        cmpny_name = request.args.get('c')
        # start_date = request.args.get('s_dt')
        # end_date = request.args.get('e_dt')
        step = datetime.timedelta(days=1)
        date_list = []
        end_date_format = datetime.datetime.now()
        start_date_format = end_date_format - datetime.timedelta(days=100)
        start_date = str(start_date_format.date())
        end_date = str(end_date_format.date())

        while start_date_format.date() <= end_date_format.date():
            if start_date_format.date().weekday() in [0,1,2,3,4]:
                date_list.append(start_date_format.date())
            else:
                pass
                # print("pass", start_date_format.date())
            start_date_format += step
        data = pdr.get_data_yahoo(cmpny_name, start=start_date, end=end_date)
        # data = pdr.DataReader('INPX', 'yahoo', start_date, end_date)
        open_d = data['Open']
        close_d = data['Close']
        high_d = data['High']
        low_d = data['Low']
        volume_d = data['Volume']

        max_d = round(max(high_d))

        return render_template('line_chart.html', title='Stock Price for ' + cmpny_name, max=max_d, labels=date_list[4:],
                               high=high_d, low=low_d, close=close_d, open=open_d, volume=volume_d, no_data=False)
    except Exception as e:
        print("In Exception: ", e)
        return render_template('line_chart.html', title='No date found for '+cmpny_name, no_data=True)


if __name__ == '__main__':
    app.run()

