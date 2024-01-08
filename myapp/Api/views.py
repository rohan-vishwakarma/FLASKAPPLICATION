
from . import bp

@bp.route('/test')
def test_page():
    return 'Testing the Flask Application Factory Pattern'