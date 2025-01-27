from datetime import datetime
import zoneinfo
from flask import Flask, request, render_template
import time

app = Flask(__name__)
# zone = zoneinfo.ZoneInfo("Europe/Moscow")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getTime", methods=['GET'])
def getTime():
    # offset = datetime.now(zone).utcoffset().total_seconds()//(60*60)
    offset = datetime.now().utcoffset().total_seconds()//(60*60)
    print(offset) # 3 / 4 - This depends on daylight saving time
    print("browser time: ", request.args.get("time"))
    print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
    return "Done"

