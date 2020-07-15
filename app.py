### Flask
from flask import Flask, render_template, request
### Download photo
from skimage import io
### Painting
from PIL import Image
from io import BytesIO
import base64
### MY functions
from static.Neuron_Network.Network_features.Neuron_Work         import calculation
from static.Neuron_Network.Network_features.Photo_Processing    import translate_arr, fragmentation
from static.Neuron_Network.Network_features.Reckoning_Equations import count


app = Flask(__name__)


@app.route('/')
@app.route('/Start.html')
def start():
    return render_template('Start.html')


@app.route("/Download.html", methods=["POST", "GET"])
def download():
    if request.method == "POST":
        try:
            file = request.files["photo"]
            photo = io.imread(file)
        except ValueError:
            return render_template("Download.html")
        io.imsave('static/Neuron_Network/img/paint.png', photo)
        translate_arr()
        return render_template("Result.html", start=True)
    return render_template("Download.html")


@app.route('/Painting.html', methods=["POST", "GET"])
def painting():
    if request.method == "POST":
        photo = request.form['PHOTO']
        image = Image.open(BytesIO(base64.b64decode(photo)))
        r, g, b, a = image.split()
        a.save('static/Neuron_Network/img/paint.png', 'PNG')
        del r, g, b, a, image, photo
        return render_template("Result.html", start=True)
    return render_template('Painting.html')


if __name__ == '__main__':
    app.run(debug=False)
