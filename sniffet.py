from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [{"title":"Your Lie in April", "ratings":"5 stars", "genre":"Musical, Drama"},{"title":"Silent Voice", "ratings":"5 stars", "genre":"Drama, Romance"}, {"title":"One Piece", "ratings":"5 stars", "genre":"Adventure"}]

@app.route('/', methods = ['GET'])
def index():
	return jsonify({'message' : '127.0.0.1:8080/<movies or titles>'})


@app.route('/movies', methods = ['GET'])
def returndata():
	
		return jsonify({"Movies" : movies})

@app.route('/titles', methods = ['GET'])
def returntitles():
	mots=[]
	for titles in movies:    
		mots.append({'title' : titles["title"]})
	return jsonify({"Movie Titles" : mots})


@app.route('/titles=<string:name>', methods = ['GET'])
def search(name):
	
	tight = [t for t in movies if t['title']==name]
	
	return jsonify({'Movie' : tight[0]})

@app.route('/movies', methods = ['POST'])
def addmovie():
	mots = {'title':request.json['title'], 'ratings':request.json['ratings'], 'genre':request.json['genre']}
	movies.append(mots)
	return jsonify({'Movies': movies})

@app.route('/movies=<string:name>', methods = ['PUT'])
def editmovie(name):
	mots = [t for t in movies if t['title'] == name]
	mots[0]['title'] = request.json['title']
	mots[0]['ratings'] = request.json['ratings']
	mots[0]['genre'] = request.json['genre']
	return jsonify({'Movies' : mots[0]})

@app.route('/movies=<string:name>', methods = ['DELETE'])
def deletemovie(name):
	mots = [t for t in movies if t['title'] == name]
	movies.remove(mots[0])
	return jsonify({'Movies' : movies})


if __name__ == '__main__':
	app.run(debug = True, port=8080)