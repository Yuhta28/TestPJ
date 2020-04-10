from PIL import Image
from StringIO import StringIO
import requests

r = requests.get('http://1.bp.blogspot.com/_r-MQun1PKUg/SlnHnaLcw6I/AAAAAAAAA_U$
i = Image.open(StringIO(r.content))
i.show()
