from pybo.models import Question

# author_id=1인 레코드를 찾아봅니다.
broken_questions = Question.objects.filter(author_id=1)
print(broken_questions)
