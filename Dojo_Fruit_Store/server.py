#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=["POST"])         
def checkout():
    print(request.form)
    return render_template("checkout.html", strawberry_quantity = request.form["strawberry"], raspberry_quantity = request.form["raspberry"], apple_quantity = request.form["apple"], 
    fname = request.form["first_name"], lname = request.form["last_name"], student_no = request.form["student_id"])
    print(f"Charging {request.form['first_name']} + request.form['last_name'] for fruits")


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    