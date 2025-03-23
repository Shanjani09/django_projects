from bottle import Bottle, run 
app = Bottle() 
@app.route('/') 
def home_page(): 
    return 'Bottle page 23B01A12G4' 
if __name__ == '__main__': 
    run(app, host='localhost', port=8081)