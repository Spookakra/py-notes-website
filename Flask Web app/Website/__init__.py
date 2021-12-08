from flask import Flask

def create_app():
    #initalize flask
    app = Flask(__name__)
    #encript sesion data
    app.config['SECRET_KEY'] = 'PS*#IrqibTg&o5e@G!0HYMD1^TK!3%iWd0VDbgb6HC!r&m*8N5uJm2#XssK!tRqIdbk1qAv#UgvTSSwTXb$z%SeL9R#TppacId%hGob%oN!^F$54J3S4R%h8KF%0DKFZUgWdf&xtZ7f7J*4JWZ$J%MOfFt@PIj*12@$9#AzgH*%XC&OrV0ITy#a%bs7c0El&f*D105' 
    
    #sets up the pages you go to
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app



