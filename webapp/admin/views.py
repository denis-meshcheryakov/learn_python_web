from pydoc import render_doc
from turtle import title
from flask import Blueprint, render_template
from webapp.user.decorators import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@admin_required
def admin_index():
    title = 'Панель управдения'
    return render_template('admin/index.html', page_title=title)
