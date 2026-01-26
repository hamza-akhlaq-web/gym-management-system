from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/membership')
def membership():
    return render_template("membership.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        # Handle contact form submission
        return jsonify({'status': 'success', 'message': 'Thank you for contacting us!'})
    return render_template("contact.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)

