# flaskweb.py ~ app.py
from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Execute app.py and capture its stdout
        result = subprocess.run(
            ['python3', 'regresi.py'],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error running regresi.py: {e.stderr}"
    except FileNotFoundError:
        output = "Error: regresi.py not found. Make sure it's in the same directory or provide the full path."

    # Render the output on a simple HTML page
    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>App Output</title>
        </head>
        <body>
            <h1>Output from regresi.py:</h1>
            <pre>{{ output }}</pre>
        </body>
        </html>
        """,
        output=output
    )

#if __name__ == '__main__':
#    app.run(debug=True)

if __name__ == '__main__':
    app.run(port=8000) #(debug=True)

