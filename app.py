from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Define the signup form
class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    education = StringField('Education', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignupForm()
    if form.validate_on_submit():
        # Collect form data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        address = form.address.data
        age = form.age.data
        education = form.education.data

        try:
            # Connect to the RDS MySQL database
            connection = mysql.connector.connect(
                host='database-1.cv8emuow4jfw.us-east-1.rds.amazonaws.com',  # Replace with your RDS endpoint
                user='admin',               # Replace with your DB username
                password='database1234',    # Replace with your DB password
                database='crafters'         # Replace with your DB name
            )

            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (first_name, last_name, email, address, age, education) VALUES (%s, %s, %s, %s, %s, %s)",
                (first_name, last_name, email, address, age, education)
            )
            connection.commit()
            cursor.close()
            connection.close()

            flash('User successfully registered!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('index'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
