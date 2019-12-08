from flask import Flask, request, render_template, jsonify
from SPARQLWrapper import SPARQLWrapper, JSON
from wikidata import WIKIDATA_REQUEST1, WIKIDATA_REQUEST2

app = Flask(__name__)

endpoint_url = "https://query.wikidata.org/sparql"
def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['post'])
def search():
    if request.method == 'POST':
        search = request.form['search']
        search = search.lower()
        print(search)

        #Apply Wikidata request
        wikidata_request_send = WIKIDATA_REQUEST1 + "\"" + search + "\"" + WIKIDATA_REQUEST2
        print(wikidata_request_send)

        results = get_results(endpoint_url, wikidata_request_send)

        #Filtering duplicates
        listIdsSPECIES = []
        listResults = []
        for result in results["results"]["bindings"]:

            id = result["identifiantSPECIES"]["value"]
            print(id)
            if id not in listIdsSPECIES:
                listIdsSPECIES.append(id)
                listResults.append(result)
                #print(result)

        return render_template('index.html', items = listResults)

if __name__ == '__main__':
    app.run()
