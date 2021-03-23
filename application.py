import os
from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Navigation link routes
@app.route("/")
def index():
    return render_template("index.html");

@app.route("/index")
def home():
    return render_template("index.html");

@app.route("/simple")
def simple():
   return render_template("simple.html");

@app.route("/cantilever")
def cantilever():
    return render_template("cantilever.html");

@app.route("/fix-support")
def fix_support():
    return render_template("fix-support.html");

@app.route("/fixed")
def fixed():
    return render_template("fixed.html");

@app.route("/overhang")
def overhang():
    return render_template("overhang.html");

@app.route("/continuous")
def continuous():
    return render_template("continuous.html");


# Simple Beam Option Routes
@app.route("/simple1")
def simple1():
    return render_template("simple1.html");

@app.route("/simple2")
def simple2():
    return render_template("simple2.html");

@app.route("/simple3")
def simple3():
    return render_template("simple3.html");

@app.route("/simple4")
def simple4():
    return render_template("simple4.html");

@app.route("/simple5")
def simple5():
    return render_template("simple5.html");

@app.route("/simple6")
def simple6():
    return render_template("simple6.html");

@app.route("/simple7")
def simple7():
    return render_template("simple7.html");

@app.route("/simple8")
def simple8():
    return render_template("simple8.html");

@app.route("/simple9")
def simple9():
    return render_template("simple9.html");

@app.route("/simple10")
def simple10():
    return render_template("simple10.html");

@app.route("/simple11")
def simple11():
    return render_template("simple11.html");


# Cantilever Beam Option Routes
@app.route("/cantilever1")
def cantilever1():
    return render_template("cantilever1.html");

@app.route("/cantilever2")
def cantilever2():
    return render_template("cantilever2.html");

@app.route("/cantilever3")
def cantilever3():
    return render_template("cantilever3.html");


# Fix-Support Beam Option Routes
@app.route("/fix-support1")
def fix_support1():
    return render_template("fix-support1.html");

@app.route("/fix-support2")
def fix_support2():
    return render_template("fix-support2.html");

@app.route("/fix-support3")
def fix_support3():
    return render_template("fix-support3.html");


# Fixed Beam Option Routes
@app.route("/fixed1")
def fixed1():
    return render_template("fixed1.html");

@app.route("/fixed2")
def fixed2():
    return render_template("fixed2.html");

@app.route("/fixed3")
def fixed3():
    return render_template("fixed3.html");


# Overhanging Beam Option Routes
@app.route("/overhang1")
def overhang1():
    return render_template("overhang1.html");

@app.route("/overhang2")
def overhang2():
    return render_template("overhang2.html");

@app.route("/overhang3")
def overhang3():
    return render_template("overhang3.html");

@app.route("/overhang4")
def overhang4():
    return render_template("overhang4.html");

@app.route("/overhang5")
def overhang5():
    return render_template("overhang5.html");


# Continuous Beam Option Routes
@app.route("/continuous1")
def continuous1():
    return render_template("continuous1.html");

@app.route("/continuous2")
def continuous2():
    return render_template("continuous2.html");

@app.route("/continuous3")
def continuous3():
    return render_template("continuous3.html");

@app.route("/continuous4")
def continuous4():
    return render_template("continuous4.html");

@app.route("/continuous5")
def continuous5():
    return render_template("continuous5.html");

@app.route("/continuous6")
def continuous6():
    return render_template("continuous6.html");

@app.route("/continuous7")
def continuous7():
    return render_template("continuous7.html");
