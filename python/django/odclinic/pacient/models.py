from django.db import models
from django.contrib import admin

class Pacient(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    
    CIVIL_STATE_CHOICES = (
        (1, 'Single'),
        (2, 'Married'),
        (3, 'Divorced'),
        (4, 'Widower'),
    )
    
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
        (3, 'Return'),
        (4, 'Indebted'),
        (5, 'Defunct'),
    )
    
    name = models.CharField(max_length=128)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=12) 
    gender = models.IntegerField(max_length=1, choices=GENDER_CHOICES)
    civil_state = models.IntegerField(max_length=1, choices=CIVIL_STATE_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=128, null=True, blank=True)
    res_address = models.CharField(max_length=256)
    res_address_number = models.IntegerField()
    res_address_complement = models.CharField(max_length=5, null=True, blank=True)
    res_address_neighborhood = models.CharField(max_length=64, null=True, blank=True)
    res_address_zipcode = models.CharField(max_length=10, null=True, blank=True)
    res_phone = models.CharField(max_length=16, null=True, blank=True)
    com_address = models.CharField(max_length=256, null=True, blank=True)
    com_address_number = models.IntegerField(null=True, blank=True)
    com_address_complement = models.CharField(max_length=5, null=True, blank=True)
    com_address_neighborhood = models.CharField(max_length=64, null=True, blank=True)
    com_address_zipcode = models.CharField(max_length=10, null=True, blank=True)
    com_phone = models.CharField(max_length=16, null=True, blank=True)
    mobile = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)    
    indicated_by = models.ForeignKey('self', null=True, blank=True) 
    father_name = models.CharField(max_length=128, null=True, blank=True)
    mother_name = models.CharField(max_length=128, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES, default=1)
    
    def get_formatted_res_address(self):
        parts = ''
        
        if self.res_address:
            parts = self.res_address
            
            if self.res_address_number:
                parts += ', ' + unicode(self.res_address_number)                
            if self.res_address_complement:
                parts += ', ' + unicode(self.res_address_complement)                
            parts += '. '
            
            if self.res_address_neighborhood:
                parts += self.res_address_neighborhood + '. '
            
            if self.res_address_zipcode:
                parts += unicode(self.res_address_zipcode) + '.'
                
        return parts.strip()
    
    def get_formatted_com_address(self):
        parts = ''
        
        if self.com_address:
            parts = self.com_address

            if self.com_address_number:
                parts += ', ' + unicode(self.com_address_number)                
            if self.com_address_complement:
                parts += ', ' + unicode(self.com_address_complement)                
            parts += '. '

            if self.com_address_neighborhood:
                parts += self.com_address_neighborhood + '. '

            if self.com_address_zipcode:
                parts += unicode(self.com_address_zipcode) + '.'

        return parts.strip()
    
    class Meta:
        ordering = ('name',)
        
    def __unicode__(self):        
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('pacient-detail', [str(self.id)])
        
class PacientAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'res_phone', 'status',)
    search_fields = ('name', 'cpf', 'rg', 'indicated_by',)
    list_filter = ('name', 'status',)
    
class OfficeRoom(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    is_active = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    
class OfficeRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active',)

class Schedule(models.Model):    
    pacient = models.ForeignKey(Pacient)
    office = models.ForeignKey(OfficeRoom)
    proceeding = models.ManyToManyField('Proceeding')
    detail = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('pacient', 'office', 'start', 'end',)
    
class Proceeding(models.Model):
    name = models.CharField(max_length=128)
    detail = models.TextField()
    is_active = models.BooleanField()
    
    def __unicode__(self):
        return self.name

class ProceedingAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail', 'is_active')