from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, abort
from werkzeug.utils import secure_filename
from jinja2 import TemplateNotFound
from Forms import *
import shelve, products, secrets, os, User1, Admin, tips, Rewards
from Location import *
from Booking import *
from Machine import *
from Review import *
from Forum import *
from User import *
from Event import *
from Rewards import *
from Service import *
import requests
from flask_bcrypt import Bcrypt, check_password_hash

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
bcrypt = Bcrypt(app)
app.config['UPLOAD_FOLDER'] = 'static/img'


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


# Jun Quan Start
@app.route('/createtip', methods=['GET', 'POST'])
def create_tip():
    create_tip_form = CreateTipForm(request.form)
    if request.method == 'POST' and create_tip_form.validate():
        tips_dict = {}
        db = shelve.open('tip.db', 'c')
        try:
            tips_dict = db['Tips']
        except:
            print("Error in retrieving Tips from tip.db.")
        count = len(tips_dict) + 1
        tip_id = count
        tip = tips.Tips(tip_id, create_tip_form.title.data, create_tip_form.desc.data)
        tips_dict[tip.get_tip_id()] = tip
        db['Tips'] = tips_dict
        db.close()
        return redirect(url_for('retrieve_tips'))
    return render_template('createTip.html', form=create_tip_form)


@app.route('/retrievetips')
def retrieve_tips():
    tips_dict = {}
    db = shelve.open('tip.db', 'r')
    tips_dict = db['Tips']
    db.close()
    tips_list = []
    for key in tips_dict:
        tip = tips_dict.get(key)
        tips_list.append(tip)
    return render_template("retrieveTips.html", count=len(tips_list), tips_list=tips_list)


@app.route('/showtips')
def show_tips():
    tips_dict = {}
    db = shelve.open('tip.db', 'r')
    tips_dict = db['Tips']
    db.close()
    tips_list = []
    for key in tips_dict:
        tip = tips_dict.get(key)
        tips_list.append(tip)
    return render_template("showTips.html", count=len(tips_list), tips_list=tips_list)


@app.route('/updateTip/<int:id>/', methods=['GET', 'POST'])
def update_tip(id):
    update_tip_form = CreateTipForm(request.form)
    if request.method == 'POST' and update_tip_form.validate():
        tips_dict = {}
        db = shelve.open('tip.db', 'w')
        tips_dict = db['Tips']
        tip = tips_dict.get(id)
        tips_list = []
        tip.set_title(update_tip_form.title.data)
        tip.set_desc(update_tip_form.desc.data)
        db['Tips'] = tips_dict
        db.close()
        return redirect(url_for('retrieve_tips'))
    else:
        tips_dict = {}
        db = shelve.open('tip.db', 'r')
        tips_dict = db['Tips']
        db.close()
        tip = tips_dict.get(id)
        update_tip_form.title.data = tip.get_title()
        update_tip_form.desc.data = tip.get_desc()
        return render_template('updateTip.html', form=update_tip_form)


@app.route('/deleteTip/<int:id>', methods=['POST'])
def delete_tip(id):
    tips_dict = {}
    db = shelve.open('tip.db', 'w')
    tips_dict = db['Tips']
    tips_dict.pop(id)
    db['Tips'] = tips_dict
    db.close()
    return redirect(url_for('retrieve_tips'))


@app.route('/createproduct', methods=['GET', 'POST'])
def create_product():
    create_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and create_product_form.validate():
        products_dict = {}
        db = shelve.open('product.db', 'c')
        try:
            products_dict = db['Products']
        except:
            print("Error in retrieving Products from product.db.")
        image_2 = request.files['image2']

        if image_2.filename == '':
            return render_template('createProduct.html', form=create_product_form)

        print("-- ** Received file: **--", image_2.filename)
        print("-- ** content type: **--", image_2.content_type)

        filename = secure_filename(image_2.filename)

        # if not filename.lower().endswith('.jpg','.jpeg','.png'):
        #     return redirect(request.url)

        image_2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        count = len(products_dict) + 1
        product_id = count
        product = products.Products(product_id, create_product_form.name.data, create_product_form.type.data,
                                    create_product_form.rating.data, filename)
        products_dict[product.get_product_id()] = product
        db['Products'] = products_dict
        db.close()
        return redirect(url_for('retrieve_products'))
    return render_template('createProduct.html', form=create_product_form)


@app.route('/retrieveproducts')
def retrieve_products():
    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()
    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)
    return render_template("retrieveProducts.html", count=len(products_list), products_list=products_list)


@app.route('/showproducts')
def show_products():
    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()
    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)
    return render_template("showProducts.html", count=len(products_list), products_list=products_list)


@app.route('/updateProduct/<int:id>/', methods=['GET', 'POST'])
def update_product(id):
    update_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and update_product_form.validate():
        products_dict = {}
        db = shelve.open('product.db', 'w')
        products_dict = db['Products']
        image_2 = request.files['image2']
        if image_2.filename == '':
            return render_template('updateProduct.html', form=update_product_form)
        filename = secure_filename(image_2.filename)
        image_2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product = products_dict.get(id)
        products_list = []
        product.set_img(filename)
        product.set_name(update_product_form.name.data)
        product.set_type(update_product_form.type.data)
        product.set_rating(update_product_form.rating.data)
        db['Products'] = products_dict
        db.close()
        return redirect(url_for('retrieve_products'))
    else:
        products_dict = {}
        db = shelve.open('product.db', 'r')
        products_dict = db['Products']
        db.close()
        product = products_dict.get(id)
        update_product_form.name.data = product.get_name()
        update_product_form.type.data = product.get_type()
        update_product_form.rating.data = product.get_rating()
        return render_template('updateProduct.html', form=update_product_form)


@app.route('/deleteProduct/<int:id>', methods=['POST'])
def delete_product(id):
    products_dict = {}
    db = shelve.open('product.db', 'w')
    products_dict = db['Products']
    products_dict.pop(id)
    db['Products'] = products_dict
    db.close()
    return redirect(url_for('retrieve_products'))


# Jun Quan End


# Shu Jie start
@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        user_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            user_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        if create_user_form.email.data in [user.get_email() for user in user_dict.values()]:
            flash('Email is already in use. Please use a different email address!!', 'danger')
            db.close()
            return render_template('Sign_up.html', form=create_user_form)

        hashed_password = bcrypt.generate_password_hash(create_user_form.password.data)
        count = len(user_dict) + 1
        user_id = count
        user = User1.User1(
            user_id,
            create_user_form.first_name.data,
            create_user_form.last_name.data,
            create_user_form.email.data,
            create_user_form.gender.data,
            create_user_form.birthdate.data,
            create_user_form.city.data,
            create_user_form.postal_code.data,
            create_user_form.address.data,
            hashed_password,
            create_user_form.security_question1.data,
            create_user_form.security_answer1.data,
            create_user_form.security_question2.data,
            create_user_form.security_answer2.data,
            create_user_form.security_question3.data,
            create_user_form.security_answer3.data

        )
        user_dict[user.get_user_id()] = user
        db['Users'] = user_dict

        db.close()

        flash('Account created successfully. You can now log in as a user!', 'success')
        return redirect(url_for('login'))

    return render_template('Sign_up.html', form=create_user_form)


@app.route('/forgot_password', methods=['POST', 'GET'])
def forgot_password():
    customer = []
    login_page = ForgotPasswordForm(request.form)
    if request.method == 'POST' and login_page.validate():
        try:
            users_dict = {}
            with shelve.open('user.db', 'r') as db:
                users_dict = db.get('Users', {})
        except Exception as e:
            print('Error in retrieving Users from user.db:', e)
            flash('Error in retrieving user data. Please try again later.', 'danger')
            return redirect(url_for('login'))

        user_email_list = [user.get_email() for user in users_dict.values()]

        if login_page.email.data in user_email_list:
            for key, user_loggedin in users_dict.items():
                if login_page.email.data == user_loggedin.get_email():
                    session['true'] = True
                    session['logged_in'] = user_loggedin.get_first_name() + ' ' + user_loggedin.get_last_name()
                    session['user_id'] = key
                    session['email'] = user_loggedin.get_email()
                    session['Selected_question1'] = user_loggedin.get_security_question1()
                    session['Selected_question2'] = user_loggedin.get_security_question2()
                    session['Selected_question3'] = user_loggedin.get_security_question3()
                    customer.append(user_loggedin)
                    flash(
                        'Hi ' + user_loggedin.get_first_name() + ' ' + user_loggedin.get_last_name() + ', You have successfully logged in!',
                        'success')
                    return redirect(url_for('verify_security_questions'))
        else:
            flash('Incorrect login details, please try again!', 'danger')

    return render_template('forgot_password.html', form=login_page)


@app.route('/verify_security_questions', methods=['GET', 'POST'])
def verify_security_questions():
    login_page = VerifySecurityQuestionsForm(request.form)

    if request.method == 'POST' and login_page.validate():
        try:
            users_dict = {}
            with shelve.open('user.db', 'r') as db:
                users_dict = db.get('Users', {})
        except Exception as e:
            print('Error in retrieving Users from user.db:', e)
            flash('Error in retrieving user data. Please try again later.', 'danger')
            return redirect(url_for('verify_security_questions'))

        user_id = session.get('user_id')
        if user_id in users_dict:
            user = users_dict[user_id]

            answer1 = login_page.security_answer1.data
            answer2 = login_page.security_answer2.data
            answer3 = login_page.security_answer3.data

            if (answer1 == user.get_security_answer1() and
                    answer2 == user.get_security_answer2() and
                    answer3 == user.get_security_answer3()):
                flash('Security questions verified. You can now reset your password.', 'success')
                return redirect(url_for('reset_password', id=user_id))
            else:
                flash('Incorrect security answers. Please try again.', 'danger')
        else:
            flash('User not found. Please try again.', 'danger')

    return render_template('verify_security_questions.html', form=login_page)


@app.route('/reset_password/<int:id>/', methods=['GET', 'POST'])
def reset_password(id):
    reset_new_password = ResetPasswordForm(request.form)
    if request.method == 'POST' and reset_new_password.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        hashed_pw = bcrypt.generate_password_hash(reset_new_password.password.data).decode('utf-8')

        user = users_dict.get(id)
        user.set_password(hashed_pw)  # 仅更新密码

        db['Users'] = users_dict
        db.close()

        flash(f'Password for {user.get_first_name()} {user.get_last_name()} updated successfully!', 'success')

        return redirect(url_for('login'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)

    return render_template('reset_password.html', form=reset_new_password)


@app.route('/login', methods=['POST', 'GET'])
def login():
    customer = []
    login_page = Login(request.form)
    if request.method == 'POST' and login_page.validate():
        try:
            users_dict = {}
            with shelve.open('user.db', 'r') as db:
                users_dict = db.get('Users', {})
        except Exception as e:
            print('Error in retrieving Users from user.db:', e)
            flash('Error in retrieving user data. Please try again later.', 'danger')
            return redirect(url_for('login'))

        user_email_list = [user.get_email() for user in users_dict.values()]

        if login_page.email.data == 'admin@123.com' and login_page.password.data == 'admin123':
            # Admin login
            session['true'] = True
            session['logged_in'] = 'Admin'
            session['user_id'] = 'admin'
            session['email'] = 'admin@123.com'
            flash('Hi Admin, You have successfully logged in!', 'success')
            return redirect(url_for('admin_home'))

        elif login_page.email.data in user_email_list:
            for key, user_loggedin in users_dict.items():
                if login_page.email.data == user_loggedin.get_email():
                    # check password hash
                    if check_password_hash(user_loggedin.get_password(), login_page.password.data):
                        session['true'] = True
                        session['logged_in'] = user_loggedin.get_first_name() + ' ' + user_loggedin.get_last_name()
                        session['user_id'] = key
                        session['email'] = user_loggedin.get_email()
                        customer.append(user_loggedin)
                        flash(
                            'Hi ' + user_loggedin.get_first_name() + ' ' + user_loggedin.get_last_name() + ', You have successfully logged in!',
                            'success')
                        return redirect(url_for('home'))
                    else:
                        flash('Incorrect password, please try again!', 'danger')
                        # return redirect(url_for('login'))
        else:
            flash('Incorrect login details, please try again!', 'danger')

    return render_template('login.html', form=login_page)


@app.route('/admin')
def admin():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('admin.html', count=len(users_list), users_list=users_list)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = UpdateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        hashed_pw = bcrypt.generate_password_hash(update_user_form.password.data).decode(
            'utf-8')  # Decode the hashed password

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_birthdate(update_user_form.birthdate.data)
        user.set_city(update_user_form.city.data)
        user.set_postal_code(update_user_form.postal_code.data)
        user.set_address(update_user_form.address.data)
        user.set_email(update_user_form.email.data)
        user.set_password(hashed_pw)

        db['Users'] = users_dict
        db.close()

        flash(f'User {user.get_first_name()} {user.get_last_name()} updated successfully!', 'success')

        return redirect(url_for('admin'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.birthdate.data = user.get_birthdate()
        update_user_form.city.data = user.get_city()
        update_user_form.postal_code.data = user.get_postal_code()
        update_user_form.address.data = user.get_address()
        update_user_form.email.data = user.get_email()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/update_profile_page', methods=['GET', 'POST'])
def update_profile_page():
    if 'user_id' not in session:
        flash('You need to be logged in to access this page!', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    update_user_form = UpdateUserForm(request.form)

    if request.method == 'POST' and update_user_form.validate():
        hashed_pw = bcrypt.generate_password_hash(update_user_form.password.data).decode(
            'utf-8')  # Decode the hashed password

        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(user_id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_birthdate(update_user_form.birthdate.data)
        user.set_city(update_user_form.city.data)
        user.set_postal_code(update_user_form.postal_code.data)
        user.set_address(update_user_form.address.data)
        user.set_email(update_user_form.email.data)
        user.set_password(hashed_pw)

        db['Users'] = users_dict
        db.close()

        flash('Info has been updated successfully!', "info")
        return redirect(url_for('update_profile_page'))

    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(user_id)

        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.birthdate.data = user.get_birthdate()
        update_user_form.city.data = user.get_city()
        update_user_form.postal_code.data = user.get_postal_code()
        update_user_form.address.data = user.get_address()
        update_user_form.email.data = user.get_email()

        return render_template('update_profile_page.html', form=update_user_form)


@app.route('/logout_page')
def logout_page():
    session.clear()
    return redirect(url_for('home'))


@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('admin'))


@app.route('/display_username')
def display_username():
    if 'user_id' in session:
        user_id = session['user_id']
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(user_id)
        if user:
            return render_template('_navbar.html', user=user)

    return redirect(url_for('login'))


@app.route('/delete_admin/<int:id>', methods=['POST'])
def delete_admin(id):
    admins_dict = {}
    db = shelve.open('admin.db', 'w')
    admin_dict = db['Admins']

    admin_dict.pop(id)

    db['Admins'] = admin_dict
    db.close()

    return redirect(url_for('admin_account'))


@app.route('/display_admin_name')
def display_admin_name():
    if 'admin_id' in session:
        user_id = session['admin_id']
        admin_dict = {}
        db = shelve.open('admin.db', 'r')
        admin_dict = db['Admins']
        db.close()

        user = admin_dict.get(user_id)
        if user:
            return render_template('_navbara.html', admin=admin)

    return redirect(url_for('login_admin'))


@app.route('/create_admin', methods=['GET', 'POST'])
def create_admin():
    create_admin_form = CreateAdminForm(request.form)
    if request.method == 'POST' and create_admin_form.validate():
        admin_dict = {}
        db = shelve.open('admin.db', 'c')

        try:
            admin_dict = db['Admins']
        except:
            print("Error in retrieving Users from user.db.")

        if create_admin_form.email.data in [admin.get_email() for admin in admin_dict.values()]:
            flash('Email is already in use. Please use a different email address!!', 'danger')
            db.close()
            return render_template('Sign_up_admin.html', form=create_admin_form)

        hashed_password = bcrypt.generate_password_hash(create_admin_form.password.data)
        count = len(admin_dict) + 1
        admin_id = count
        admin = Admin.Admin(
            admin_id,
            create_admin_form.first_name.data,
            create_admin_form.last_name.data,
            create_admin_form.authority.data,
            create_admin_form.email.data,
            hashed_password,
            create_admin_form.description.data

        )
        admin_dict[admin.get_admin_id()] = admin
        db['Admins'] = admin_dict

        db.close()

        flash('Account created successfully. You can now log in as admin!', 'success')
        return redirect(url_for('login_admin'))

    return render_template('Sign_up_admin.html', form=create_admin_form)


@app.route('/login_admin', methods=['POST', 'GET'])
def login_admin():
    admin = []
    login_admin = Login(request.form)
    if request.method == 'POST' and login_admin.validate():

        try:
            admin_dict = {}
            db = shelve.open('admin.db', 'r')
            admin_dict = db['Admins']
            db.close()
        except:
            print('Error in retrieving Admin from admin.db.')

        admin_email_list = [admin.get_email() for admin in admin_dict.values()]

        if login_admin.email.data == 'admin@123.com' and login_admin.password.data == 'admin123':
            # Admin login
            session['true'] = True
            session['logged_in'] = 'Admin'
            session['admin_id'] = 'admin'
            session['email'] = 'admin@123.com'
            flash('Hi Admin, You have successfully logged in!', 'success')
            return redirect(url_for('admin_home'))

        elif login_admin.email.data in admin_email_list:
            for key, admin_loggedin in admin_dict.items():
                if login_admin.email.data == admin_loggedin.get_email():
                    # check hash
                    if check_password_hash(admin_loggedin.get_password(), login_admin.password.data):
                        session['true'] = True
                        session['logged_in'] = admin_loggedin.get_first_name() + ' ' + admin_loggedin.get_last_name()
                        session['admin_id'] = key
                        session['email'] = admin_loggedin.get_email()
                        session['selected_authorities'] = admin_loggedin.get_authority()
                        admin.append(admin_loggedin)
                        flash(
                            'Hi ' + admin_loggedin.get_first_name() + ' ' + admin_loggedin.get_last_name() + ', You have successfully logged in!',
                            'success')
                        return redirect(url_for('admin_home'))
                    else:
                        flash('Incorrect login details, please try again!', 'danger')
        else:
            flash('Incorrect login details, please try again!', 'danger')

    return render_template('login_admin.html', form=login_admin)


@app.route('/admin_account')
def admin_account():
    admin_dict = {}
    db = shelve.open('admin.db', 'r')
    admin_dict = db['Admins']
    db.close()

    admin_list = []
    for key in admin_dict:
        admin = admin_dict.get(key)
        admin_list.append(admin)

    return render_template('admin_account.html', count=len(admin_list), admin_list=admin_list)


@app.route('/updateAdminAccount/<int:id>/', methods=['GET', 'POST'])
def update_admin(id):
    update_Admin_form = UpdateAdminForm(request.form)

    if request.method == 'POST' and update_Admin_form.validate():
        admin_dict = {}
        db = shelve.open('admin.db', 'w')
        admin_dict = db['Admins']
        hashed_pw = bcrypt.generate_password_hash(update_Admin_form.password.data)

        admin = admin_dict.get(id)
        admin.set_first_name(update_Admin_form.first_name.data)
        admin.set_last_name(update_Admin_form.last_name.data)
        admin.set_authority(update_Admin_form.authority.data)
        admin.set_email(update_Admin_form.email.data)
        admin.set_description(update_Admin_form.description.data)
        admin.set_password(hashed_pw)

        db['Admins'] = admin_dict
        db.close()

        flash(f'Admin {admin.get_first_name()} {admin.get_last_name()} updated successfully!', 'success')

        return redirect(url_for('admin_account'))
    else:
        admin_dict = {}
        db = shelve.open('admin.db', 'r')
        admin_dict = db['Admins']
        db.close()

        admin = admin_dict.get(id)
        update_Admin_form.first_name.data = admin.get_first_name()
        update_Admin_form.last_name.data = admin.get_last_name()
        update_Admin_form.authority.data = admin.get_authority()
        update_Admin_form.email.data = admin.get_email()
        update_Admin_form.description.data = admin.get_description()
        return render_template('updateAdminAccount.html', form=update_Admin_form)
    # Shu Jie end


# Nigga start
@app.route('/C_forum', methods=['GET', 'POST'])
def create_forum():
    create_forum_form = CreateForumForm(request.form)
    if request.method == 'POST' and create_forum_form.validate():
        forum_dict = {}
        db = shelve.open('forum.db', 'c')
        try:
            forum_dict = db['Forums']
        except:
            print("Error in retrieving forums from forum.db.")

        forum_id = len(forum_dict) + 1
        if forum_id != 1:
            forum_id = list(forum_dict.keys())[-1] + 1

        posted_On = datetime.now().strftime("%d-%b-%Y")
        forum = Forum(forum_id, create_forum_form.name.data, create_forum_form.gender.data,
                      create_forum_form.content.data, posted_On)

        forum_dict[forum.get_forum_id()] = forum
        db['Forums'] = forum_dict

        forum_dict = db['Forums']
        forum = forum_dict[forum.get_forum_id()]
        print(forum.get_name(), ' , ', forum.get_gender(), ' , ', 'and', forum.get_content(),
              "was stored in forum.db successfully with forum_id ==",
              forum.get_forum_id)

        db.close()

        # ----------Start adding reward points----------#
        # if session.get("user_id") is not None:
        myUserID = session.get("user_id")
        rewards = Rewards.PointDetails(myUserID)
        rewards.set_points(5)
        rewards.add_rewards()
        # ----------End adding reward points----------#

        return redirect('/R_forum')

    return render_template('create_Forum.html', form=create_forum_form)


@app.route('/R_forum')
def retrieve_forum():
    forum_dict = {}
    db = shelve.open('forum.db', 'c')
    try:
        forum_dict = db['Forums']
    except:
        print("Error in retrieving forums from forum.db.")

    db.close()

    forums_list = []
    for key in forum_dict:
        forum = forum_dict.get(key)
        forums_list.append(forum)
    return render_template('retrieve_Forum.html', count=len(forums_list), forums_list=forums_list)


@app.route('/U_forum/<int:id>/', methods=['GET', 'POST'])
def update_forum(id):
    update_forum_form = CreateForumForm(request.form)
    if request.method == 'POST' and update_forum_form.validate():
        db = shelve.open('forum.db', 'w')
        forum_dict = db['Forums']
        forum = forum_dict.get(id)
        forum.set_name(update_forum_form.name.data)
        forum.set_gender(update_forum_form.gender.data)
        forum.set_content(update_forum_form.content.data)

        db['Forums'] = forum_dict
        db.close()

        return redirect('/R_forum')

    else:
        db = shelve.open('forum.db', 'r')
        forums_dict = db['Forums']
        db.close()
        forum = forums_dict.get(id)
        update_forum_form.name.data = forum.get_name()
        update_forum_form.gender.data = forum.get_gender()
        update_forum_form.content.data = forum.get_content()

        return render_template('update_Forum.html', form=update_forum_form)


@app.route('/D_forum/<int:id>/', methods=['GET', 'POST'])
def delete_forum(id):
    db = shelve.open('forum.db', 'c')
    try:
        forum_dict = db['Forums']
        print(len(forum_dict))
        forum_dict.pop(id)
        db['Forums'] = forum_dict
    except:
        print("Error while delete forums from forum.db.")

    db.close()

    return redirect('/R_forum')


@app.route('/C_review', methods=['GET', 'POST'])
def create_review():
    create_review_form = CreateReviewForm(request.form)
    if request.method == 'POST' and create_review_form.validate():
        review_dict = {}
        db = shelve.open('review.db', 'c')
        try:
            review_dict = db['Reviews']
        except:
            print("Error in retrieving reviews from review.db.")

        review_id = len(review_dict) + 1
        if review_id != 1:
            review_id = list(review_dict.keys())[-1] + 1

        review = Review(review_id, create_review_form.first_name.data, create_review_form.last_name.data,
                        create_review_form.gender.data, create_review_form.star_rating.data,
                        create_review_form.remarks.data)

        review_dict[review.get_review_id()] = review
        db['Reviews'] = review_dict

        review_dict = db['Reviews']
        review = review_dict[review.get_review_id()]
        print(review.get_first_name(), review.get_last_name(), "was stored in review.db successfully with review_id ==",
              review.get_review_id)

        db.close()

        # ----------Start adding reward points----------#
        # if session.get("user_id") is not None:
        myUserID = session.get("user_id")
        rewards = Rewards.PointDetails(myUserID)
        rewards.set_points(2)
        rewards.add_rewards()
        # ----------End adding reward points----------#

        return redirect('/R_review')

    return render_template('create_Review.html', form=create_review_form)


@app.route('/R_review')
def retrieve_review():
    review_dict = {}
    db = shelve.open('review.db', 'r')
    try:
        review_dict = db['Reviews']
    except:
        print("Error in retrieving reviews from review.db.")

    db.close()

    reviews_list = []
    for key in review_dict:
        review = review_dict.get(key)
        reviews_list.append(review)

    return render_template('retrieve_Review.html', count=len(reviews_list), reviews_list=reviews_list)


@app.route('/U_review/<int:id>/', methods=['GET', 'POST'])
def update_review(id):
    update_review_form = CreateReviewForm(request.form)
    if request.method == 'POST' and update_review_form.validate():
        db = shelve.open('review.db', 'w')
        review_dict = db['Reviews']
        review = review_dict.get(id)
        review.set_first_name(update_review_form.first_name.data)
        review.set_last_name(update_review_form.last_name.data)
        review.set_gender(update_review_form.gender.data)
        review.set_star_rating(update_review_form.star_rating.data)
        review.set_remarks(update_review_form.remarks.data)

        db['Reviews'] = review_dict
        db.close()

        return redirect('/R_review')

    else:
        db = shelve.open('review.db', 'r')
        reviews_dict = db['Reviews']
        db.close()
        review = reviews_dict.get(id)
        update_review_form.first_name.data = review.get_first_name()
        update_review_form.last_name.data = review.get_last_name()
        update_review_form.gender.data = review.get_gender()
        update_review_form.star_rating.data = review.get_star_rating()
        update_review_form.remarks.data = review.get_remarks()

        return render_template('updateReview.html', form=update_review_form)


@app.route('/D_review/<int:id>/', methods=['GET', 'POST'])
def delete_review(id):
    db = shelve.open('review.db', 'w')
    try:
        review_dict = db['Reviews']
        review_dict.pop(id)
        db['Reviews'] = review_dict
    except:
        print("Error while delete reviews from review.db.")

    db.close()

    return redirect('/R_review')


@app.route('/R_Reward')
def retrieve_reward():
    reward_dict = {}
    db = shelve.open('reward.db', 'r')
    try:
        reward_dict = db['Reward']
    except:
        print("Error while retrieve Reward from reward.db.")

    db.close()

    rewards_list = []
    for key in reward_dict:
        reward = key + "-" + reward_dict.get(key)
        rewards_list.append(reward)

    return render_template('retrieve_Review.html', count=len(rewards_list), reviews_list=rewards_list)


@app.route('/R_Howtogetpoints')
def Howtogetpoints():
    # ------Start Retrieve Reward Points--------#
    reward_point = None
    # if session.get("user_id") is not None:
    myUserID = session.get("user_id")
    rewards = Rewards.PointDetails(myUserID)
    reward_point = rewards.get_reward_points()

    # ------End Retrieve Reward Points--------#

    return render_template('howtogetpoints.html', reward_point=reward_point)


# Nigga end

# Sherman Start

# For Carbon Footprint Calculator
@app.route('/createCF', methods=['GET', 'POST'])
def create_CF():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))

    # The user_id from the session will be used to track CF entries for that user
    user_id = session['user_id']
    create_CF_form = CreateCarbonForm(request.form)
    if request.method == 'POST' and create_CF_form.validate():
        cf_dict = {}
        db = shelve.open('cf.db', 'c')

        try:
            # Attempt to retrieve existing CF entries for this user
            cf_dict = db['CF']
        except:
            print("Error in retrieving CF from cf.db.")

        service = create_CF_form.service.data
        temp = create_CF_form.temp.data
        load = create_CF_form.load.data
        try:
            time = float(create_CF_form.time.data)
        except ValueError:
            flash("Invalid time input. Please enter a valid number.", 'danger')
            return redirect(url_for('create_CF'))

        # Factors for calculating carbon footprint
        service_factor = {'Dryer': 1, 'Washer': 0.5}
        temp_factor = {'Hot': 0.98, 'Warm': 0.66, 'Cold': 0.33}
        load_factor = {'Large': 2, 'Medium': 1.5, 'Small': 1}

        # Calculate the carbon footprint
        carbon_footprint = float((service_factor[service] + temp_factor[temp] + load_factor[load]) * time / 60)

        # Create a new Carbon object with the user_id from the session
        carbon_entry = Carbon(user_id, service, temp, load, time, carbon_footprint)

        # If the user already has entries, append to them. Otherwise, create a new list.
        if user_id in cf_dict:
            cf_dict[user_id].append(carbon_entry)
        else:
            cf_dict[user_id] = [carbon_entry]

        # Save the updated CF entries back to the database
        db['CF'] = cf_dict
        db.close()

        flash('Carbon footprint entry created successfully!', 'success')
        return redirect(url_for('retrieve_CF'))

    return render_template('createCF.html', form=create_CF_form)


@app.route('/retrieveCF')
def retrieve_CF():
    if 'user_id' not in session:
        flash('Please log in to view your carbon footprint entries.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    cf_dict = {}
    db = shelve.open('cf.db', 'r')

    try:
        # Retrieve only the CF entries for the logged-in user
        cf_dict = db['CF']
        user_cf_entries = cf_dict.get(user_id, [])
    except KeyError:
        user_cf_entries = []
    finally:
        db.close()
    print(user_cf_entries)
    print("CF Entries:", user_cf_entries)
    return render_template('retrieveCF.html', cf_list=user_cf_entries)


@app.route('/updateCF/<int:index>/', methods=['GET', 'POST'])
def update_CF(index):
    if 'user_id' not in session:
        flash('Please log in to update your carbon footprint entries.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    update_CF_form = CreateCarbonForm(request.form)
    if request.method == 'POST' and update_CF_form.validate():
        db = shelve.open('cf.db', 'w')
        cf_dict = db['CF']

        try:
            user_cf_entries = cf_dict[user_id]
            carbon_entry = user_cf_entries[index]  # Get the specific CF entry by index

            # Update the carbon entry's attributes
            carbon_entry.set_service(update_CF_form.service.data)
            carbon_entry.set_temp(update_CF_form.temp.data)
            carbon_entry.set_load(update_CF_form.load.data)
            carbon_entry.set_time(float(update_CF_form.time.data))

            # Update the CF entry in the list and database
            user_cf_entries[index] = carbon_entry
            cf_dict[user_id] = user_cf_entries
            db['CF'] = cf_dict
            flash('Carbon footprint entry updated successfully!', 'success')
        except IndexError:
            flash('Carbon footprint entry not found.', 'danger')
        finally:
            db.close()

        return redirect(url_for('retrieve_CF'))
    else:
        db = shelve.open('cf.db', 'r')
        cf_dict = db['CF']
        db.close()

        try:
            user_cf_entries = cf_dict[user_id]
            carbon_entry = user_cf_entries[index]  # Get the specific CF entry by index

            # Populate the form with the current CF entry data
            update_CF_form.service.data = carbon_entry.get_service()
            update_CF_form.temp.data = carbon_entry.get_temp()
            update_CF_form.load.data = carbon_entry.get_load()
            update_CF_form.time.data = carbon_entry.get_time()
        except IndexError:
            flash('Carbon footprint entry not found.', 'danger')
            return redirect(url_for('retrieve_CF'))

        # Pass the index to the template
        return render_template('updateCF.html', form=update_CF_form, index=index)


@app.route('/deleteCF/<int:index>/', methods=['POST'])
def delete_CF(index):
    if 'user_id' not in session:
        flash('Please log in to delete your carbon footprint entries.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']
    db = shelve.open('cf.db', 'w')
    cf_dict = db['CF']

    try:
        user_cf_entries = cf_dict[user_id]
        # Remove the CF entry by index
        user_cf_entries.pop(index)
        # Save the updated list back to the database
        cf_dict[user_id] = user_cf_entries
        db['CF'] = cf_dict
        flash('Carbon footprint entry deleted successfully!', 'success')
    except IndexError:
        flash('Carbon footprint entry not found.', 'danger')
    finally:
        db.close()

    return redirect(url_for('retrieve_CF'))


# For Location tracker
@app.route('/createLoc', methods=['GET', 'POST'])
def createLoc():
    form1 = LocationForm(request.form)
    if request.method == "POST" and form1.validate():
        loc_dict = {}
        db = shelve.open('loc.db', 'c')

        try:
            loc_dict = db['Location']
        except:
            print("Error in retrieving Location from loc.db.")

        country = form1.country.data
        postal_code = form1.postal_code.data

        count = len(loc_dict) + 1
        location_id = count
        Location1 = Location(location_id, country, postal_code)
        loc_dict[Location1.get_location_id()] = Location1
        db['Location'] = loc_dict
        db.close()

        return redirect(url_for('retrieve_Loc'))
    return render_template('createLoc.html', form=form1)


@app.route('/retrieve_Loc', methods=['GET'])
def retrieve_Loc():
    laund_dict = {}
    db = shelve.open('laund.db', 'r')
    laund_dict = db['Laund']
    db.close()

    laundromats_list = []
    for key in laund_dict:
        laund = laund_dict.get(key)
        laundromats_list.append(laund)

    return render_template('retrieveLoc.html', count=len(laundromats_list), laundromats_list=laundromats_list)


@app.route('/AcreateLoc', methods=['GET', 'POST'])
def Acreate_Loc():
    form = LaundromatForm(request.form)
    if request.method == 'POST' and form.validate():
        laund_dict = {}
        db = shelve.open('laund.db', 'c')

        try:
            laund_dict = db['Laund']
        except:
            print("Error in retrieving Users from laund.db.")
            print('no')

        print('---Request file is ----', request.files)
        image_1 = request.files['image']

        if image_1.filename == '':
            return render_template('AcreateLoc.html', form=form)

        print("-- ** Received file: **--", image_1.filename)
        print("-- ** content type: **--", image_1.content_type)

        filename = secure_filename(image_1.filename)

        # if not filename.lower().endswith('.jpg','.jpeg','.png'):
        #     return redirect(request.url)

        image_1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        name = form.name.data
        address = form.address.data
        opening_time = form.opening_time.data
        closing_time = form.closing_time.data
        star_rating = form.star_rating.data

        new_laundromat = Laundromat(name, address, opening_time, closing_time, star_rating, filename)

        laund_dict[new_laundromat.get_name()] = new_laundromat
        db['Laund'] = laund_dict
        db.close()
        print('Stored')

        # flash('New laundromat added successfully!', 'success')
        return redirect(url_for('Aretrieve_Loc'))
    return render_template('AcreateLoc.html', form=form)


@app.route('/AretrieveLoc')
def Aretrieve_Loc():
    laund_dict = {}
    db = shelve.open('laund.db', 'r')
    laund_dict = db['Laund']
    db.close()

    laundromats_list = []
    for key in laund_dict:
        laund = laund_dict.get(key)
        laundromats_list.append(laund)

    return render_template('AretrieveLoc.html', count=len(laundromats_list), laundromats_list=laundromats_list)


@app.route('/AupdateLoc/<laundromat_name>', methods=['GET', 'POST'])
def Aupdate_Loc(laundromat_name):
    update_form = UpdateLaundromatForm(request.form)
    if request.method == 'POST' and update_form.validate():
        laund_dict = {}
        db = shelve.open('laund.db', 'w')
        laund_dict = db['Laund']

        image_1 = request.files['image']
        filename = secure_filename(image_1.filename)
        image_1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        laund = laund_dict.get(laundromat_name)
        laund.set_name(update_form.name.data)
        laund.set_image(filename)
        laund.set_address(update_form.address.data)
        laund.set_opening_time(update_form.opening_time.data)
        laund.set_closing_time(update_form.closing_time.data)
        laund.set_star_rating(update_form.star_rating.data)

        db['Laund'] = laund_dict
        db.close()

        return redirect(url_for('Aretrieve_Loc'))
    else:
        laund_dict = {}
        db = shelve.open('laund.db', 'r')
        laund_dict = db['Laund']
        db.close()

        laund = laund_dict.get(laundromat_name)
        update_form.name.data = laund.get_name()
        update_form.address.data = laund.get_address()
        update_form.opening_time.data = laund.get_opening_time()
        update_form.closing_time.data = laund.get_closing_time()
        update_form.star_rating.data = laund.get_star_rating()

        return render_template('AupdateLoc.html', form=update_form)


@app.route('/AdeleteLoc/<laundromat_name>', methods=['POST'])
def Adelete_Loc(laundromat_name):
    laund_dict = {}
    db = shelve.open('laund.db', 'w')
    laund_dict = db['Laund']
    laund_dict.pop(laundromat_name)

    db['Laund'] = laund_dict
    db.close()

    return redirect(url_for('Aretrieve_Loc'))


# For Event
@app.route('/Pevent', methods=['GET', 'POST'])
def Event_part():
    if 'user_id' not in session:
        flash('Please log in to see participate in the event', 'danger')
        return redirect(url_for('login'))
    db = shelve.open('Event.db', 'r')
    try:
        Event_dict = db['Event']
    except Exception as e:
        print("Error in retrieving Events from Event.db:", e)
        Event_dict = {}
    db.close()

    event_names = [event.get_name() for event in Event_dict.values()]

    success_message = ""

    if request.method == 'POST':
        selected_event_name = request.form.get('event_name')

        # Check if the user is logged in
        if 'user_id' in session:
            user_id = session['user_id']  # Retrieve the user ID from the session

            # Open another database (or another shelf) for saving the selected event
            registration_db = shelve.open('EventRegistrations.db', 'c')

            try:
                # If 'Registrations' shelf exists, retrieve it, else initialize an empty dict
                if 'Registrations' in registration_db:
                    registrations = registration_db['Registrations']
                else:
                    registrations = {}

                # Update the registrations dictionary with the new registration
                if selected_event_name not in registrations:
                    registrations[selected_event_name] = []
                registrations[selected_event_name].append(user_id)

                # Save the updated dictionary back to the shelf
                registration_db['Registrations'] = registrations

                success_message = f"Successful registration for Event: {selected_event_name}"
            except Exception as e:
                print(f"Error in saving registration: {e}")
            finally:
                registration_db.close()
        else:
            # Handle the case where the user is not logged in
            success_message = "Please log in to register for an event."

    return render_template('Pevent.html', event_names=event_names, success_message=success_message)


@app.route('/view_registrations')
def view_registrations():
    # Check if the user is logged in
    if 'user_id' not in session:
        # Redirect to login page or display a message if the user is not logged in
        flash('Please log in to view your registrations.', 'warning')
        return redirect(url_for('login'))

    user_id = session['user_id']  # Retrieve the user ID from the session

    # Open the EventRegistrations.db database
    registration_db = shelve.open('EventRegistrations.db', 'r')
    try:
        # Retrieve all registrations
        all_registrations = registration_db.get('Registrations', {})

        # Filter registrations for the current user
        user_registrations = {event_name: user_ids for event_name, user_ids in all_registrations.items() if
                              user_id in user_ids}
    except Exception as e:
        print(f"Error in retrieving registrations: {e}")
        user_registrations = {}
    finally:
        registration_db.close()

    # Render a template, passing the filtered registrations data to it
    return render_template('view_registrations.html', registrations=user_registrations)


@app.route('/AcreateEvent', methods=['GET', 'POST'])
def Acreate_Event():
    form = EventForm(request.form)
    if request.method == 'POST' and form.validate():
        Event_dict = {}
        db = shelve.open('Event.db', 'c')

        try:
            Event_dict = db['Event']
        except:
            print("Error in retrieving Users from Event.db.")
            print('no')

        print('---Request file is ----', request.files)
        image_e = request.files['image']

        if image_e.filename == '':
            return render_template('AcreateEvent.html', form=form)

        print("-- ** Received file: **--", image_e.filename)
        print("-- ** content type: **--", image_e.content_type)

        filename = secure_filename(image_e.filename)

        # if not filename.lower().endswith('.jpg','.jpeg','.png'):
        #     return redirect(request.url)

        image_e.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        name = form.name.data
        description = form.description.data
        date = form.date.data

        new_event = Event(name, description, date, filename)

        Event_dict[new_event.get_name()] = new_event
        db['Event'] = Event_dict
        db.close()
        print('Stored')

        # flash('New laundromat added successfully!', 'success')
        return redirect(url_for('Aretrieve_Event'))
    return render_template('AcreateEvent.html', form=form)


@app.route('/AretrieveEvent')
def Aretrieve_Event():
    start = request.args.get('start', 0, type=int)
    limit = 5

    db = shelve.open('Event.db', 'r')
    Event_dict = db['Event']
    db.close()

    total_count = len(Event_dict)

    # Sorting keys and getting a slice of events based on current start and limit
    Event_keys_sorted = sorted(Event_dict.keys())
    Event_list = [Event_dict[key] for key in Event_keys_sorted[start:start + limit]]

    # Determine whether to show the 'Load More' button
    show_load_more = start + limit < total_count

    return render_template('AretrieveEvent.html', count=total_count, Event_list=Event_list,
                           show_load_more=show_load_more)


@app.route('/AupdateEvent/<Event_name>', methods=['GET', 'POST'])
def Aupdate_Event(Event_name):
    update_form = UpdateEventForm(request.form)
    if request.method == 'POST' and update_form.validate():
        Event_dict = {}
        db = shelve.open('Event.db', 'w')
        Event_dict = db['Event']

        image_1 = request.files['image']
        filename = secure_filename(image_1.filename)
        image_1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        Event = Event_dict.get(Event_name)
        Event.set_name(update_form.name.data)
        Event.set_image(filename)
        Event.set_description(update_form.description.data)
        Event.set_date(update_form.date.data)

        db['Event'] = Event_dict
        db.close()

        return redirect(url_for('Aretrieve_Event'))
    else:
        Event_dict = {}
        db = shelve.open('Event.db', 'r')
        Event_dict = db['Event']
        db.close()

        Event = Event_dict.get(Event_name)
        update_form.name.data = Event.get_name()
        update_form.description.data = Event.get_description()
        update_form.date.data = Event.get_date()

        return render_template('AupdateEvent.html', form=update_form)


@app.route('/AdeleteEvent/<Event_name>', methods=['POST'])
def Adelete_Event(Event_name):
    Event_dict = {}
    db = shelve.open('Event.db', 'w')
    Event_dict = db['Event']
    Event_dict.pop(Event_name)

    db['Event'] = Event_dict
    db.close()

    return redirect(url_for('Aretrieve_Event'))


@app.route('/retrieveEvent')
def retrieve_Event():
    start = request.args.get('start', 0, type=int)
    limit = 100  # Or your predefined limit

    db = shelve.open('Event.db', 'r')
    Event_dict = db['Event']
    db.close()

    Event_keys_sorted = sorted(Event_dict.keys())
    filtered_keys = Event_keys_sorted

    filter_option = request.args.get('filter', 'all')

    if filter_option == 'weekday':
        filtered_keys = [key for key in Event_keys_sorted if Event_dict[key].get_date().weekday() < 5]
    elif filter_option == 'weekend':
        filtered_keys = [key for key in Event_keys_sorted if Event_dict[key].get_date().weekday() >= 5]

    Event_list = [Event_dict[key] for key in filtered_keys[start:start + limit]]
    show_load_more = start + limit < len(filtered_keys)

    return render_template('retrieveEvent.html', count=len(filtered_keys), Event_list=Event_list,
                           show_load_more=show_load_more, filter_option=filter_option)


# For pickup and delivery

@app.route('/AcreateService', methods=['GET', 'POST'])
def Acreate_Service():
    form = ServiceForm(request.form)
    if request.method == 'POST' and form.validate():
        service_dict = {}
        db = shelve.open('Service.db', 'c')

        try:
            service_dict = db['Service']
        except:
            print("Error in retrieving Services from Service.db.")
            print('no')

        name = form.name.data
        description = form.description.data

        new_service = Service(name, description)

        service_dict[new_service.get_name()] = new_service
        db['Service'] = service_dict
        db.close()
        print('Stored')
        print(f"New service created: {new_service.get_name()}, Description: {new_service.get_description()}")

        return redirect(url_for('Aretrieve_Service'))
    return render_template('AcreateService.html', form=form)


@app.route('/AretrieveService')
def Aretrieve_Service():
    start = request.args.get('start', 0, type=int)
    limit = 6

    db = shelve.open('Service.db', 'r')
    service_dict = db['Service']
    db.close()

    total_count = len(service_dict)

    # Sorting keys and getting a slice of events based on current start and limit
    Service_keys_sorted = sorted(service_dict.keys())
    service_list = [service_dict[key] for key in Service_keys_sorted[start:start + limit]]

    # Determine whether to show the 'Load More' button
    show_load_more = start + limit < total_count
    print(f"Services being retrieved: {[service.get_name() for service in service_list]}")

    return render_template('AretrieveService.html', count=total_count, service_list=service_list,
                           show_load_more=show_load_more)


@app.route('/AupdateService/<Service_name>', methods=['GET', 'POST'])
def Aupdate_Service(Service_name):
    update_form = UpdateServiceForm(request.form)
    if request.method == 'POST' and update_form.validate():
        service_dict = {}
        db = shelve.open('Service.db', 'w')
        service_dict = db['Service']

        Service = service_dict.get(Service_name)
        Service.set_name(update_form.name.data)
        Service.set_description(update_form.description.data)

        db['Service'] = service_dict
        db.close()

        return redirect(url_for('Aretrieve_Service'))
    else:
        service_dict = {}
        db = shelve.open('Service.db', 'r')
        service_dict = db['Service']
        db.close()

        Service = service_dict.get(Service_name)
        update_form.name.data = Service.get_name()
        update_form.description.data = Service.get_description()

        return render_template('AupdateService.html', form=update_form)


@app.route('/AdeleteService/<Service_name>', methods=['POST'])
def Adelete_Service(Service_name):
    service_dict = {}
    db = shelve.open('Service.db', 'w')
    service_dict = db['Service']
    service_dict.pop(Service_name)

    db['Service'] = service_dict
    db.close()

    return redirect(url_for('Aretrieve_Service'))


@app.route('/homeservice')
def home_service():
    return render_template('homeservice.html')


@app.route('/servicechoose')
def service_choose():
    start = request.args.get('start', 0, type=int)
    limit = 6

    db = shelve.open('Service.db', 'r')
    service_dict = db['Service']
    db.close()

    total_count = len(service_dict)

    # Sorting keys and getting a slice of events based on current start and limit
    Service_keys_sorted = sorted(service_dict.keys())
    service_list = [service_dict[key] for key in Service_keys_sorted[start:start + limit]]

    # Determine whether to show the 'Load More' button
    show_load_more = start + limit < total_count
    print(
        f"Service URLs being created: {[url_for('service_page', service_name=service.get_name().replace(' ', '')) for service in service_list]}")

    return render_template('servicechoose.html', count=total_count, service_list=service_list,
                           show_load_more=show_load_more)


@app.route('/<service_name>.html')
def service_page(service_name):
    print(f"Original requested service name: {service_name}")
    db = shelve.open('Service.db', 'r')
    service_dict = db['Service']
    db.close()

    # Debug: Print all keys in the database
    print(f"Keys in the database: {list(service_dict.keys())}")

    service_key = service_name.replace('-', ' ')
    print(f"Formatted service key being searched for: {service_key}")

    service = service_dict.get(service_key)

    if service:
        template_name = f"{service_name}.html"
        return render_template(template_name, service=service)
    else:
        print(f"Service with key '{service_key}' not found - returning 404")
        return 'Service Not Found', 404


# Sherman End


if __name__ == '__main__':
    app.run(debug=True)
