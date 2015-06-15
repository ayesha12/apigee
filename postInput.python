from flask import Flask, url_for, Response, request,jsonify
#from flask_cache import Cache
from werkzeug.contrib.cache import SimpleCache
import json
import math
#import numpy as np

#from werkzeug.contrib.cache import MemcachedCache
#cache = MemcachedCache(['127.0.0.1:8080'])

app = Flask(__name__)
cache = SimpleCache()
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})

def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

@app.route('/stats')
def api_stats():
	#global cache
	#resp = cache.get_dic('statValues')
	rs = cache.get_dict("count","start","end","maxValue","minValue","averageValue","99thPercentile")
        print rs["count"]

	res = {"count": rs["count"],"timeRange": {"start": rs["start"],"end": rs["end"]},"maxValue": rs["maxValue"],"minValue": rs["minValue"],"averageValue": rs["averageValue"],"99thPercentile": rs["99thPercentile"]}
        resFinal = jsonify(res)

	print resFinal
	#respStat = Response(resp, status=200, mimetype='application/json')
	return resFinal

@app.route('/input', methods=['POST'])
def api_input():
	values = []
	times = []
	#global cache

	indata = request.data
	eachln = indata.splitlines()
	for item in eachln :
		#print item
		eachline = item.split(" ")
		#print eachline
		values.append(float(eachline[0]))
		times.append(int(eachline[1]))
	avg = float(float(sum(values))/float(len(values)))
	avg = round(avg,2)
	nnP = percentile(values, 99)
	#res = {"count": len(values),"timeRange": {"start": min(times),"end": max(times)},"maxValue": max(values),"minValue": min(values),"averageValue": avg,"99thPercentile": nnP}
	#resFinal = jsonify(res)
	resp = Response(status=200, mimetype='application/json')

	valDic = {'count' : len(values), 'start': min(times), 'end': max(times), 'maxValue': max(values),'minValue': min(values),'averageValue': avg, '99thPercentile': nnP }

	#print valDic	
	cache.set_many(valDic,timeout=60 * 50)	
	#rs = cache.get_dict("count","start")
	#print rs["count"]
	#print avg
	#print len(values)
	#print min(values)
	#print min(times)
	#print indata
      	return resp


@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'message'  : 'Hello World!'
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    #resp.headers['Link'] = 'http://luisrei.com'
    return resp



if __name__ == '__main__':
#    cache.init_app(app)
    app.config["JSON_SORT_KEYS"] = False
    app.debug = True
    app.run(threaded=True, host='127.0.0.1', port=8080)
    #app.config['CACHE_TYPE'] = 'simple'

