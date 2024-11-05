from flask import Flask, jsonify, request

# إنشاء تطبيق Flask
app = Flask(__name__)

# نقطة النهاية الافتراضية
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

# مثال على نقطة نهاية GET
@app.route('/greet/<string:name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# مثال على نقطة نهاية POST
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()  # استقبال البيانات بصيغة JSON
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    result = num1 + num2
    return jsonify({"result": result})

# بدء التطبيق
if __name__ == '__main__':
    app.run(debug=True)