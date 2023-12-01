from flask import Flask, render_template
def administrator():
    return render_template('administrator.html')