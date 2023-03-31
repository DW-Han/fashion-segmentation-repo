# import all libraires
from io import BytesIO
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from classification1_use import predict

# Initialize flask and create sqlite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create datatable
class Upload(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(50))
	data = db.Column(db.LargeBinary)

# Create index function for upload and return files
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		file = request.files['file']
		upload = Upload(filename=file.filename, data=file.read())
		db.session.add(upload)
		db.session.commit()
		last_record = db.session.query(Upload).order_by(Upload.id.desc()).first()
		prediction =predict(last_record.data)
		#print(last_record.data)
		print(prediction)


		# return f'Your Image was: {prediction}'

		prediction_data = {'prediction': "classification: " + prediction}
		return render_template('index.html', prediction_data=prediction_data)

	prediction_data = {'prediction': "please submit image below"}
	return render_template('index.html', prediction_data=prediction_data)

# create download function for download files
@app.route('/download/<upload_id>')
def download(upload_id):
	upload = Upload.query.filter_by(id=upload_id).first()
	return send_file(BytesIO(upload.data),
					download_name=upload.filename, as_attachment=True)
