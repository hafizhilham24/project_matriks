# flaskweb.py ~ app.py

from flask import Flask, render_template, render_template_string
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

# Import the function from the regression script
from regresi import run_regression_and_get_results

app = Flask(__name__)

# --- HTML Template (No change from before) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Regresi Linear Berganda</title>
    <style>
        body { font-family: monospace; background-color: #1a1a1a; color: #f0f0f0; }
        pre { white-space: pre-wrap; word-wrap: break-word; }
        .container { max-width: 1000px; margin: 2rem auto; padding: 1rem; background-color: #333; border-radius: 8px; }
        img { max-width: 100%; height: auto; margin-top: 20px; border: 1px solid #555; }
        .plot-container { margin-bottom: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hasil Analisis Regresi</h1>
        {% if output %}
        <pre>{{ output }}</pre>
        {% else %}
        <pre>{{ error }}</pre>
        {% endif %}
        
        <h2>Grafik Regresi</h2>
        {% if plots %}
            {% for plot in plots %}
                <div class="plot-container">
                    <h3>{{ plot.feature_name }} vs {{ plot.target_name }}</h3>
                    <img src="data:image/png;base64,{{ plot.url }}" alt="Linear Regression Plot">
                </div>
            {% endfor %}
        {% endif %}
    </div>
</body>
</html>
"""

def generate_plot(feature_data, target_data, theta, feature_index, feature_name, target_name):
    """Generates a Matplotlib plot and returns a Base64 encoded string."""
    try:
        x_data = np.array([row[feature_index] for row in feature_data])
        y_data = np.array(target_data)

        intercept = theta.get_value(0, 0)
        slope = theta.get_value(feature_index + 1, 0)
        regression_line = intercept + slope * x_data

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(x_data, y_data, color='blue', label='Data Points')
        ax.plot(x_data, regression_line, color='red', label='Regression Line')
        ax.set_title(f'Plot Regresi: {feature_name.replace("_", " ")} vs {target_name.replace("_", " ")}')
        ax.set_xlabel(feature_name.replace("_", " "))
        ax.set_ylabel(target_name.replace("_", " "))
        ax.legend()
        plt.tight_layout()

        buf = BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        
        plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')
        return {"url": plot_url, "feature_name": feature_name, "target_name": target_name}
    except Exception as e:
        return {"error": f"Error generating plot for {feature_name}: {e}"}

# --- FUNGSI BARU DITAMBAHKAN DI SINI ---
def generate_actual_vs_predicted_plot(theta, feature_data, target_data, target_name):
    """
    Generates an 'Actual vs. Predicted' plot for the full model
    and returns a Base64 encoded string.
    """
    try:
        y_actual = np.array(target_data)
        predictions = []
        
        # Dapatkan intercept (theta[0])
        intercept = theta.get_value(0, 0)
        
        # Hitung prediksi penuh untuk setiap baris data
        for row in feature_data:
            prediction = intercept
            for i in range(len(row)):
                # Dapatkan slope untuk feature_index 'i' (theta[i+1])
                slope = theta.get_value(i + 1, 0)
                prediction += slope * row[i]
            predictions.append(prediction)
        
        x_predicted = np.array(predictions)

        # Mulai plotting
        fig, ax = plt.subplots(figsize=(8, 6))
        # Gunakan warna lain agar terlihat beda
        ax.scatter(x_predicted, y_actual, color='green', alpha=0.6, label='Data Points (Prediksi vs Aktual)')
        
        # Buat garis y=x (perfect fit line)
        min_val = min(np.min(x_predicted), np.min(y_actual))
        max_val = max(np.max(x_predicted), np.max(y_actual))
        ax.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='Perfect Fit Line (Prediksi = Aktual)')
        
        ax.set_title(f'Plot Regresi: Aktual vs. Prediksi Model Penuh')
        ax.set_xlabel(f'Prediksi {target_name.replace("_", " ")}')
        ax.set_ylabel(f'Aktual {target_name.replace("_", " ")}')
        ax.legend()
        plt.tight_layout()

        # Konversi ke Base64 (sama seperti fungsi lainnya)
        buf = BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        
        plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')
        # Kita sesuaikan 'feature_name' dan 'target_name' agar judul <h3> di HTML pas
        return {"url": plot_url, "feature_name": "Aktual vs. Prediksi", "target_name": "Model Penuh"}

    except Exception as e:
        return {"error": f"Error generating Actual vs Predicted plot: {e}"}
# --- AKHIR FUNGSI BARU ---


@app.route('/')
def run_script_and_show_plot():
    """
    Executes the regression analysis, generates a plot for each feature,
    and displays the output and plots.
    """
    results = run_regression_and_get_results()

    if "error" in results:
        return render_template_string(HTML_TEMPLATE, error=results["error"], output=None, plots=[])
    
    model_output = results["model_str"]
    theta = results["theta"]
    feature_data = results["raw_features"]
    target_data = results["raw_target"]
    target_name = results["target_name"]
    feature_names = results["feature_names"]
    
    plots = []

    # --- TAMBAHAN KODE: Buat plot Aktual vs. Prediksi (Plot Alternatif) ---
    # Plot ini dibuat pertama kali dan ditambahkan ke list 'plots'
    try:
        avp_plot_info = generate_actual_vs_predicted_plot(
            theta, 
            feature_data, 
            target_data, 
            target_name
        )
        plots.append(avp_plot_info) # Menambahkan plot ini di urutan pertama
    except Exception as e:
        plots.append({"error": f"Error generating A-v-P plot: {e}", "feature_name": "Error Plot", "target_name": ""})
    # --- AKHIR TAMBAHAN KODE ---
    
    # Loop through all feature variables to create a plot for each one
    # (Kode ini tetap sama, plot-plot ini akan ditambahkan SETELAH plot di atas)
    for i, feature_name in enumerate(feature_names):
        plot_info = generate_plot(feature_data, target_data, theta, i, feature_name, target_name)
        if "url" in plot_info:
            plots.append(plot_info)
        else:
            # Handle plot generation error
            plots.append(plot_info)

    return render_template_string(
        HTML_TEMPLATE,  
        output=model_output,  
        plots=plots
    )


if __name__ == '__main__':
    app.run(port=8000) #(debug=True)
