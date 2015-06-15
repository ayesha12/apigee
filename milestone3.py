from flask import Flask, url_for, Response, request,jsonify
from werkzeug.contrib.cache import SimpleCache
import json
import math

app = Flask(__name__)
cache = SimpleCache()

def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

@app.route('/stats')
def api_stats():
	rs = cache.get_dict("cpucount","cpustart","cpuend","cpumaxValue","cpuminValue","cpuaverageValue","cpu99thPercentile","memcount","memstart","memend","memmaxValue","memminValue","memaverageValue","mem99thPercentile","dcount","dstart","dend","dmaxValue","dminValue","daverageValue","d99thPercentile")
        print rs["cpucount"]
	
	ccount = rs["cpucount"]
	cstart = rs["cpustart"]

	res = {"cpu": { "count": ccount ,"timeRange": {"start": cstart,"end": rs["cpuend"]},"maxValue": rs["cpumaxValue"],"minValue": rs["cpuminValue"],"averageValue": rs["cpuaverageValue"],"99thPercentile": rs["cpu99thPercentile"]}, "memory": { "count": rs["memcount"],"timeRange": {"start": rs["memstart"],"end": rs["memend"]},"maxValue": rs["memmaxValue"],"minValue": rs["memminValue"],"averageValue": rs["memaverageValue"],"99thPercentile": rs["mem99thPercentile"]}, "disk": { "count": rs["dcount"],"timeRange": {"start": rs["dstart"],"end": rs["dend"]},"maxValue": rs["dmaxValue"],"minValue": rs["dminValue"],"averageValue": rs["daverageValue"],"99thPercentile": rs["d99thPercentile"]}}

        resFinal = jsonify(res)

	print resFinal
	return resFinal

@app.route('/input', methods=['POST'])
def api_input():
	cpuvalues = []
	cputimes = []
	memvalues = []
        memtimes = []
	dvalues = []
        dtimes = []

	indata = request.data
	eachln = indata.splitlines()
	for item in eachln :
		eachline = item.split(" ")
		mName = eachline[0]
		if mName == "cpu" :
			cpuvalues.append(float(eachline[1]))
			cputimes.append(int(eachline[2]))
		elif mName == "memory" :
			memvalues.append(float(eachline[1]))
                        memtimes.append(int(eachline[2]))
		elif mName == "disk" :
			dvalues.append(float(eachline[1]))
                        dtimes.append(int(eachline[2]))

	cpuavg = float(float(sum(cpuvalues))/float(len(cpuvalues)))
	cpuavg = round(cpuavg,2)
	cpunnP = percentile(cpuvalues, 99)
	
	memavg = float(float(sum(memvalues))/float(len(memvalues)))
        memavg = round(memavg,2)
        memnnP = percentile(memvalues, 99)

	davg = float(float(sum(dvalues))/float(len(dvalues)))
        davg = round(davg,2)
        dnnP = percentile(dvalues, 99)


	resp = Response(status=200, mimetype='application/json')

	cpuvalDic = {'cpucount' : len(cpuvalues), 'cpustart': min(cputimes), 'cpuend': max(cputimes), 'cpumaxValue': max(cpuvalues),'cpuminValue': min(cpuvalues),'cpuaverageValue': cpuavg, 'cpu99thPercentile': cpunnP, 'memcount' : len(memvalues), 'memstart': min(memtimes), 'memend': max(memtimes), 'memmaxValue': max(memvalues),'memminValue': min(memvalues),'memaverageValue': memavg, 'mem99thPercentile': memnnP, 'dcount' : len(dvalues), 'dstart': min(dtimes), 'dend': max(dtimes), 'dmaxValue': max(dvalues),'dminValue': min(dvalues),'daverageValue': davg, 'd99thPercentile': dnnP }


	cache.set_many(cpuvalDic,timeout=60 * 50)	
      	return resp


@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'message'  : 'Hello World!'
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp



if __name__ == '__main__':
    app.config["JSON_SORT_KEYS"] = False
    app.debug = True
    app.run(threaded=True, host='127.0.0.1', port=8080)

