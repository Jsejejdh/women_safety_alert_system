from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/send-alert', methods=['POST'])
def send_alert():
    data = request.json
    location = data.get("location")

    sender_email = "abcd@gmail.com"
    receiver_email = "xyz@gmail.com"
    password = "cjetwbzvrwrgxvmc"

    message = f"Subject: EMERGENCY ALERT\n\nUser is in danger!\nLocation: {location}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

        print("✅ EMAIL SENT SUCCESSFULLY")
        return jsonify({"status": "Email sent!"})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"status": str(e)})

if __name__ == '__main__':
    app.run(debug=True)