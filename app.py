from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚨 FloodGuard AI Live - Chennai Flood Prediction"

@app.route('/map')
def map():
    return "🗺️ Live Flood Heatmap - Red zones = Danger!"

if __name__ == '__main__':
    app.run(debug=True)
