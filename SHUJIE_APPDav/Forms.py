from wtforms import Form, StringField, RadioField, SelectField, SelectMultipleField, validators, PasswordField, IntegerField, TextAreaField, ValidationError, FloatField, TimeField, SubmitField, DecimalField, widgets, BooleanField, PasswordField
from wtforms.fields import EmailField, DateField
from wtforms import widgets, BooleanField
import re
from wtforms.validators import DataRequired, Length, InputRequired, Length, NumberRange, ValidationError
from flask_wtf.file import FileField
from flask_wtf import FlaskForm
import datetime
from datetime import date, timedelta, datetime, time
import string


# JQ start
class CreateProductForm(Form):
    name = StringField('Product Name', [validators.Length(max=50)])
    type = StringField('Product Type', [validators.Length(max=50)])
    rating = RadioField('Sustainability', choices=[('1', 'Bad'), ('2', 'Neutral'), ('3', 'Good')], default='2')
    img = FileField('Image', [validators.Length(max=50)])

    def validate_name(form, field):
        if field.data == "":
            raise ValidationError('Enter a product name')

    def validate_type(form, field):
        if field.data == "":
            raise ValidationError('Enter the product type')


class CreateTipForm(Form):
    title = StringField('Title', [validators.Length(max=50)])
    desc = TextAreaField('Description')

    def validate_title(form, field):
        if field.data == "":
            raise ValidationError('Enter a Title')

    def validate_desc(form, field):
        if field.data == "":
            raise ValidationError('Enter the description')


# JQ end


# Shu Jie start
class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    email = EmailField('Email Address',
                       [validators.DataRequired(), validators.Length(min=4, max=150), validators.Email()])
    gender = RadioField('Gender', [validators.DataRequired()], choices=[('F', 'Female'), ('M', 'Male')], default=None)
    birthdate = DateField("Date Of Birth", [validators.DataRequired(message='Enter valid date'), ], format="%Y-%m-%d")
    postal_code = IntegerField('Postal Code', [validators.NumberRange(min=000000, max=999999),
                                               validators.DataRequired(message='Please enter valid postal code')])
    city = SelectField('City', [validators.DataRequired()], choices=[('Ang Mo Kio', 'Ang Mo Kio'),
                                                                     ('Bedok', 'Bedok'),
                                                                     ('Bishan', 'Bishan'),
                                                                     ('Boon Lay', 'Boon Lay'),
                                                                     ('Bukit Batok', 'Bukit Batok'),
                                                                     ('Bukit Merah', 'Bukit Merah'),
                                                                     ('Bukit Panjang', 'Bukit Panjang'),
                                                                     ('Bukit Timah', 'Bukit Timah'),
                                                                     ('Central Area', 'Central Area'),
                                                                     ('Choa Chu Kang', 'Choa Chu Kang'),
                                                                     ('Clementi', 'Clementi'),
                                                                     ('Geylang', 'Geylang'),
                                                                     ('Hougang', 'Hougang'),
                                                                     ('Jurong East', 'Jurong East'),
                                                                     ('Jurong West', 'Jurong West'),
                                                                     ('Kallang/Whampoa', 'Kallang/Whampoa'),
                                                                     ('Lim Chu Kang', 'Lim Chu Kang'),
                                                                     ('Mandai', 'Mandai'),
                                                                     ('Marine Parade', 'Marine Parade'),
                                                                     ('Novena', 'Novena'),
                                                                     ('Pasir Ris', 'Pasir Ris'),
                                                                     ('Punggol', 'Punggol'),
                                                                     ('Queenstown', 'Queenstown'),
                                                                     ('Rochor', 'Rochor'),
                                                                     ('Sembawang', 'Sembawang'),
                                                                     ('Sengkang', 'Sengkang'),
                                                                     ('Serangoon', 'Serangoon'),
                                                                     ('Tampines', 'Tampines'),
                                                                     ('Tanglin', 'Tanglin'),
                                                                     ('Toa Payoh', 'Toa Payoh'),
                                                                     ('Woodlands', 'Woodlands'),
                                                                     ('Yishun', 'Yishun')], default=None)
    address = StringField('Address', [validators.Length(min=4, max=50),
                                      validators.DataRequired(message='Please enter a valid address')])
    password = PasswordField('Password', [validators.InputRequired(), validators.Length(min=6, max=100),
                                          validators.EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.InputRequired('please re enter password')])
    agree_terms = BooleanField("", validators=[validators.DataRequired()])

    security_question1 = SelectField('Security Question 1:',
                                     choices=[('What city were you born in?',
                                               'What city were you born in?'),
                                              ('What is the name of your first pet?',
                                               'What is the name of your first pet?'),
                                              ('What is your favorite book?',
                                               'What is your favorite book?')])
    security_answer1 = StringField('Security Answer 1:',
                                   validators=[validators.Length(min=1, max=150), validators.DataRequired()])

    security_question2 = SelectField('Security Question 2:',
                                     choices=[('What is your favorite movie?',
                                               'What is your favorite movie?'),
                                              ('What is your favorite food?',
                                               'What is your favorite food?'),
                                              ('What is your favorite sports?',
                                               'What is your favorite sports?')])
    security_answer2 = StringField('Security Answer 2:',
                                   validators=[validators.Length(min=1, max=150), validators.DataRequired()])

    security_question3 = SelectField('Security Question 3:',
                                     choices=[('What is the name of your favorite teacher?',
                                               'What is the name of your favorite teacher?'),
                                              ('What is the name of your best friend in high school?',
                                               'What is the name of your best friend in high school?'),
                                              ('What is your favorite color?',
                                               'What is your favorite color?')])
    security_answer3 = StringField('Security Answer 3:',
                                   validators=[validators.Length(min=1, max=150), validators.DataRequired()])

    def validate_first_name(form, field):
        if not re.match("^[a-zA-Z]*$", field.data):
            raise ValidationError('First name must contain only letters')

    def validate_last_name(form, field):
        if not re.match("^[a-zA-Z]*$", field.data):
            raise ValidationError('Last name must contain only letters')

    def validate_email(form, field):
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", field.data):
            raise ValidationError('Enter a valid email address')

    def validate_birthdate(form, field):
        today = date.today()
        if field.data > today:
            raise validators.ValidationError('Birthdate cannot be a future date')

        min_birthdate = today - timedelta(days=365 * 10)  # Minimum birthdate is 10 years ago
        if field.data > min_birthdate:
            raise validators.ValidationError('You must be at least 10 years old')

    def validate_postal_code(form, field):
        if not (0 <= field.data <= 999999):
            raise ValidationError('Please enter a valid postal code')

    def validate_address(form, field):
        if not (4 <= len(field.data) <= 50):
            raise ValidationError('Address must be between 4 to 50 characters')

    def validate_password(form, field):
        # Check if the password contains at least one letter
        if not any(char.isalpha() for char in field.data):
            raise ValidationError('Password must contain at least one letter')

        # Check if the password contains at least one number
        if not any(char.isdigit() for char in field.data):
            raise ValidationError('Password must contain at least one number')

        # Check if the password contains at least one special character
        special_characters = r"!@#$%^&*()-_+="
        if not any(char in special_characters for char in field.data):
            raise ValidationError('Password must contain at least one special character')

    def validate_confirm(form, field):
        if form.password.data != field.data:
            raise ValidationError('Passwords must match')


class Login(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired(message='Please enter a valid email')])
    password = PasswordField('password', [validators.length(min=6, max=200), validators.DataRequired()])


class VerifySecurityQuestionsForm(Form):
    security_answer1 = StringField('Security Answer 1：',
                                   validators=[validators.Length(min=1, max=150), validators.DataRequired()])
    security_answer2 = StringField('Security Answer 2：',
                                   validators=[validators.Length(min=1, max=150), validators.DataRequired()])
    security_answer3 = StringField('Security Answer 3：',
                                   validators=[validators.Length(min=1, max=150), validators.DataRequired()])


class CreateAdminForm(Form):
    first_name = StringField('First Name:', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name:', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email Address:',
                       [validators.DataRequired(), validators.Length(min=4, max=150), validators.Email()])
    authority = SelectMultipleField('Authority:',
                                    choices=[('Products', 'Products'), ('Event', 'Event'),
                                             ('Carbon Footprint', 'Carbon Footprint'),
                                             ('Store Locator', 'Store Locator'),
                                             ('Rewords', 'Rewords'), ('Forum', 'Forum'), ('Book', 'Book'),
                                             ('Tips', 'Tips'),
                                             ('Manage Users', 'Manage Users'), ('Manage Admin', 'Manage Admin')],
                                    option_widget=widgets.CheckboxInput(),
                                    widget=widgets.ListWidget(prefix_label=False)
                                    )
    description = TextAreaField('Description:', [validators.Length(min=1, max=500)])
    password = PasswordField('Password:', [validators.InputRequired(), validators.Length(min=6, max=100),
                                           validators.EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Repeat Password:', [validators.InputRequired('please re enter password')])
    agree_terms = BooleanField("", validators=[validators.DataRequired()])

    def validate_first_name(form, field):
        if not re.match("^[a-zA-Z]*$", field.data):
            raise ValidationError('First name must contain only letters')

    def validate_last_name(form, field):
        if not re.match("^[a-zA-Z]*$", field.data):
            raise ValidationError('Last name must contain only letters')

    def validate_email(form, field):
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", field.data):
            raise ValidationError('Enter a valid email address')

    def validate_description(form, field):
        if not (1 <= len(field.data) <= 500):
            raise ValidationError('Description must be between 1 to 500 characters')

    def validate_password(form, field):
        # Check if the password contains at least one letter
        if not any(char.isalpha() for char in field.data):
            raise ValidationError('Password must contain at least one letter')

        # Check if the password contains at least one number
        if not any(char.isdigit() for char in field.data):
            raise ValidationError('Password must contain at least one number')

        # Check if the password contains at least one special character
        special_characters = r"!@#$%^&*()-_+="
        if not any(char in special_characters for char in field.data):
            raise ValidationError('Password must contain at least one special character')

    def validate_confirm(form, field):
        if form.password.data != field.data:
            raise ValidationError('Passwords must match')

    def validate_agree_terms(form, field):
        if not field.data:
            raise ValidationError('You must agree to the terms')


class ForgotPasswordForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired(message='Please enter a valid email')])


class ResetPasswordForm(Form):
    password = PasswordField('Password', [validators.InputRequired(), validators.Length(min=6, max=100),
                                          validators.EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.InputRequired('please re enter password')])

    def validate_password(form, field):
        # Check if the password contains at least one letter
        if not any(char.isalpha() for char in field.data):
            raise ValidationError('Password must contain at least one letter')

        # Check if the password contains at least one number
        if not any(char.isdigit() for char in field.data):
            raise ValidationError('Password must contain at least one number')

        # Check if the password contains at least one special character
        special_characters = r"!@#$%^&*()-_+="
        if not any(char in special_characters for char in field.data):
            raise ValidationError('Password must contain at least one special character')

    def validate_confirm(form, field):
        if form.password.data != field.data:
            raise ValidationError('Passwords must match')


class UpdateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    email = EmailField('Email Address',
                       [validators.DataRequired(), validators.Length(min=4, max=150), validators.Email()])
    gender = RadioField('Gender', [validators.DataRequired()], choices=[('F', 'Female'), ('M', 'Male')], default=None)
    birthdate = DateField("Date Of Birth", [validators.DataRequired(message='Enter valid date'), ], format="%Y-%m-%d")
    postal_code = IntegerField('Postal Code', [validators.NumberRange(min=000000, max=999999),
                                               validators.DataRequired(message='Please enter valid postal code')])
    city = SelectField('City', [validators.DataRequired()], choices=[('Ang Mo Kio', 'Ang Mo Kio'),
                                                                     ('Bedok', 'Bedok'),
                                                                     ('Bishan', 'Bishan'),
                                                                     ('Boon Lay', 'Boon Lay'),
                                                                     ('Bukit Batok', 'Bukit Batok'),
                                                                     ('Bukit Merah', 'Bukit Merah'),
                                                                     ('Bukit Panjang', 'Bukit Panjang'),
                                                                     ('Bukit Timah', 'Bukit Timah'),
                                                                     ('Central Area', 'Central Area'),
                                                                     ('Choa Chu Kang', 'Choa Chu Kang'),
                                                                     ('Clementi', 'Clementi'),
                                                                     ('Geylang', 'Geylang'),
                                                                     ('Hougang', 'Hougang'),
                                                                     ('Jurong East', 'Jurong East'),
                                                                     ('Jurong West', 'Jurong West'),
                                                                     ('Kallang/Whampoa', 'Kallang/Whampoa'),
                                                                     ('Lim Chu Kang', 'Lim Chu Kang'),
                                                                     ('Mandai', 'Mandai'),
                                                                     ('Marine Parade', 'Marine Parade'),
                                                                     ('Novena', 'Novena'),
                                                                     ('Pasir Ris', 'Pasir Ris'),
                                                                     ('Punggol', 'Punggol'),
                                                                     ('Queenstown', 'Queenstown'),
                                                                     ('Rochor', 'Rochor'),
                                                                     ('Sembawang', 'Sembawang'),
                                                                     ('Sengkang', 'Sengkang'),
                                                                     ('Serangoon', 'Serangoon'),
                                                                     ('Tampines', 'Tampines'),
                                                                     ('Tanglin', 'Tanglin'),
                                                                     ('Toa Payoh', 'Toa Payoh'),
                                                                     ('Woodlands', 'Woodlands'),
                                                                     ('Yishun', 'Yishun')], default=None)
    address = StringField('Address', [validators.Length(min=4, max=50),
                                      validators.DataRequired(message='Please enter a valid address')])
    password = PasswordField('Password', [validators.InputRequired(), validators.Length(min=6, max=100),
                                          validators.EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Confirm Password', [validators.InputRequired('please re enter password')])

    def validate_first_name(form, field):
        if not re.match("^[a-zA-Z]*$", field.data):
            raise ValidationError('First name must contain only letters')

    def validate_last_name(form, field):
        if not re.match("^[a-zA-Z]*$", field.data):
            raise ValidationError('Last name must contain only letters')

    def validate_email(form, field):
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", field.data):
            raise ValidationError('Enter a valid email address')

    def validate_birthdate(form, field):
        current_year = datetime.now().year
        if field.data.year > current_year or field.data.year < current_year - 150:
            raise ValidationError('Enter a valid birthdate')

    def validate_postal_code(form, field):
        if not (0 <= field.data <= 999999):
            raise ValidationError('Please enter a valid postal code')

    def validate_address(form, field):
        if not (4 <= len(field.data) <= 50):
            raise ValidationError('Address must be between 4 to 50 characters')

    def validate_password(form, field):
        # Check if the password contains at least one letter
        if not any(char.isalpha() for char in field.data):
            raise ValidationError('Password must contain at least one letter')

        # Check if the password contains at least one number
        if not any(char.isdigit() for char in field.data):
            raise ValidationError('Password must contain at least one number')

        # Check if the password contains at least one special character
        special_characters = r"!@#$%^&*()-_+="
        if not any(char in special_characters for char in field.data):
            raise ValidationError('Password must contain at least one special character')

    def validate_confirm(form, field):
        if form.password.data != field.data:
            raise ValidationError('Passwords must match')


class UpdateAdminForm(Form):
    first_name = StringField('First Name:', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name:', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email Address:',
                       [validators.DataRequired(), validators.Length(min=4, max=150), validators.Email()])
    authority = SelectMultipleField('Authority:',
                                    choices=[('Products', 'Products'), ('Event', 'Event'),
                                             ('Carbon Footprint', 'Carbon Footprint'),
                                             ('Store Locator', 'Store Locator'),
                                             ('Rewords', 'Rewords'), ('Forum', 'Forum'), ('Book', 'Book'),
                                             ('Manage Users', 'Manage Users'), ('Manage Admin', 'Manage Admin')],
                                    option_widget=widgets.CheckboxInput(),
                                    widget=widgets.ListWidget(prefix_label=False)
                                    )
    description = TextAreaField('Description:', [validators.Length(min=1, max=500)])
    password = PasswordField('Password:', [validators.InputRequired(), validators.Length(min=6, max=100),
                                           validators.EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Repeat Password:', [validators.InputRequired('please re enter password')])

    def validate_first_name(form, field):
        if not re.match("^[a-zA-Z]*$", field.data):
            raise ValidationError('First name must contain only letters')

    def validate_last_name(form, field):
        if not re.match("^[a-zA-Z]*$", field.data):
            raise ValidationError('Last name must contain only letters')

    def validate_email(form, field):
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", field.data):
            raise ValidationError('Enter a valid email address')

    def validate_description(form, field):
        if not (1 <= len(field.data) <= 500):
            raise ValidationError('Description must be between 1 to 500 characters')

    def validate_password(form, field):
        # Check if the password contains at least one letter
        if not any(char.isalpha() for char in field.data):
            raise ValidationError('Password must contain at least one letter')

        # Check if the password contains at least one number
        if not any(char.isdigit() for char in field.data):
            raise ValidationError('Password must contain at least one number')

        # Check if the password contains at least one special character
        special_characters = r"!@#$%^&*()-_+="
        if not any(char in special_characters for char in field.data):
            raise ValidationError('Password must contain at least one special character')

    def validate_confirm(form, field):
        if form.password.data != field.data:
            raise ValidationError('Passwords must match')

    def validate_agree_terms(form, field):
        if not field.data:
            raise ValidationError('You must agree to the terms')


# Shu Jie end
# Nigga start
class CreateReviewForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150)])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150)])
    gender = SelectField('Gender',
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    star_rating = SelectField('Star_Rating',
                              choices=[('', 'Select'), ('1', '1 Star'), ('2', '2 Star'), ('3', '3 Star'),
                                       ('4', '4 Star'), ('5', '5 Star')], default='')
    remarks = TextAreaField('Remarks', [validators.Optional()])

    def validate_star_rating(form, field):
        try:
            rating = int(field.data)
            if not (0 <= rating <= 5):
                raise ValidationError('Star rating must be between 0 and 5')
        except ValueError:
            raise ValidationError('Invalid star rating')

    def validate_gender(form, field):
        valid_genders = ['F', 'M']
        if field.data not in valid_genders:
            raise validators.ValidationError('Invalid gender selection.')

    def validate_name(form, field):
        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError('Name must not contain special characters like @#$%')

    def validate_content(form, field):
        if not (1 <= len(field.data) <= 700):
            raise ValidationError(
                'Forum content must be between 1 to 700 characters and must not contain special characters like @#$% ')

        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError('Forum content must not contain special characters like @#$%')


class CreateForumForm(Form):
    gender = SelectField('Gender',
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    name = StringField('Name', [validators.Length(min=1, max=150)])
    content = TextAreaField('Content',
                            [validators.length(min=1, max=1500)])

    def validate_gender(form, field):
        valid_genders = ['F', 'M']
        if field.data not in valid_genders:
            raise validators.ValidationError('Select a gender')

    def validate_name(form, field):
        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError('Name must not contain special characters like @#$%')

    def validate_content(form, field):
        if not (1 <= len(field.data) <= 700):
            raise ValidationError(
                'Forum content must be between 1 to 700 characters and must not contain special characters like @#$% ')

        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError('Forum content must not contain special characters like @#$%')


# Nigga end


# Sherman Start
class CreateCarbonForm(Form):
    service = RadioField('Type of service used', choices=[('Dryer', 'Dryer'), ('Washer', 'Washer')])
    temp = RadioField('Temperature used',
                      choices=[('Hot', 'Hot (90°C)'), ('Warm', 'Warm (60°C)'), ('Cold', 'Cold (40°C)')])
    load = SelectField('Load Size', [validators.DataRequired()],
                       choices=[('', 'Select'), ('Large', 'Large'), ('Medium', 'Medium'), ('Small', 'Small')],
                       render_kw={"class": "custom-select"})
    time = StringField('Input how long was the service used for', render_kw={"placeholder": "Enter time in minutes"})

    def validate_service(form, field):
        if field.data not in ['Dryer', 'Washer']:
            raise ValidationError('Service selection is required. Please choose between Dryer and Washer.')

    def validate_temp(form, field):
        if field.data not in ['Hot', 'Warm', 'Cold']:
            raise ValidationError(
                'Temperature selection is required. Please choose one of the available options: Hot, Warm, or Cold.')

    def validate_load(form, field):
        if field.data == '':
            raise ValidationError('Load size is required. Please select a load size.')
        if field.data not in ['Large', 'Medium', 'Small']:
            raise ValidationError('Invalid load size. Please select a valid option: Large, Medium, or Small.')

    def validate_time(form, field):
        if not field.data.isdigit():
            raise ValidationError('Invalid time format. Time must be an integer representing the duration in minutes.')
        if int(field.data) <= 0:
            raise ValidationError('Invalid duration. The time must be a positive integer.')


class LocationForm(Form):
    country = StringField('Country', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])

    def validate_country(form, field):
        if not re.match("^[a-zA-Z -]*$", field.data):
            raise ValidationError('Country name must only contain letters, spaces, and hyphens.')

    def validate_postal_code(form, field):
        if not re.match("^\d{6}$", field.data):
            raise ValidationError('Postal code must be exactly 6 digits.')


class LaundromatForm(Form):
    name = StringField('Input the laundromat name', [DataRequired(message='Enter a name')])
    address = StringField('Input the postal code of the location',
                          [Length(min=1, max=200, message='Address must be between 1 and 200 characters')])
    opening_time = TimeField('Opening Time', validators=[validators.InputRequired()])
    closing_time = TimeField('Closing Time', [InputRequired()])
    star_rating = FloatField('Star Rating', [DataRequired(message='Enter a rating')])
    image = FileField('Put an image of the laundromat')

    def validate_name(form, field):
        if len(field.data) > 100:
            raise ValidationError('Name is too long. The maximum allowed length is 100 characters.')
        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError(
                'Invalid name format. The name must consist only of alphanumeric characters (letters and numbers) and spaces, without special characters like @, #, $, and %.')

    def validate_address(form, field):
        if not re.match("^[a-zA-Z0-9 ,.]*\d{6}$", field.data):
            raise ValidationError(
                'Invalid address format. The address must consist of alphanumeric characters, spaces, commas, and periods, and must end with exactly 6 digits.')

    def validate_opening_time(form, field):
        if field.data is None or not isinstance(field.data, time):
            raise ValidationError('Invalid opening time format. Please enter a valid time.')
        if not time(5, 0) <= field.data <= time(12, 0):
            raise ValidationError('Opening time must be between 5:00 AM and 12:00 PM.')

    def validate_closing_time(form, field):
        if form.opening_time.data and field.data and form.opening_time.data >= field.data:
            raise ValidationError('Closing time must be after opening time')

    def validate_star_rating(form, field):
        if not (0 <= field.data <= 5):
            raise ValidationError('Star rating error. The rating must be a number between 0 and 5, inclusive.')


class UpdateLaundromatForm(Form):
    name = StringField('Input the laundromat name', render_kw={"readonly": True})
    address = StringField('Input the postal code of the location',
                          render_kw={"placeholder": "End with the postal code"})
    opening_time = TimeField('Opening Time')
    closing_time = TimeField('Closing Time')
    star_rating = FloatField('Star Rating')
    image = FileField('Put an image of the laundromat')

    def validate_address(form, field):
        if not re.match("^[a-zA-Z0-9 ,.]*\d{6}$", field.data):
            raise ValidationError(
                'Invalid address format. The address must consist of alphanumeric characters, spaces, commas, and periods, and must end with exactly 6 digits.')

    def validate_opening_time(form, field):
        if field.data is None or not isinstance(field.data, time):
            raise ValidationError('Invalid opening time format. Please enter a valid time.')
        if not time(5, 0) <= field.data <= time(12, 0):
            raise ValidationError('Opening time must be between 5:00 AM and 12:00 PM.')

    def validate_closing_time(form, field):
        if form.opening_time.data and field.data and form.opening_time.data >= field.data:
            raise ValidationError('Closing time must be after opening time')

    def validate_star_rating(form, field):
        if not (0 <= field.data <= 5):
            raise ValidationError('Star rating error. The rating must be a number between 0 and 5, inclusive.')


# what ive added
class EventForm(Form):
    name = StringField('Input the event name')
    description = StringField('Input the description of the event')
    date = DateField('Choose a date', format='%Y-%m-%d')
    image = FileField('Put an image of the Event')

    def validate_name(self, field):
        if len(field.data) < 3 or len(field.data) > 100:
            raise ValidationError('Event name must be between 3 and 50 characters.')
        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError(
                'Invalid name format. The name must consist only of alphanumeric characters (letters and numbers) and spaces, without special characters like @, #, $, and %.')

    def validate_description(self, field):
        if len(field.data) > 200:
            raise ValidationError('Description must not exceed 200 characters.')

    def validate_date(self, field):
        if field.data < datetime.date.today():
            raise ValidationError('The date cannot be in the past.')

    def validate_image(self, field):
        if field.data:
            filename = field.data.filename
            allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
            if not ('.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions):
                raise ValidationError('Only image files are allowed.')


class UpdateEventForm(Form):
    name = StringField('Input the event name', render_kw={"readonly": True})
    description = StringField('Input the description of the event')
    date = DateField('Choose a date', format='%Y-%m-%d')
    image = FileField('Put an image of the Event')

    def validate_name(self, field):
        if len(field.data) < 3 or len(field.data) > 100:
            raise ValidationError('Event name must be between 3 and 50 characters.')
        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError(
                'Invalid name format. The name must consist only of alphanumeric characters (letters and numbers) and spaces, without special characters like @, #, $, and %.')

    def validate_description(self, field):
        if len(field.data) > 200:
            raise ValidationError('Description must not exceed 200 characters.')

    def validate_date(self, field):
        if field.data < datetime.date.today():
            raise ValidationError('The date cannot be in the past.')

    def validate_image(self, field):
        if field.data:
            filename = field.data.filename
            allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
            if not ('.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions):
                raise ValidationError('Only image files are allowed.')


class ServiceForm(Form):
    name = StringField('Input the service name')
    description = StringField('Input the description of the service')

    def validate_name(self, field):
        if len(field.data) < 3 or len(field.data) > 100:
            raise ValidationError('Service name must be between 3 and 50 characters.')
        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError(
                'Invalid name format. The name must consist only of alphanumeric characters (letters and numbers) and spaces, without special characters like @, #, $, and %.')

    def validate_description(self, field):
        if len(field.data) > 200:
            raise ValidationError('Description must not exceed 200 characters.')


class UpdateServiceForm(Form):
    name = StringField('Input the service name', render_kw={"readonly": True})
    description = StringField('Input the description of the service')

    def validate_name(self, field):
        if len(field.data) < 3 or len(field.data) > 100:
            raise ValidationError('Service name must be between 3 and 50 characters.')
        if not re.match("^[a-zA-Z0-9 ]*$", field.data):
            raise ValidationError(
                'Invalid name format. The name must consist only of alphanumeric characters (letters and numbers) and spaces, without special characters like @, #, $, and %.')

    def validate_description(self, field):
        if len(field.data) > 200:
            raise ValidationError('Description must not exceed 200 characters.')

# Sherman Form End
