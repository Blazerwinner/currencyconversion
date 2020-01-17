from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/littogals")
def render_littogals():
    return render_template('littogals.html')
    
@app.route("/ustocan")
def render_ustocan():
    return render_template('ustocan.html')

@app.route("/response")
def render_response():
    unit = request.args['unit'] #get user's input for color input
    starting_value = request.args['starting_value']
    if starting_value == "":
        response = ""
    else:
        if unit == 'inches':
            response = str(float(starting_value)/36) + "Yards"
        if unit == 'liters':
                response = str(float(starting_value)/3.78541) + "Gallons"
        if unit == 'usd':
                   response = str(float(starting_value)*1.30) + "Can" 
    return render_template('response.html', responseFromServer=response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
