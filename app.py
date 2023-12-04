from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, Email
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from datetime import datetime, date


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../backend_app/database/luxury_wheels.db'
app.secret_key = 'senhaPadrao123'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    categoria = db.Column(db.String(60), nullable=False)


class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    imagem = db.Column(db.String(255), nullable=True)
    quilometragem = db.Column(db.Integer, nullable=False)
    manutencao = db.Column(db.Integer, nullable=False)
    data_inicio_manut = db.Column(db.Date, nullable=True)
    data_final_manut = db.Column(db.Date, nullable=True)
    licenciamento = db.Column(db.Date, nullable=False)
    disponibilidade = db.Column(db.String, nullable=False)


class RegistrationForm(FlaskForm):
    name = StringField('Nome e Apelido', validators=[DataRequired()])
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    categoria = SelectField('Categoria', choices=[('GOLD', 'GOLD'), ('SILVER', 'SILVER'), ['Economico', 'Economico']])
    submit = SubmitField('Registar')


class LoginForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')


class PaymentForm(FlaskForm):
    nome_cartao = StringField('Nome como está no cartão de crédito', validators=[DataRequired(),
                                                                                 Length(min=2, max=100)])
    numero_cartao = StringField('Número do cartão de crédito', validators=[DataRequired(), Length(min=16, max=16)])
    data_validade = StringField('Data de validade do cartão de crédito (xx/xx)', validators=[DataRequired(),
                                                                                             Length(min=4, max=4)])
    codigo_seguranca = StringField('Código de segurança do cartão de crédito', validators=[DataRequired(),
                                                                                           Length(min=3, max=4)])
    submit = SubmitField('Pagar')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('aluguer', categoria=user.categoria))
        else:
            flash('Login não foi bem-sucedido.\nVerifique seu nome de usuário e senha.', 'danger')
    return render_template('index.html', title='Login', form=form)


@app.route('/registo', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('Email já registrado anteriormente. Por favor, use outro email', 'danger')
        elif existing_user:
            flash('Nome de usuário já em uso. Favor escolher outro.', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(
                name=form.name.data,
                username=form.username.data,
                email=form.email.data,
                password=hashed_password,
                categoria=form.categoria.data
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('registo.html', title='Registrar', form=form)


@app.route('/aluguer/<categoria>', methods=['GET', 'POST'])
def aluguer(categoria):
    veiculos = Veiculo.query.filter_by(categoria=categoria, disponibilidade='sim').all()

    if request.method == 'POST':
        data_retirada = datetime.strptime(request.form['data_retirada'], '%Y-%m-%d').date()
        data_devolucao = datetime.strptime(request.form['data_devolucao'], '%Y-%m-%d').date()

        # Verificação se a data retirada é anterior a data atual
        if data_retirada < date.today():
            flash('A data de retirada não pode ser anterior a data atual', 'danger')
            return redirect(url_for('aluguer', categoria=categoria))

        # Verificação se a data devolução tem pelo menos 1 dia a mais que a data retirada
        if data_devolucao <= data_retirada:
            flash('A data de devolução deve ser pelo menos um dia após a data de retirada', 'danger')
            return redirect(url_for('aluguer', categoria=categoria))

        if not veiculos:
            flash('Não possuimos veículos disponíveis na sua categoria. Cadastre-se em uma categoria diferente',
                  'danger')
            return redirect(url_for('index'))

        # cálculo do valor baseado nas datas que foram colocadas
        total_dias_aluguer = (data_devolucao - data_retirada).days
        veiculo_id = int(request.form['veiculo_id'])
        return redirect(url_for('pagamento', veiculo_id=veiculo_id, data_devolucao=data_devolucao,
                                data_retirada=data_retirada, total_dias_aluguer=total_dias_aluguer))

    return render_template('aluguer.html', veiculos=veiculos, categoria=categoria)


@app.route('/pagamento/<int:veiculo_id>', methods=['GET', 'POST'])
@login_required
def pagamento(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)

    data_retirada = request.args.get('data_retirada')
    data_devolucao = request.args.get('data_devolucao')
    total_dias_aluguer = int(request.args.get('total_dias_aluguer'))

    if request.method == 'POST':
        total_valor_aluguer = total_dias_aluguer * float(veiculo.preco)
        return redirect(url_for('comprovante', veiculo_id=veiculo.id, data_retirada=data_retirada,
                                data_devolucao=data_devolucao, total_valor_aluguer=total_valor_aluguer))

    form = PaymentForm(request.form)

    total = total_dias_aluguer * float(veiculo.preco)

    return render_template('pagamento.html', veiculo=veiculo, data_retirada=data_retirada,
                           data_devolucao=data_devolucao, total=total, form=form)


@app.route('/comprovante/<int:veiculo_id>')
@login_required
def comprovante(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    data_retirada = request.args.get('data_retirada')
    data_devolucao = request.args.get('data_devolucao')
    valor_total_pago = request.args.get('total_valor_aluguer')
    nome_cliente = current_user.name
    email_cliente = current_user.email

    return render_template('comprovante.html', veiculo=veiculo, nome_cliente=nome_cliente,
                           email_cliente=email_cliente, data_devolucao=data_devolucao, data_retirada=data_retirada,
                           valor_total_pago=valor_total_pago)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
