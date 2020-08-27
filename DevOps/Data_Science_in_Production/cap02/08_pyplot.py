import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
import base64
image = open("luna.png", "rb").read()
encoded = base64.b64encode(image)
result = requests.get("http://52.90.199.190:5000/",
json = {'msg': encoded})
encoded = result.json()['response']
imgData = base64.b64decode(encoded)
plt.imshow( np.array(Image.open(io.BytesIO(imgData))))
