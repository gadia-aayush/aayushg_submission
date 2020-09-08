from django.db import models


class Survey(models.Model):
	s_id = models.IntegerField(primary_key=True)
	s_desc = models.CharField(max_length=255)
	s_start = models.DateTimeField()
	s_end = models.DateTimeField()
	s_active = models.IntegerField()

	class Meta:
		managed = True
		db_table = "survey"


class Question(models.Model):
	q_id = models.IntegerField(primary_key=True)
	q_text = models.CharField(max_length=255)

	class Meta:
		managed = True
		db_table = "question"


class Options(models.Model):
	op_id = models.IntegerField(primary_key=True)
	op_text = models.CharField(max_length=255)

	class Meta:
		managed = True
		db_table = "options"


class Relation_Survey_Qn(models.Model):
	rel_id = models.IntegerField(primary_key=True)
	rel_sid = models.ForeignKey(Survey, on_delete=models.CASCADE)
	rel_qid = models.ForeignKey(Question, on_delete=models.CASCADE)
	rel_last = models.IntegerField()

	class Meta:
		managed = True
		db_table = "relation_survery_qn"


class Relation_Question_Opn(models.Model):
	rel_id = models.IntegerField(primary_key=True)
	rel_qid = models.ForeignKey(Question, on_delete=models.CASCADE)
	rel_opid = models.ForeignKey(Options, on_delete=models.CASCADE)

	class Meta:
		managed = True
		db_table = "relation_question_opn"

