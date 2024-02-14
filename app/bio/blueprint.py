from flask import Blueprint , render_template

bio_bp = Blueprint('bio_blueprint', __name__   ,
                   template_folder='templates', static_folder='static', static_url_path='/assets/bio')

@bio_bp.route('/bio')
def index():
    return render_template('bio.html')