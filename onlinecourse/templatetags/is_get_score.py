from django.template.defaultfilters import register
#from onlinecourse.models import Question


@register.filter(name='is_get_score')
def is_get_score(question_id, selected_ids):
    #question = Question.objects.get(id=question_id)
    return True#question.is_get_score(selected_ids)
