import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        response = json.load(f)
        return response


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate_id == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidates_from_json():
        if candidate_name == candidate["name"]:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result
