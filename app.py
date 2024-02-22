from flask import Flask, render_template
from flask import jsonify
from flask_cors import CORS
import speedtest

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Render a simple HTML template
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Data to be accessed in JavaScript
    st = speedtest.Speedtest()
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    data = {'download': f"Download Speed: {download_speed:.2f} Mbps",'upload' :f"Upload Speed: {upload_speed:.2f} Mbps"}
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)
