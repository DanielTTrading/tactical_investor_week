from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)

# Diccionario con enlaces por fecha exacta (YYYY-MM-DD)
links = {
    "2025-08-12": "https://youtube.com/live/b1X-e2FmA64?feature=share",  # 12 de agosto 2025
    "2025-08-13": "https://youtube.com/live/4aqdIyB3lK4?feature=share",  # 13 de agosto 2025
    "2025-08-14": "https://youtube.com/live/BEP9XNzL3n4?feature=share"   # 14 de agosto 2025
}

@app.route("/tactical_investor_week")
def tactical_investor_week():
    today = datetime.today().strftime('%Y-%m-%d')  # Fecha actual
    url = links.get(today, links["2025-08-12"])
  # Si no está en el diccionario, redirige a YouTube genérico
    return redirect(url)

if __name__ == "__main__":
    # Puerto que Railway usará, si no existe usa 5000
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
