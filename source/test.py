from adflush_encodings import *

a = "https://use.typekit.net/xdg0gnq.css"
b = "https://use.typekit.net/xdg0gnq.css#onloiq=i"

url_emb_a = char2vec_pretrained(a, True)
url_emb_b = char2vec_pretrained(b, True)

print(url_emb_a[10:15])
print(url_emb_b[10:15])