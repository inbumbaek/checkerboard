from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("checkerboard.html", row=8, col=8, color1='red', color2='black')

@app.route('/<int:x>')
def row(x):
    return render_template("checkerboard.html", row=x, col=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("checkerboard.html", row=x, col=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<string:one>')
def row_col_one(x,y,one):
    return render_template("checkerboard.html", row=x, col=y, color1='black', color2='one')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_two(x,y,one,two):
    return render_template("checkerboard.html", row=x, col=y, color1=two, color2=one)

if __name__=="__main__":
    app.run(debug=True)

# http://localhost:5000 - should display 8 by 8 checkerboard
# http://localhost:5000/4 - should display 8 by 4 checkerboar
# http://localhost:5000/(x)/(y) - should display x by y checkerboard.