from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/index.html')
def man():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/<pagename>')
def render_page(pagename):
    return render_template(pagename)


def write_to_file(data):
    with open('database.txt', 'a') as f:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = f.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as f1:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(
            f1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])


@app.route('/submit_form', methods=['GET', 'POST'])
def get_data():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong"
