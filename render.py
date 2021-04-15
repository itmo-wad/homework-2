from flask import Flask, render_template
app = Flask(__name__, static_folder='images')

@app.route('/')
def render():
    return render_template('myfile.html')

@app.route('/<path:path>')
def images(path):
    return send_from_directory(app.static_folder,path)


if __name__=='__main__':
    app.run(debug=True)