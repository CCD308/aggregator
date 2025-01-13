from flask import Flask, jsonify

app = Flask(__name__)

# 存储工作流输出数据
output_data = {"status": "pending", "message": "No output yet"}

@app.route("/")
def home():
    return jsonify(output_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
