from flask import Flask, render_template, request,redirect,url_for,jsonify

# Creating simple flask application

app = Flask(__name__)

@app.route("/",methods=["GET"]) #route() is a Python decorator to assign URLs in app to functions easily
def welcome():
    return "<h1>Hello World. Please visit index page<h1>"


@app.route("/index",methods=["GET"])
def index():
    return "<h2>This is the index page<h2>"


## variable rule
@app.route('/success/<int:score>')     #parameter
def success(score):
    return "The person has passed and scored an ELO: "+ str(score)

@app.route('/fail/<int:score>')     #parameter
def fail(score):
    return "The person has failed and scored an ELO: "+ str(score)

# A simple form

# We would need render_template, request library too
@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('form.html') 
    #Now we will create an html page to display at templates folder
    else:
        maths = float(request.form['maths']) #maths is text name field value declared in html
        science = float(request.form['science']) #science is text name field value declared in html
        history = float(request.form['history']) #history is text name field value declared in html

        average_marks = (maths+science+history)/3
        res = ""
        if average_marks>=50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res, score=average_marks))
        #return render_template('form.html',score=average_marks)

# Working with API
@app.route('/api', methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)


if __name__ == "__main__":
    app.run(debug=True)