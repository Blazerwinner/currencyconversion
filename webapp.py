from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    favorite_color = request.args['colors'] #get user's input for color input
    if favorite_color == "pink":
        response = "That's my favorite color, too!"
    else:
        response = "My favorite color is pink."
    return render_template('response.html', responsefromServer=response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
