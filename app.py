from flask import Flask, redirect
from datetime import datetime
import os

app = Flask(__name__)

# Diccionario con enlaces por fecha exacta (YYYY-MM-DD)
links = {
    "2025-08-12": "https://youtube.com/live/nBpGc4Q_NVQ?feature=share",  # 12 de agosto 2025
    "2025-08-13": "https://youtube.com/live/dMv3Io7ju_o?feature=share",  # 13 de agosto 2025
    "2025-08-14": "https://youtube.com/live/nBpGc4Q_NVQ?feature=share"   # 14 de agosto 2025
}

@app.route("/")
def redirect_to_event():
    today = datetime.today().strftime('%Y-%m-%d')  # Fecha actual
    # Si la fecha no está en el diccionario, usa siempre el enlace del 12 de agosto
    url = links.get(today, links["2025-08-12"])
    return redirect(url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

