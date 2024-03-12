from django.db import models

class Property(models.Model):
    transaction_unique_identifier = models.CharField(max_length=50, db_column='Transaction Unique Identifier',primary_key=True)
    price = models.CharField(max_length=50, db_column='Price')
    transfer_date = models.CharField(max_length=50, db_column='Transfer Date')
    postcode = models.CharField(max_length=50, db_index=True)
    property_type = models.CharField(max_length=50, db_column='Property Type')
    old_new = models.CharField(max_length=50, db_column='Old New')
    duration = models.CharField(max_length=50, db_column='Duration')
    primary_address = models.CharField(max_length=255, db_column='Primary Address')
    secondary_address = models.CharField(max_length=255, blank=True, null=True, db_column='Secondary Address')
    street = models.CharField(max_length=255, blank=True, null=True, db_column='Street')
    locality = models.CharField(max_length=50, blank=True, null=True, db_column='Locality')
    town_city = models.CharField(max_length=50, db_column='Town City')
    district = models.CharField(max_length=50, db_column='District')
    county = models.CharField(max_length=50, db_column='County')
    ppd_category_type = models.CharField(max_length=50, db_column='PPD Category Type')
    record_status = models.CharField(max_length=255, db_column='Record Status')

    class Meta:
        db_table = 'pp-complete'  
        managed = False  



class CrimeRate(models.Model):
    postcode = models.CharField(max_length=20)
    month = models.DateField()
    crime_type = models.CharField(max_length=100)
    crime_count = models.IntegerField()

    class Meta:
        db_table = 'crime_rate' 
        managed = False

class Migration(models.Model):
    out_la = models.CharField(max_length=100)
    in_la = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    count = models.IntegerField()
    borough = models.CharField(max_length=100)

    class Meta:
        db_table = 'migrations'  
        managed = False

class EPC(models.Model):
    lmk_key = models.CharField(max_length=100)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    address3 = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=20)
    building_reference_number = models.CharField(max_length=100)
    current_energy_rating = models.CharField(max_length=5)
    potential_energy_rating = models.CharField(max_length=5)
    current_energy_efficiency = models.IntegerField()
    potential_energy_efficiency = models.IntegerField()
    property_type = models.CharField(max_length=50)
    built_form = models.CharField(max_length=50)
    inspection_date = models.DateField()
    local_authority = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    lodgement_date = models.DateField()
    transaction_type = models.CharField(max_length=50)
    environment_impact_current = models.IntegerField()
    environment_impact_potential = models.IntegerField()

    class Meta:
        db_table = 'epc' 
        managed = False
