from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates_info = load_candidates_from_json()
    return render_template('list.html', candidates=candidates_info)


@app.route('/candidate/<int:id>')
def candidate_id(id):
    candidate = get_candidate(id)
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_by_name(candidate_name):
    list_of_candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=list_of_candidates)


@app.route('/skill/<skill_name>')
def search_by_skill(skill_name):
    list_of_skills = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=list_of_skills)


app.run()
