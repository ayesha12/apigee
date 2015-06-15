Ayesha :

My Apigee Assignment

Steps to run :
1. install Flask : 
	sudo pip install flask
2. For Milestone 1: 
	2.1. Run the script jsonRes.py :
		python jsonRes.py
	2.2. To test the request :
		curl -v http://127.0.0.1:8080/hello
	2.3. To test milestone 2 following is the request :
		curl -H "Content-type: text/plain" -X POST http://127.0.0.1:8080/input -d $'34.8 1432681200\n31.4 1432684800\n30.9 1432688400\n31.3 1432692000\n33.1 1432695600\n41.3 1432699200\n50.4 1432702800\n57.3 1432706400\n64.2 1432710000\n63.2 1432713600\n'

3. milestone 3 :
	run milestone3.py
	test request :
		curl -H "Content-type: text/plain" -X POST http://127.0.0.1:8080/input -d $'cpu 34.8 1432681200\ndisk 30.9 1432688400\nmemory 63.2 1432713600\ncpu 31.4 1432684800\ndisk 64.2 1432710000\n' 

4. Yet to handle negative test cases. 
	
