from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    news_id = HiddenField('ID новости', validators=[DataRequired()])
    comment_text = StringField('Ваш комментарий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
