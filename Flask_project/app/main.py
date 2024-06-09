from flask import Flask, request, jsonify, render_template

from torch_utils import transform_image, get_prediction

app = Flask(__name__)

# Enable auto-reloading for HTML templates
app.config['TEMPLATES_AUTO_RELOAD'] = True

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/predict", methods=["POST"])
def predict():

    if request.method != "POST":
        return jsonify({"error": "Method is not allowed"}), 405

    try:
        file = request.files.get("file")

        if file is None or file.filename == "":
            return jsonify({"error": "no file"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": "format not supported"}), 400

        img_bytes = file.read()
        tensor = transform_image(img_bytes)
        prediction = get_prediction(tensor)
        data = {
            "prediction": prediction.item(),
            "class_name": str(prediction.item()),
        }

        return render_template('result.html', data=data)
    except Exception as e:
        return jsonify({"error dring prediction": e})


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')
