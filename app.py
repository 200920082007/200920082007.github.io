import os
from flask import Flask, flash, render_template, redirect, request
from tasks import add

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

      
