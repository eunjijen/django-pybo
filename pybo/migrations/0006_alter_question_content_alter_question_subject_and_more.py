# Generated by Django 4.1.7 on 2023-02-27 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pybo", "0005_answer_modify_date_question_modify_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="content",
            field=models.TextField(help_text="질문의 내용을 상세히 작성하세요.", verbose_name="내용"),
        ),
        migrations.AlterField(
            model_name="question",
            name="subject",
            field=models.CharField(
                help_text="질문의 제목을 한줄로 작성하세요.", max_length=200, verbose_name="제목"
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contetn", models.TextField(verbose_name="댓글 내용")),
                ("create_date", models.DateTimeField(verbose_name="생성일")),
                (
                    "modify_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="수정일"),
                ),
                (
                    "answer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pybo.answer",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pybo.question",
                    ),
                ),
            ],
        ),
    ]
