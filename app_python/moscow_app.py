"""
- flask is a general python webapp framework
- Module datetime gives us time of any Timezone
"""
from datetime import datetime, timedelta, timezone
from flask import Flask, render_template
from prometheus_client import start_http_server, Counter

app = Flask(__name__)
MOSCOW = timezone(timedelta(hours=3), "Moscow")
HOST = "0.0.0.0"
PORT = 5000
PROMETHEUS_PORT = 5005

VISITS_FILE = "/data/visits"
TOTAL_REQUESTS = Counter('moscow_total_requests', 'Total number of requests')
start_http_server(PROMETHEUS_PORT)

def read_visits():
    try:
        with open(VISITS_FILE, "r", encoding="utf-8") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def write_visits(count):
    with open(VISITS_FILE, "w", encoding="utf-8") as file:
        file.write(str(count))

@app.route("/")
def index():
    """A primary method generating main and only webpage"""
    TOTAL_REQUESTS.inc()
    visits = read_visits() + 1
    print("Requests Counter updated:", visits, flush=True)
    write_visits(visits)

    msc = datetime.now(MOSCOW)
    current = datetime.today()

    msc = msc.strftime("%H:%M:%S %Z")
    current = current.strftime("%H:%M:%S %Z")

    return render_template("index.html", msc=msc, current=current)


if __name__ == "__main__":
    app.run(HOST, PORT)
