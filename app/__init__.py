from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '$up3r$3cretkey'



from app import views