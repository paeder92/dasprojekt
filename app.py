from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', imageSource = "static/theProject.jpg")

    

@app.route('/createGraph', methods=['POST'])
def createGraph():
    
    valueA = request.form['valueA']     # this variable stores the value of textfield "Value A"
    valueB = request.form['valueB']     # this variable stores the value of textfield "Value B"
    plotType = request.form["plotType"]
    
    print("Value A: " + valueA)
    print("Value B: " + valueB)

    # Have fun working with valueA and valueB ♥

    # Random Graph gets generated
    x = np.arange(0, 1000, 1)
    y = [np.random.normal(float(valueA), float(valueB)) for xs in x]

    imageName = "normal_dist_" +str(np.random.randint(0,1000))
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    if plotType == "plot":
        axis.plot(x,y)
        
    elif plotType == "hist":
        axis.hist(y, bins=20)
    
    axis.grid(True)
    axis.set_title(imageName)
    FigureCanvas(fig).print_png("static/"+imageName+".jpg")

    # HTML Page with random graph gets rendered
    return render_template('index.html', imageSource = "static/"+imageName+'.jpg')
