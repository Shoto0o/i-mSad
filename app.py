from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    user_location = request.json.get('location', 'Unknown')
    weather_data = {
        "location": user_location,
        "temperature": random.randint(15, 30),
        "humidity": random.randint(40, 90),
        "uv_index": random.randint(1, 10),
        "condition": random.choice(["Sunny", "Cloudy", "Rainy", "Stormy"])
    }
    return jsonify(weather_data)

@app.route('/adjust_temperature', methods=['POST'])
def adjust_temperature():
    user_temp = request.json.get('temperature')
    return jsonify({"status": "Temperature set to {}".format(user_temp)})

@app.route('/foot_analysis', methods=['POST'])
def foot_analysis():
    foot_pressure_data = {
        "high_burden": ["Heel", "Ball of Foot"],
        "low_burden": ["Toes", "Arch"]
    }
    return jsonify(foot_pressure_data)

@app.route('/performance_suggestions', methods=['POST'])
def performance_suggestions():
    suggestions = [
        "Try adjusting your stride for better stability.",
        "Distribute weight evenly to reduce foot pressure.",
        "Use softer insoles for comfort.",
        "Improve ankle mobility to enhance performance."
    ]
    return jsonify({"suggestion": random.choice(suggestions)})

if __name__ == '__main__':
    app.run(debug=True)
