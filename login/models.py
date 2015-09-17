from django.db import models

# Create your models here.

DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

class User_Details(models.Model):
	userid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=512,null=True,blank=True)
	country = models.CharField(max_length=512,null=True,blank=True)
	interests = models.CharField(max_length=512,null=True,blank=True)
	email = models.CharField(max_length=512,null=True,blank=True)
	username = models.CharField(max_length=512,null=True,blank=True)
	password = models.CharField(max_length=512,null=True,blank=True)
	google_id = models.CharField(max_length=512,null=True,blank=True)
	google_acc_img = models.CharField(max_length=512,null=True,blank=True)
	dropbox_id = models.CharField(max_length=512,null=True,blank=True)
	facebook_id = models.CharField(max_length=512,null=True,blank=True)
	fb_img_url = models.CharField(max_length=512,null=True,blank=True)
	signup_type = models.CharField(max_length=512,null=True,blank=True)
	referal_id = models.CharField(max_length=512,null=True,blank=True)
	active_status = models.CharField(max_length=512,null=True,blank=True)
	signup_date = models.DateField(null=True,blank=True)

class Project_Table(models.Model):
	projectid = models.AutoField(primary_key=True)
	userid = models.IntegerField(null=True,blank=True)
	project_title = models.CharField(max_length=512,null=True,blank=True)
	project_instructions = models.CharField(max_length=512,null=True,blank=True)
	project_status = models.CharField(max_length=512,null=True,blank=True)
	admin_comments = models.CharField(max_length=512,null=True,blank=True)
	project_cost = models.CharField(max_length=512,null=True,blank=True)
	pricing_detail_id = models.CharField(max_length=512,null=True,blank=True)
	order_no = models.CharField(max_length=512,null=True,blank=True)
	project_feedback = models.CharField(max_length=512,null=True,blank=True)
	satisfaction_rating = models.CharField(max_length=512,null=True,blank=True)
	material_rating = models.CharField(max_length=512,null=True,blank=True)
	visual_effect_rating = models.CharField(max_length=512,null=True,blank=True)
	storyline_rating = models.CharField(max_length=512,null=True,blank=True)
	start_date = models.DateField(null=True,blank=True)
	end_date = models.DateField(null=True,blank=True)
	
class User_File_Table(models.Model):
	fileid = models.AutoField(primary_key=True)
	userid = models.IntegerField(null=True,blank=True)
	projectid = models.IntegerField(null=True,blank=True)
	file_type = models.CharField(max_length=512,null=True,blank=True)
	file_title = models.CharField(max_length=512,null=True,blank=True)
	file_web_path = models.CharField(max_length=512,null=True,blank=True)
	file_server_path = models.CharField(max_length=512,null=True,blank=True)
	file_source_type = models.CharField(max_length=512,null=True,blank=True)
	file_status = models.CharField(max_length=512,null=True,blank=True)
	file_upload_date = models.DateField(null=True,blank=True)
	admin_comments = models.CharField(max_length=512,null=True,blank=True)
	
class Admin_File_Table(models.Model):
	fileid = models.AutoField(primary_key=True)
	userid = models.IntegerField(null=True,blank=True)
	projectid = models.IntegerField(null=True,blank=True)
	user_file_id = models.IntegerField(null=True,blank=True)
	admin_file_path = models.CharField(max_length=512,null=True,blank=True)
	file_status = models.CharField(max_length=512,null=True,blank=True)
	upload_date = models.DateField(null=True,blank=True)
	admin_comments = models.CharField(max_length=512,null=True,blank=True)

class Pricing_Table(models.Model):
	id = models.AutoField(primary_key=True)
	userid = models.IntegerField(null=True,blank=True)
	payee_name = models.CharField(max_length=512,null=True,blank=True)
	payee_email = models.CharField(max_length=512,null=True,blank=True)
	payee_details = models.CharField(max_length=512,null=True,blank=True)
	status = models.CharField(max_length=512,null=True,blank=True)

class Cost_Table(models.Model):
	id = models.AutoField(primary_key=True)
	cost_type = models.CharField(max_length=512,null=True,blank=True)
	file_type = models.CharField(max_length=512,null=True,blank=True)
	cost_per_unit = models.CharField(max_length=512,null=True,blank=True)
	unit_size = models.CharField(max_length=512,null=True,blank=True)

class Credit_Table(models.Model):
	id = models.AutoField(primary_key=True)
	userid = models.IntegerField(null=True,blank=True)
	credit_type = models.CharField(max_length=512,null=True,blank=True)
	credit_amount = models.CharField(max_length=512,null=True,blank=True)
	status = models.CharField(max_length=512,null=True,blank=True)

class Referal_Table(models.Model):
	id = models.AutoField(primary_key=True)
	userid = models.IntegerField(null=True,blank=True)
	referal_url = models.CharField(max_length=512,null=True,blank=True)
	succesful_referals = models.CharField(max_length=512,null=True,blank=True)
