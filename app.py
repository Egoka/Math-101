### Flask
from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=False)
