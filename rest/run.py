from eve import Eve
import platform
import psutil
from flask import jsonify

app = Eve()

#Machine type
@app.route('/function/machinetype')
def machine():
    name = platform.machine()
    return name

#System's release
@app.route('/function/release')
def sysrelease():
    release = platform.release()
    return release

#Release version
@app.route('/function/version')
def versionInfo():
    relversion = platform.version()
    return relversion

#CPU times
@app.route('/cpu/cputimes')
def cpu_times():
    cputimes = psutil.cpu_times()
    cputimes_json = jsonify(cputimes)
    return cputimes_json

if __name__ == '__main__':
    app.run(host='localhost')
