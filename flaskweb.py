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
    # Loop through all feature variables to create a plot for each one
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

