from flask import Flask, request
import os
import glob

app = Flask(__name__)

@app.route("/health", methods=['GET'])
def health():
    return "Good",200

@app.route("/clean/logs", methods=['GET'])
def clean_logs():
    try:
        log_path = "/app/*.log.*"
        log_files = glob.glob(log_path)

        for item in log_files:
            os.remove(item)
        return "OK"
    except Exception as e:
        return {"error":str(e)}

@app.route("/authorization", methods=['GET'])
def authorization():
    print("call authorization for client")

    return "OK", 200

@app.route("/api/v2/info", methods=['GET'])
def info():
    print("call info api")
    return {"state":"info api"}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)