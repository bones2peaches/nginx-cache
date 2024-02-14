from flask import Flask , render_template
from bio.blueprint import bio_bp

app = Flask(__name__ ,    template_folder='templates', static_folder='static', static_url_path='/assets')
app.register_blueprint(bio_bp)

@app.route('/')
def hello():
    return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug=True)