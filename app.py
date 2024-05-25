import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

def get_recommendation(prediction):
    recommendations = {
        "severely stunted": "Anak Anda mengalami stunting parah. Segera konsultasikan dengan dokter untuk penanganan lebih lanjut.",
        "stunted": "Anak Anda mengalami stunting. Konsultasikan dengan ahli gizi dan pastikan anak mendapatkan asupan gizi yang cukup.",
        "normal": "Anak Anda memiliki tinggi badan normal. Pertahankan asupan gizi yang baik dan rutin periksa kesehatan anak.",
        "tinggi": "Anak Anda memiliki tinggi badan di atas rata-rata. Pastikan untuk tetap menjaga asupan gizi seimbang."
    }
    return recommendations.get(prediction, "Hasil tidak dikenali. Silakan coba lagi.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        if not all(key in request.form for key in ("Tinggi_Badan_(cm)", "Umur_(bulan)", "Jenis_Kelamin_(laki-laki/perempuan)")):
            return render_template("index.html", prediction_text="Pastikan semua input terisi.", recommendation="")
        else:
            float_features = [1.0 if x == 'laki-laki' else 0.0 if x == 'perempuan' else float(x) for x in request.form.values()]
            feature = np.array(float_features).reshape(1, -1)
            prediction = model.predict(feature)[0]
            recommendation = get_recommendation(prediction)
            return render_template("index.html", prediction_text=prediction, recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)
