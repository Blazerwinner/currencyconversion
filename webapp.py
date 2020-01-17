from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    inches_yards = request.args['Inches'] #get user's input for color input
    if inches_yards == "":
        liters = request.args['Liters']
        if liters == "":
            USD = request.args['USD']
            if USD == "":
                response = ""
            else:
               response = str(int(USD)*1.30) + "Can" 
        else:
            response = str(int(liters)/3.78541) + "Gallons"
    else:
        response = str(int(inches_yards)/36) + "Yards"
    return render_template('response.html', responseFromServer=response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
