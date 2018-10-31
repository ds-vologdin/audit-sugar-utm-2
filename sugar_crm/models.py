# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class A0001Notes(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a0001_notes'


class A0001NotesAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a0001_notes_audit'


class AccAccesscontract(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    inet = models.IntegerField(blank=True, null=True)
    typecontract = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accesscontract'


class AccAccesscontractAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accesscontract_audit'


class AccAccesscontractContactsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_accesscontract_contactsacc_accesscontract_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_accesscontract_contactscontacts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accesscontract_contacts_c'


class AccAccesscontractNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_accesscontract_notesacc_accesscontract_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_accesscontract_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accesscontract_notes_c'


class AccAccessdocuments(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    document_name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    file_ext = models.CharField(max_length=100, blank=True, null=True)
    file_mime_type = models.CharField(max_length=100, blank=True, null=True)
    active_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    category_id = models.CharField(max_length=100, blank=True, null=True)
    subcategory_id = models.CharField(max_length=100, blank=True, null=True)
    status_id = models.CharField(max_length=100, blank=True, null=True)
    teypedoc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accessdocuments'


class AccAccessdocumentsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accessdocuments_audit'


class AccAccessdocumentsNotes1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_accessdocuments_notes_1acc_accessdocuments_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_accessdocuments_notes_1notes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accessdocuments_notes_1_c'


class AccAccessdocumentsNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_accessdocuments_notesacc_accessdocuments_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_accessdocuments_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accessdocuments_notes_c'


class AccAccesserror(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    dateerror = models.DateField(blank=True, null=True)
    dateaccess = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accesserror'


class AccAccesserrorAccFacilityC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_accesserror_acc_facilityacc_facility_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_accesserror_acc_facilityacc_accesserror_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accesserror_acc_facility_c'


class AccAccesserrorAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accesserror_audit'


class AccAccesserrorNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_accesserror_notesacc_accesserror_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_accesserror_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_accesserror_notes_c'


class AccFacility(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    accessmode = models.TextField(blank=True, null=True)
    presencekey = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    facilitymap = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_facility'


class AccFacilityAccAccesscontractC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_facility_acc_accesscontractacc_facility_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_facility_acc_accesscontractacc_accesscontract_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_facility_acc_accesscontract_c'


class AccFacilityAccAccessdocumentsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_facility_acc_accessdocumentsacc_facility_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_facility_acc_accessdocumentsacc_accessdocuments_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_facility_acc_accessdocuments_c'


class AccFacilityAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_facility_audit'


class AccFacilityContactsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_facility_contactsacc_facility_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_facility_contactscontacts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_facility_contacts_c'


class AccFacilityCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    district_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_facility_cstm'


class AccFacilityNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_facility_notesacc_facility_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_facility_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_facility_notes_c'


class AccRequisition(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    accessmode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_requisition'


class AccRequisitionAccAccessdocumentsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_requisition_acc_accessdocumentsacc_requisition_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_requisition_acc_accessdocumentsacc_accessdocuments_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_requisition_acc_accessdocuments_c'


class AccRequisitionAccFacilityC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_requisition_acc_facilityacc_requisition_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_requisition_acc_facilityacc_facility_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_requisition_acc_facility_c'


class AccRequisitionAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_requisition_audit'


class AccRequisitionCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    accessmodecheck_c = models.CharField(max_length=100, blank=True, null=True)
    equipment_c = models.CharField(max_length=255, blank=True, null=True)
    address_sogl_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_requisition_cstm'


class AccRequisitionNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_requisition_notesacc_requisition_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_requisition_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_requisition_notes_c'


class AccUk(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_uk'


class AccUkAccAccesscontractC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_uk_acc_accesscontractacc_uk_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_uk_acc_accesscontractacc_accesscontract_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_uk_acc_accesscontract_c'


class AccUkAccAccessdocumentsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_uk_acc_accessdocumentsacc_uk_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_uk_acc_accessdocumentsacc_accessdocuments_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_uk_acc_accessdocuments_c'


class AccUkAccFacilityC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_uk_acc_facilityacc_uk_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_uk_acc_facilityacc_facility_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_uk_acc_facility_c'


class AccUkAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_uk_audit'


class AccUkContactsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_uk_contactsacc_uk_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_uk_contactscontacts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_uk_contacts_c'


class AccUkNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    acc_uk_notesacc_uk_ida = models.CharField(max_length=36, blank=True, null=True)
    acc_uk_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_uk_notes_c'


class Accounts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=150, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    account_type = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    annual_revenue = models.CharField(max_length=100, blank=True, null=True)
    phone_fax = models.CharField(max_length=100, blank=True, null=True)
    billing_address_street = models.CharField(max_length=150, blank=True, null=True)
    billing_address_city = models.CharField(max_length=100, blank=True, null=True)
    billing_address_state = models.CharField(max_length=100, blank=True, null=True)
    billing_address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    billing_address_country = models.CharField(max_length=255, blank=True, null=True)
    rating = models.CharField(max_length=100, blank=True, null=True)
    phone_office = models.CharField(max_length=100, blank=True, null=True)
    phone_alternate = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    ownership = models.CharField(max_length=100, blank=True, null=True)
    employees = models.CharField(max_length=10, blank=True, null=True)
    ticker_symbol = models.CharField(max_length=10, blank=True, null=True)
    shipping_address_street = models.CharField(max_length=150, blank=True, null=True)
    shipping_address_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_address_state = models.CharField(max_length=100, blank=True, null=True)
    shipping_address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    shipping_address_country = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)
    sic_code = models.CharField(max_length=10, blank=True, null=True)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class AccountsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_audit'


class AccountsBugs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    account_id = models.CharField(max_length=36, blank=True, null=True)
    bug_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_bugs'


class AccountsCalls1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    accounts_calls_1accounts_ida = models.CharField(max_length=36, blank=True, null=True)
    accounts_calls_1calls_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_calls_1_c'


class AccountsCases(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    account_id = models.CharField(max_length=36, blank=True, null=True)
    case_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_cases'


class AccountsConPConnectionsPlan1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    accounts_con_p_connections_plan_1accounts_ida = models.CharField(max_length=36, blank=True, null=True)
    accounts_con_p_connections_plan_1con_p_connections_plan_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_con_p_connections_plan_1_c'


class AccountsContacts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    account_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_contacts'


class AccountsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    internet_acc_c = models.IntegerField(blank=True, null=True)
    phone_acc_c = models.IntegerField(blank=True, null=True)
    pdcpgi_acc_c = models.IntegerField(blank=True, null=True)
    inet_pvk_acc_c = models.IntegerField(blank=True, null=True)
    inet_ip_acc_c = models.IntegerField(blank=True, null=True)
    month_profit_acc_c = models.IntegerField(blank=True, null=True)
    packet_acc_c = models.IntegerField(blank=True, null=True)
    block_acc_c = models.IntegerField(blank=True, null=True)
    vats_acc_c = models.IntegerField(blank=True, null=True)
    tv_acc_c = models.IntegerField(blank=True, null=True)
    inet_date_acc_c = models.DateField(blank=True, null=True)
    phone_date_acc_c = models.DateField(blank=True, null=True)
    closed_acc_c = models.IntegerField(blank=True, null=True)
    date_close_acc_c = models.DateField(blank=True, null=True)
    blockletter_acc_c = models.IntegerField(blank=True, null=True)
    date_blockletter_acc_c = models.DateField(blank=True, null=True)
    close_couse_acc_c = models.CharField(max_length=100, blank=True, null=True)
    close_comment_acc_c = models.TextField(blank=True, null=True)
    status_acc_c = models.CharField(max_length=100, blank=True, null=True)
    priority_acc_c = models.CharField(max_length=100, blank=True, null=True)
    debtor_acc_c = models.IntegerField(blank=True, null=True)
    address_map_acc_c = models.CharField(max_length=255, blank=True, null=True)
    cctv_acc_c = models.IntegerField(blank=True, null=True)
    cost_pdcpgi_acc_c = models.IntegerField(blank=True, null=True)
    company_acc_c = models.IntegerField(blank=True, null=True)
    bandwidth_c = models.FloatField(blank=True, null=True)
    login_ph_c = models.CharField(max_length=255, blank=True, null=True)
    phone_new_c = models.CharField(max_length=255, blank=True, null=True)
    phone_from_bug_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_lng_c = models.FloatField(blank=True, null=True)
    jjwg_maps_lat_c = models.FloatField(blank=True, null=True)
    jjwg_maps_geocode_status_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_address_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_cstm'


class AccountsMaMount1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    accounts_ma_mount_1accounts_ida = models.CharField(max_length=36, blank=True, null=True)
    accounts_ma_mount_1ma_mount_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_ma_mount_1_c'


class AccountsNotes1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    accounts_notes_1accounts_ida = models.CharField(max_length=36, blank=True, null=True)
    accounts_notes_1notes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_notes_1_c'


class AccountsOpportunities(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    opportunity_id = models.CharField(max_length=36, blank=True, null=True)
    account_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_opportunities'


class AccountsPoPo1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    accounts_po_po_1accounts_ida = models.CharField(max_length=36, blank=True, null=True)
    accounts_po_po_1po_po_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_po_po_1_c'


class AccountsTcTariffchangeinet1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    accounts_tc_tariffchangeinet_1accounts_ida = models.CharField(max_length=36, blank=True, null=True)
    accounts_tc_tariffchangeinet_1tc_tariffchangeinet_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_tc_tariffchangeinet_1_c'


class AclActions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    acltype = models.CharField(max_length=100, blank=True, null=True)
    aclaccess = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acl_actions'


class AclRoles(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acl_roles'


class AclRolesActions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    role_id = models.CharField(max_length=36, blank=True, null=True)
    action_id = models.CharField(max_length=36, blank=True, null=True)
    access_override = models.IntegerField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acl_roles_actions'


class AclRolesUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    role_id = models.CharField(max_length=36, blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acl_roles_users'


class AddressBook(models.Model):
    assigned_user_id = models.CharField(max_length=36)
    bean = models.CharField(max_length=50, blank=True, null=True)
    bean_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'address_book'


class Bugs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    bug_number = models.AutoField(unique=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=100, blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    work_log = models.TextField(blank=True, null=True)
    found_in_release = models.CharField(max_length=255, blank=True, null=True)
    fixed_in_release = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    product_category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bugs'


class BugsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bugs_audit'


class BugsCBugComments1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    bugs_c_bug_comments_1bugs_ida = models.CharField(max_length=36, blank=True, null=True)
    bugs_c_bug_comments_1c_bug_comments_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bugs_c_bug_comments_1_c'


class BugsCalls1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    bugs_calls_1bugs_ida = models.CharField(max_length=36, blank=True, null=True)
    bugs_calls_1calls_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bugs_calls_1_c'


class BugsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    phone_bugs_c = models.CharField(max_length=255, blank=True, null=True)
    department_bugs_c = models.CharField(max_length=100, blank=True, null=True)
    reason_for_closure_bugs_c = models.CharField(max_length=255, blank=True, null=True)
    type_bugs_c = models.CharField(max_length=100, blank=True, null=True)
    status_bugs_c = models.CharField(max_length=100, blank=True, null=True)
    address_bugs_c = models.CharField(max_length=255, blank=True, null=True)
    account_id_c = models.CharField(max_length=36, blank=True, null=True)
    bug_id_c = models.CharField(max_length=36, blank=True, null=True)
    date_close_c = models.DateTimeField(blank=True, null=True)
    priority_bugs_c = models.CharField(max_length=255, blank=True, null=True)
    departure_bugs_c = models.IntegerField(blank=True, null=True)
    new_reason_for_closure_bugs_c = models.TextField(blank=True, null=True)
    new_priority_bugs_c = models.CharField(max_length=100, blank=True, null=True)
    service_is_delivered_c = models.CharField(max_length=255, blank=True, null=True)
    duration_bug_c = models.FloatField(blank=True, null=True)
    perform_c = models.TextField(blank=True, null=True)
    localisation_c = models.TextField(blank=True, null=True)
    todo_c = models.CharField(max_length=255, blank=True, null=True)
    duration_min_c = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bugs_cstm'


class CBugComments(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_bug_comments'


class CBugCommentsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_bug_comments_audit'


class CBugCommentsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)

    class Meta:
        managed = False
        db_table = 'c_bug_comments_cstm'


class Calls(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    duration_hours = models.IntegerField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    parent_type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    direction = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)
    reminder_time = models.IntegerField(blank=True, null=True)
    email_reminder_time = models.IntegerField(blank=True, null=True)
    email_reminder_sent = models.IntegerField(blank=True, null=True)
    outlook_id = models.CharField(max_length=255, blank=True, null=True)
    repeat_type = models.CharField(max_length=36, blank=True, null=True)
    repeat_interval = models.IntegerField(blank=True, null=True)
    repeat_dow = models.CharField(max_length=7, blank=True, null=True)
    repeat_until = models.DateField(blank=True, null=True)
    repeat_count = models.IntegerField(blank=True, null=True)
    repeat_parent_id = models.CharField(max_length=36, blank=True, null=True)
    recurring_source = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls'


class CallsContacts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    call_id = models.CharField(max_length=36, blank=True, null=True)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    accept_status = models.CharField(max_length=25, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls_contacts'


class CallsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    number_call_c = models.IntegerField(blank=True, null=True)
    check_call_c = models.IntegerField(blank=True, null=True)
    input_number_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls_cstm'


class CallsLeads(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    call_id = models.CharField(max_length=36, blank=True, null=True)
    lead_id = models.CharField(max_length=36, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    accept_status = models.CharField(max_length=25, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls_leads'


class CallsNumbers(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    input_number = models.CharField(max_length=20, blank=True, null=True)
    date_call = models.DateTimeField(blank=True, null=True)
    output_number = models.CharField(max_length=20, blank=True, null=True)
    not_received_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls_numbers'


class CallsUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    call_id = models.CharField(max_length=36, blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    accept_status = models.CharField(max_length=25, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls_users'


class CampaignLog(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)
    target_tracker_key = models.CharField(max_length=36, blank=True, null=True)
    target_id = models.CharField(max_length=36, blank=True, null=True)
    target_type = models.CharField(max_length=100, blank=True, null=True)
    activity_type = models.CharField(max_length=100, blank=True, null=True)
    activity_date = models.DateTimeField(blank=True, null=True)
    related_id = models.CharField(max_length=36, blank=True, null=True)
    related_type = models.CharField(max_length=100, blank=True, null=True)
    archived = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    list_id = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    more_information = models.CharField(max_length=100, blank=True, null=True)
    marketing_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_log'


class CampaignTrkrs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    tracker_name = models.CharField(max_length=30, blank=True, null=True)
    tracker_url = models.CharField(max_length=255, blank=True, null=True)
    tracker_key = models.AutoField()
    campaign_id = models.CharField(max_length=36, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    is_optout = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_trkrs'


class Campaigns(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    tracker_key = models.AutoField()
    tracker_count = models.IntegerField(blank=True, null=True)
    refer_url = models.CharField(max_length=255, blank=True, null=True)
    tracker_text = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    impressions = models.IntegerField(blank=True, null=True)
    currency_id = models.CharField(max_length=36, blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    expected_cost = models.FloatField(blank=True, null=True)
    actual_cost = models.FloatField(blank=True, null=True)
    expected_revenue = models.FloatField(blank=True, null=True)
    campaign_type = models.CharField(max_length=100, blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    frequency = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaigns'


class CampaignsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaigns_audit'


class Cases(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    case_number = models.AutoField(unique=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=100, blank=True, null=True)
    resolution = models.TextField(blank=True, null=True)
    work_log = models.TextField(blank=True, null=True)
    account_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cases'


class CasesAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cases_audit'


class CasesBugs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    case_id = models.CharField(max_length=36, blank=True, null=True)
    bug_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cases_bugs'


class CasesCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    jjwg_maps_lng_c = models.FloatField(blank=True, null=True)
    jjwg_maps_lat_c = models.FloatField(blank=True, null=True)
    jjwg_maps_geocode_status_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_address_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cases_cstm'


class CatRepairsList(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_repairs_list'


class CatWorkList(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_work_list'


class ConPConnectionsPlan(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_p_connections_plan'


class ConPConnectionsPlanAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_p_connections_plan_audit'


class ConPConnectionsPlanCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    address_plan_c = models.CharField(max_length=255, blank=True, null=True)
    time_connection_c = models.CharField(max_length=255, blank=True, null=True)
    date_connection_c = models.DateField(blank=True, null=True)
    contacts_c = models.CharField(max_length=255, blank=True, null=True)
    account_id_c = models.CharField(max_length=36, blank=True, null=True)
    number_opp_c = models.CharField(max_length=255, blank=True, null=True)
    tariff_plan_c = models.CharField(max_length=255, blank=True, null=True)
    issued_hard_c = models.IntegerField(blank=True, null=True)
    user_id_c = models.CharField(max_length=36, blank=True, null=True)
    base_station_c = models.TextField(blank=True, null=True)
    level_signal_c = models.CharField(max_length=255, blank=True, null=True)
    enter_roof_c = models.TextField(blank=True, null=True)
    type_conn_c = models.CharField(max_length=100, blank=True, null=True)
    type_hard_c = models.TextField(blank=True, null=True)
    radio_c = models.IntegerField(blank=True, null=True)
    point_address_c = models.CharField(max_length=255, blank=True, null=True)
    ip_address_c = models.CharField(max_length=255, blank=True, null=True)
    brigada_c = models.CharField(max_length=100, blank=True, null=True)
    gps_check_c = models.IntegerField(blank=True, null=True)
    ra_survey_id_c = models.CharField(max_length=36, blank=True, null=True)
    comment_mount_c = models.TextField(blank=True, null=True)
    check_mount_c = models.IntegerField(blank=True, null=True)
    call_pl_c = models.IntegerField(blank=True, null=True)
    user_id1_c = models.CharField(max_length=36, blank=True, null=True)
    call_comment_c = models.TextField(blank=True, null=True)
    start_time_c = models.DateTimeField(blank=True, null=True)
    end_time_c = models.DateTimeField(blank=True, null=True)
    user_id2_c = models.CharField(max_length=36, blank=True, null=True)
    user_id3_c = models.CharField(max_length=36, blank=True, null=True)
    job_list_c = models.TextField(blank=True, null=True)
    cat_work_c = models.CharField(max_length=100, blank=True, null=True)
    remarks_c = models.CharField(max_length=255, blank=True, null=True)
    photo_one_c = models.CharField(max_length=255, blank=True, null=True)
    photo_two_c = models.CharField(max_length=255, blank=True, null=True)
    photo_three_c = models.CharField(max_length=255, blank=True, null=True)
    photo_four_c = models.CharField(max_length=255, blank=True, null=True)
    user_id4_c = models.CharField(max_length=36, blank=True, null=True)
    acc_requisition_id_c = models.CharField(max_length=36, blank=True, null=True)
    call_date_c = models.DateField(blank=True, null=True)
    status_mount_c = models.CharField(max_length=100, blank=True, null=True)
    channel_speed_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_p_connections_plan_cstm'


class ConPConnectionsPlanNotes1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    con_p_connections_plan_notes_1con_p_connections_plan_ida = models.CharField(max_length=36, blank=True, null=True)
    con_p_connections_plan_notes_1notes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'con_p_connections_plan_notes_1_c'


class Config(models.Model):
    category = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class Contacts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    salutation = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    do_not_call = models.IntegerField(blank=True, null=True)
    phone_home = models.CharField(max_length=100, blank=True, null=True)
    phone_mobile = models.CharField(max_length=100, blank=True, null=True)
    phone_work = models.CharField(max_length=100, blank=True, null=True)
    phone_other = models.CharField(max_length=100, blank=True, null=True)
    phone_fax = models.CharField(max_length=100, blank=True, null=True)
    primary_address_street = models.CharField(max_length=150, blank=True, null=True)
    primary_address_city = models.CharField(max_length=100, blank=True, null=True)
    primary_address_state = models.CharField(max_length=100, blank=True, null=True)
    primary_address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    primary_address_country = models.CharField(max_length=255, blank=True, null=True)
    alt_address_street = models.CharField(max_length=150, blank=True, null=True)
    alt_address_city = models.CharField(max_length=100, blank=True, null=True)
    alt_address_state = models.CharField(max_length=100, blank=True, null=True)
    alt_address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    alt_address_country = models.CharField(max_length=255, blank=True, null=True)
    assistant = models.CharField(max_length=75, blank=True, null=True)
    assistant_phone = models.CharField(max_length=100, blank=True, null=True)
    lead_source = models.CharField(max_length=255, blank=True, null=True)
    reports_to_id = models.CharField(max_length=36, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class ContactsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_audit'


class ContactsBugs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    bug_id = models.CharField(max_length=36, blank=True, null=True)
    contact_role = models.CharField(max_length=50, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_bugs'


class ContactsCases(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    case_id = models.CharField(max_length=36, blank=True, null=True)
    contact_role = models.CharField(max_length=50, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_cases'


class ContactsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    jjwg_maps_lng_c = models.FloatField(blank=True, null=True)
    jjwg_maps_lat_c = models.FloatField(blank=True, null=True)
    jjwg_maps_geocode_status_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_address_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_cstm'


class ContactsUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_users'


class CronRemoveDocuments(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    bean_id = models.CharField(max_length=36, blank=True, null=True)
    module = models.CharField(max_length=25, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cron_remove_documents'


class Currencies(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=36, blank=True, null=True)
    symbol = models.CharField(max_length=36, blank=True, null=True)
    iso4217 = models.CharField(max_length=3, blank=True, null=True)
    conversion_rate = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'currencies'


class CustomFields(models.Model):
    bean_id = models.CharField(max_length=36, blank=True, null=True)
    set_num = models.IntegerField(blank=True, null=True)
    field0 = models.CharField(max_length=255, blank=True, null=True)
    field1 = models.CharField(max_length=255, blank=True, null=True)
    field2 = models.CharField(max_length=255, blank=True, null=True)
    field3 = models.CharField(max_length=255, blank=True, null=True)
    field4 = models.CharField(max_length=255, blank=True, null=True)
    field5 = models.CharField(max_length=255, blank=True, null=True)
    field6 = models.CharField(max_length=255, blank=True, null=True)
    field7 = models.CharField(max_length=255, blank=True, null=True)
    field8 = models.CharField(max_length=255, blank=True, null=True)
    field9 = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_fields'


class DevDevelopment(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    finish = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_development'


class DevDevelopmentAccRequisitionC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    dev_development_acc_requisitiondev_development_ida = models.CharField(max_length=36, blank=True, null=True)
    dev_development_acc_requisitionacc_requisition_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_development_acc_requisition_c'


class DevDevelopmentAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_development_audit'


class DevDevelopmentNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    dev_development_notesdev_development_ida = models.CharField(max_length=36, blank=True, null=True)
    dev_development_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_development_notes_c'


class DevDevelopmentRaSurveyC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    dev_development_ra_surveydev_development_ida = models.CharField(max_length=36, blank=True, null=True)
    dev_development_ra_surveyra_survey_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_development_ra_survey_c'


class DevDevelopmentSkSketchC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    dev_development_sk_sketchdev_development_ida = models.CharField(max_length=36, blank=True, null=True)
    dev_development_sk_sketchsk_sketch_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_development_sk_sketch_c'


class DocumentRevisions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    change_log = models.CharField(max_length=255, blank=True, null=True)
    document_id = models.CharField(max_length=36, blank=True, null=True)
    doc_id = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=100, blank=True, null=True)
    doc_url = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    file_ext = models.CharField(max_length=100, blank=True, null=True)
    file_mime_type = models.CharField(max_length=100, blank=True, null=True)
    revision = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_revisions'


class Documents(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    document_name = models.CharField(max_length=255, blank=True, null=True)
    doc_id = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=100, blank=True, null=True)
    doc_url = models.CharField(max_length=255, blank=True, null=True)
    active_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    category_id = models.CharField(max_length=100, blank=True, null=True)
    subcategory_id = models.CharField(max_length=100, blank=True, null=True)
    status_id = models.CharField(max_length=100, blank=True, null=True)
    document_revision_id = models.CharField(max_length=36, blank=True, null=True)
    related_doc_id = models.CharField(max_length=36, blank=True, null=True)
    related_doc_rev_id = models.CharField(max_length=36, blank=True, null=True)
    is_template = models.IntegerField(blank=True, null=True)
    template_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class DocumentsAccounts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    document_id = models.CharField(max_length=36, blank=True, null=True)
    account_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_accounts'


class DocumentsBugs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    document_id = models.CharField(max_length=36, blank=True, null=True)
    bug_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_bugs'


class DocumentsCases(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    document_id = models.CharField(max_length=36, blank=True, null=True)
    case_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_cases'


class DocumentsContacts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    document_id = models.CharField(max_length=36, blank=True, null=True)
    contact_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_contacts'


class DocumentsOpportunities(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    document_id = models.CharField(max_length=36, blank=True, null=True)
    opportunity_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_opportunities'


class EaddrAction(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    type_action = models.CharField(max_length=100, blank=True, null=True)
    date_action = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eaddr_action'


class EaddrActionAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eaddr_action_audit'


class EaddrActionEaddrEmptyAddressC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    eaddr_action_eaddr_empty_addresseaddr_empty_address_ida = models.CharField(max_length=36, blank=True, null=True)
    eaddr_action_eaddr_empty_addresseaddr_action_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eaddr_action_eaddr_empty_address_c'


class EaddrEmptyAddress(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    type_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eaddr_empty_address'


class EaddrEmptyAddressAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    eaddr_empty_address_accountseaddr_empty_address_ida = models.CharField(max_length=36, blank=True, null=True)
    eaddr_empty_address_accountsaccounts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eaddr_empty_address_accounts_c'


class EaddrEmptyAddressAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eaddr_empty_address_audit'


class Eapm(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    application = models.CharField(max_length=100, blank=True, null=True)
    api_data = models.TextField(blank=True, null=True)
    consumer_key = models.CharField(max_length=255, blank=True, null=True)
    consumer_secret = models.CharField(max_length=255, blank=True, null=True)
    oauth_token = models.CharField(max_length=255, blank=True, null=True)
    oauth_secret = models.CharField(max_length=255, blank=True, null=True)
    validated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eapm'


class EmElectricMeters(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_install = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'em_electric_meters'


class EmElectricMetersAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'em_electric_meters_audit'


class EmElectricMetersEmMetersDataC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    em_electric_meters_em_meters_dataem_electric_meters_ida = models.CharField(max_length=36, blank=True, null=True)
    em_electric_meters_em_meters_dataem_meters_data_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'em_electric_meters_em_meters_data_c'


class EmMetersData(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    date_meters_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'em_meters_data'


class EmMetersDataAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'em_meters_data_audit'


class EmailAddrBeanRel(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    email_address_id = models.CharField(max_length=36)
    bean_id = models.CharField(max_length=36)
    bean_module = models.CharField(max_length=100, blank=True, null=True)
    primary_address = models.IntegerField(blank=True, null=True)
    reply_to_address = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_addr_bean_rel'


class EmailAddresses(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    email_address_caps = models.CharField(max_length=255, blank=True, null=True)
    invalid_email = models.IntegerField(blank=True, null=True)
    opt_out = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_addresses'


class EmailCache(models.Model):
    ie_id = models.CharField(max_length=36, blank=True, null=True)
    mbox = models.CharField(max_length=60, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    fromaddr = models.CharField(max_length=100, blank=True, null=True)
    toaddr = models.CharField(max_length=255, blank=True, null=True)
    senddate = models.DateTimeField(blank=True, null=True)
    message_id = models.CharField(max_length=255, blank=True, null=True)
    mailsize = models.PositiveIntegerField(blank=True, null=True)
    imap_uid = models.PositiveIntegerField(blank=True, null=True)
    msgno = models.PositiveIntegerField(blank=True, null=True)
    recent = models.IntegerField(blank=True, null=True)
    flagged = models.IntegerField(blank=True, null=True)
    answered = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    seen = models.IntegerField(blank=True, null=True)
    draft = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_cache'


class EmailMarketing(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    from_name = models.CharField(max_length=100, blank=True, null=True)
    from_addr = models.CharField(max_length=100, blank=True, null=True)
    reply_to_name = models.CharField(max_length=100, blank=True, null=True)
    reply_to_addr = models.CharField(max_length=100, blank=True, null=True)
    inbound_email_id = models.CharField(max_length=36, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    template_id = models.CharField(max_length=36)
    status = models.CharField(max_length=100, blank=True, null=True)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)
    all_prospect_lists = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_marketing'


class EmailMarketingProspectLists(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    prospect_list_id = models.CharField(max_length=36, blank=True, null=True)
    email_marketing_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_marketing_prospect_lists'


class EmailTemplates(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    published = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    text_only = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates'


class Emailman(models.Model):
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)
    marketing_id = models.CharField(max_length=36, blank=True, null=True)
    list_id = models.CharField(max_length=36, blank=True, null=True)
    send_date_time = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    in_queue = models.IntegerField(blank=True, null=True)
    in_queue_date = models.DateTimeField(blank=True, null=True)
    send_attempts = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    related_id = models.CharField(max_length=36, blank=True, null=True)
    related_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emailman'


class Emails(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    message_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    flagged = models.IntegerField(blank=True, null=True)
    reply_to_status = models.IntegerField(blank=True, null=True)
    intent = models.CharField(max_length=100, blank=True, null=True)
    mailbox_id = models.CharField(max_length=36, blank=True, null=True)
    parent_type = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emails'


class EmailsBeans(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    email_id = models.CharField(max_length=36, blank=True, null=True)
    bean_id = models.CharField(max_length=36, blank=True, null=True)
    bean_module = models.CharField(max_length=100, blank=True, null=True)
    campaign_data = models.TextField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emails_beans'


class EmailsEmailAddrRel(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    email_id = models.CharField(max_length=36)
    address_type = models.CharField(max_length=4, blank=True, null=True)
    email_address_id = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emails_email_addr_rel'


class EmailsText(models.Model):
    email_id = models.CharField(primary_key=True, max_length=36)
    from_addr = models.CharField(max_length=255, blank=True, null=True)
    reply_to_addr = models.CharField(max_length=255, blank=True, null=True)
    to_addrs = models.TextField(blank=True, null=True)
    cc_addrs = models.TextField(blank=True, null=True)
    bcc_addrs = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_html = models.TextField(blank=True, null=True)
    raw_source = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emails_text'


class EqPickupeq(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    list = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    requestdate = models.DateField(blank=True, null=True)
    performdate = models.DateField(blank=True, null=True)
    account_id_c = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eq_pickupeq'


class EqPickupeqAccFacilityC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    eq_pickupeq_acc_facilityeq_pickupeq_ida = models.CharField(max_length=36, blank=True, null=True)
    eq_pickupeq_acc_facilityacc_facility_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eq_pickupeq_acc_facility_c'


class EqPickupeqAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eq_pickupeq_audit'


class EqPickupeqContactsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    eq_pickupeq_contactseq_pickupeq_ida = models.CharField(max_length=36, blank=True, null=True)
    eq_pickupeq_contactscontacts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eq_pickupeq_contacts_c'


class EqPickupeqNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    eq_pickupeq_noteseq_pickupeq_ida = models.CharField(max_length=36, blank=True, null=True)
    eq_pickupeq_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eq_pickupeq_notes_c'


class FieldsMetaData(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    vname = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    help = models.CharField(max_length=255, blank=True, null=True)
    custom_module = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    len = models.IntegerField(blank=True, null=True)
    required = models.IntegerField(blank=True, null=True)
    default_value = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    audited = models.IntegerField(blank=True, null=True)
    massupdate = models.IntegerField(blank=True, null=True)
    duplicate_merge = models.SmallIntegerField(blank=True, null=True)
    reportable = models.IntegerField(blank=True, null=True)
    importable = models.CharField(max_length=255, blank=True, null=True)
    ext1 = models.CharField(max_length=255, blank=True, null=True)
    ext2 = models.CharField(max_length=255, blank=True, null=True)
    ext3 = models.CharField(max_length=255, blank=True, null=True)
    ext4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fields_meta_data'


class Folders(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=25, blank=True, null=True)
    folder_type = models.CharField(max_length=25, blank=True, null=True)
    parent_folder = models.CharField(max_length=36, blank=True, null=True)
    has_child = models.IntegerField(blank=True, null=True)
    is_group = models.IntegerField(blank=True, null=True)
    is_dynamic = models.IntegerField(blank=True, null=True)
    dynamic_query = models.TextField(blank=True, null=True)
    assign_to_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36)
    modified_by = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'folders'


class FoldersRel(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    folder_id = models.CharField(max_length=36)
    polymorphic_module = models.CharField(max_length=25, blank=True, null=True)
    polymorphic_id = models.CharField(max_length=36)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'folders_rel'


class FoldersSubscriptions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    folder_id = models.CharField(max_length=36)
    assigned_user_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'folders_subscriptions'


class ImportMaps(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=254, blank=True, null=True)
    source = models.CharField(max_length=36, blank=True, null=True)
    enclosure = models.CharField(max_length=1, blank=True, null=True)
    delimiter = models.CharField(max_length=1, blank=True, null=True)
    module = models.CharField(max_length=36, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    default_values = models.TextField(blank=True, null=True)
    has_header = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    is_published = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_maps'


class InboundEmail(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    server_url = models.CharField(max_length=100, blank=True, null=True)
    email_user = models.CharField(max_length=100, blank=True, null=True)
    email_password = models.CharField(max_length=100, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    service = models.CharField(max_length=50, blank=True, null=True)
    mailbox = models.TextField(blank=True, null=True)
    delete_seen = models.IntegerField(blank=True, null=True)
    mailbox_type = models.CharField(max_length=10, blank=True, null=True)
    template_id = models.CharField(max_length=36, blank=True, null=True)
    stored_options = models.TextField(blank=True, null=True)
    group_id = models.CharField(max_length=36, blank=True, null=True)
    is_personal = models.IntegerField(blank=True, null=True)
    groupfolder_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inbound_email'


class InboundEmailAutoreply(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    autoreplied_to = models.CharField(max_length=100, blank=True, null=True)
    ie_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'inbound_email_autoreply'


class InboundEmailCacheTs(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    ie_timestamp = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inbound_email_cache_ts'


class InstComments(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_comments'


class InstCommentsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_comments_audit'


class InstCommentsInstPlanC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    inst_comments_inst_planinst_comments_ida = models.CharField(max_length=36, blank=True, null=True)
    inst_comments_inst_planinst_plan_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_comments_inst_plan_c'


class InstPlan(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    actual_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)
    tu = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    account_id_c = models.CharField(max_length=36, blank=True, null=True)
    reservation_time = models.CharField(max_length=255, blank=True, null=True)
    date_work = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_plan'


class InstPlanAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    inst_plan_accountsinst_plan_ida = models.CharField(max_length=36, blank=True, null=True)
    inst_plan_accountsaccounts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_plan_accounts_c'


class InstPlanAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_plan_audit'


class InstPlanContactsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    inst_plan_contactsinst_plan_ida = models.CharField(max_length=36, blank=True, null=True)
    inst_plan_contactscontacts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_plan_contacts_c'


class InstPlanNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    inst_plan_notesinst_plan_ida = models.CharField(max_length=36, blank=True, null=True)
    inst_plan_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_plan_notes_c'


class InstPlanPhysiPhisicC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    inst_plan_physi_phisicinst_plan_ida = models.CharField(max_length=36, blank=True, null=True)
    inst_plan_physi_phisicphysi_phisic_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_plan_physi_phisic_c'


class InstPlanRaSurveyC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    inst_plan_ra_surveyinst_plan_ida = models.CharField(max_length=36, blank=True, null=True)
    inst_plan_ra_surveyra_survey_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inst_plan_ra_survey_c'


class JjwgAddressCache(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_address_cache'


class JjwgAddressCacheAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_address_cache_audit'


class JjwgAreas(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    coordinates = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_areas'


class JjwgAreasAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_areas_audit'


class JjwgMaps(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    unit_type = models.CharField(max_length=100, blank=True, null=True)
    module_type = models.CharField(max_length=100, blank=True, null=True)
    parent_type = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_maps'


class JjwgMapsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_maps_audit'


class JjwgMapsJjwgAreasC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    jjwg_maps_5304wg_maps_ida = models.CharField(max_length=36, blank=True, null=True)
    jjwg_maps_41f2g_areas_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_maps_jjwg_areas_c'


class JjwgMapsJjwgMarkersC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    jjwg_maps_b229wg_maps_ida = models.CharField(max_length=36, blank=True, null=True)
    jjwg_maps_2e31markers_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_maps_jjwg_markers_c'


class JjwgMarkers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_lat = models.FloatField(blank=True, null=True)
    jjwg_maps_lng = models.FloatField(blank=True, null=True)
    marker_image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_markers'


class JjwgMarkersAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_markers_audit'


class JjwgMarkersRaSurvey1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    jjwg_markers_ra_survey_1jjwg_markers_ida = models.CharField(max_length=36, blank=True, null=True)
    jjwg_markers_ra_survey_1ra_survey_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjwg_markers_ra_survey_1_c'


class JobQueue(models.Model):
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    scheduler_id = models.CharField(max_length=36, blank=True, null=True)
    execute_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    resolution = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    requeue = models.IntegerField(blank=True, null=True)
    retry_count = models.IntegerField(blank=True, null=True)
    failure_count = models.IntegerField(blank=True, null=True)
    job_delay = models.IntegerField(blank=True, null=True)
    client = models.CharField(max_length=255, blank=True, null=True)
    percent_complete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_queue'


class Leads(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    salutation = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    do_not_call = models.IntegerField(blank=True, null=True)
    phone_home = models.CharField(max_length=100, blank=True, null=True)
    phone_mobile = models.CharField(max_length=100, blank=True, null=True)
    phone_work = models.CharField(max_length=100, blank=True, null=True)
    phone_other = models.CharField(max_length=100, blank=True, null=True)
    phone_fax = models.CharField(max_length=100, blank=True, null=True)
    primary_address_street = models.CharField(max_length=150, blank=True, null=True)
    primary_address_city = models.CharField(max_length=100, blank=True, null=True)
    primary_address_state = models.CharField(max_length=100, blank=True, null=True)
    primary_address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    primary_address_country = models.CharField(max_length=255, blank=True, null=True)
    alt_address_street = models.CharField(max_length=150, blank=True, null=True)
    alt_address_city = models.CharField(max_length=100, blank=True, null=True)
    alt_address_state = models.CharField(max_length=100, blank=True, null=True)
    alt_address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    alt_address_country = models.CharField(max_length=255, blank=True, null=True)
    assistant = models.CharField(max_length=75, blank=True, null=True)
    assistant_phone = models.CharField(max_length=100, blank=True, null=True)
    converted = models.IntegerField(blank=True, null=True)
    refered_by = models.CharField(max_length=100, blank=True, null=True)
    lead_source = models.CharField(max_length=100, blank=True, null=True)
    lead_source_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    status_description = models.TextField(blank=True, null=True)
    reports_to_id = models.CharField(max_length=36, blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_description = models.TextField(blank=True, null=True)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    account_id = models.CharField(max_length=36, blank=True, null=True)
    opportunity_id = models.CharField(max_length=36, blank=True, null=True)
    opportunity_name = models.CharField(max_length=255, blank=True, null=True)
    opportunity_amount = models.CharField(max_length=50, blank=True, null=True)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    portal_name = models.CharField(max_length=255, blank=True, null=True)
    portal_app = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'


class LeadsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads_audit'


class LeadsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    jjwg_maps_lng_c = models.FloatField(blank=True, null=True)
    jjwg_maps_lat_c = models.FloatField(blank=True, null=True)
    jjwg_maps_geocode_status_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_address_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads_cstm'


class LetLetters(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    inputnumber = models.CharField(max_length=255, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    outputnumber = models.CharField(max_length=255, blank=True, null=True)
    outputdate = models.DateField(blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    let_to = models.CharField(max_length=255, blank=True, null=True)
    let_from = models.CharField(max_length=255, blank=True, null=True)
    typeletters = models.CharField(max_length=100, blank=True, null=True)
    performer = models.CharField(max_length=255, blank=True, null=True)
    file_mime_type = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'let_letters'


class LetLettersAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    let_letters_accountslet_letters_ida = models.CharField(max_length=36, blank=True, null=True)
    let_letters_accountsaccounts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'let_letters_accounts_c'


class LetLettersAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'let_letters_audit'


class LetLettersContactsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    let_letters_contactslet_letters_ida = models.CharField(max_length=36, blank=True, null=True)
    let_letters_contactscontacts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'let_letters_contacts_c'


class LetLettersCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    number_kor_c = models.IntegerField(blank=True, null=True)
    number_kor_new_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'let_letters_cstm'


class LetLettersNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    let_letters_noteslet_letters_ida = models.CharField(max_length=36, blank=True, null=True)
    let_letters_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'let_letters_notes_c'


class LinkedDocuments(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36, blank=True, null=True)
    parent_type = models.CharField(max_length=25, blank=True, null=True)
    document_id = models.CharField(max_length=36, blank=True, null=True)
    document_revision_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linked_documents'


class MaMount(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    document_name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    file_ext = models.CharField(max_length=100, blank=True, null=True)
    file_mime_type = models.CharField(max_length=100, blank=True, null=True)
    active_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    category_id = models.CharField(max_length=100, blank=True, null=True)
    subcategory_id = models.CharField(max_length=100, blank=True, null=True)
    status_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ma_mount'


class MaMountAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ma_mount_audit'


class MaMountConPConnectionsPlan1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ma_mount_con_p_connections_plan_1ma_mount_ida = models.CharField(max_length=36, blank=True, null=True)
    ma_mount_con_p_connections_plan_1con_p_connections_plan_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ma_mount_con_p_connections_plan_1_c'


class MaMountCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    address_mount_c = models.CharField(max_length=255, blank=True, null=True)
    contact_mount_c = models.CharField(max_length=255, blank=True, null=True)
    level_signal_mount_c = models.CharField(max_length=255, blank=True, null=True)
    mount_photo_c = models.CharField(max_length=255, blank=True, null=True)
    mount_photo_1_c = models.CharField(max_length=255, blank=True, null=True)
    mount_photo_2_c = models.CharField(max_length=255, blank=True, null=True)
    mount_photo_3_c = models.CharField(max_length=255, blank=True, null=True)
    con_p_connections_plan_id_c = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ma_mount_cstm'


class MaMountPoPo1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ma_mount_po_po_1ma_mount_ida = models.CharField(max_length=36, blank=True, null=True)
    ma_mount_po_po_1po_po_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ma_mount_po_po_1_c'


class Meetings(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    join_url = models.CharField(max_length=200, blank=True, null=True)
    host_url = models.CharField(max_length=400, blank=True, null=True)
    displayed_url = models.CharField(max_length=400, blank=True, null=True)
    creator = models.CharField(max_length=50, blank=True, null=True)
    external_id = models.CharField(max_length=50, blank=True, null=True)
    duration_hours = models.IntegerField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    parent_type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)
    reminder_time = models.IntegerField(blank=True, null=True)
    email_reminder_time = models.IntegerField(blank=True, null=True)
    email_reminder_sent = models.IntegerField(blank=True, null=True)
    outlook_id = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    repeat_type = models.CharField(max_length=36, blank=True, null=True)
    repeat_interval = models.IntegerField(blank=True, null=True)
    repeat_dow = models.CharField(max_length=7, blank=True, null=True)
    repeat_until = models.DateField(blank=True, null=True)
    repeat_count = models.IntegerField(blank=True, null=True)
    repeat_parent_id = models.CharField(max_length=36, blank=True, null=True)
    recurring_source = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings'


class MeetingsContacts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    meeting_id = models.CharField(max_length=36, blank=True, null=True)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    accept_status = models.CharField(max_length=25, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings_contacts'


class MeetingsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    jjwg_maps_lng_c = models.FloatField(blank=True, null=True)
    jjwg_maps_lat_c = models.FloatField(blank=True, null=True)
    jjwg_maps_geocode_status_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_address_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings_cstm'


class MeetingsLeads(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    meeting_id = models.CharField(max_length=36, blank=True, null=True)
    lead_id = models.CharField(max_length=36, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    accept_status = models.CharField(max_length=25, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings_leads'


class MeetingsUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    meeting_id = models.CharField(max_length=36, blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    required = models.CharField(max_length=1, blank=True, null=True)
    accept_status = models.CharField(max_length=25, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings_users'


class NodeNode(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_node'


class NodeNodeAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_node_audit'


class NodeNodeDocumentsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    node_node_documentsnode_node_ida = models.CharField(max_length=36, blank=True, null=True)
    node_node_documentsdocuments_idb = models.CharField(max_length=36, blank=True, null=True)
    document_revision_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_node_documents_c'


class NodeNodeNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    node_node_notesnode_node_ida = models.CharField(max_length=36, blank=True, null=True)
    node_node_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_node_notes_c'


class NodeNodeProjectC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    node_node_projectnode_node_ida = models.CharField(max_length=36, blank=True, null=True)
    node_node_projectproject_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_node_project_c'


class NodeNodeTasksC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    node_node_tasksnode_node_ida = models.CharField(max_length=36, blank=True, null=True)
    node_node_taskstasks_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_node_tasks_c'


class Notes(models.Model):
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    file_mime_type = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    parent_type = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    portal_flag = models.IntegerField(blank=True, null=True)
    embed_flag = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'


class NotesCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    peeve_c = models.IntegerField(blank=True, null=True)
    move_c = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes_cstm'


class OauthConsumer(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    c_key = models.CharField(unique=True, max_length=255, blank=True, null=True)
    c_secret = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_consumer'


class OauthNonce(models.Model):
    conskey = models.CharField(primary_key=True, max_length=32)
    nonce = models.CharField(max_length=32)
    nonce_ts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_nonce'
        unique_together = (('conskey', 'nonce'),)


class OauthTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    secret = models.CharField(max_length=32, blank=True, null=True)
    tstate = models.CharField(max_length=1, blank=True, null=True)
    consumer = models.CharField(max_length=36)
    token_ts = models.BigIntegerField(blank=True, null=True)
    verify = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.IntegerField()
    callback_url = models.CharField(max_length=255, blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_tokens'
        unique_together = (('id', 'deleted'),)


class ObjNNetObj(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj'


class ObjNNetObjAccounts1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    obj_n_net_obj_accounts_1obj_n_net_obj_ida = models.CharField(max_length=36, blank=True, null=True)
    obj_n_net_obj_accounts_1accounts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj_accounts_1_c'


class ObjNNetObjAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj_audit'


class ObjNNetObjCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    num_obj_c = models.IntegerField(blank=True, null=True)
    address_obj_c = models.CharField(max_length=255, blank=True, null=True)
    photo_obj_c = models.CharField(max_length=255, blank=True, null=True)
    address_map_obj_c = models.CharField(max_length=255, blank=True, null=True)
    photo_obj2_c = models.CharField(max_length=255, blank=True, null=True)
    photo_obj3_c = models.CharField(max_length=255, blank=True, null=True)
    photo_obj4_c = models.CharField(max_length=255, blank=True, null=True)
    photo_obj5_c = models.CharField(max_length=255, blank=True, null=True)
    photo_obj6_c = models.CharField(max_length=255, blank=True, null=True)
    devices_for_audit_c = models.TextField(blank=True, null=True)
    status_obj_c = models.CharField(max_length=100, blank=True, null=True)
    photo_others_c = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj_cstm'


class ObjNNetObjDocuments1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    obj_n_net_obj_documents_1obj_n_net_obj_ida = models.CharField(max_length=36, blank=True, null=True)
    obj_n_net_obj_documents_1documents_idb = models.CharField(max_length=36, blank=True, null=True)
    document_revision_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj_documents_1_c'


class ObjNNetObjPoPo1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    obj_n_net_obj_po_po_1obj_n_net_obj_ida = models.CharField(max_length=36, blank=True, null=True)
    obj_n_net_obj_po_po_1po_po_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj_po_po_1_c'


class ObjNNetObjRaActions1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    obj_n_net_obj_ra_actions_1obj_n_net_obj_ida = models.CharField(max_length=36, blank=True, null=True)
    obj_n_net_obj_ra_actions_1ra_actions_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj_ra_actions_1_c'


class ObjNNetObjRaClaim1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    obj_n_net_obj_ra_claim_1obj_n_net_obj_ida = models.CharField(max_length=36, blank=True, null=True)
    obj_n_net_obj_ra_claim_1ra_claim_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj_ra_claim_1_c'


class ObjNNetObjSecuritygroups1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    obj_n_net_obj_securitygroups_1obj_n_net_obj_ida = models.CharField(max_length=36, blank=True, null=True)
    obj_n_net_obj_securitygroups_1securitygroups_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obj_n_net_obj_securitygroups_1_c'


class Opportunities(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    opportunity_type = models.CharField(max_length=255, blank=True, null=True)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)
    lead_source = models.CharField(max_length=100, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amount_usdollar = models.FloatField(blank=True, null=True)
    currency_id = models.CharField(max_length=36, blank=True, null=True)
    date_closed = models.DateField(blank=True, null=True)
    next_step = models.CharField(max_length=100, blank=True, null=True)
    sales_stage = models.CharField(max_length=255, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opportunities'


class OpportunitiesAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opportunities_audit'


class OpportunitiesContacts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    opportunity_id = models.CharField(max_length=36, blank=True, null=True)
    contact_role = models.CharField(max_length=50, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opportunities_contacts'


class OpportunitiesCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    wifi_bandwidth_opp_c = models.IntegerField(blank=True, null=True)
    internet_opp_c = models.IntegerField(blank=True, null=True)
    opp_date_opp_c = models.DateField(blank=True, null=True)
    phone_opp_c = models.IntegerField(blank=True, null=True)
    pdcpgi_opp_c = models.IntegerField(blank=True, null=True)
    pvk_opp_c = models.IntegerField(blank=True, null=True)
    inet_bandwidth_opp_c = models.FloatField(blank=True, null=True)
    packet_opp_c = models.IntegerField(blank=True, null=True)
    vats_opp_c = models.IntegerField(blank=True, null=True)
    tv_opp_c = models.IntegerField(blank=True, null=True)
    cctv_opp_c = models.IntegerField(blank=True, null=True)
    ip_cost_opp_c = models.IntegerField(blank=True, null=True)
    closed_opp_c = models.IntegerField(blank=True, null=True)
    blockletter_opp_c = models.IntegerField(blank=True, null=True)
    date_blockletter_opp_c = models.DateField(blank=True, null=True)
    close_date_c = models.DateField(blank=True, null=True)
    date_apply_c = models.DateField(blank=True, null=True)
    organization_opp_c = models.CharField(max_length=100, blank=True, null=True)
    code_fineko_c = models.IntegerField(blank=True, null=True)
    type_cost_opp_c = models.CharField(max_length=100, blank=True, null=True)
    billing_id_opp_c = models.IntegerField(blank=True, null=True)
    cost_pdcpgi_opp_c = models.IntegerField(blank=True, null=True)
    quantity_phone_lines_c = models.IntegerField(blank=True, null=True)
    jjwg_maps_lng_c = models.FloatField(blank=True, null=True)
    jjwg_maps_lat_c = models.FloatField(blank=True, null=True)
    jjwg_maps_geocode_status_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_address_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opportunities_cstm'


class OutboundEmail(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    user_id = models.CharField(max_length=36)
    mail_sendtype = models.CharField(max_length=8, blank=True, null=True)
    mail_smtptype = models.CharField(max_length=20, blank=True, null=True)
    mail_smtpserver = models.CharField(max_length=100, blank=True, null=True)
    mail_smtpport = models.IntegerField(blank=True, null=True)
    mail_smtpuser = models.CharField(max_length=100, blank=True, null=True)
    mail_smtppass = models.CharField(max_length=100, blank=True, null=True)
    mail_smtpauth_req = models.IntegerField(blank=True, null=True)
    mail_smtpssl = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outbound_email'


class PaPlanAccess(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    date_plan = models.DateField(blank=True, null=True)
    date_complete = models.DateField(blank=True, null=True)
    status_plan_access = models.CharField(max_length=100, blank=True, null=True)
    type_plan_access = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_plan_access'


class PaPlanAccessAccFacilityC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    pa_plan_access_acc_facilitypa_plan_access_ida = models.CharField(max_length=36, blank=True, null=True)
    pa_plan_access_acc_facilityacc_facility_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_plan_access_acc_facility_c'


class PaPlanAccessAccRequisitionC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    pa_plan_access_acc_requisitionpa_plan_access_ida = models.CharField(max_length=36, blank=True, null=True)
    pa_plan_access_acc_requisitionacc_requisition_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_plan_access_acc_requisition_c'


class PaPlanAccessAccUkC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    pa_plan_access_acc_ukpa_plan_access_ida = models.CharField(max_length=36, blank=True, null=True)
    pa_plan_access_acc_ukacc_uk_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_plan_access_acc_uk_c'


class PaPlanAccessAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_plan_access_audit'


class PaPlanAccessCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    type_request_c = models.CharField(max_length=100, blank=True, null=True)
    area_c = models.CharField(max_length=255, blank=True, null=True)
    type_account_c = models.CharField(max_length=100, blank=True, null=True)
    acc_uk_id_c = models.CharField(max_length=36, blank=True, null=True)
    acc_requisition_id_c = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_plan_access_cstm'


class PaPlanAccessNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    pa_plan_access_notespa_plan_access_ida = models.CharField(max_length=36, blank=True, null=True)
    pa_plan_access_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_plan_access_notes_c'


class PhmoPhoto(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    document_name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    file_ext = models.CharField(max_length=100, blank=True, null=True)
    file_mime_type = models.CharField(max_length=100, blank=True, null=True)
    active_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    category_id = models.CharField(max_length=100, blank=True, null=True)
    subcategory_id = models.CharField(max_length=100, blank=True, null=True)
    status_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phmo_photo'


class PhmoPhotoAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phmo_photo_audit'


class PhmoPhotoCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    photo_ph_mounts_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phmo_photo_cstm'


class PhysiCasesP(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    case_numb = models.IntegerField(blank=True, null=True)
    date_case = models.DateTimeField(blank=True, null=True)
    date_close = models.DateTimeField(blank=True, null=True)
    resolution = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=100, blank=True, null=True)
    physi_phisic_id_c = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_cases_p'


class PhysiCasesPAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_cases_p_audit'


class PhysiCasesPNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    physi_cases_p_notesphysi_cases_p_ida = models.CharField(max_length=36, blank=True, null=True)
    physi_cases_p_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_cases_p_notes_c'


class PhysiContractNetwork(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    date_contr = models.DateField(blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    bandwidth = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    block = models.IntegerField(blank=True, null=True)
    tarif = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_contract_network'


class PhysiContractNetworkAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_contract_network_audit'


class PhysiContractNetworkNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    physi_contract_network_notesphysi_contract_network_ida = models.CharField(max_length=36, blank=True, null=True)
    physi_contract_network_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_contract_network_notes_c'


class PhysiContractPhone(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    date_contr = models.DateField(blank=True, null=True)
    cost = models.CharField(max_length=255, blank=True, null=True)
    tarif = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_contract_phone'


class PhysiContractPhoneAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_contract_phone_audit'


class PhysiContractPhoneNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    physi_contract_phone_notesphysi_contract_phone_ida = models.CharField(max_length=36, blank=True, null=True)
    physi_contract_phone_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_contract_phone_notes_c'


class PhysiPhisic(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    serial_passport = models.CharField(max_length=5, blank=True, null=True)
    number_passport = models.CharField(max_length=6, blank=True, null=True)
    issue_passport = models.CharField(max_length=255, blank=True, null=True)
    date_passport = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_phisic'


class PhysiPhisicAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_phisic_audit'


class PhysiPhisicCallsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    physi_phisic_callsphysi_phisic_ida = models.CharField(max_length=36, blank=True, null=True)
    physi_phisic_callscalls_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_phisic_calls_c'


class PhysiPhisicNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    physi_phisic_notesphysi_phisic_ida = models.CharField(max_length=36, blank=True, null=True)
    physi_phisic_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_phisic_notes_c'


class PhysiPhisicPhysiCasesPC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    physi_phisic_physi_cases_pphysi_phisic_ida = models.CharField(max_length=36, blank=True, null=True)
    physi_phisic_physi_cases_pphysi_cases_p_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_phisic_physi_cases_p_c'


class PhysiPhisicPhysiContractNetworkC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    physi_phisic_physi_contract_networkphysi_phisic_ida = models.CharField(max_length=36, blank=True, null=True)
    physi_phisic_physi_contract_networkphysi_contract_network_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_phisic_physi_contract_network_c'


class PhysiPhisicPhysiContractPhoneC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    physi_phisic_physi_contract_phonephysi_phisic_ida = models.CharField(max_length=36, blank=True, null=True)
    physi_phisic_physi_contract_phonephysi_contract_phone_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_phisic_physi_contract_phone_c'


class PhysiRequest(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    document_name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    file_ext = models.CharField(max_length=100, blank=True, null=True)
    file_mime_type = models.CharField(max_length=100, blank=True, null=True)
    active_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    category_id = models.CharField(max_length=100, blank=True, null=True)
    subcategory_id = models.CharField(max_length=100, blank=True, null=True)
    status_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_request'


class PhysiRequestAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physi_request_audit'


class PoPo(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    parent_type = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_po'


class PoPoAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_po_audit'


class PoPoConPConnectionsPlan1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    po_po_con_p_connections_plan_1po_po_ida = models.CharField(max_length=36, blank=True, null=True)
    po_po_con_p_connections_plan_1con_p_connections_plan_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_po_con_p_connections_plan_1_c'


class PoPoCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    invnum_c = models.CharField(max_length=255, blank=True, null=True)
    status_c = models.CharField(max_length=100, blank=True, null=True)
    hardware_types_c = models.CharField(max_length=100, blank=True, null=True)
    account_id_c = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_po_cstm'


class PoPoNotes1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    po_po_notes_1po_po_ida = models.CharField(max_length=36, blank=True, null=True)
    po_po_notes_1notes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_po_notes_1_c'


class PoPoRepRepairs1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    po_po_rep_repairs_1po_po_ida = models.CharField(max_length=36, blank=True, null=True)
    po_po_rep_repairs_1rep_repairs_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_po_rep_repairs_1_c'


class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    estimated_start_date = models.DateField(blank=True, null=True)
    estimated_end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    date_close_c = models.DateField(blank=True, null=True)
    jjwg_maps_lng_c = models.FloatField(blank=True, null=True)
    jjwg_maps_lat_c = models.FloatField(blank=True, null=True)
    jjwg_maps_geocode_status_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_address_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_cstm'


class ProjectTask(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    project_id = models.CharField(max_length=36)
    project_task_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    predecessors = models.TextField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    time_start = models.IntegerField(blank=True, null=True)
    time_finish = models.IntegerField(blank=True, null=True)
    date_finish = models.DateField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    duration_unit = models.TextField(blank=True, null=True)
    actual_duration = models.IntegerField(blank=True, null=True)
    percent_complete = models.IntegerField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    time_due = models.TimeField(blank=True, null=True)
    parent_task_id = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    milestone_flag = models.IntegerField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    task_number = models.IntegerField(blank=True, null=True)
    estimated_effort = models.IntegerField(blank=True, null=True)
    actual_effort = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    utilization = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task'


class ProjectTaskAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_audit'


class ProjectsAccounts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    account_id = models.CharField(max_length=36, blank=True, null=True)
    project_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_accounts'


class ProjectsBugs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    bug_id = models.CharField(max_length=36, blank=True, null=True)
    project_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_bugs'


class ProjectsCases(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    case_id = models.CharField(max_length=36, blank=True, null=True)
    project_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_cases'


class ProjectsContacts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    project_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_contacts'


class ProjectsOpportunities(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    opportunity_id = models.CharField(max_length=36, blank=True, null=True)
    project_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_opportunities'


class ProjectsProducts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    product_id = models.CharField(max_length=36, blank=True, null=True)
    project_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_products'


class ProjecttaskContacts1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    projecttask_contacts_1projecttask_ida = models.CharField(max_length=36, blank=True, null=True)
    projecttask_contacts_1contacts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projecttask_contacts_1_c'


class ProspectListCampaigns(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    prospect_list_id = models.CharField(max_length=36, blank=True, null=True)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospect_list_campaigns'


class ProspectLists(models.Model):
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=50, blank=True, null=True)
    list_type = models.CharField(max_length=100, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    domain_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospect_lists'


class ProspectListsProspects(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    prospect_list_id = models.CharField(max_length=36, blank=True, null=True)
    related_id = models.CharField(max_length=36, blank=True, null=True)
    related_type = models.CharField(max_length=25, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospect_lists_prospects'


class Prospects(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    salutation = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    do_not_call = models.IntegerField(blank=True, null=True)
    phone_home = models.CharField(max_length=100, blank=True, null=True)
    phone_mobile = models.CharField(max_length=100, blank=True, null=True)
    phone_work = models.CharField(max_length=100, blank=True, null=True)
    phone_other = models.CharField(max_length=100, blank=True, null=True)
    phone_fax = models.CharField(max_length=100, blank=True, null=True)
    primary_address_street = models.CharField(max_length=150, blank=True, null=True)
    primary_address_city = models.CharField(max_length=100, blank=True, null=True)
    primary_address_state = models.CharField(max_length=100, blank=True, null=True)
    primary_address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    primary_address_country = models.CharField(max_length=255, blank=True, null=True)
    alt_address_street = models.CharField(max_length=150, blank=True, null=True)
    alt_address_city = models.CharField(max_length=100, blank=True, null=True)
    alt_address_state = models.CharField(max_length=100, blank=True, null=True)
    alt_address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    alt_address_country = models.CharField(max_length=255, blank=True, null=True)
    assistant = models.CharField(max_length=75, blank=True, null=True)
    assistant_phone = models.CharField(max_length=100, blank=True, null=True)
    tracker_key = models.AutoField()
    birthdate = models.DateField(blank=True, null=True)
    lead_id = models.CharField(max_length=36, blank=True, null=True)
    account_name = models.CharField(max_length=150, blank=True, null=True)
    campaign_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospects'


class ProspectsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    jjwg_maps_lng_c = models.FloatField(blank=True, null=True)
    jjwg_maps_lat_c = models.FloatField(blank=True, null=True)
    jjwg_maps_geocode_status_c = models.CharField(max_length=255, blank=True, null=True)
    jjwg_maps_address_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospects_cstm'


class PurPurchases(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    grouppur = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    date_pur = models.DateField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pur_purchases'


class PurPurchasesAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pur_purchases_audit'


class PurPurchasesNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    pur_purchases_notespur_purchases_ida = models.CharField(max_length=36, blank=True, null=True)
    pur_purchases_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pur_purchases_notes_c'


class QuQuestion(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    user_id_c = models.CharField(max_length=36, blank=True, null=True)
    account_id_c = models.CharField(max_length=36, blank=True, null=True)
    date_question = models.DateField(blank=True, null=True)
    user_accounts = models.CharField(max_length=255, blank=True, null=True)
    service_problem = models.TextField(blank=True, null=True)
    support_calls = models.CharField(max_length=100, blank=True, null=True)
    support = models.CharField(max_length=100, blank=True, null=True)
    install = models.CharField(max_length=100, blank=True, null=True)
    sell = models.CharField(max_length=100, blank=True, null=True)
    quality_client = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qu_question'


class QuQuestionAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    qu_question_accountsqu_question_ida = models.CharField(max_length=36, blank=True, null=True)
    qu_question_accountsaccounts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qu_question_accounts_c'


class QuQuestionAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qu_question_audit'


class RaActions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    planactiondate = models.DateTimeField(blank=True, null=True)
    actiondate = models.DateTimeField(blank=True, null=True)
    planduration = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    noservice = models.IntegerField(blank=True, null=True)
    plannoservice = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    goal = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_actions'


class RaActionsAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_actions_accountsra_actions_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_actions_accountsaccounts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_actions_accounts_c'


class RaActionsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_actions_audit'


class RaActionsCasesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_actions_casesra_actions_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_actions_casescases_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_actions_cases_c'


class RaActionsNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_actions_notesra_actions_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_actions_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_actions_notes_c'


class RaActionsSecuritygroups1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_actions_securitygroups_1ra_actions_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_actions_securitygroups_1securitygroups_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_actions_securitygroups_1_c'


class RaActionsTasksC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_actions_tasksra_actions_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_actions_taskstasks_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_actions_tasks_c'


class RaClaim(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    date_event = models.DateField(blank=True, null=True)
    group_onus = models.CharField(max_length=100, blank=True, null=True)
    volume = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_claim'


class RaClaimAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_claim_audit'


class RaClaimBugs1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_claim_bugs_1ra_claim_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_claim_bugs_1bugs_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_claim_bugs_1_c'


class RaClaimCasesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_claim_casesra_claim_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_claim_casescases_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_claim_cases_c'


class RaClaimNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_claim_notesra_claim_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_claim_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_claim_notes_c'


class RaClaimPhysiCasesPC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_claim_physi_cases_pra_claim_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_claim_physi_cases_pphysi_cases_p_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_claim_physi_cases_p_c'


class RaClaimRaActionsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_claim_ra_actionsra_claim_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_claim_ra_actionsra_actions_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_claim_ra_actions_c'


class RaSurvey(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    description_survey = models.TextField(blank=True, null=True)
    date_request = models.DateField(blank=True, null=True)
    addressmap = models.CharField(max_length=255, blank=True, null=True)
    date_survey = models.DateField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_survey'


class RaSurveyAccRequisition1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_survey_acc_requisition_1ra_survey_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_survey_acc_requisition_1acc_requisition_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_survey_acc_requisition_1_c'


class RaSurveyAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_survey_accountsra_survey_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_survey_accountsaccounts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_survey_accounts_c'


class RaSurveyAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_survey_audit'


class RaSurveyCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    source_inf_c = models.TextField(blank=True, null=True)
    permit_installation_c = models.CharField(max_length=100, blank=True, null=True)
    ess_comment_c = models.TextField(blank=True, null=True)
    date_installation_c = models.DateField(blank=True, null=True)
    position_c = models.CharField(max_length=50, blank=True, null=True)
    maps_pos_c = models.CharField(max_length=255, blank=True, null=True)
    status_rs_c = models.CharField(max_length=100, blank=True, null=True)
    comment_rs_c = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_survey_cstm'


class RaSurveyNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_survey_notesra_survey_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_survey_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_survey_notes_c'


class RaSurveyPhysiPhisicC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    ra_survey_physi_phisicra_survey_ida = models.CharField(max_length=36, blank=True, null=True)
    ra_survey_physi_phisicphysi_phisic_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ra_survey_physi_phisic_c'


class Relationships(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    relationship_name = models.CharField(max_length=150, blank=True, null=True)
    lhs_module = models.CharField(max_length=100, blank=True, null=True)
    lhs_table = models.CharField(max_length=64, blank=True, null=True)
    lhs_key = models.CharField(max_length=64, blank=True, null=True)
    rhs_module = models.CharField(max_length=100, blank=True, null=True)
    rhs_table = models.CharField(max_length=64, blank=True, null=True)
    rhs_key = models.CharField(max_length=64, blank=True, null=True)
    join_table = models.CharField(max_length=128, blank=True, null=True)
    join_key_lhs = models.CharField(max_length=128, blank=True, null=True)
    join_key_rhs = models.CharField(max_length=128, blank=True, null=True)
    relationship_type = models.CharField(max_length=64, blank=True, null=True)
    relationship_role_column = models.CharField(max_length=64, blank=True, null=True)
    relationship_role_column_value = models.CharField(max_length=50, blank=True, null=True)
    reverse = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relationships'


class Releases(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    list_order = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'releases'


class RepRepairs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_repairs'


class RepRepairsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_repairs_audit'


class RepRepairsBugs1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    rep_repairs_bugs_1rep_repairs_ida = models.CharField(max_length=36, blank=True, null=True)
    rep_repairs_bugs_1bugs_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_repairs_bugs_1_c'


class RepRepairsCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    user_id_c = models.CharField(max_length=36, blank=True, null=True)
    user_id1_c = models.CharField(max_length=36, blank=True, null=True)
    date_of_completion_c = models.DateField(blank=True, null=True)
    cat_work_c = models.CharField(max_length=100, blank=True, null=True)
    account_id_c = models.CharField(max_length=36, blank=True, null=True)
    address_c = models.CharField(max_length=255, blank=True, null=True)
    check_ovm_c = models.IntegerField(blank=True, null=True)
    photo_one_c = models.CharField(max_length=255, blank=True, null=True)
    photo_two_c = models.CharField(max_length=255, blank=True, null=True)
    photo_three_c = models.CharField(max_length=255, blank=True, null=True)
    photo_four_c = models.CharField(max_length=255, blank=True, null=True)
    photo_five_c = models.CharField(max_length=255, blank=True, null=True)
    photo_six_c = models.CharField(max_length=255, blank=True, null=True)
    contacts_c = models.CharField(max_length=255, blank=True, null=True)
    time_c = models.CharField(max_length=255, blank=True, null=True)
    user_id2_c = models.CharField(max_length=36, blank=True, null=True)
    status_c = models.CharField(max_length=100, blank=True, null=True)
    comment_c = models.TextField(blank=True, null=True)
    new_cat_work_c = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_repairs_cstm'


class RepRepairsNotes1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    rep_repairs_notes_1rep_repairs_ida = models.CharField(max_length=36, blank=True, null=True)
    rep_repairs_notes_1notes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_repairs_notes_1_c'


class RepTechnicalConnections(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    date_work = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_technical_connections'


class RepTechnicalConnectionsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep_technical_connections_audit'


class Roles(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    modules = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class RolesModules(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    role_id = models.CharField(max_length=36, blank=True, null=True)
    module_id = models.CharField(max_length=36, blank=True, null=True)
    allow = models.IntegerField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_modules'


class RolesUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    role_id = models.CharField(max_length=36, blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_users'


class SavedSearch(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=150, blank=True, null=True)
    search_module = models.CharField(max_length=150, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saved_search'


class Schedulers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    date_time_start = models.DateTimeField(blank=True, null=True)
    date_time_end = models.DateTimeField(blank=True, null=True)
    job_interval = models.CharField(max_length=100, blank=True, null=True)
    time_from = models.TimeField(blank=True, null=True)
    time_to = models.TimeField(blank=True, null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    catch_up = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedulers'


class Securitygroups(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    noninheritable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'securitygroups'


class SecuritygroupsAclRoles(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    securitygroup_id = models.CharField(max_length=36, blank=True, null=True)
    role_id = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'securitygroups_acl_roles'


class SecuritygroupsAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'securitygroups_audit'


class SecuritygroupsDefault(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    securitygroup_id = models.CharField(max_length=36, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'securitygroups_default'


class SecuritygroupsRecords(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    securitygroup_id = models.CharField(max_length=36, blank=True, null=True)
    record_id = models.CharField(max_length=36, blank=True, null=True)
    module = models.CharField(max_length=36, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'securitygroups_records'


class SecuritygroupsUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    securitygroup_id = models.CharField(max_length=36, blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    noninheritable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'securitygroups_users'


class SkSketch(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    document_name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    file_ext = models.CharField(max_length=100, blank=True, null=True)
    file_mime_type = models.CharField(max_length=100, blank=True, null=True)
    active_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    category_id = models.CharField(max_length=100, blank=True, null=True)
    subcategory_id = models.CharField(max_length=100, blank=True, null=True)
    status_id = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    status_requisition = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sk_sketch'


class SkSketchAccRequisitionC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    sk_sketch_acc_requisitionsk_sketch_ida = models.CharField(max_length=36, blank=True, null=True)
    sk_sketch_acc_requisitionacc_requisition_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sk_sketch_acc_requisition_c'


class SkSketchAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sk_sketch_audit'


class SkSketchRaSurveyC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    sk_sketch_ra_surveysk_sketch_ida = models.CharField(max_length=36, blank=True, null=True)
    sk_sketch_ra_surveyra_survey_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sk_sketch_ra_survey_c'


class Sugarfeed(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    related_module = models.CharField(max_length=100, blank=True, null=True)
    related_id = models.CharField(max_length=36, blank=True, null=True)
    link_url = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sugarfeed'


class Tasks(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    date_due_flag = models.IntegerField(blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    date_start_flag = models.IntegerField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    parent_type = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.CharField(max_length=36, blank=True, null=True)
    contact_id = models.CharField(max_length=36, blank=True, null=True)
    priority = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class TasksAccounts1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tasks_accounts_1tasks_ida = models.CharField(max_length=36, blank=True, null=True)
    tasks_accounts_1accounts_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks_accounts_1_c'


class TasksCalls1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tasks_calls_1tasks_ida = models.CharField(max_length=36, blank=True, null=True)
    tasks_calls_1calls_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks_calls_1_c'


class TcClosecontract(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    dateclose = models.DateField(blank=True, null=True)
    dateperform = models.DateField(blank=True, null=True)
    user_id_c = models.CharField(max_length=36, blank=True, null=True)
    opportunity_id_c = models.CharField(max_length=36, blank=True, null=True)
    note_id_c = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_closecontract'


class TcClosecontractAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_closecontract_audit'


class TcClosecontractNotesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_closecontract_notestc_closecontract_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_closecontract_notesnotes_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_closecontract_notes_c'


class TcRenamecontract(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    daterename = models.DateField(blank=True, null=True)
    dateperform = models.DateField(blank=True, null=True)
    user_id_c = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract'


class TcRenamecontractAccounts1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_renamecontract_accounts_1accounts_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_renamecontract_accounts_1tc_renamecontract_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract_accounts_1_c'


class TcRenamecontractAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_renamecontract_accountsaccounts_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_renamecontract_accountstc_renamecontract_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract_accounts_c'


class TcRenamecontractAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract_audit'


class TcRenamecontractCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    status_c = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract_cstm'


class TcRenamecontractOpportunities1C(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_renamecontract_opportunities_1opportunities_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_renamecontract_opportunities_1tc_renamecontract_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract_opportunities_1_c'


class TcRenamecontractOpportunitiesC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_renamecontract_opportunitiesopportunities_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_renamecontract_opportunitiestc_renamecontract_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract_opportunities_c'


class TcRenamecontractTcTarifchangephoneC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_renamecontract_tc_tarifchangephonetc_renamecontract_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_renamecontract_tc_tarifchangephonetc_tarifchangephone_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract_tc_tarifchangephone_c'


class TcRenamecontractTcTariffchangeinetC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_renamecontract_tc_tariffchangeinettc_renamecontract_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_renamecontract_tc_tariffchangeinettc_tariffchangeinet_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_renamecontract_tc_tariffchangeinet_c'


class TcTarifchangephone(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    datechange = models.DateField(blank=True, null=True)
    dateperform = models.DateField(blank=True, null=True)
    user_id_c = models.CharField(max_length=36, blank=True, null=True)
    oldservice = models.TextField(blank=True, null=True)
    newservice = models.TextField(blank=True, null=True)
    opportunity_id_c = models.CharField(max_length=36, blank=True, null=True)
    opportunity_id1_c = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_tarifchangephone'


class TcTarifchangephoneAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_tarifchangephone_accountsaccounts_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_tarifchangephone_accountstc_tarifchangephone_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_tarifchangephone_accounts_c'


class TcTarifchangephoneAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_tarifchangephone_audit'


class TcTarifchangephoneCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    status_c = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_tarifchangephone_cstm'


class TcTariffchangeinet(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    oldbandwith = models.FloatField(blank=True, null=True)
    newbandwith = models.FloatField(blank=True, null=True)
    oldcost = models.IntegerField(blank=True, null=True)
    newcost = models.IntegerField(blank=True, null=True)
    datechange = models.DateField(blank=True, null=True)
    daterealchange = models.DateField(blank=True, null=True)
    checked = models.IntegerField(blank=True, null=True)
    datechecked = models.DateField(blank=True, null=True)
    user_id_c = models.CharField(max_length=36, blank=True, null=True)
    opportunity_id_c = models.CharField(max_length=36, blank=True, null=True)
    opportunity_id1_c = models.CharField(max_length=36, blank=True, null=True)
    checkcomment = models.TextField(blank=True, null=True)
    user_id1_c = models.CharField(max_length=36, blank=True, null=True)
    oldlimit = models.IntegerField(blank=True, null=True)
    newlimit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_tariffchangeinet'


class TcTariffchangeinetAccountsC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    tc_tariffchangeinet_accountsaccounts_ida = models.CharField(max_length=36, blank=True, null=True)
    tc_tariffchangeinet_accountstc_tariffchangeinet_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_tariffchangeinet_accounts_c'


class TcTariffchangeinetAudit(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    parent_id = models.CharField(max_length=36)
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)
    before_value_string = models.CharField(max_length=255, blank=True, null=True)
    after_value_string = models.CharField(max_length=255, blank=True, null=True)
    before_value_text = models.TextField(blank=True, null=True)
    after_value_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_tariffchangeinet_audit'


class TcTariffchangeinetCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    status_c = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_tariffchangeinet_cstm'


class Tracker(models.Model):
    monitor_id = models.CharField(max_length=36)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    module_name = models.CharField(max_length=255, blank=True, null=True)
    item_id = models.CharField(max_length=36, blank=True, null=True)
    item_summary = models.CharField(max_length=255, blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    session_id = models.CharField(max_length=36, blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracker'


class UpgradeHistory(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    filename = models.CharField(max_length=255, blank=True, null=True)
    md5sum = models.CharField(unique=True, max_length=32, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id_name = models.CharField(max_length=255, blank=True, null=True)
    manifest = models.TextField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upgrade_history'


class UserPreferences(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    category = models.CharField(max_length=50, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_preferences'


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    user_name = models.CharField(max_length=60, blank=True, null=True)
    user_hash = models.CharField(max_length=255, blank=True, null=True)
    system_generated_password = models.IntegerField(blank=True, null=True)
    pwd_last_changed = models.DateTimeField(blank=True, null=True)
    authenticate_id = models.CharField(max_length=100, blank=True, null=True)
    sugar_login = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    external_auth_only = models.IntegerField(blank=True, null=True)
    receive_notifications = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    phone_home = models.CharField(max_length=50, blank=True, null=True)
    phone_mobile = models.CharField(max_length=50, blank=True, null=True)
    phone_work = models.CharField(max_length=50, blank=True, null=True)
    phone_other = models.CharField(max_length=50, blank=True, null=True)
    phone_fax = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    address_street = models.CharField(max_length=150, blank=True, null=True)
    address_city = models.CharField(max_length=100, blank=True, null=True)
    address_state = models.CharField(max_length=100, blank=True, null=True)
    address_country = models.CharField(max_length=100, blank=True, null=True)
    address_postalcode = models.CharField(max_length=20, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    portal_only = models.IntegerField(blank=True, null=True)
    show_on_employees = models.IntegerField(blank=True, null=True)
    employee_status = models.CharField(max_length=100, blank=True, null=True)
    messenger_id = models.CharField(max_length=100, blank=True, null=True)
    messenger_type = models.CharField(max_length=100, blank=True, null=True)
    reports_to_id = models.CharField(max_length=36, blank=True, null=True)
    is_group = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersCstm(models.Model):
    id_c = models.CharField(primary_key=True, max_length=36)
    dept_c = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_cstm'


class UsersFeeds(models.Model):
    user_id = models.CharField(max_length=36, blank=True, null=True)
    feed_id = models.CharField(max_length=36, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_feeds'


class UsersLastImport(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    import_module = models.CharField(max_length=36, blank=True, null=True)
    bean_type = models.CharField(max_length=36, blank=True, null=True)
    bean_id = models.CharField(max_length=36, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_last_import'


class UsersPasswordLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    username = models.CharField(max_length=36, blank=True, null=True)
    date_generated = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_password_link'


class UsersSignatures(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    signature_html = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_signatures'


class Vcals(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=36)
    type = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vcals'


class Versions(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    deleted = models.IntegerField(blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    file_version = models.CharField(max_length=255, blank=True, null=True)
    db_version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versions'


class Zr2Querytemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    sql1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_querytemplate'


class Zr2Report(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_report'


class Zr2Reportcontainer(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_reportcontainer'


class Zr2ReportcontainerZr2ReportC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    zr2_reportcontainer_zr2_reportzr2_reportcontainer_ida = models.CharField(max_length=36, blank=True, null=True)
    zr2_reportcontainer_zr2_reportzr2_report_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_reportcontainer_zr2_report_c'


class Zr2Reportparameter(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    friendly_name = models.CharField(max_length=255, blank=True, null=True)
    default_name = models.CharField(max_length=255, blank=True, null=True)
    default_value = models.CharField(max_length=255, blank=True, null=True)
    range_name = models.CharField(max_length=255, blank=True, null=True)
    range_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_reportparameter'


class Zr2Reportparameterlink(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    default_value = models.CharField(max_length=255, blank=True, null=True)
    bind_to_module_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_reportparameterlink'


class Zr2ReportparameterlinkZr2QuerytemplateC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    zr2_query313cemplate_ida = models.CharField(max_length=36, blank=True, null=True)
    zr2_report0ed1terlink_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_reportparameterlink_zr2_querytemplate_c'


class Zr2ReportparameterlinkZr2ReportparameterC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    zr2_report29aerameter_ida = models.CharField(max_length=36, blank=True, null=True)
    zr2_report53a6terlink_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_reportparameterlink_zr2_reportparameter_c'


class Zr2ReportparameterlinkZr2ReporttemplateC(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    date_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    zr2_report313cemplate_ida = models.CharField(max_length=36, blank=True, null=True)
    zr2_report0ed1terlink_idb = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_reportparameterlink_zr2_reporttemplate_c'


class Zr2Reporttemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    modified_user_id = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.CharField(max_length=36, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    export_as = models.CharField(max_length=255, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zr2_reporttemplate'
