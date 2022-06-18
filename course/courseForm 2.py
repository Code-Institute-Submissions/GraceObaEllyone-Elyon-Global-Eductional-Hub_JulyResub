from django import forms

from course.models import Course, CourseReview, Category


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('rating',)


class CourseReviewForm(forms.ModelForm):
    class Meta:
        model = CourseReview
        fields = ('rating_score', 'review_title', 'review_comment')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')