from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
import sys
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import io
import matplotlib.pyplot as plt

app = Flask(__name__, static_url_path='/static')

@app.route('/')

def index():

    x = np.arange(0, 100, 1)
    y = [np.random.normal(0,1) for xs in x]

    
    imageName = "paddy" +str(np.random.randint(0,1000))
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(x,y)
    axis.grid(True)
    axis.set_title(imageName)
    FigureCanvas(fig).print_png("static/"+imageName+".jpg")

    return render_template('index.html', imageSource = "static/"+imageName+'.jpg')


