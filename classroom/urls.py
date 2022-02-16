from django.urls import path
from classroom.views import Categories, CategoryCourses, NewCourse, Enroll, DeleteCourse, EditCourse, MyCourses, \
    CourseDetail
from module.views import NewModule, CourseModules
from page.views import NewPageModule, PageDetail
from quiz.views import NewQuiz, NewQuestion, QuizDetail, TakeQuiz, SubmitAttempt, AttemptDetail

urlpatterns = [
    # Course - Classroom Views
    path('newcourse/', NewCourse, name='newcourse'),
    path('MyCourses/', MyCourses, name='my-courses'),
    path('categories/', Categories, name='categories'),
    path('categories/<category_slug>', CategoryCourses, name='category-courses'),
    path('<course_id>/', CourseDetail, name='course'),
    path('<course_id>/enroll', Enroll, name='enroll'),
    path('<course_id>/edit', EditCourse, name='edit-course'),
    path('<course_id>/delete', DeleteCourse, name='delete-course'),
    # Modules
    path('<course_id>/modules', CourseModules, name='modules'),
    path('<course_id>/modules/newmodule', NewModule, name='new-module'),
    # pages
    path('<course_id>/modules/<module_id>/pages/newpage', NewPageModule, name='new-page'),
    path('<course_id>/modules/<module_id>/pages/<page_id>', PageDetail, name='page-detail'),
    # Quizzes
    path('<course_id>/modules/<module_id>/quiz/newquiz', NewQuiz, name='new-quiz'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/newquestion', NewQuestion, name='new-question'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/', QuizDetail, name='quiz-detail'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/take', TakeQuiz, name='take-quiz'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/take/submit', SubmitAttempt, name='submit-quiz'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/<attempt_id>/results', AttemptDetail, name='attempt-detail'),

]
