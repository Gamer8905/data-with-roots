import os
import io
import base64
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

dataset_path = os.path.join(os.path.dirname(__file__), 'data', 'delivery_dataset.csv')
df = pd.read_csv(dataset_path)

X = df[['distance_km']].values
y = df['delivery_time_min'].values

model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]
intercept = model.intercept_
r_squared = model.score(X, y)

def generate_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['distance_km'], df['delivery_time_min'],
               alpha=0.4, color='#4cc9f0', edgecolors='none', s=30, label='Datos reales')

    x_line = np.linspace(df['distance_km'].min(), df['distance_km'].max(), 100).reshape(-1, 1)
    y_line = model.predict(x_line)
    ax.plot(x_line, y_line, color='#e94560', linewidth=2.5,
            label=f'Línea de regresión: y = {slope:.4f}x + {intercept:.2f}')

    ax.set_xlabel('Distancia (km)', fontsize=12, color='#e2e8f0')
    ax.set_ylabel('Tiempo de entrega (min)', fontsize=12, color='#e2e8f0')
    ax.set_title('Relación Distancia vs Tiempo de Entrega', fontsize=14, fontweight='bold', color='#f1f5f9')
    ax.legend(fontsize=10, loc='upper left')
    ax.set_facecolor('#131b2e')
    fig.patch.set_facecolor('#0b0f19')
    ax.tick_params(colors='#94a3b8')
    ax.spines['bottom'].set_color('#334155')
    ax.spines['left'].set_color('#334155')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.15, color='#94a3b8')

    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    plot_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return plot_base64

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ml/concepts')
def ml_concepts():
    return render_template('ml_concepts.html')

@app.route('/ml/types')
def ml_types():
    return render_template('ml_types.html')

@app.route('/ml/use-cases/use-case-1')
def use_case_1():
    return render_template('use_case_1.html')

@app.route('/ml/use-cases/use-case-2')
def use_case_2():
    return render_template('use_case_2.html')

@app.route('/ml/use-cases/use-case-3')
def use_case_3():
    return render_template('use_case_3.html')

@app.route('/ml/use-cases/use-case-4')
def use_case_4():
    return render_template('use_case_4.html')

@app.route('/ml/supervised/lr/concepts')
def lr_concepts():
    return render_template('lr_concepts.html')

@app.route('/ml/supervised/lr/application', methods=['GET', 'POST'])
def lr_application():
    prediction = None
    distance_input = None
    error = None
    plot_url = generate_plot()

    if request.method == 'POST':
        distance_input = request.form.get('distance', '')
        try:
            distance_val = float(distance_input)
            if distance_val <= 0:
                error = 'Ingrese un valor positivo.'
            else:
                prediction = model.predict([[distance_val]])[0]
                prediction = round(prediction, 2)
        except ValueError:
            error = 'Ingrese un valor numerico valido.'

    stats = {
        'total_records': len(df),
        'slope': round(slope, 4),
        'intercept': round(intercept, 2),
        'r_squared': round(r_squared, 4),
        'mean_distance': round(df['distance_km'].mean(), 2),
        'mean_time': round(df['delivery_time_min'].mean(), 2),
        'min_distance': round(df['distance_km'].min(), 2),
        'max_distance': round(df['distance_km'].max(), 2),
    }

    sample_data = df.head(10).to_dict('records')

    return render_template('lr_application.html',
                           prediction=prediction,
                           distance_input=distance_input,
                           error=error,
                           plot_url=plot_url,
                           stats=stats,
                           sample_data=sample_data)

if __name__ == '__main__':
    app.run(debug=True)
