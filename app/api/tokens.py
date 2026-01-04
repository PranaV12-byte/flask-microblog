from app.api import bp

@bp.route('/tokens', methods=['POST'])
def get_token():
    pass

@bp.route('/tokens', methods=['DELETE'])
def revoke_token():
    pass
