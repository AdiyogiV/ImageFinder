from flask import Flask, request, render_template
from retrieve_image import retrieve_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        image_path, image_clusters, cluster_counts, cluster_image_paths = retrieve_image(description, 10)
        return render_template('index.html', image_path=image_path, image_clusters=image_clusters, cluster_counts=cluster_counts, cluster_image_paths=cluster_image_paths)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
