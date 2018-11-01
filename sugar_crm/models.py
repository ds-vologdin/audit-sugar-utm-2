from sqlalchemy import CHAR, Column, Date, DateTime, Float, Index, String, Table, Text, Time, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

from .database import Session_crm


Base = declarative_base()
metadata = Base.metadata
Base.query = Session_crm.query_property()


class A0001Note(Base):
    __tablename__ = 'a0001_notes'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    notes = Column(Text)


class A0001NotesAudit(Base):
    __tablename__ = 'a0001_notes_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class AccAccesscontract(Base):
    __tablename__ = 'acc_accesscontract'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    cost = Column(INTEGER(255))
    inet = Column(TINYINT(1), server_default=text("'0'"))
    typecontract = Column(String(100), server_default=text("'contract'"))


class AccAccesscontractAudit(Base):
    __tablename__ = 'acc_accesscontract_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class AccAccesscontractContactsC(Base):
    __tablename__ = 'acc_accesscontract_contacts_c'
    __table_args__ = (
        Index('acc_accesscontract_contacts_alt', 'acc_accesscontract_contactsacc_accesscontract_ida', 'acc_accesscontract_contactscontacts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_accesscontract_contactsacc_accesscontract_ida = Column(String(36))
    acc_accesscontract_contactscontacts_idb = Column(String(36))


class AccAccesscontractNotesC(Base):
    __tablename__ = 'acc_accesscontract_notes_c'
    __table_args__ = (
        Index('acc_accesscontract_notes_alt', 'acc_accesscontract_notesacc_accesscontract_ida', 'acc_accesscontract_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_accesscontract_notesacc_accesscontract_ida = Column(String(36))
    acc_accesscontract_notesnotes_idb = Column(String(36))


class AccAccessdocument(Base):
    __tablename__ = 'acc_accessdocuments'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    document_name = Column(String(255))
    filename = Column(String(255))
    file_ext = Column(String(100))
    file_mime_type = Column(String(100))
    active_date = Column(Date)
    exp_date = Column(Date)
    category_id = Column(String(100))
    subcategory_id = Column(String(100))
    status_id = Column(String(100))
    teypedoc = Column(String(100), server_default=text("'contract'"))


class AccAccessdocumentsAudit(Base):
    __tablename__ = 'acc_accessdocuments_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class AccAccessdocumentsNotes1C(Base):
    __tablename__ = 'acc_accessdocuments_notes_1_c'
    __table_args__ = (
        Index('acc_accessdocuments_notes_1_alt', 'acc_accessdocuments_notes_1acc_accessdocuments_ida', 'acc_accessdocuments_notes_1notes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_accessdocuments_notes_1acc_accessdocuments_ida = Column(String(36))
    acc_accessdocuments_notes_1notes_idb = Column(String(36))


class AccAccessdocumentsNotesC(Base):
    __tablename__ = 'acc_accessdocuments_notes_c'
    __table_args__ = (
        Index('acc_accessdocuments_notes_alt', 'acc_accessdocuments_notesacc_accessdocuments_ida', 'acc_accessdocuments_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_accessdocuments_notesacc_accessdocuments_ida = Column(String(36))
    acc_accessdocuments_notesnotes_idb = Column(String(36))


class AccAccesserror(Base):
    __tablename__ = 'acc_accesserror'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    status = Column(String(100), server_default=text("'analysis'"))
    dateerror = Column(Date)
    dateaccess = Column(Date)


class AccAccesserrorAccFacilityC(Base):
    __tablename__ = 'acc_accesserror_acc_facility_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_accesserror_acc_facilityacc_facility_ida = Column(String(36), index=True)
    acc_accesserror_acc_facilityacc_accesserror_idb = Column(String(36), index=True)


class AccAccesserrorAudit(Base):
    __tablename__ = 'acc_accesserror_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class AccAccesserrorNotesC(Base):
    __tablename__ = 'acc_accesserror_notes_c'
    __table_args__ = (
        Index('acc_accesserror_notes_alt', 'acc_accesserror_notesacc_accesserror_ida', 'acc_accesserror_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_accesserror_notesacc_accesserror_ida = Column(String(36))
    acc_accesserror_notesnotes_idb = Column(String(36))


class AccFacility(Base):
    __tablename__ = 'acc_facility'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    accessmode = Column(Text)
    presencekey = Column(TINYINT(1), server_default=text("'0'"))
    status = Column(String(100), server_default=text("'bs'"))
    facilitymap = Column(String(255), server_default=text("'maps.google.com?q=Kirov {name}&output=embed'"))


class AccFacilityAccAccesscontractC(Base):
    __tablename__ = 'acc_facility_acc_accesscontract_c'
    __table_args__ = (
        Index('acc_facility_acc_accesscontract_alt', 'acc_facility_acc_accesscontractacc_facility_ida', 'acc_facility_acc_accesscontractacc_accesscontract_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_facility_acc_accesscontractacc_facility_ida = Column(String(36))
    acc_facility_acc_accesscontractacc_accesscontract_idb = Column(String(36))


class AccFacilityAccAccessdocumentsC(Base):
    __tablename__ = 'acc_facility_acc_accessdocuments_c'
    __table_args__ = (
        Index('acc_facility_acc_accessdocuments_alt', 'acc_facility_acc_accessdocumentsacc_facility_ida', 'acc_facility_acc_accessdocumentsacc_accessdocuments_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_facility_acc_accessdocumentsacc_facility_ida = Column(String(36))
    acc_facility_acc_accessdocumentsacc_accessdocuments_idb = Column(String(36))


class AccFacilityAudit(Base):
    __tablename__ = 'acc_facility_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class AccFacilityContactsC(Base):
    __tablename__ = 'acc_facility_contacts_c'
    __table_args__ = (
        Index('acc_facility_contacts_alt', 'acc_facility_contactsacc_facility_ida', 'acc_facility_contactscontacts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_facility_contactsacc_facility_ida = Column(String(36))
    acc_facility_contactscontacts_idb = Column(String(36))


class AccFacilityCstm(Base):
    __tablename__ = 'acc_facility_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    district_c = Column(String(255))


class AccFacilityNotesC(Base):
    __tablename__ = 'acc_facility_notes_c'
    __table_args__ = (
        Index('acc_facility_notes_alt', 'acc_facility_notesacc_facility_ida', 'acc_facility_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_facility_notesacc_facility_ida = Column(String(36))
    acc_facility_notesnotes_idb = Column(String(36))


class AccRequisition(Base):
    __tablename__ = 'acc_requisition'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    status = Column(String(100), server_default=text("'planed'"))
    accessmode = Column(Text)


class AccRequisitionAccAccessdocumentsC(Base):
    __tablename__ = 'acc_requisition_acc_accessdocuments_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_requisition_acc_accessdocumentsacc_requisition_ida = Column(String(36), index=True)
    acc_requisition_acc_accessdocumentsacc_accessdocuments_idb = Column(String(36), index=True)


class AccRequisitionAccFacilityC(Base):
    __tablename__ = 'acc_requisition_acc_facility_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_requisition_acc_facilityacc_requisition_ida = Column(String(36), index=True)
    acc_requisition_acc_facilityacc_facility_idb = Column(String(36), index=True)


class AccRequisitionAudit(Base):
    __tablename__ = 'acc_requisition_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class AccRequisitionCstm(Base):
    __tablename__ = 'acc_requisition_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    accessmodecheck_c = Column(String(100), server_default=text("'24'"))
    equipment_c = Column(String(255))
    address_sogl_c = Column(String(255))


class AccRequisitionNotesC(Base):
    __tablename__ = 'acc_requisition_notes_c'
    __table_args__ = (
        Index('acc_requisition_notes_alt', 'acc_requisition_notesacc_requisition_ida', 'acc_requisition_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_requisition_notesacc_requisition_ida = Column(String(36))
    acc_requisition_notesnotes_idb = Column(String(36))


class AccUk(Base):
    __tablename__ = 'acc_uk'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    address = Column(String(255))
    status = Column(String(100), server_default=text("'uk'"))
    phone = Column(String(255))
    fax = Column(String(255))


class AccUkAccAccesscontractC(Base):
    __tablename__ = 'acc_uk_acc_accesscontract_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_uk_acc_accesscontractacc_uk_ida = Column(String(36), index=True)
    acc_uk_acc_accesscontractacc_accesscontract_idb = Column(String(36), index=True)


class AccUkAccAccessdocumentsC(Base):
    __tablename__ = 'acc_uk_acc_accessdocuments_c'
    __table_args__ = (
        Index('acc_uk_acc_accessdocuments_alt', 'acc_uk_acc_accessdocumentsacc_uk_ida', 'acc_uk_acc_accessdocumentsacc_accessdocuments_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_uk_acc_accessdocumentsacc_uk_ida = Column(String(36))
    acc_uk_acc_accessdocumentsacc_accessdocuments_idb = Column(String(36))


class AccUkAccFacilityC(Base):
    __tablename__ = 'acc_uk_acc_facility_c'
    __table_args__ = (
        Index('acc_uk_acc_facility_alt', 'acc_uk_acc_facilityacc_uk_ida', 'acc_uk_acc_facilityacc_facility_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_uk_acc_facilityacc_uk_ida = Column(String(36))
    acc_uk_acc_facilityacc_facility_idb = Column(String(36))


class AccUkAudit(Base):
    __tablename__ = 'acc_uk_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class AccUkContactsC(Base):
    __tablename__ = 'acc_uk_contacts_c'
    __table_args__ = (
        Index('acc_uk_contacts_alt', 'acc_uk_contactsacc_uk_ida', 'acc_uk_contactscontacts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_uk_contactsacc_uk_ida = Column(String(36))
    acc_uk_contactscontacts_idb = Column(String(36))


class AccUkNotesC(Base):
    __tablename__ = 'acc_uk_notes_c'
    __table_args__ = (
        Index('acc_uk_notes_alt', 'acc_uk_notesacc_uk_ida', 'acc_uk_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    acc_uk_notesacc_uk_ida = Column(String(36))
    acc_uk_notesnotes_idb = Column(String(36))


class Account(Base):
    __tablename__ = 'accounts'
    __table_args__ = (
        Index('idx_accnt_assigned_del', 'deleted', 'assigned_user_id'),
        Index('idx_accnt_name_del', 'name', 'deleted'),
        Index('idx_accnt_id_del', 'id', 'deleted')
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(150))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    account_type = Column(String(100))
    industry = Column(String(100))
    annual_revenue = Column(String(100))
    phone_fax = Column(String(100))
    billing_address_street = Column(String(150))
    billing_address_city = Column(String(100))
    billing_address_state = Column(String(100))
    billing_address_postalcode = Column(String(20))
    billing_address_country = Column(String(255))
    rating = Column(String(100))
    phone_office = Column(String(100))
    phone_alternate = Column(String(100))
    website = Column(String(255))
    ownership = Column(String(100))
    employees = Column(String(10))
    ticker_symbol = Column(String(10))
    shipping_address_street = Column(String(150))
    shipping_address_city = Column(String(100))
    shipping_address_state = Column(String(100))
    shipping_address_postalcode = Column(String(20))
    shipping_address_country = Column(String(255))
    parent_id = Column(CHAR(36), index=True)
    sic_code = Column(String(10))
    campaign_id = Column(CHAR(36))


class AccountsAudit(Base):
    __tablename__ = 'accounts_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class AccountsBug(Base):
    __tablename__ = 'accounts_bugs'
    __table_args__ = (
        Index('idx_account_bug', 'account_id', 'bug_id'),
    )

    id = Column(String(36), primary_key=True)
    account_id = Column(String(36), index=True)
    bug_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class AccountsCalls1C(Base):
    __tablename__ = 'accounts_calls_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    accounts_calls_1accounts_ida = Column(String(36), index=True)
    accounts_calls_1calls_idb = Column(String(36), index=True)


class AccountsCase(Base):
    __tablename__ = 'accounts_cases'

    id = Column(String(36), primary_key=True)
    account_id = Column(String(36), index=True)
    case_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class AccountsConPConnectionsPlan1C(Base):
    __tablename__ = 'accounts_con_p_connections_plan_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    accounts_con_p_connections_plan_1accounts_ida = Column(String(36), index=True)
    accounts_con_p_connections_plan_1con_p_connections_plan_idb = Column(String(36), index=True)


class AccountsContact(Base):
    __tablename__ = 'accounts_contacts'
    __table_args__ = (
        Index('idx_contid_del_accid', 'contact_id', 'deleted', 'account_id'),
        Index('idx_account_contact', 'account_id', 'contact_id')
    )

    id = Column(String(36), primary_key=True)
    contact_id = Column(String(36))
    account_id = Column(String(36))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class AccountsCstm(Base):
    __tablename__ = 'accounts_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    internet_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    phone_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    pdcpgi_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    inet_pvk_acc_c = Column(INTEGER(255))
    inet_ip_acc_c = Column(INTEGER(255))
    month_profit_acc_c = Column(INTEGER(255))
    packet_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    block_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    vats_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    tv_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    inet_date_acc_c = Column(Date)
    phone_date_acc_c = Column(Date)
    closed_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    date_close_acc_c = Column(Date)
    blockletter_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    date_blockletter_acc_c = Column(Date)
    close_couse_acc_c = Column(String(100), server_default=text("'zero'"))
    close_comment_acc_c = Column(Text)
    status_acc_c = Column(String(100), server_default=text("'active'"))
    priority_acc_c = Column(String(100), server_default=text("'low'"))
    debtor_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    address_map_acc_c = Column(String(255), server_default=text("'maps.google.com?q= Russia, Kirov, {billing_address_street}&output=embed'"))
    cctv_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    cost_pdcpgi_acc_c = Column(INTEGER(255))
    company_acc_c = Column(TINYINT(1), server_default=text("'0'"))
    bandwidth_c = Column(Float(18))
    login_ph_c = Column(String(255), index=True)
    phone_new_c = Column(String(255))
    phone_from_bug_c = Column(String(255))
    jjwg_maps_lng_c = Column(Float(11), server_default=text("'0.00000000'"))
    jjwg_maps_lat_c = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_geocode_status_c = Column(String(255))
    jjwg_maps_address_c = Column(String(255))


class AccountsMaMount1C(Base):
    __tablename__ = 'accounts_ma_mount_1_c'
    __table_args__ = (
        Index('accounts_ma_mount_1_alt', 'accounts_ma_mount_1accounts_ida', 'accounts_ma_mount_1ma_mount_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    accounts_ma_mount_1accounts_ida = Column(String(36))
    accounts_ma_mount_1ma_mount_idb = Column(String(36))


class AccountsNotes1C(Base):
    __tablename__ = 'accounts_notes_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    accounts_notes_1accounts_ida = Column(String(36), index=True)
    accounts_notes_1notes_idb = Column(String(36), index=True)


class AccountsOpportunity(Base):
    __tablename__ = 'accounts_opportunities'
    __table_args__ = (
        Index('idx_oppid_del_accid', 'opportunity_id', 'deleted', 'account_id'),
        Index('idx_account_opportunity', 'account_id', 'opportunity_id')
    )

    id = Column(String(36), primary_key=True)
    opportunity_id = Column(String(36))
    account_id = Column(String(36))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class AccountsPoPo1C(Base):
    __tablename__ = 'accounts_po_po_1_c'
    __table_args__ = (
        Index('accounts_po_po_1_alt', 'accounts_po_po_1accounts_ida', 'accounts_po_po_1po_po_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    accounts_po_po_1accounts_ida = Column(String(36))
    accounts_po_po_1po_po_idb = Column(String(36))


class AccountsTcTariffchangeinet1C(Base):
    __tablename__ = 'accounts_tc_tariffchangeinet_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    accounts_tc_tariffchangeinet_1accounts_ida = Column(String(36), index=True)
    accounts_tc_tariffchangeinet_1tc_tariffchangeinet_idb = Column(String(36), index=True)


class AclAction(Base):
    __tablename__ = 'acl_actions'
    __table_args__ = (
        Index('idx_aclaction_id_del', 'id', 'deleted'),
        Index('idx_category_name', 'category', 'name')
    )

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(150))
    category = Column(String(100))
    acltype = Column(String(100))
    aclaccess = Column(INTEGER(3))
    deleted = Column(TINYINT(1))


class AclRole(Base):
    __tablename__ = 'acl_roles'
    __table_args__ = (
        Index('idx_aclrole_id_del', 'id', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(150))
    description = Column(Text)
    deleted = Column(TINYINT(1))


class AclRolesAction(Base):
    __tablename__ = 'acl_roles_actions'
    __table_args__ = (
        Index('idx_aclrole_action', 'role_id', 'action_id'),
    )

    id = Column(String(36), primary_key=True)
    role_id = Column(String(36), index=True)
    action_id = Column(String(36), index=True)
    access_override = Column(INTEGER(3))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class AclRolesUser(Base):
    __tablename__ = 'acl_roles_users'
    __table_args__ = (
        Index('idx_aclrole_user', 'role_id', 'user_id'),
    )

    id = Column(String(36), primary_key=True)
    role_id = Column(String(36), index=True)
    user_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


t_address_book = Table(
    'address_book', metadata,
    Column('assigned_user_id', CHAR(36), nullable=False),
    Column('bean', String(50)),
    Column('bean_id', CHAR(36), nullable=False),
    Index('ab_user_bean_idx', 'assigned_user_id', 'bean')
)


class Bug(Base):
    __tablename__ = 'bugs'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255), index=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36), index=True)
    bug_number = Column(INTEGER(11), nullable=False, unique=True)
    type = Column(String(255))
    status = Column(String(100))
    priority = Column(String(100))
    resolution = Column(String(255))
    work_log = Column(Text)
    found_in_release = Column(String(255))
    fixed_in_release = Column(String(255))
    source = Column(String(255))
    product_category = Column(String(255))


class BugsAudit(Base):
    __tablename__ = 'bugs_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class BugsCBugComments1C(Base):
    __tablename__ = 'bugs_c_bug_comments_1_c'
    __table_args__ = (
        Index('bugs_c_bug_comments_1_alt', 'bugs_c_bug_comments_1bugs_ida', 'bugs_c_bug_comments_1c_bug_comments_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    bugs_c_bug_comments_1bugs_ida = Column(String(36))
    bugs_c_bug_comments_1c_bug_comments_idb = Column(String(36))


class BugsCalls1C(Base):
    __tablename__ = 'bugs_calls_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    bugs_calls_1bugs_ida = Column(String(36), index=True)
    bugs_calls_1calls_idb = Column(String(36), index=True)


class BugsCstm(Base):
    __tablename__ = 'bugs_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    phone_bugs_c = Column(String(255))
    department_bugs_c = Column(String(100), server_default=text("'tp'"))
    reason_for_closure_bugs_c = Column(String(255))
    type_bugs_c = Column(String(100), server_default=text("'null'"))
    status_bugs_c = Column(String(100), server_default=text("'open'"))
    address_bugs_c = Column(String(255))
    account_id_c = Column(CHAR(36))
    bug_id_c = Column(CHAR(36))
    date_close_c = Column(DateTime)
    priority_bugs_c = Column(String(255))
    departure_bugs_c = Column(TINYINT(1), server_default=text("'0'"))
    new_reason_for_closure_bugs_c = Column(Text)
    new_priority_bugs_c = Column(String(100), server_default=text("'one'"))
    service_is_delivered_c = Column(String(255))
    duration_bug_c = Column(Float(18))
    perform_c = Column(Text)
    localisation_c = Column(Text)
    todo_c = Column(String(255))
    duration_min_c = Column(INTEGER(255))


class CBugComment(Base):
    __tablename__ = 'c_bug_comments'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))


class CBugCommentsAudit(Base):
    __tablename__ = 'c_bug_comments_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class CBugCommentsCstm(Base):
    __tablename__ = 'c_bug_comments_cstm'

    id_c = Column(CHAR(36), primary_key=True)


class Call(Base):
    __tablename__ = 'calls'
    __table_args__ = (
        Index('idx_calls_par_del', 'parent_id', 'parent_type', 'deleted'),
        Index('idx_calls_assigned_del', 'deleted', 'assigned_user_id')
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(50), index=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    duration_hours = Column(INTEGER(2))
    duration_minutes = Column(INTEGER(2))
    date_start = Column(DateTime, index=True)
    date_end = Column(DateTime)
    parent_type = Column(String(255))
    status = Column(String(100), index=True, server_default=text("'Planned'"))
    direction = Column(String(100))
    parent_id = Column(CHAR(36))
    reminder_time = Column(INTEGER(11), server_default=text("'60'"))
    email_reminder_time = Column(INTEGER(11), server_default=text("'60'"))
    email_reminder_sent = Column(TINYINT(1), server_default=text("'0'"))
    outlook_id = Column(String(255))
    repeat_type = Column(String(36))
    repeat_interval = Column(INTEGER(3), server_default=text("'1'"))
    repeat_dow = Column(String(7))
    repeat_until = Column(Date)
    repeat_count = Column(INTEGER(7))
    repeat_parent_id = Column(CHAR(36))
    recurring_source = Column(String(36))


class CallsContact(Base):
    __tablename__ = 'calls_contacts'
    __table_args__ = (
        Index('idx_call_contact', 'call_id', 'contact_id'),
    )

    id = Column(String(36), primary_key=True)
    call_id = Column(String(36), index=True)
    contact_id = Column(String(36), index=True)
    required = Column(String(1), server_default=text("'1'"))
    accept_status = Column(String(25), server_default=text("'none'"))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class CallsCstm(Base):
    __tablename__ = 'calls_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    number_call_c = Column(INTEGER(255))
    check_call_c = Column(TINYINT(1), server_default=text("'0'"))
    input_number_c = Column(String(255))


class CallsLead(Base):
    __tablename__ = 'calls_leads'
    __table_args__ = (
        Index('idx_call_lead', 'call_id', 'lead_id'),
    )

    id = Column(String(36), primary_key=True)
    call_id = Column(String(36), index=True)
    lead_id = Column(String(36), index=True)
    required = Column(String(1), server_default=text("'1'"))
    accept_status = Column(String(25), server_default=text("'none'"))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class CallsNumber(Base):
    __tablename__ = 'calls_numbers'

    id_c = Column(CHAR(36), primary_key=True, unique=True)
    input_number = Column(CHAR(20))
    date_call = Column(DateTime)
    output_number = Column(CHAR(20))
    not_received_number = Column(CHAR(20))


class CallsUser(Base):
    __tablename__ = 'calls_users'
    __table_args__ = (
        Index('idx_call_users', 'call_id', 'user_id'),
    )

    id = Column(String(36), primary_key=True)
    call_id = Column(String(36), index=True)
    user_id = Column(String(36), index=True)
    required = Column(String(1), server_default=text("'1'"))
    accept_status = Column(String(25), server_default=text("'none'"))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class CampaignLog(Base):
    __tablename__ = 'campaign_log'
    __table_args__ = (
        Index('idx_target_id_deleted', 'target_id', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    campaign_id = Column(CHAR(36), index=True)
    target_tracker_key = Column(String(36), index=True)
    target_id = Column(String(36), index=True)
    target_type = Column(String(100))
    activity_type = Column(String(100))
    activity_date = Column(DateTime)
    related_id = Column(String(36))
    related_type = Column(String(100))
    archived = Column(TINYINT(1), server_default=text("'0'"))
    hits = Column(INTEGER(11), server_default=text("'0'"))
    list_id = Column(CHAR(36))
    deleted = Column(TINYINT(1))
    date_modified = Column(DateTime)
    more_information = Column(String(100), index=True)
    marketing_id = Column(CHAR(36))


class CampaignTrkr(Base):
    __tablename__ = 'campaign_trkrs'

    id = Column(CHAR(36), primary_key=True)
    tracker_name = Column(String(30))
    tracker_url = Column(String(255), server_default=text("'http://'"))
    tracker_key = Column(INTEGER(11), nullable=False, index=True)
    campaign_id = Column(CHAR(36))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    is_optout = Column(TINYINT(1), server_default=text("'0'"))
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(50), index=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    tracker_key = Column(INTEGER(11), nullable=False, index=True)
    tracker_count = Column(INTEGER(11), server_default=text("'0'"))
    refer_url = Column(String(255), server_default=text("'http://'"))
    tracker_text = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(100))
    impressions = Column(INTEGER(11), server_default=text("'0'"))
    currency_id = Column(CHAR(36))
    budget = Column(Float(asdecimal=True))
    expected_cost = Column(Float(asdecimal=True))
    actual_cost = Column(Float(asdecimal=True))
    expected_revenue = Column(Float(asdecimal=True))
    campaign_type = Column(String(100))
    objective = Column(Text)
    content = Column(Text)
    frequency = Column(String(100))


class CampaignsAudit(Base):
    __tablename__ = 'campaigns_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class Case(Base):
    __tablename__ = 'cases'
    __table_args__ = (
        Index('idx_cases_stat_del', 'assigned_user_id', 'status', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255), index=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    case_number = Column(INTEGER(11), nullable=False, unique=True)
    type = Column(String(255))
    status = Column(String(100))
    priority = Column(String(100))
    resolution = Column(Text)
    work_log = Column(Text)
    account_id = Column(CHAR(36), index=True)


class CasesAudit(Base):
    __tablename__ = 'cases_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class CasesBug(Base):
    __tablename__ = 'cases_bugs'
    __table_args__ = (
        Index('idx_case_bug', 'case_id', 'bug_id'),
    )

    id = Column(String(36), primary_key=True)
    case_id = Column(String(36), index=True)
    bug_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class CasesCstm(Base):
    __tablename__ = 'cases_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    jjwg_maps_lng_c = Column(Float(11), server_default=text("'0.00000000'"))
    jjwg_maps_lat_c = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_geocode_status_c = Column(String(255))
    jjwg_maps_address_c = Column(String(255))


class CatRepairsList(Base):
    __tablename__ = 'cat_repairs_list'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))


class CatWorkList(Base):
    __tablename__ = 'cat_work_list'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))


class ConPConnectionsPlan(Base):
    __tablename__ = 'con_p_connections_plan'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))


class ConPConnectionsPlanAudit(Base):
    __tablename__ = 'con_p_connections_plan_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class ConPConnectionsPlanCstm(Base):
    __tablename__ = 'con_p_connections_plan_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    address_plan_c = Column(String(255))
    time_connection_c = Column(String(255))
    date_connection_c = Column(Date)
    contacts_c = Column(String(255))
    account_id_c = Column(CHAR(36))
    number_opp_c = Column(String(255))
    tariff_plan_c = Column(String(255))
    issued_hard_c = Column(TINYINT(1), server_default=text("'0'"))
    user_id_c = Column(CHAR(36))
    base_station_c = Column(Text)
    level_signal_c = Column(String(255))
    enter_roof_c = Column(Text)
    type_conn_c = Column(String(100), server_default=text("'ur'"))
    type_hard_c = Column(Text)
    radio_c = Column(TINYINT(1), server_default=text("'0'"))
    point_address_c = Column(String(255))
    ip_address_c = Column(String(255))
    brigada_c = Column(String(100))
    gps_check_c = Column(TINYINT(1), server_default=text("'0'"))
    ra_survey_id_c = Column(CHAR(36))
    comment_mount_c = Column(Text)
    check_mount_c = Column(TINYINT(1), server_default=text("'0'"))
    call_pl_c = Column(TINYINT(1), server_default=text("'0'"))
    user_id1_c = Column(CHAR(36))
    call_comment_c = Column(Text)
    start_time_c = Column(DateTime)
    end_time_c = Column(DateTime)
    user_id2_c = Column(CHAR(36))
    user_id3_c = Column(CHAR(36))
    job_list_c = Column(Text)
    cat_work_c = Column(String(100))
    remarks_c = Column(String(255))
    photo_one_c = Column(String(255))
    photo_two_c = Column(String(255))
    photo_three_c = Column(String(255))
    photo_four_c = Column(String(255))
    user_id4_c = Column(CHAR(36))
    acc_requisition_id_c = Column(CHAR(36))
    call_date_c = Column(Date)
    status_mount_c = Column(String(100), server_default=text("'1'"))
    channel_speed_c = Column(String(255))


class ConPConnectionsPlanNotes1C(Base):
    __tablename__ = 'con_p_connections_plan_notes_1_c'
    __table_args__ = (
        Index('con_p_connections_plan_notes_1_alt', 'con_p_connections_plan_notes_1con_p_connections_plan_ida', 'con_p_connections_plan_notes_1notes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    con_p_connections_plan_notes_1con_p_connections_plan_ida = Column(String(36))
    con_p_connections_plan_notes_1notes_idb = Column(String(36))


t_config = Table(
    'config', metadata,
    Column('category', String(32), index=True),
    Column('name', String(32)),
    Column('value', Text)
)


class Contact(Base):
    __tablename__ = 'contacts'
    __table_args__ = (
        Index('idx_contacts_del_last', 'deleted', 'last_name'),
        Index('idx_cont_del_reports', 'deleted', 'reports_to_id', 'last_name'),
        Index('idx_del_id_user', 'deleted', 'id', 'assigned_user_id'),
        Index('idx_cont_last_first', 'last_name', 'first_name', 'deleted')
    )

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36), index=True)
    salutation = Column(String(255))
    first_name = Column(String(100))
    last_name = Column(String(100))
    title = Column(String(100))
    department = Column(String(255))
    do_not_call = Column(TINYINT(1), server_default=text("'0'"))
    phone_home = Column(String(100))
    phone_mobile = Column(String(100))
    phone_work = Column(String(100))
    phone_other = Column(String(100))
    phone_fax = Column(String(100))
    primary_address_street = Column(String(150))
    primary_address_city = Column(String(100))
    primary_address_state = Column(String(100))
    primary_address_postalcode = Column(String(20))
    primary_address_country = Column(String(255))
    alt_address_street = Column(String(150))
    alt_address_city = Column(String(100))
    alt_address_state = Column(String(100))
    alt_address_postalcode = Column(String(20))
    alt_address_country = Column(String(255))
    assistant = Column(String(75))
    assistant_phone = Column(String(100))
    lead_source = Column(String(255))
    reports_to_id = Column(CHAR(36), index=True)
    birthdate = Column(Date)
    campaign_id = Column(CHAR(36))


class ContactsAudit(Base):
    __tablename__ = 'contacts_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class ContactsBug(Base):
    __tablename__ = 'contacts_bugs'
    __table_args__ = (
        Index('idx_contact_bug', 'contact_id', 'bug_id'),
    )

    id = Column(String(36), primary_key=True)
    contact_id = Column(String(36), index=True)
    bug_id = Column(String(36), index=True)
    contact_role = Column(String(50))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ContactsCase(Base):
    __tablename__ = 'contacts_cases'
    __table_args__ = (
        Index('idx_contacts_cases', 'contact_id', 'case_id'),
    )

    id = Column(String(36), primary_key=True)
    contact_id = Column(String(36), index=True)
    case_id = Column(String(36), index=True)
    contact_role = Column(String(50))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ContactsCstm(Base):
    __tablename__ = 'contacts_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    jjwg_maps_lng_c = Column(Float(11), server_default=text("'0.00000000'"))
    jjwg_maps_lat_c = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_geocode_status_c = Column(String(255))
    jjwg_maps_address_c = Column(String(255))


class ContactsUser(Base):
    __tablename__ = 'contacts_users'
    __table_args__ = (
        Index('idx_contacts_users', 'contact_id', 'user_id'),
    )

    id = Column(String(36), primary_key=True)
    contact_id = Column(String(36), index=True)
    user_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class CronRemoveDocument(Base):
    __tablename__ = 'cron_remove_documents'

    id = Column(String(36), primary_key=True)
    bean_id = Column(String(36), index=True)
    module = Column(String(25))
    date_modified = Column(DateTime, index=True)


class Currency(Base):
    __tablename__ = 'currencies'
    __table_args__ = (
        Index('idx_currency_name', 'name', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(36))
    symbol = Column(String(36))
    iso4217 = Column(String(3))
    conversion_rate = Column(Float(asdecimal=True), server_default=text("'0'"))
    status = Column(String(100))
    deleted = Column(TINYINT(1))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    created_by = Column(CHAR(36), nullable=False)


t_custom_fields = Table(
    'custom_fields', metadata,
    Column('bean_id', String(36)),
    Column('set_num', INTEGER(11), server_default=text("'0'")),
    Column('field0', String(255)),
    Column('field1', String(255)),
    Column('field2', String(255)),
    Column('field3', String(255)),
    Column('field4', String(255)),
    Column('field5', String(255)),
    Column('field6', String(255)),
    Column('field7', String(255)),
    Column('field8', String(255)),
    Column('field9', String(255)),
    Column('deleted', TINYINT(1), server_default=text("'0'")),
    Index('idx_beanid_set_num', 'bean_id', 'set_num')
)


class DevDevelopment(Base):
    __tablename__ = 'dev_development'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    status = Column(String(100), server_default=text("'1'"))
    finish = Column(Date)


class DevDevelopmentAccRequisitionC(Base):
    __tablename__ = 'dev_development_acc_requisition_c'
    __table_args__ = (
        Index('dev_development_acc_requisition_alt', 'dev_development_acc_requisitiondev_development_ida', 'dev_development_acc_requisitionacc_requisition_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    dev_development_acc_requisitiondev_development_ida = Column(String(36))
    dev_development_acc_requisitionacc_requisition_idb = Column(String(36))


class DevDevelopmentAudit(Base):
    __tablename__ = 'dev_development_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class DevDevelopmentNotesC(Base):
    __tablename__ = 'dev_development_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    dev_development_notesdev_development_ida = Column(String(36), index=True)
    dev_development_notesnotes_idb = Column(String(36), index=True)


class DevDevelopmentRaSurveyC(Base):
    __tablename__ = 'dev_development_ra_survey_c'
    __table_args__ = (
        Index('dev_development_ra_survey_alt', 'dev_development_ra_surveydev_development_ida', 'dev_development_ra_surveyra_survey_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    dev_development_ra_surveydev_development_ida = Column(String(36))
    dev_development_ra_surveyra_survey_idb = Column(String(36))


class DevDevelopmentSkSketchC(Base):
    __tablename__ = 'dev_development_sk_sketch_c'
    __table_args__ = (
        Index('dev_development_sk_sketch_alt', 'dev_development_sk_sketchdev_development_ida', 'dev_development_sk_sketchsk_sketch_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    dev_development_sk_sketchdev_development_ida = Column(String(36))
    dev_development_sk_sketchsk_sketch_idb = Column(String(36))


class DocumentRevision(Base):
    __tablename__ = 'document_revisions'

    id = Column(String(36), primary_key=True)
    change_log = Column(String(255))
    document_id = Column(String(36))
    doc_id = Column(String(100))
    doc_type = Column(String(100))
    doc_url = Column(String(255))
    date_entered = Column(DateTime)
    created_by = Column(CHAR(36))
    filename = Column(String(255))
    file_ext = Column(String(100))
    file_mime_type = Column(String(100), index=True)
    revision = Column(String(100))
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    date_modified = Column(DateTime)


class Document(Base):
    __tablename__ = 'documents'
    __table_args__ = (
        Index('idx_doc_cat', 'category_id', 'subcategory_id'),
    )

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    document_name = Column(String(255))
    doc_id = Column(String(100))
    doc_type = Column(String(100), server_default=text("'Sugar'"))
    doc_url = Column(String(255))
    active_date = Column(Date)
    exp_date = Column(Date)
    category_id = Column(String(100))
    subcategory_id = Column(String(100))
    status_id = Column(String(100))
    document_revision_id = Column(String(36))
    related_doc_id = Column(CHAR(36))
    related_doc_rev_id = Column(CHAR(36))
    is_template = Column(TINYINT(1), server_default=text("'0'"))
    template_type = Column(String(100))


class DocumentsAccount(Base):
    __tablename__ = 'documents_accounts'
    __table_args__ = (
        Index('documents_accounts_document_id', 'document_id', 'account_id'),
        Index('documents_accounts_account_id', 'account_id', 'document_id')
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    document_id = Column(String(36))
    account_id = Column(String(36))


class DocumentsBug(Base):
    __tablename__ = 'documents_bugs'
    __table_args__ = (
        Index('documents_bugs_document_id', 'document_id', 'bug_id'),
        Index('documents_bugs_bug_id', 'bug_id', 'document_id')
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    document_id = Column(String(36))
    bug_id = Column(String(36))


class DocumentsCase(Base):
    __tablename__ = 'documents_cases'
    __table_args__ = (
        Index('documents_cases_document_id', 'document_id', 'case_id'),
        Index('documents_cases_case_id', 'case_id', 'document_id')
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    document_id = Column(String(36))
    case_id = Column(String(36))


class DocumentsContact(Base):
    __tablename__ = 'documents_contacts'
    __table_args__ = (
        Index('documents_contacts_document_id', 'document_id', 'contact_id'),
        Index('documents_contacts_contact_id', 'contact_id', 'document_id')
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    document_id = Column(String(36))
    contact_id = Column(String(36))


class DocumentsOpportunity(Base):
    __tablename__ = 'documents_opportunities'
    __table_args__ = (
        Index('idx_docu_oppo_docu_id', 'document_id', 'opportunity_id'),
        Index('idx_docu_opps_oppo_id', 'opportunity_id', 'document_id')
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    document_id = Column(String(36))
    opportunity_id = Column(String(36))


class EaddrAction(Base):
    __tablename__ = 'eaddr_action'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    type_action = Column(String(100), server_default=text("'call'"))
    date_action = Column(Date)
    status = Column(String(100), server_default=text("'plan'"))


class EaddrActionAudit(Base):
    __tablename__ = 'eaddr_action_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class EaddrActionEaddrEmptyAddressC(Base):
    __tablename__ = 'eaddr_action_eaddr_empty_address_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    eaddr_action_eaddr_empty_addresseaddr_empty_address_ida = Column(String(36), index=True)
    eaddr_action_eaddr_empty_addresseaddr_action_idb = Column(String(36), index=True)


class EaddrEmptyAddres(Base):
    __tablename__ = 'eaddr_empty_address'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    type_address = Column(String(100), server_default=text("'none'"))


class EaddrEmptyAddressAccountsC(Base):
    __tablename__ = 'eaddr_empty_address_accounts_c'
    __table_args__ = (
        Index('eaddr_empty_address_accounts_alt', 'eaddr_empty_address_accountseaddr_empty_address_ida', 'eaddr_empty_address_accountsaccounts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    eaddr_empty_address_accountseaddr_empty_address_ida = Column(String(36))
    eaddr_empty_address_accountsaccounts_idb = Column(String(36))


class EaddrEmptyAddressAudit(Base):
    __tablename__ = 'eaddr_empty_address_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class Eapm(Base):
    __tablename__ = 'eapm'
    __table_args__ = (
        Index('idx_app_active', 'assigned_user_id', 'application', 'validated'),
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    password = Column(String(255))
    url = Column(String(255))
    application = Column(String(100), server_default=text("'webex'"))
    api_data = Column(Text)
    consumer_key = Column(String(255))
    consumer_secret = Column(String(255))
    oauth_token = Column(String(255))
    oauth_secret = Column(String(255))
    validated = Column(TINYINT(1))


class EmElectricMeter(Base):
    __tablename__ = 'em_electric_meters'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    address = Column(String(255))
    date_install = Column(Date)


class EmElectricMetersAudit(Base):
    __tablename__ = 'em_electric_meters_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class EmElectricMetersEmMetersDataC(Base):
    __tablename__ = 'em_electric_meters_em_meters_data_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    em_electric_meters_em_meters_dataem_electric_meters_ida = Column(String(36), index=True)
    em_electric_meters_em_meters_dataem_meters_data_idb = Column(String(36), index=True)


class EmMetersDatum(Base):
    __tablename__ = 'em_meters_data'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    date_meters_date = Column(Date)


class EmMetersDataAudit(Base):
    __tablename__ = 'em_meters_data_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class EmailAddrBeanRel(Base):
    __tablename__ = 'email_addr_bean_rel'
    __table_args__ = (
        Index('idx_bean_id', 'bean_id', 'bean_module'),
    )

    id = Column(CHAR(36), primary_key=True)
    email_address_id = Column(CHAR(36), nullable=False, index=True)
    bean_id = Column(CHAR(36), nullable=False)
    bean_module = Column(String(100))
    primary_address = Column(TINYINT(1), server_default=text("'0'"))
    reply_to_address = Column(TINYINT(1), server_default=text("'0'"))
    date_created = Column(DateTime)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class EmailAddress(Base):
    __tablename__ = 'email_addresses'
    __table_args__ = (
        Index('idx_ea_opt_out_invalid', 'email_address', 'opt_out', 'invalid_email'),
        Index('idx_ea_caps_opt_out_invalid', 'email_address_caps', 'opt_out', 'invalid_email')
    )

    id = Column(CHAR(36), primary_key=True)
    email_address = Column(String(255))
    email_address_caps = Column(String(255))
    invalid_email = Column(TINYINT(1), server_default=text("'0'"))
    opt_out = Column(TINYINT(1), server_default=text("'0'"))
    date_created = Column(DateTime)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


t_email_cache = Table(
    'email_cache', metadata,
    Column('ie_id', CHAR(36), index=True),
    Column('mbox', String(60)),
    Column('subject', String(255), index=True),
    Column('fromaddr', String(100)),
    Column('toaddr', String(255), index=True),
    Column('senddate', DateTime),
    Column('message_id', String(255)),
    Column('mailsize', INTEGER(10)),
    Column('imap_uid', INTEGER(10)),
    Column('msgno', INTEGER(10)),
    Column('recent', TINYINT(4)),
    Column('flagged', TINYINT(4)),
    Column('answered', TINYINT(4)),
    Column('deleted', TINYINT(4)),
    Column('seen', TINYINT(4)),
    Column('draft', TINYINT(4)),
    Index('idx_mail_date', 'ie_id', 'mbox', 'senddate'),
    Index('idx_mail_from', 'ie_id', 'mbox', 'fromaddr')
)


class EmailMarketing(Base):
    __tablename__ = 'email_marketing'

    id = Column(CHAR(36), primary_key=True)
    deleted = Column(TINYINT(1), index=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(255), index=True)
    from_name = Column(String(100))
    from_addr = Column(String(100))
    reply_to_name = Column(String(100))
    reply_to_addr = Column(String(100))
    inbound_email_id = Column(String(36))
    date_start = Column(DateTime)
    template_id = Column(CHAR(36), nullable=False)
    status = Column(String(100))
    campaign_id = Column(CHAR(36))
    all_prospect_lists = Column(TINYINT(1), server_default=text("'0'"))


class EmailMarketingProspectList(Base):
    __tablename__ = 'email_marketing_prospect_lists'
    __table_args__ = (
        Index('email_mp_prospects', 'email_marketing_id', 'prospect_list_id'),
    )

    id = Column(String(36), primary_key=True)
    prospect_list_id = Column(String(36))
    email_marketing_id = Column(String(36))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class EmailTemplate(Base):
    __tablename__ = 'email_templates'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(String(36))
    published = Column(String(3))
    name = Column(String(255), index=True)
    description = Column(Text)
    subject = Column(String(255))
    body = Column(Text)
    body_html = Column(Text)
    deleted = Column(TINYINT(1))
    assigned_user_id = Column(CHAR(36))
    text_only = Column(TINYINT(1))
    type = Column(String(255))


class Emailman(Base):
    __tablename__ = 'emailman'
    __table_args__ = (
        Index('idx_eman_list', 'list_id', 'user_id', 'deleted'),
        Index('idx_eman_relid_reltype_id', 'related_id', 'related_type', 'campaign_id')
    )

    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    user_id = Column(CHAR(36))
    id = Column(INTEGER(11), primary_key=True)
    campaign_id = Column(CHAR(36), index=True)
    marketing_id = Column(CHAR(36))
    list_id = Column(CHAR(36))
    send_date_time = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    in_queue = Column(TINYINT(1), server_default=text("'0'"))
    in_queue_date = Column(DateTime)
    send_attempts = Column(INTEGER(11), server_default=text("'0'"))
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    related_id = Column(CHAR(36))
    related_type = Column(String(100))


class Email(Base):
    __tablename__ = 'emails'
    __table_args__ = (
        Index('idx_email_assigned', 'assigned_user_id', 'type', 'status'),
    )

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    assigned_user_id = Column(CHAR(36))
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    deleted = Column(TINYINT(1))
    date_sent = Column(DateTime)
    message_id = Column(String(255), index=True)
    name = Column(String(255), index=True)
    type = Column(String(100))
    status = Column(String(100))
    flagged = Column(TINYINT(1))
    reply_to_status = Column(TINYINT(1))
    intent = Column(String(100), server_default=text("'pick'"))
    mailbox_id = Column(CHAR(36))
    parent_type = Column(String(100))
    parent_id = Column(CHAR(36), index=True)


class EmailsBean(Base):
    __tablename__ = 'emails_beans'
    __table_args__ = (
        Index('idx_emails_beans_email_bean', 'email_id', 'bean_id', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    email_id = Column(CHAR(36))
    bean_id = Column(CHAR(36), index=True)
    bean_module = Column(String(100))
    campaign_data = Column(Text)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class EmailsEmailAddrRel(Base):
    __tablename__ = 'emails_email_addr_rel'
    __table_args__ = (
        Index('idx_eearl_email_id', 'email_id', 'address_type'),
    )

    id = Column(CHAR(36), primary_key=True)
    email_id = Column(CHAR(36), nullable=False)
    address_type = Column(String(4))
    email_address_id = Column(CHAR(36), nullable=False, index=True)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class EmailsText(Base):
    __tablename__ = 'emails_text'

    email_id = Column(CHAR(36), primary_key=True)
    from_addr = Column(String(255), index=True)
    reply_to_addr = Column(String(255))
    to_addrs = Column(Text)
    cc_addrs = Column(Text)
    bcc_addrs = Column(Text)
    description = Column(LONGTEXT)
    description_html = Column(LONGTEXT)
    raw_source = Column(LONGTEXT)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class EqPickupeq(Base):
    __tablename__ = 'eq_pickupeq'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    list = Column(String(255))
    contact = Column(String(255))
    status = Column(String(100), server_default=text("'request'"))
    requestdate = Column(Date)
    performdate = Column(Date)
    account_id_c = Column(CHAR(36))


class EqPickupeqAccFacilityC(Base):
    __tablename__ = 'eq_pickupeq_acc_facility_c'
    __table_args__ = (
        Index('eq_pickupeq_acc_facility_alt', 'eq_pickupeq_acc_facilityeq_pickupeq_ida', 'eq_pickupeq_acc_facilityacc_facility_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    eq_pickupeq_acc_facilityeq_pickupeq_ida = Column(String(36))
    eq_pickupeq_acc_facilityacc_facility_idb = Column(String(36))


class EqPickupeqAudit(Base):
    __tablename__ = 'eq_pickupeq_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class EqPickupeqContactsC(Base):
    __tablename__ = 'eq_pickupeq_contacts_c'
    __table_args__ = (
        Index('eq_pickupeq_contacts_alt', 'eq_pickupeq_contactseq_pickupeq_ida', 'eq_pickupeq_contactscontacts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    eq_pickupeq_contactseq_pickupeq_ida = Column(String(36))
    eq_pickupeq_contactscontacts_idb = Column(String(36))


class EqPickupeqNotesC(Base):
    __tablename__ = 'eq_pickupeq_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    eq_pickupeq_noteseq_pickupeq_ida = Column(String(36), index=True)
    eq_pickupeq_notesnotes_idb = Column(String(36), index=True)


class FieldsMetaDatum(Base):
    __tablename__ = 'fields_meta_data'
    __table_args__ = (
        Index('idx_meta_cm_del', 'custom_module', 'deleted'),
        Index('idx_meta_id_del', 'id', 'deleted')
    )

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    vname = Column(String(255))
    comments = Column(String(255))
    help = Column(String(255))
    custom_module = Column(String(255))
    type = Column(String(255))
    len = Column(INTEGER(11))
    required = Column(TINYINT(1), server_default=text("'0'"))
    default_value = Column(String(255))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    audited = Column(TINYINT(1), server_default=text("'0'"))
    massupdate = Column(TINYINT(1), server_default=text("'0'"))
    duplicate_merge = Column(SMALLINT(6), server_default=text("'0'"))
    reportable = Column(TINYINT(1), server_default=text("'1'"))
    importable = Column(String(255))
    ext1 = Column(String(255))
    ext2 = Column(String(255))
    ext3 = Column(String(255))
    ext4 = Column(Text)


class Folder(Base):
    __tablename__ = 'folders'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(25))
    folder_type = Column(String(25))
    parent_folder = Column(CHAR(36), index=True)
    has_child = Column(TINYINT(1), server_default=text("'0'"))
    is_group = Column(TINYINT(1), server_default=text("'0'"))
    is_dynamic = Column(TINYINT(1), server_default=text("'0'"))
    dynamic_query = Column(Text)
    assign_to_id = Column(CHAR(36))
    created_by = Column(CHAR(36), nullable=False)
    modified_by = Column(CHAR(36), nullable=False)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class FoldersRel(Base):
    __tablename__ = 'folders_rel'
    __table_args__ = (
        Index('idx_fr_id_deleted_poly', 'folder_id', 'deleted', 'polymorphic_id'),
        Index('idx_poly_module_poly_id', 'polymorphic_module', 'polymorphic_id')
    )

    id = Column(CHAR(36), primary_key=True)
    folder_id = Column(CHAR(36), nullable=False)
    polymorphic_module = Column(String(25))
    polymorphic_id = Column(CHAR(36), nullable=False)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class FoldersSubscription(Base):
    __tablename__ = 'folders_subscriptions'
    __table_args__ = (
        Index('idx_folder_id_assigned_user_id', 'folder_id', 'assigned_user_id'),
    )

    id = Column(CHAR(36), primary_key=True)
    folder_id = Column(CHAR(36), nullable=False)
    assigned_user_id = Column(CHAR(36), nullable=False)


class ImportMap(Base):
    __tablename__ = 'import_maps'
    __table_args__ = (
        Index('idx_owner_module_name', 'assigned_user_id', 'module', 'name', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(254))
    source = Column(String(36))
    enclosure = Column(String(1), server_default=text("' '"))
    delimiter = Column(String(1), server_default=text("','"))
    module = Column(String(36))
    content = Column(Text)
    default_values = Column(Text)
    has_header = Column(TINYINT(1), server_default=text("'1'"))
    deleted = Column(TINYINT(1))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    assigned_user_id = Column(CHAR(36))
    is_published = Column(String(3), server_default=text("'no'"))


class InboundEmail(Base):
    __tablename__ = 'inbound_email'

    id = Column(String(36), primary_key=True)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(255))
    status = Column(String(100), server_default=text("'Active'"))
    server_url = Column(String(100))
    email_user = Column(String(100))
    email_password = Column(String(100))
    port = Column(INTEGER(5))
    service = Column(String(50))
    mailbox = Column(Text)
    delete_seen = Column(TINYINT(1), server_default=text("'0'"))
    mailbox_type = Column(String(10))
    template_id = Column(CHAR(36))
    stored_options = Column(Text)
    group_id = Column(CHAR(36))
    is_personal = Column(TINYINT(1), server_default=text("'0'"))
    groupfolder_id = Column(CHAR(36))


class InboundEmailAutoreply(Base):
    __tablename__ = 'inbound_email_autoreply'

    id = Column(CHAR(36), primary_key=True)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    autoreplied_to = Column(String(100), index=True)
    ie_id = Column(CHAR(36), nullable=False)


class InboundEmailCacheT(Base):
    __tablename__ = 'inbound_email_cache_ts'

    id = Column(String(255), primary_key=True)
    ie_timestamp = Column(INTEGER(10))


class InstComment(Base):
    __tablename__ = 'inst_comments'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    status = Column(String(100), server_default=text("'consider'"))
    type = Column(String(100), server_default=text("'work'"))


class InstCommentsAudit(Base):
    __tablename__ = 'inst_comments_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class InstCommentsInstPlanC(Base):
    __tablename__ = 'inst_comments_inst_plan_c'
    __table_args__ = (
        Index('inst_comments_inst_plan_alt', 'inst_comments_inst_planinst_comments_ida', 'inst_comments_inst_planinst_plan_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    inst_comments_inst_planinst_comments_ida = Column(String(36))
    inst_comments_inst_planinst_plan_idb = Column(String(36))


class InstPlan(Base):
    __tablename__ = 'inst_plan'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    actual_time = Column(DateTime)
    status = Column(String(100), server_default=text("'request'"))
    duration = Column(INTEGER(255))
    contact = Column(String(255))
    equipment = Column(Text)
    tu = Column(String(255))
    type = Column(String(100))
    account_id_c = Column(CHAR(36))
    reservation_time = Column(String(255))
    date_work = Column(Date)


class InstPlanAccountsC(Base):
    __tablename__ = 'inst_plan_accounts_c'
    __table_args__ = (
        Index('inst_plan_accounts_alt', 'inst_plan_accountsinst_plan_ida', 'inst_plan_accountsaccounts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    inst_plan_accountsinst_plan_ida = Column(String(36))
    inst_plan_accountsaccounts_idb = Column(String(36))


class InstPlanAudit(Base):
    __tablename__ = 'inst_plan_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class InstPlanContactsC(Base):
    __tablename__ = 'inst_plan_contacts_c'
    __table_args__ = (
        Index('inst_plan_contacts_alt', 'inst_plan_contactsinst_plan_ida', 'inst_plan_contactscontacts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    inst_plan_contactsinst_plan_ida = Column(String(36))
    inst_plan_contactscontacts_idb = Column(String(36))


class InstPlanNotesC(Base):
    __tablename__ = 'inst_plan_notes_c'
    __table_args__ = (
        Index('inst_plan_notes_alt', 'inst_plan_notesinst_plan_ida', 'inst_plan_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    inst_plan_notesinst_plan_ida = Column(String(36))
    inst_plan_notesnotes_idb = Column(String(36))


class InstPlanPhysiPhisicC(Base):
    __tablename__ = 'inst_plan_physi_phisic_c'
    __table_args__ = (
        Index('inst_plan_physi_phisic_alt', 'inst_plan_physi_phisicinst_plan_ida', 'inst_plan_physi_phisicphysi_phisic_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    inst_plan_physi_phisicinst_plan_ida = Column(String(36))
    inst_plan_physi_phisicphysi_phisic_idb = Column(String(36))


class InstPlanRaSurveyC(Base):
    __tablename__ = 'inst_plan_ra_survey_c'
    __table_args__ = (
        Index('inst_plan_ra_survey_alt', 'inst_plan_ra_surveyinst_plan_ida', 'inst_plan_ra_surveyra_survey_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    inst_plan_ra_surveyinst_plan_ida = Column(String(36))
    inst_plan_ra_surveyra_survey_idb = Column(String(36))


class JjwgAddressCache(Base):
    __tablename__ = 'jjwg_address_cache'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    lat = Column(Float(10))
    lng = Column(Float(11))


class JjwgAddressCacheAudit(Base):
    __tablename__ = 'jjwg_address_cache_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class JjwgArea(Base):
    __tablename__ = 'jjwg_areas'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    city = Column(String(255))
    state = Column(String(255))
    country = Column(String(255))
    coordinates = Column(Text)


class JjwgAreasAudit(Base):
    __tablename__ = 'jjwg_areas_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class JjwgMap(Base):
    __tablename__ = 'jjwg_maps'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    distance = Column(Float(9))
    unit_type = Column(String(100), server_default=text("'mi'"))
    module_type = Column(String(100), server_default=text("'Accounts'"))
    parent_type = Column(String(255))
    parent_id = Column(CHAR(36))


class JjwgMapsAudit(Base):
    __tablename__ = 'jjwg_maps_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class JjwgMapsJjwgAreasC(Base):
    __tablename__ = 'jjwg_maps_jjwg_areas_c'
    __table_args__ = (
        Index('jjwg_maps_jjwg_areas_alt', 'jjwg_maps_5304wg_maps_ida', 'jjwg_maps_41f2g_areas_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    jjwg_maps_5304wg_maps_ida = Column(String(36))
    jjwg_maps_41f2g_areas_idb = Column(String(36))


class JjwgMapsJjwgMarkersC(Base):
    __tablename__ = 'jjwg_maps_jjwg_markers_c'
    __table_args__ = (
        Index('jjwg_maps_jjwg_markers_alt', 'jjwg_maps_b229wg_maps_ida', 'jjwg_maps_2e31markers_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    jjwg_maps_b229wg_maps_ida = Column(String(36))
    jjwg_maps_2e31markers_idb = Column(String(36))


class JjwgMarker(Base):
    __tablename__ = 'jjwg_markers'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    city = Column(String(255))
    state = Column(String(255))
    country = Column(String(255))
    jjwg_maps_lat = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_lng = Column(Float(11), server_default=text("'0.00000000'"))
    marker_image = Column(String(100), server_default=text("'company'"))


class JjwgMarkersAudit(Base):
    __tablename__ = 'jjwg_markers_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class JjwgMarkersRaSurvey1C(Base):
    __tablename__ = 'jjwg_markers_ra_survey_1_c'
    __table_args__ = (
        Index('jjwg_markers_ra_survey_1_alt', 'jjwg_markers_ra_survey_1jjwg_markers_ida', 'jjwg_markers_ra_survey_1ra_survey_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    jjwg_markers_ra_survey_1jjwg_markers_ida = Column(String(36))
    jjwg_markers_ra_survey_1ra_survey_idb = Column(String(36))


class JobQueue(Base):
    __tablename__ = 'job_queue'
    __table_args__ = (
        Index('idx_status_modified', 'status', 'date_modified'),
        Index('idx_status_entered', 'status', 'date_entered'),
        Index('idx_status_time', 'status', 'execute_time', 'date_entered'),
        Index('idx_status_scheduler', 'status', 'scheduler_id')
    )

    assigned_user_id = Column(CHAR(36))
    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    scheduler_id = Column(CHAR(36))
    execute_time = Column(DateTime)
    status = Column(String(20))
    resolution = Column(String(20))
    message = Column(Text)
    target = Column(String(255))
    data = Column(Text)
    requeue = Column(TINYINT(1), server_default=text("'0'"))
    retry_count = Column(TINYINT(4))
    failure_count = Column(TINYINT(4))
    job_delay = Column(INTEGER(11))
    client = Column(String(255))
    percent_complete = Column(INTEGER(11))


class Lead(Base):
    __tablename__ = 'leads'
    __table_args__ = (
        Index('idx_lead_acct_name_first', 'account_name', 'deleted'),
        Index('idx_del_user', 'deleted', 'assigned_user_id'),
        Index('idx_leads_id_del', 'id', 'deleted'),
        Index('idx_lead_last_first', 'last_name', 'first_name', 'deleted'),
        Index('idx_lead_del_stat', 'last_name', 'status', 'deleted', 'first_name'),
        Index('idx_lead_opp_del', 'opportunity_id', 'deleted'),
        Index('idx_leads_acct_del', 'account_id', 'deleted')
    )

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36), index=True)
    salutation = Column(String(255))
    first_name = Column(String(100))
    last_name = Column(String(100))
    title = Column(String(100))
    department = Column(String(100))
    do_not_call = Column(TINYINT(1), server_default=text("'0'"))
    phone_home = Column(String(100))
    phone_mobile = Column(String(100))
    phone_work = Column(String(100), index=True)
    phone_other = Column(String(100))
    phone_fax = Column(String(100))
    primary_address_street = Column(String(150))
    primary_address_city = Column(String(100))
    primary_address_state = Column(String(100))
    primary_address_postalcode = Column(String(20))
    primary_address_country = Column(String(255))
    alt_address_street = Column(String(150))
    alt_address_city = Column(String(100))
    alt_address_state = Column(String(100))
    alt_address_postalcode = Column(String(20))
    alt_address_country = Column(String(255))
    assistant = Column(String(75))
    assistant_phone = Column(String(100))
    converted = Column(TINYINT(1), server_default=text("'0'"))
    refered_by = Column(String(100))
    lead_source = Column(String(100))
    lead_source_description = Column(Text)
    status = Column(String(100))
    status_description = Column(Text)
    reports_to_id = Column(CHAR(36), index=True)
    account_name = Column(String(255))
    account_description = Column(Text)
    contact_id = Column(CHAR(36), index=True)
    account_id = Column(CHAR(36))
    opportunity_id = Column(CHAR(36))
    opportunity_name = Column(String(255))
    opportunity_amount = Column(String(50))
    campaign_id = Column(CHAR(36))
    birthdate = Column(Date)
    portal_name = Column(String(255))
    portal_app = Column(String(255))
    website = Column(String(255))


class LeadsAudit(Base):
    __tablename__ = 'leads_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class LeadsCstm(Base):
    __tablename__ = 'leads_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    jjwg_maps_lng_c = Column(Float(11), server_default=text("'0.00000000'"))
    jjwg_maps_lat_c = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_geocode_status_c = Column(String(255))
    jjwg_maps_address_c = Column(String(255))


class LetLetter(Base):
    __tablename__ = 'let_letters'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    inputnumber = Column(String(255))
    inputdate = Column(Date)
    outputnumber = Column(String(255))
    outputdate = Column(Date)
    organization = Column(String(100), server_default=text("'gts'"))
    let_to = Column(String(255))
    let_from = Column(String(255))
    typeletters = Column(String(100), server_default=text("'output'"))
    performer = Column(String(255))
    file_mime_type = Column(String(100))
    filename = Column(String(255))


class LetLettersAccountsC(Base):
    __tablename__ = 'let_letters_accounts_c'
    __table_args__ = (
        Index('let_letters_accounts_alt', 'let_letters_accountslet_letters_ida', 'let_letters_accountsaccounts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    let_letters_accountslet_letters_ida = Column(String(36))
    let_letters_accountsaccounts_idb = Column(String(36))


class LetLettersAudit(Base):
    __tablename__ = 'let_letters_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class LetLettersContactsC(Base):
    __tablename__ = 'let_letters_contacts_c'
    __table_args__ = (
        Index('let_letters_contacts_alt', 'let_letters_contactslet_letters_ida', 'let_letters_contactscontacts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    let_letters_contactslet_letters_ida = Column(String(36))
    let_letters_contactscontacts_idb = Column(String(36))


class LetLettersCstm(Base):
    __tablename__ = 'let_letters_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    number_kor_c = Column(INTEGER(255))
    number_kor_new_c = Column(String(255))


class LetLettersNotesC(Base):
    __tablename__ = 'let_letters_notes_c'
    __table_args__ = (
        Index('let_letters_notes_alt', 'let_letters_noteslet_letters_ida', 'let_letters_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    let_letters_noteslet_letters_ida = Column(String(36))
    let_letters_notesnotes_idb = Column(String(36))


class LinkedDocument(Base):
    __tablename__ = 'linked_documents'
    __table_args__ = (
        Index('idx_parent_document', 'parent_type', 'parent_id', 'document_id'),
    )

    id = Column(String(36), primary_key=True)
    parent_id = Column(String(36))
    parent_type = Column(String(25))
    document_id = Column(String(36))
    document_revision_id = Column(String(36))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class MaMount(Base):
    __tablename__ = 'ma_mount'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    document_name = Column(String(255))
    filename = Column(String(255))
    file_ext = Column(String(100))
    file_mime_type = Column(String(100))
    active_date = Column(Date)
    exp_date = Column(Date)
    category_id = Column(String(100))
    subcategory_id = Column(String(100))
    status_id = Column(String(100))


class MaMountAudit(Base):
    __tablename__ = 'ma_mount_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class MaMountConPConnectionsPlan1C(Base):
    __tablename__ = 'ma_mount_con_p_connections_plan_1_c'
    __table_args__ = (
        Index('ma_mount_con_p_connections_plan_1_alt', 'ma_mount_con_p_connections_plan_1ma_mount_ida', 'ma_mount_con_p_connections_plan_1con_p_connections_plan_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ma_mount_con_p_connections_plan_1ma_mount_ida = Column(String(36))
    ma_mount_con_p_connections_plan_1con_p_connections_plan_idb = Column(String(36))


class MaMountCstm(Base):
    __tablename__ = 'ma_mount_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    address_mount_c = Column(String(255))
    contact_mount_c = Column(String(255))
    level_signal_mount_c = Column(String(255))
    mount_photo_c = Column(String(255))
    mount_photo_1_c = Column(String(255))
    mount_photo_2_c = Column(String(255))
    mount_photo_3_c = Column(String(255))
    con_p_connections_plan_id_c = Column(CHAR(36))


class MaMountPoPo1C(Base):
    __tablename__ = 'ma_mount_po_po_1_c'
    __table_args__ = (
        Index('ma_mount_po_po_1_alt', 'ma_mount_po_po_1ma_mount_ida', 'ma_mount_po_po_1po_po_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ma_mount_po_po_1ma_mount_ida = Column(String(36))
    ma_mount_po_po_1po_po_idb = Column(String(36))


class Meeting(Base):
    __tablename__ = 'meetings'
    __table_args__ = (
        Index('idx_meet_stat_del', 'assigned_user_id', 'status', 'deleted'),
        Index('idx_meet_par_del', 'parent_id', 'parent_type', 'deleted')
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(50), index=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    location = Column(String(50))
    password = Column(String(50))
    join_url = Column(String(200))
    host_url = Column(String(400))
    displayed_url = Column(String(400))
    creator = Column(String(50))
    external_id = Column(String(50))
    duration_hours = Column(INTEGER(3))
    duration_minutes = Column(INTEGER(2))
    date_start = Column(DateTime, index=True)
    date_end = Column(DateTime)
    parent_type = Column(String(100))
    status = Column(String(100), server_default=text("'Planned'"))
    type = Column(String(255), server_default=text("'Sugar'"))
    parent_id = Column(CHAR(36))
    reminder_time = Column(INTEGER(11), server_default=text("'-1'"))
    email_reminder_time = Column(INTEGER(11), server_default=text("'-1'"))
    email_reminder_sent = Column(TINYINT(1), server_default=text("'0'"))
    outlook_id = Column(String(255))
    sequence = Column(INTEGER(11), server_default=text("'0'"))
    repeat_type = Column(String(36))
    repeat_interval = Column(INTEGER(3), server_default=text("'1'"))
    repeat_dow = Column(String(7))
    repeat_until = Column(Date)
    repeat_count = Column(INTEGER(7))
    repeat_parent_id = Column(CHAR(36))
    recurring_source = Column(String(36))


class MeetingsContact(Base):
    __tablename__ = 'meetings_contacts'
    __table_args__ = (
        Index('idx_meeting_contact', 'meeting_id', 'contact_id'),
    )

    id = Column(String(36), primary_key=True)
    meeting_id = Column(String(36), index=True)
    contact_id = Column(String(36), index=True)
    required = Column(String(1), server_default=text("'1'"))
    accept_status = Column(String(25), server_default=text("'none'"))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class MeetingsCstm(Base):
    __tablename__ = 'meetings_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    jjwg_maps_lng_c = Column(Float(11), server_default=text("'0.00000000'"))
    jjwg_maps_lat_c = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_geocode_status_c = Column(String(255))
    jjwg_maps_address_c = Column(String(255))


class MeetingsLead(Base):
    __tablename__ = 'meetings_leads'
    __table_args__ = (
        Index('idx_meeting_lead', 'meeting_id', 'lead_id'),
    )

    id = Column(String(36), primary_key=True)
    meeting_id = Column(String(36), index=True)
    lead_id = Column(String(36), index=True)
    required = Column(String(1), server_default=text("'1'"))
    accept_status = Column(String(25), server_default=text("'none'"))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class MeetingsUser(Base):
    __tablename__ = 'meetings_users'
    __table_args__ = (
        Index('idx_meeting_users', 'meeting_id', 'user_id'),
    )

    id = Column(String(36), primary_key=True)
    meeting_id = Column(String(36), index=True)
    user_id = Column(String(36), index=True)
    required = Column(String(1), server_default=text("'1'"))
    accept_status = Column(String(25), server_default=text("'none'"))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class NodeNode(Base):
    __tablename__ = 'node_node'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    organization = Column(String(100), server_default=text("'gts'"))


class NodeNodeAudit(Base):
    __tablename__ = 'node_node_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class NodeNodeDocumentsC(Base):
    __tablename__ = 'node_node_documents_c'
    __table_args__ = (
        Index('node_node_documents_alt', 'node_node_documentsnode_node_ida', 'node_node_documentsdocuments_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    node_node_documentsnode_node_ida = Column(String(36))
    node_node_documentsdocuments_idb = Column(String(36))
    document_revision_id = Column(String(36))


class NodeNodeNotesC(Base):
    __tablename__ = 'node_node_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    node_node_notesnode_node_ida = Column(String(36), index=True)
    node_node_notesnotes_idb = Column(String(36), index=True)


class NodeNodeProjectC(Base):
    __tablename__ = 'node_node_project_c'
    __table_args__ = (
        Index('node_node_project_alt', 'node_node_projectnode_node_ida', 'node_node_projectproject_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    node_node_projectnode_node_ida = Column(String(36))
    node_node_projectproject_idb = Column(String(36))


class NodeNodeTasksC(Base):
    __tablename__ = 'node_node_tasks_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    node_node_tasksnode_node_ida = Column(String(36), index=True)
    node_node_taskstasks_idb = Column(String(36), index=True)


class Note(Base):
    __tablename__ = 'notes'
    __table_args__ = (
        Index('idx_notes_assigned_del', 'deleted', 'assigned_user_id'),
        Index('idx_notes_parent', 'parent_id', 'parent_type')
    )

    assigned_user_id = Column(CHAR(36))
    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(255), index=True)
    file_mime_type = Column(String(100))
    filename = Column(String(255))
    parent_type = Column(String(255))
    parent_id = Column(CHAR(36))
    contact_id = Column(CHAR(36), index=True)
    portal_flag = Column(TINYINT(1))
    embed_flag = Column(TINYINT(1), server_default=text("'0'"))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class NotesCstm(Base):
    __tablename__ = 'notes_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    peeve_c = Column(TINYINT(1), server_default=text("'0'"))
    move_c = Column(TINYINT(1), server_default=text("'0'"))


class OauthConsumer(Base):
    __tablename__ = 'oauth_consumer'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    c_key = Column(String(255), unique=True)
    c_secret = Column(String(255))


class OauthNonce(Base):
    __tablename__ = 'oauth_nonce'
    __table_args__ = (
        Index('oauth_nonce_keyts', 'conskey', 'nonce_ts'),
    )

    conskey = Column(String(32), primary_key=True, nullable=False)
    nonce = Column(String(32), primary_key=True, nullable=False)
    nonce_ts = Column(BIGINT(20))


class OauthToken(Base):
    __tablename__ = 'oauth_tokens'
    __table_args__ = (
        Index('oauth_state_ts', 'tstate', 'token_ts'),
    )

    id = Column(CHAR(36), primary_key=True, nullable=False)
    secret = Column(String(32))
    tstate = Column(String(1))
    consumer = Column(CHAR(36), nullable=False, index=True)
    token_ts = Column(BIGINT(20))
    verify = Column(String(32))
    deleted = Column(TINYINT(1), primary_key=True, nullable=False, server_default=text("'0'"))
    callback_url = Column(String(255))
    assigned_user_id = Column(CHAR(36))


class ObjNNetObj(Base):
    __tablename__ = 'obj_n_net_obj'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))


class ObjNNetObjAccounts1C(Base):
    __tablename__ = 'obj_n_net_obj_accounts_1_c'
    __table_args__ = (
        Index('obj_n_net_obj_accounts_1_alt', 'obj_n_net_obj_accounts_1obj_n_net_obj_ida', 'obj_n_net_obj_accounts_1accounts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    obj_n_net_obj_accounts_1obj_n_net_obj_ida = Column(String(36))
    obj_n_net_obj_accounts_1accounts_idb = Column(String(36))


class ObjNNetObjAudit(Base):
    __tablename__ = 'obj_n_net_obj_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class ObjNNetObjCstm(Base):
    __tablename__ = 'obj_n_net_obj_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    num_obj_c = Column(INTEGER(255))
    address_obj_c = Column(String(255))
    photo_obj_c = Column(String(255))
    address_map_obj_c = Column(String(255), server_default=text("'maps.google.com?q= Russia, Kirov, {address_obj_c}&output=embed'"))
    photo_obj2_c = Column(String(255))
    photo_obj3_c = Column(String(255))
    photo_obj4_c = Column(String(255))
    photo_obj5_c = Column(String(255))
    photo_obj6_c = Column(String(255))
    devices_for_audit_c = Column(Text)
    status_obj_c = Column(String(100))
    photo_others_c = Column(Text)


class ObjNNetObjDocuments1C(Base):
    __tablename__ = 'obj_n_net_obj_documents_1_c'
    __table_args__ = (
        Index('obj_n_net_obj_documents_1_alt', 'obj_n_net_obj_documents_1obj_n_net_obj_ida', 'obj_n_net_obj_documents_1documents_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    obj_n_net_obj_documents_1obj_n_net_obj_ida = Column(String(36))
    obj_n_net_obj_documents_1documents_idb = Column(String(36))
    document_revision_id = Column(String(36))


class ObjNNetObjPoPo1C(Base):
    __tablename__ = 'obj_n_net_obj_po_po_1_c'
    __table_args__ = (
        Index('obj_n_net_obj_po_po_1_alt', 'obj_n_net_obj_po_po_1obj_n_net_obj_ida', 'obj_n_net_obj_po_po_1po_po_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    obj_n_net_obj_po_po_1obj_n_net_obj_ida = Column(String(36))
    obj_n_net_obj_po_po_1po_po_idb = Column(String(36))


class ObjNNetObjRaActions1C(Base):
    __tablename__ = 'obj_n_net_obj_ra_actions_1_c'
    __table_args__ = (
        Index('obj_n_net_obj_ra_actions_1_alt', 'obj_n_net_obj_ra_actions_1obj_n_net_obj_ida', 'obj_n_net_obj_ra_actions_1ra_actions_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    obj_n_net_obj_ra_actions_1obj_n_net_obj_ida = Column(String(36))
    obj_n_net_obj_ra_actions_1ra_actions_idb = Column(String(36))


class ObjNNetObjRaClaim1C(Base):
    __tablename__ = 'obj_n_net_obj_ra_claim_1_c'
    __table_args__ = (
        Index('obj_n_net_obj_ra_claim_1_alt', 'obj_n_net_obj_ra_claim_1obj_n_net_obj_ida', 'obj_n_net_obj_ra_claim_1ra_claim_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    obj_n_net_obj_ra_claim_1obj_n_net_obj_ida = Column(String(36))
    obj_n_net_obj_ra_claim_1ra_claim_idb = Column(String(36))


class ObjNNetObjSecuritygroups1C(Base):
    __tablename__ = 'obj_n_net_obj_securitygroups_1_c'
    __table_args__ = (
        Index('obj_n_net_obj_securitygroups_1_alt', 'obj_n_net_obj_securitygroups_1obj_n_net_obj_ida', 'obj_n_net_obj_securitygroups_1securitygroups_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    obj_n_net_obj_securitygroups_1obj_n_net_obj_ida = Column(String(36))
    obj_n_net_obj_securitygroups_1securitygroups_idb = Column(String(36))


class Opportunity(Base):
    __tablename__ = 'opportunities'
    __table_args__ = (
        Index('idx_opp_id_deleted', 'id', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(50), index=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36), index=True)
    opportunity_type = Column(String(255))
    campaign_id = Column(CHAR(36))
    lead_source = Column(String(100))
    amount = Column(Float(asdecimal=True))
    amount_usdollar = Column(Float(asdecimal=True))
    currency_id = Column(CHAR(36))
    date_closed = Column(Date)
    next_step = Column(String(100))
    sales_stage = Column(String(255))
    probability = Column(Float(asdecimal=True))


class OpportunitiesAudit(Base):
    __tablename__ = 'opportunities_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class OpportunitiesContact(Base):
    __tablename__ = 'opportunities_contacts'
    __table_args__ = (
        Index('idx_opportunities_contacts', 'opportunity_id', 'contact_id'),
    )

    id = Column(String(36), primary_key=True)
    contact_id = Column(String(36), index=True)
    opportunity_id = Column(String(36), index=True)
    contact_role = Column(String(50))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class OpportunitiesCstm(Base):
    __tablename__ = 'opportunities_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    wifi_bandwidth_opp_c = Column(INTEGER(255))
    internet_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    opp_date_opp_c = Column(Date)
    phone_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    pdcpgi_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    pvk_opp_c = Column(INTEGER(255))
    inet_bandwidth_opp_c = Column(Float(18))
    packet_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    vats_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    tv_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    cctv_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    ip_cost_opp_c = Column(INTEGER(255))
    closed_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    blockletter_opp_c = Column(TINYINT(1), server_default=text("'0'"))
    date_blockletter_opp_c = Column(Date)
    close_date_c = Column(Date)
    date_apply_c = Column(Date)
    organization_opp_c = Column(String(100), server_default=text("'empty'"))
    code_fineko_c = Column(INTEGER(255))
    type_cost_opp_c = Column(String(100), server_default=text("'zero'"))
    billing_id_opp_c = Column(INTEGER(255))
    cost_pdcpgi_opp_c = Column(INTEGER(255))
    quantity_phone_lines_c = Column(INTEGER(255))
    jjwg_maps_lng_c = Column(Float(11), server_default=text("'0.00000000'"))
    jjwg_maps_lat_c = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_geocode_status_c = Column(String(255))
    jjwg_maps_address_c = Column(String(255))


class OutboundEmail(Base):
    __tablename__ = 'outbound_email'
    __table_args__ = (
        Index('oe_user_id_idx', 'id', 'user_id'),
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(50))
    type = Column(String(15), server_default=text("'user'"))
    user_id = Column(CHAR(36), nullable=False)
    mail_sendtype = Column(String(8), server_default=text("'smtp'"))
    mail_smtptype = Column(String(20), server_default=text("'other'"))
    mail_smtpserver = Column(String(100))
    mail_smtpport = Column(INTEGER(5), server_default=text("'0'"))
    mail_smtpuser = Column(String(100))
    mail_smtppass = Column(String(100))
    mail_smtpauth_req = Column(TINYINT(1), server_default=text("'0'"))
    mail_smtpssl = Column(INTEGER(1), server_default=text("'0'"))


class PaPlanAcces(Base):
    __tablename__ = 'pa_plan_access'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    date_plan = Column(Date)
    date_complete = Column(Date)
    status_plan_access = Column(String(100), server_default=text("'planed'"))
    type_plan_access = Column(String(100), server_default=text("'call'"))


class PaPlanAccessAccFacilityC(Base):
    __tablename__ = 'pa_plan_access_acc_facility_c'
    __table_args__ = (
        Index('pa_plan_access_acc_facility_alt', 'pa_plan_access_acc_facilitypa_plan_access_ida', 'pa_plan_access_acc_facilityacc_facility_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    pa_plan_access_acc_facilitypa_plan_access_ida = Column(String(36))
    pa_plan_access_acc_facilityacc_facility_idb = Column(String(36))


class PaPlanAccessAccRequisitionC(Base):
    __tablename__ = 'pa_plan_access_acc_requisition_c'
    __table_args__ = (
        Index('pa_plan_access_acc_requisition_alt', 'pa_plan_access_acc_requisitionpa_plan_access_ida', 'pa_plan_access_acc_requisitionacc_requisition_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    pa_plan_access_acc_requisitionpa_plan_access_ida = Column(String(36))
    pa_plan_access_acc_requisitionacc_requisition_idb = Column(String(36))


class PaPlanAccessAccUkC(Base):
    __tablename__ = 'pa_plan_access_acc_uk_c'
    __table_args__ = (
        Index('pa_plan_access_acc_uk_alt', 'pa_plan_access_acc_ukpa_plan_access_ida', 'pa_plan_access_acc_ukacc_uk_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    pa_plan_access_acc_ukpa_plan_access_ida = Column(String(36))
    pa_plan_access_acc_ukacc_uk_idb = Column(String(36))


class PaPlanAccessAudit(Base):
    __tablename__ = 'pa_plan_access_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PaPlanAccessCstm(Base):
    __tablename__ = 'pa_plan_access_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    type_request_c = Column(String(100), server_default=text("'new'"))
    area_c = Column(String(255))
    type_account_c = Column(String(100), server_default=text("'uk'"))
    acc_uk_id_c = Column(CHAR(36))
    acc_requisition_id_c = Column(CHAR(36))


class PaPlanAccessNotesC(Base):
    __tablename__ = 'pa_plan_access_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    pa_plan_access_notespa_plan_access_ida = Column(String(36), index=True)
    pa_plan_access_notesnotes_idb = Column(String(36), index=True)


class PhmoPhoto(Base):
    __tablename__ = 'phmo_photo'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    document_name = Column(String(255))
    filename = Column(String(255))
    file_ext = Column(String(100))
    file_mime_type = Column(String(100))
    active_date = Column(Date)
    exp_date = Column(Date)
    category_id = Column(String(100))
    subcategory_id = Column(String(100))
    status_id = Column(String(100))


class PhmoPhotoAudit(Base):
    __tablename__ = 'phmo_photo_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PhmoPhotoCstm(Base):
    __tablename__ = 'phmo_photo_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    photo_ph_mounts_c = Column(String(255))


class PhysiCasesP(Base):
    __tablename__ = 'physi_cases_p'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    case_numb = Column(INTEGER(255))
    date_case = Column(DateTime)
    date_close = Column(DateTime)
    resolution = Column(Text)
    status = Column(String(100), server_default=text("'New'"))
    priority = Column(String(100), server_default=text("'P1'"))
    physi_phisic_id_c = Column(CHAR(36))


class PhysiCasesPAudit(Base):
    __tablename__ = 'physi_cases_p_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PhysiCasesPNotesC(Base):
    __tablename__ = 'physi_cases_p_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    physi_cases_p_notesphysi_cases_p_ida = Column(String(36), index=True)
    physi_cases_p_notesnotes_idb = Column(String(36), index=True)


class PhysiContractNetwork(Base):
    __tablename__ = 'physi_contract_network'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    date_contr = Column(Date)
    organization = Column(String(100), server_default=text("'gts'"))
    bandwidth = Column(String(255))
    cost = Column(INTEGER(255))
    block = Column(TINYINT(1), server_default=text("'0'"))
    tarif = Column(Text)
    address = Column(String(255))


class PhysiContractNetworkAudit(Base):
    __tablename__ = 'physi_contract_network_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PhysiContractNetworkNotesC(Base):
    __tablename__ = 'physi_contract_network_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    physi_contract_network_notesphysi_contract_network_ida = Column(String(36), index=True)
    physi_contract_network_notesnotes_idb = Column(String(36), index=True)


class PhysiContractPhone(Base):
    __tablename__ = 'physi_contract_phone'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    date_contr = Column(Date)
    cost = Column(String(255))
    tarif = Column(Text)
    address = Column(String(255))


class PhysiContractPhoneAudit(Base):
    __tablename__ = 'physi_contract_phone_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PhysiContractPhoneNotesC(Base):
    __tablename__ = 'physi_contract_phone_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    physi_contract_phone_notesphysi_contract_phone_ida = Column(String(36), index=True)
    physi_contract_phone_notesnotes_idb = Column(String(36), index=True)


class PhysiPhisic(Base):
    __tablename__ = 'physi_phisic'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    address = Column(String(255))
    phone = Column(String(255))
    mobile = Column(String(255))
    email = Column(String(255))
    serial_passport = Column(String(5))
    number_passport = Column(String(6))
    issue_passport = Column(String(255))
    date_passport = Column(Date)


class PhysiPhisicAudit(Base):
    __tablename__ = 'physi_phisic_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PhysiPhisicCallsC(Base):
    __tablename__ = 'physi_phisic_calls_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    physi_phisic_callsphysi_phisic_ida = Column(String(36), index=True)
    physi_phisic_callscalls_idb = Column(String(36), index=True)


class PhysiPhisicNotesC(Base):
    __tablename__ = 'physi_phisic_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    physi_phisic_notesphysi_phisic_ida = Column(String(36), index=True)
    physi_phisic_notesnotes_idb = Column(String(36), index=True)


class PhysiPhisicPhysiCasesPC(Base):
    __tablename__ = 'physi_phisic_physi_cases_p_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    physi_phisic_physi_cases_pphysi_phisic_ida = Column(String(36), index=True)
    physi_phisic_physi_cases_pphysi_cases_p_idb = Column(String(36), index=True)


class PhysiPhisicPhysiContractNetworkC(Base):
    __tablename__ = 'physi_phisic_physi_contract_network_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    physi_phisic_physi_contract_networkphysi_phisic_ida = Column(String(36), index=True)
    physi_phisic_physi_contract_networkphysi_contract_network_idb = Column(String(36), index=True)


class PhysiPhisicPhysiContractPhoneC(Base):
    __tablename__ = 'physi_phisic_physi_contract_phone_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    physi_phisic_physi_contract_phonephysi_phisic_ida = Column(String(36), index=True)
    physi_phisic_physi_contract_phonephysi_contract_phone_idb = Column(String(36), index=True)


class PhysiRequest(Base):
    __tablename__ = 'physi_request'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    document_name = Column(String(255))
    filename = Column(String(255))
    file_ext = Column(String(100))
    file_mime_type = Column(String(100))
    active_date = Column(Date)
    exp_date = Column(Date)
    category_id = Column(String(100))
    subcategory_id = Column(String(100))
    status_id = Column(String(100))


class PhysiRequestAudit(Base):
    __tablename__ = 'physi_request_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PoPo(Base):
    __tablename__ = 'po_po'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    parent_type = Column(String(255))
    parent_id = Column(CHAR(36))


class PoPoAudit(Base):
    __tablename__ = 'po_po_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PoPoConPConnectionsPlan1C(Base):
    __tablename__ = 'po_po_con_p_connections_plan_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    po_po_con_p_connections_plan_1po_po_ida = Column(String(36), index=True)
    po_po_con_p_connections_plan_1con_p_connections_plan_idb = Column(String(36), index=True)


class PoPoCstm(Base):
    __tablename__ = 'po_po_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    invnum_c = Column(String(255))
    status_c = Column(String(100), server_default=text("'three'"))
    hardware_types_c = Column(String(100))
    account_id_c = Column(CHAR(36))


class PoPoNotes1C(Base):
    __tablename__ = 'po_po_notes_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    po_po_notes_1po_po_ida = Column(String(36), index=True)
    po_po_notes_1notes_idb = Column(String(36), index=True)


class PoPoRepRepairs1C(Base):
    __tablename__ = 'po_po_rep_repairs_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    po_po_rep_repairs_1po_po_ida = Column(String(36), index=True)
    po_po_rep_repairs_1rep_repairs_idb = Column(String(36), index=True)


class Project(Base):
    __tablename__ = 'project'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    assigned_user_id = Column(CHAR(36))
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(50))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    estimated_start_date = Column(Date)
    estimated_end_date = Column(Date)
    status = Column(String(255))
    priority = Column(String(255))


class ProjectCstm(Base):
    __tablename__ = 'project_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    date_close_c = Column(Date)
    jjwg_maps_lng_c = Column(Float(11), server_default=text("'0.00000000'"))
    jjwg_maps_lat_c = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_geocode_status_c = Column(String(255))
    jjwg_maps_address_c = Column(String(255))


class ProjectTask(Base):
    __tablename__ = 'project_task'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    project_id = Column(CHAR(36), nullable=False)
    project_task_id = Column(INTEGER(11))
    name = Column(String(50))
    status = Column(String(255))
    description = Column(Text)
    predecessors = Column(Text)
    date_start = Column(Date)
    time_start = Column(INTEGER(11))
    time_finish = Column(INTEGER(11))
    date_finish = Column(Date)
    duration = Column(INTEGER(11))
    duration_unit = Column(Text)
    actual_duration = Column(INTEGER(11))
    percent_complete = Column(INTEGER(11))
    date_due = Column(Date)
    time_due = Column(Time)
    parent_task_id = Column(INTEGER(11))
    assigned_user_id = Column(CHAR(36))
    modified_user_id = Column(CHAR(36))
    priority = Column(String(255))
    created_by = Column(CHAR(36))
    milestone_flag = Column(TINYINT(1))
    order_number = Column(INTEGER(11), server_default=text("'1'"))
    task_number = Column(INTEGER(11))
    estimated_effort = Column(INTEGER(11))
    actual_effort = Column(INTEGER(11))
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    utilization = Column(INTEGER(11), server_default=text("'100'"))


class ProjectTaskAudit(Base):
    __tablename__ = 'project_task_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class ProjectsAccount(Base):
    __tablename__ = 'projects_accounts'
    __table_args__ = (
        Index('projects_accounts_alt', 'project_id', 'account_id'),
    )

    id = Column(String(36), primary_key=True)
    account_id = Column(String(36), index=True)
    project_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ProjectsBug(Base):
    __tablename__ = 'projects_bugs'
    __table_args__ = (
        Index('projects_bugs_alt', 'project_id', 'bug_id'),
    )

    id = Column(String(36), primary_key=True)
    bug_id = Column(String(36), index=True)
    project_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ProjectsCase(Base):
    __tablename__ = 'projects_cases'
    __table_args__ = (
        Index('projects_cases_alt', 'project_id', 'case_id'),
    )

    id = Column(String(36), primary_key=True)
    case_id = Column(String(36), index=True)
    project_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ProjectsContact(Base):
    __tablename__ = 'projects_contacts'
    __table_args__ = (
        Index('projects_contacts_alt', 'project_id', 'contact_id'),
    )

    id = Column(String(36), primary_key=True)
    contact_id = Column(String(36), index=True)
    project_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ProjectsOpportunity(Base):
    __tablename__ = 'projects_opportunities'
    __table_args__ = (
        Index('projects_opportunities_alt', 'project_id', 'opportunity_id'),
    )

    id = Column(String(36), primary_key=True)
    opportunity_id = Column(String(36), index=True)
    project_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ProjectsProduct(Base):
    __tablename__ = 'projects_products'
    __table_args__ = (
        Index('projects_products_alt', 'project_id', 'product_id'),
    )

    id = Column(String(36), primary_key=True)
    product_id = Column(String(36), index=True)
    project_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ProjecttaskContacts1C(Base):
    __tablename__ = 'projecttask_contacts_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    projecttask_contacts_1projecttask_ida = Column(String(36), index=True)
    projecttask_contacts_1contacts_idb = Column(String(36), index=True)


class ProspectListCampaign(Base):
    __tablename__ = 'prospect_list_campaigns'
    __table_args__ = (
        Index('idx_prospect_list_campaigns', 'prospect_list_id', 'campaign_id'),
    )

    id = Column(String(36), primary_key=True)
    prospect_list_id = Column(String(36), index=True)
    campaign_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class ProspectList(Base):
    __tablename__ = 'prospect_lists'

    assigned_user_id = Column(CHAR(36))
    id = Column(CHAR(36), primary_key=True)
    name = Column(String(50), index=True)
    list_type = Column(String(100))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    deleted = Column(TINYINT(1))
    description = Column(Text)
    domain_name = Column(String(255))


class ProspectListsProspect(Base):
    __tablename__ = 'prospect_lists_prospects'
    __table_args__ = (
        Index('idx_plp_rel_id', 'related_id', 'related_type', 'prospect_list_id'),
    )

    id = Column(String(36), primary_key=True)
    prospect_list_id = Column(String(36), index=True)
    related_id = Column(String(36))
    related_type = Column(String(25))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class Prospect(Base):
    __tablename__ = 'prospects'
    __table_args__ = (
        Index('idx_prospects_id_del', 'id', 'deleted'),
        Index('idx_prospects_last_first', 'last_name', 'first_name', 'deleted'),
        Index('idx_prospecs_del_last', 'last_name', 'deleted')
    )

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36), index=True)
    salutation = Column(String(255))
    first_name = Column(String(100))
    last_name = Column(String(100))
    title = Column(String(100))
    department = Column(String(255))
    do_not_call = Column(TINYINT(1), server_default=text("'0'"))
    phone_home = Column(String(100))
    phone_mobile = Column(String(100))
    phone_work = Column(String(100))
    phone_other = Column(String(100))
    phone_fax = Column(String(100))
    primary_address_street = Column(String(150))
    primary_address_city = Column(String(100))
    primary_address_state = Column(String(100))
    primary_address_postalcode = Column(String(20))
    primary_address_country = Column(String(255))
    alt_address_street = Column(String(150))
    alt_address_city = Column(String(100))
    alt_address_state = Column(String(100))
    alt_address_postalcode = Column(String(20))
    alt_address_country = Column(String(255))
    assistant = Column(String(75))
    assistant_phone = Column(String(100))
    tracker_key = Column(INTEGER(11), nullable=False, index=True)
    birthdate = Column(Date)
    lead_id = Column(CHAR(36))
    account_name = Column(String(150))
    campaign_id = Column(CHAR(36))


class ProspectsCstm(Base):
    __tablename__ = 'prospects_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    jjwg_maps_lng_c = Column(Float(11), server_default=text("'0.00000000'"))
    jjwg_maps_lat_c = Column(Float(10), server_default=text("'0.00000000'"))
    jjwg_maps_geocode_status_c = Column(String(255))
    jjwg_maps_address_c = Column(String(255))


class PurPurchase(Base):
    __tablename__ = 'pur_purchases'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    grouppur = Column(String(100))
    type = Column(String(100), server_default=text("'new'"))
    status = Column(String(100), server_default=text("'requisition'"))
    date_pur = Column(Date)
    purpose = Column(Text)
    cost = Column(INTEGER(255))


class PurPurchasesAudit(Base):
    __tablename__ = 'pur_purchases_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class PurPurchasesNotesC(Base):
    __tablename__ = 'pur_purchases_notes_c'
    __table_args__ = (
        Index('pur_purchases_notes_alt', 'pur_purchases_notespur_purchases_ida', 'pur_purchases_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    pur_purchases_notespur_purchases_ida = Column(String(36))
    pur_purchases_notesnotes_idb = Column(String(36))


class QuQuestion(Base):
    __tablename__ = 'qu_question'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    type = Column(String(100), server_default=text("'new'"))
    user_id_c = Column(CHAR(36))
    account_id_c = Column(CHAR(36))
    date_question = Column(Date)
    user_accounts = Column(String(255))
    service_problem = Column(Text)
    support_calls = Column(String(100), server_default=text("'none'"))
    support = Column(String(100), server_default=text("'none'"))
    install = Column(String(100), server_default=text("'none'"))
    sell = Column(String(100), server_default=text("'none'"))
    quality_client = Column(String(100), server_default=text("'0'"))


class QuQuestionAccountsC(Base):
    __tablename__ = 'qu_question_accounts_c'
    __table_args__ = (
        Index('qu_question_accounts_alt', 'qu_question_accountsqu_question_ida', 'qu_question_accountsaccounts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    qu_question_accountsqu_question_ida = Column(String(36))
    qu_question_accountsaccounts_idb = Column(String(36))


class QuQuestionAudit(Base):
    __tablename__ = 'qu_question_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class RaAction(Base):
    __tablename__ = 'ra_actions'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    planactiondate = Column(DateTime)
    actiondate = Column(DateTime)
    planduration = Column(INTEGER(255))
    duration = Column(INTEGER(255))
    noservice = Column(TINYINT(1), server_default=text("'0'"))
    plannoservice = Column(TINYINT(1), server_default=text("'0'"))
    address = Column(String(255))
    status = Column(String(100), server_default=text("'adapting'"))
    goal = Column(Text)
    comment = Column(Text)


class RaActionsAccountsC(Base):
    __tablename__ = 'ra_actions_accounts_c'
    __table_args__ = (
        Index('ra_actions_accounts_alt', 'ra_actions_accountsra_actions_ida', 'ra_actions_accountsaccounts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_actions_accountsra_actions_ida = Column(String(36))
    ra_actions_accountsaccounts_idb = Column(String(36))


class RaActionsAudit(Base):
    __tablename__ = 'ra_actions_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class RaActionsCasesC(Base):
    __tablename__ = 'ra_actions_cases_c'
    __table_args__ = (
        Index('ra_actions_cases_alt', 'ra_actions_casesra_actions_ida', 'ra_actions_casescases_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_actions_casesra_actions_ida = Column(String(36))
    ra_actions_casescases_idb = Column(String(36))


class RaActionsNotesC(Base):
    __tablename__ = 'ra_actions_notes_c'
    __table_args__ = (
        Index('ra_actions_notes_alt', 'ra_actions_notesra_actions_ida', 'ra_actions_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_actions_notesra_actions_ida = Column(String(36))
    ra_actions_notesnotes_idb = Column(String(36))


class RaActionsSecuritygroups1C(Base):
    __tablename__ = 'ra_actions_securitygroups_1_c'
    __table_args__ = (
        Index('ra_actions_securitygroups_1_alt', 'ra_actions_securitygroups_1ra_actions_ida', 'ra_actions_securitygroups_1securitygroups_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_actions_securitygroups_1ra_actions_ida = Column(String(36))
    ra_actions_securitygroups_1securitygroups_idb = Column(String(36))


class RaActionsTasksC(Base):
    __tablename__ = 'ra_actions_tasks_c'
    __table_args__ = (
        Index('ra_actions_tasks_alt', 'ra_actions_tasksra_actions_ida', 'ra_actions_taskstasks_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_actions_tasksra_actions_ida = Column(String(36))
    ra_actions_taskstasks_idb = Column(String(36))


class RaClaim(Base):
    __tablename__ = 'ra_claim'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    date_event = Column(Date)
    group_onus = Column(String(100))
    volume = Column(Text)


class RaClaimAudit(Base):
    __tablename__ = 'ra_claim_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class RaClaimBugs1C(Base):
    __tablename__ = 'ra_claim_bugs_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_claim_bugs_1ra_claim_ida = Column(String(36), index=True)
    ra_claim_bugs_1bugs_idb = Column(String(36), index=True)


class RaClaimCasesC(Base):
    __tablename__ = 'ra_claim_cases_c'
    __table_args__ = (
        Index('ra_claim_cases_alt', 'ra_claim_casesra_claim_ida', 'ra_claim_casescases_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_claim_casesra_claim_ida = Column(String(36))
    ra_claim_casescases_idb = Column(String(36))


class RaClaimNotesC(Base):
    __tablename__ = 'ra_claim_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_claim_notesra_claim_ida = Column(String(36), index=True)
    ra_claim_notesnotes_idb = Column(String(36), index=True)


class RaClaimPhysiCasesPC(Base):
    __tablename__ = 'ra_claim_physi_cases_p_c'
    __table_args__ = (
        Index('ra_claim_physi_cases_p_alt', 'ra_claim_physi_cases_pra_claim_ida', 'ra_claim_physi_cases_pphysi_cases_p_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_claim_physi_cases_pra_claim_ida = Column(String(36))
    ra_claim_physi_cases_pphysi_cases_p_idb = Column(String(36))


class RaClaimRaActionsC(Base):
    __tablename__ = 'ra_claim_ra_actions_c'
    __table_args__ = (
        Index('ra_claim_ra_actions_alt', 'ra_claim_ra_actionsra_claim_ida', 'ra_claim_ra_actionsra_actions_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_claim_ra_actionsra_claim_ida = Column(String(36))
    ra_claim_ra_actionsra_actions_idb = Column(String(36))


class RaSurvey(Base):
    __tablename__ = 'ra_survey'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    address = Column(String(255))
    contact = Column(String(255))
    status = Column(String(100), server_default=text("'request'"))
    description_survey = Column(Text)
    date_request = Column(Date)
    addressmap = Column(String(255), server_default=text("'maps.google.com?q= Russia, Kirov, {address}&output=embed'"))
    date_survey = Column(Date)
    resolution = Column(String(255))


class RaSurveyAccRequisition1C(Base):
    __tablename__ = 'ra_survey_acc_requisition_1_c'
    __table_args__ = (
        Index('ra_survey_acc_requisition_1_alt', 'ra_survey_acc_requisition_1ra_survey_ida', 'ra_survey_acc_requisition_1acc_requisition_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_survey_acc_requisition_1ra_survey_ida = Column(String(36))
    ra_survey_acc_requisition_1acc_requisition_idb = Column(String(36))


class RaSurveyAccountsC(Base):
    __tablename__ = 'ra_survey_accounts_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_survey_accountsra_survey_ida = Column(String(36), index=True)
    ra_survey_accountsaccounts_idb = Column(String(36), index=True)


class RaSurveyAudit(Base):
    __tablename__ = 'ra_survey_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class RaSurveyCstm(Base):
    __tablename__ = 'ra_survey_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    source_inf_c = Column(Text)
    permit_installation_c = Column(String(100), server_default=text("'none'"))
    ess_comment_c = Column(Text)
    date_installation_c = Column(Date)
    position_c = Column(String(50))
    maps_pos_c = Column(String(255), server_default=text("'https://www.google.ru/maps/place/58.6008947,49.6473304,14z'"))
    status_rs_c = Column(String(100), server_default=text("'none'"))
    comment_rs_c = Column(Text)


class RaSurveyNotesC(Base):
    __tablename__ = 'ra_survey_notes_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_survey_notesra_survey_ida = Column(String(36), index=True)
    ra_survey_notesnotes_idb = Column(String(36), index=True)


class RaSurveyPhysiPhisicC(Base):
    __tablename__ = 'ra_survey_physi_phisic_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    ra_survey_physi_phisicra_survey_ida = Column(String(36), index=True)
    ra_survey_physi_phisicphysi_phisic_idb = Column(String(36), index=True)


class Relationship(Base):
    __tablename__ = 'relationships'

    id = Column(CHAR(36), primary_key=True)
    relationship_name = Column(String(150), index=True)
    lhs_module = Column(String(100))
    lhs_table = Column(String(64))
    lhs_key = Column(String(64))
    rhs_module = Column(String(100))
    rhs_table = Column(String(64))
    rhs_key = Column(String(64))
    join_table = Column(String(128))
    join_key_lhs = Column(String(128))
    join_key_rhs = Column(String(128))
    relationship_type = Column(String(64))
    relationship_role_column = Column(String(64))
    relationship_role_column_value = Column(String(50))
    reverse = Column(TINYINT(1), server_default=text("'0'"))
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class Release(Base):
    __tablename__ = 'releases'
    __table_args__ = (
        Index('idx_releases', 'name', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    deleted = Column(TINYINT(1))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(50))
    list_order = Column(INTEGER(4))
    status = Column(String(100))


class RepRepair(Base):
    __tablename__ = 'rep_repairs'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))


class RepRepairsAudit(Base):
    __tablename__ = 'rep_repairs_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class RepRepairsBugs1C(Base):
    __tablename__ = 'rep_repairs_bugs_1_c'
    __table_args__ = (
        Index('rep_repairs_bugs_1_alt', 'rep_repairs_bugs_1rep_repairs_ida', 'rep_repairs_bugs_1bugs_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    rep_repairs_bugs_1rep_repairs_ida = Column(String(36))
    rep_repairs_bugs_1bugs_idb = Column(String(36))


class RepRepairsCstm(Base):
    __tablename__ = 'rep_repairs_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    user_id_c = Column(CHAR(36))
    user_id1_c = Column(CHAR(36))
    date_of_completion_c = Column(Date)
    cat_work_c = Column(String(100), server_default=text("'1'"))
    account_id_c = Column(CHAR(36))
    address_c = Column(String(255))
    check_ovm_c = Column(TINYINT(1), server_default=text("'0'"))
    photo_one_c = Column(String(255))
    photo_two_c = Column(String(255))
    photo_three_c = Column(String(255))
    photo_four_c = Column(String(255))
    photo_five_c = Column(String(255))
    photo_six_c = Column(String(255))
    contacts_c = Column(String(255))
    time_c = Column(String(255))
    user_id2_c = Column(CHAR(36))
    status_c = Column(String(100), server_default=text("'one'"))
    comment_c = Column(Text)
    new_cat_work_c = Column(Text)


class RepRepairsNotes1C(Base):
    __tablename__ = 'rep_repairs_notes_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    rep_repairs_notes_1rep_repairs_ida = Column(String(36), index=True)
    rep_repairs_notes_1notes_idb = Column(String(36), index=True)


class RepTechnicalConnection(Base):
    __tablename__ = 'rep_technical_connections'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    date_work = Column(Date)
    type = Column(String(100))


class RepTechnicalConnectionsAudit(Base):
    __tablename__ = 'rep_technical_connections_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class Role(Base):
    __tablename__ = 'roles'
    __table_args__ = (
        Index('idx_role_id_del', 'id', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(150))
    description = Column(Text)
    modules = Column(Text)
    deleted = Column(TINYINT(1))


class RolesModule(Base):
    __tablename__ = 'roles_modules'

    id = Column(String(36), primary_key=True)
    role_id = Column(String(36), index=True)
    module_id = Column(String(36), index=True)
    allow = Column(TINYINT(1), server_default=text("'0'"))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class RolesUser(Base):
    __tablename__ = 'roles_users'

    id = Column(String(36), primary_key=True)
    role_id = Column(String(36), index=True)
    user_id = Column(String(36), index=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class SavedSearch(Base):
    __tablename__ = 'saved_search'
    __table_args__ = (
        Index('idx_desc', 'name', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(150))
    search_module = Column(String(150))
    deleted = Column(TINYINT(1))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    assigned_user_id = Column(CHAR(36))
    contents = Column(Text)
    description = Column(Text)


class Scheduler(Base):
    __tablename__ = 'schedulers'
    __table_args__ = (
        Index('idx_schedule', 'date_time_start', 'deleted'),
    )

    id = Column(String(36), primary_key=True)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    created_by = Column(CHAR(36))
    modified_user_id = Column(CHAR(36))
    name = Column(String(255))
    job = Column(String(255))
    date_time_start = Column(DateTime)
    date_time_end = Column(DateTime)
    job_interval = Column(String(100))
    time_from = Column(Time)
    time_to = Column(Time)
    last_run = Column(DateTime)
    status = Column(String(100))
    catch_up = Column(TINYINT(1), server_default=text("'1'"))


class Securitygroup(Base):
    __tablename__ = 'securitygroups'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    noninheritable = Column(TINYINT(1))


class SecuritygroupsAclRole(Base):
    __tablename__ = 'securitygroups_acl_roles'

    id = Column(CHAR(36), primary_key=True)
    securitygroup_id = Column(CHAR(36))
    role_id = Column(CHAR(36))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class SecuritygroupsAudit(Base):
    __tablename__ = 'securitygroups_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class SecuritygroupsDefault(Base):
    __tablename__ = 'securitygroups_default'

    id = Column(CHAR(36), primary_key=True)
    securitygroup_id = Column(CHAR(36))
    module = Column(String(50))
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class SecuritygroupsRecord(Base):
    __tablename__ = 'securitygroups_records'
    __table_args__ = (
        Index('idx_securitygroups_records_del', 'deleted', 'record_id', 'module', 'securitygroup_id'),
        Index('idx_securitygroups_records_mod', 'module', 'deleted', 'record_id', 'securitygroup_id')
    )

    id = Column(CHAR(36), primary_key=True)
    securitygroup_id = Column(CHAR(36))
    record_id = Column(CHAR(36))
    module = Column(CHAR(36))
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class SecuritygroupsUser(Base):
    __tablename__ = 'securitygroups_users'
    __table_args__ = (
        Index('securitygroups_users_idxd', 'user_id', 'deleted', 'securitygroup_id'),
        Index('securitygroups_users_idxc', 'user_id', 'deleted', 'securitygroup_id', 'id')
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    securitygroup_id = Column(String(36), index=True)
    user_id = Column(String(36), index=True)
    noninheritable = Column(TINYINT(1))


class SkSketch(Base):
    __tablename__ = 'sk_sketch'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    document_name = Column(String(255))
    filename = Column(String(255))
    file_ext = Column(String(100))
    file_mime_type = Column(String(100))
    active_date = Column(Date)
    exp_date = Column(Date)
    category_id = Column(String(100), server_default=text("'scheme'"))
    subcategory_id = Column(String(100), server_default=text("'requisition'"))
    status_id = Column(String(100))
    address = Column(String(255))
    status_requisition = Column(String(100), server_default=text("'request'"))


class SkSketchAccRequisitionC(Base):
    __tablename__ = 'sk_sketch_acc_requisition_c'
    __table_args__ = (
        Index('sk_sketch_acc_requisition_alt', 'sk_sketch_acc_requisitionsk_sketch_ida', 'sk_sketch_acc_requisitionacc_requisition_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    sk_sketch_acc_requisitionsk_sketch_ida = Column(String(36))
    sk_sketch_acc_requisitionacc_requisition_idb = Column(String(36))


class SkSketchAudit(Base):
    __tablename__ = 'sk_sketch_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class SkSketchRaSurveyC(Base):
    __tablename__ = 'sk_sketch_ra_survey_c'
    __table_args__ = (
        Index('sk_sketch_ra_survey_alt', 'sk_sketch_ra_surveysk_sketch_ida', 'sk_sketch_ra_surveyra_survey_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    sk_sketch_ra_surveysk_sketch_ida = Column(String(36))
    sk_sketch_ra_surveyra_survey_idb = Column(String(36))


class Sugarfeed(Base):
    __tablename__ = 'sugarfeed'
    __table_args__ = (
        Index('idx_sgrfeed_rmod_rid_date', 'related_module', 'related_id', 'date_entered'),
        Index('sgrfeed_date', 'date_entered', 'deleted')
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(String(255))
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    related_module = Column(String(100))
    related_id = Column(CHAR(36))
    link_url = Column(String(255))
    link_type = Column(String(30))


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = (
        Index('idx_task_par_del', 'parent_id', 'parent_type', 'deleted'),
        Index('idx_task_con_del', 'contact_id', 'deleted')
    )

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(50), index=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36), index=True)
    status = Column(String(100), index=True, server_default=text("'Not Started'"))
    date_due_flag = Column(TINYINT(1), server_default=text("'0'"))
    date_due = Column(DateTime)
    date_start_flag = Column(TINYINT(1), server_default=text("'0'"))
    date_start = Column(DateTime)
    parent_type = Column(String(255))
    parent_id = Column(CHAR(36))
    contact_id = Column(CHAR(36))
    priority = Column(String(100))


class TasksAccounts1C(Base):
    __tablename__ = 'tasks_accounts_1_c'
    __table_args__ = (
        Index('tasks_accounts_1_alt', 'tasks_accounts_1tasks_ida', 'tasks_accounts_1accounts_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tasks_accounts_1tasks_ida = Column(String(36))
    tasks_accounts_1accounts_idb = Column(String(36))


class TasksCalls1C(Base):
    __tablename__ = 'tasks_calls_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tasks_calls_1tasks_ida = Column(String(36), index=True)
    tasks_calls_1calls_idb = Column(String(36), index=True)


class TcClosecontract(Base):
    __tablename__ = 'tc_closecontract'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    dateclose = Column(Date)
    dateperform = Column(Date)
    user_id_c = Column(CHAR(36))
    opportunity_id_c = Column(CHAR(36))
    note_id_c = Column(CHAR(36))


class TcClosecontractAudit(Base):
    __tablename__ = 'tc_closecontract_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class TcClosecontractNotesC(Base):
    __tablename__ = 'tc_closecontract_notes_c'
    __table_args__ = (
        Index('tc_closecontract_notes_alt', 'tc_closecontract_notestc_closecontract_ida', 'tc_closecontract_notesnotes_idb'),
    )

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_closecontract_notestc_closecontract_ida = Column(String(36))
    tc_closecontract_notesnotes_idb = Column(String(36))


class TcRenamecontract(Base):
    __tablename__ = 'tc_renamecontract'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    daterename = Column(Date)
    dateperform = Column(Date)
    user_id_c = Column(CHAR(36))


class TcRenamecontractAccounts1C(Base):
    __tablename__ = 'tc_renamecontract_accounts_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_renamecontract_accounts_1accounts_ida = Column(String(36), index=True)
    tc_renamecontract_accounts_1tc_renamecontract_idb = Column(String(36), index=True)


class TcRenamecontractAccountsC(Base):
    __tablename__ = 'tc_renamecontract_accounts_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_renamecontract_accountsaccounts_ida = Column(String(36), index=True)
    tc_renamecontract_accountstc_renamecontract_idb = Column(String(36), index=True)


class TcRenamecontractAudit(Base):
    __tablename__ = 'tc_renamecontract_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class TcRenamecontractCstm(Base):
    __tablename__ = 'tc_renamecontract_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    status_c = Column(String(100), server_default=text("'one'"))


class TcRenamecontractOpportunities1C(Base):
    __tablename__ = 'tc_renamecontract_opportunities_1_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_renamecontract_opportunities_1opportunities_ida = Column(String(36), index=True)
    tc_renamecontract_opportunities_1tc_renamecontract_idb = Column(String(36), index=True)


class TcRenamecontractOpportunitiesC(Base):
    __tablename__ = 'tc_renamecontract_opportunities_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_renamecontract_opportunitiesopportunities_ida = Column(String(36), index=True)
    tc_renamecontract_opportunitiestc_renamecontract_idb = Column(String(36), index=True)


class TcRenamecontractTcTarifchangephoneC(Base):
    __tablename__ = 'tc_renamecontract_tc_tarifchangephone_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_renamecontract_tc_tarifchangephonetc_renamecontract_ida = Column(String(36), index=True)
    tc_renamecontract_tc_tarifchangephonetc_tarifchangephone_idb = Column(String(36), index=True)


class TcRenamecontractTcTariffchangeinetC(Base):
    __tablename__ = 'tc_renamecontract_tc_tariffchangeinet_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_renamecontract_tc_tariffchangeinettc_renamecontract_ida = Column(String(36), index=True)
    tc_renamecontract_tc_tariffchangeinettc_tariffchangeinet_idb = Column(String(36), index=True)


class TcTarifchangephone(Base):
    __tablename__ = 'tc_tarifchangephone'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    datechange = Column(Date)
    dateperform = Column(Date)
    user_id_c = Column(CHAR(36))
    oldservice = Column(Text)
    newservice = Column(Text)
    opportunity_id_c = Column(CHAR(36))
    opportunity_id1_c = Column(CHAR(36))


class TcTarifchangephoneAccountsC(Base):
    __tablename__ = 'tc_tarifchangephone_accounts_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_tarifchangephone_accountsaccounts_ida = Column(String(36), index=True)
    tc_tarifchangephone_accountstc_tarifchangephone_idb = Column(String(36), index=True)


class TcTarifchangephoneAudit(Base):
    __tablename__ = 'tc_tarifchangephone_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class TcTarifchangephoneCstm(Base):
    __tablename__ = 'tc_tarifchangephone_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    status_c = Column(String(100), server_default=text("'one'"))


class TcTariffchangeinet(Base):
    __tablename__ = 'tc_tariffchangeinet'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    oldbandwith = Column(Float(18))
    newbandwith = Column(Float(18))
    oldcost = Column(INTEGER(255))
    newcost = Column(INTEGER(255))
    datechange = Column(Date)
    daterealchange = Column(Date)
    checked = Column(TINYINT(1), server_default=text("'0'"))
    datechecked = Column(Date)
    user_id_c = Column(CHAR(36))
    opportunity_id_c = Column(CHAR(36))
    opportunity_id1_c = Column(CHAR(36))
    checkcomment = Column(Text)
    user_id1_c = Column(CHAR(36))
    oldlimit = Column(INTEGER(255))
    newlimit = Column(INTEGER(255))


class TcTariffchangeinetAccountsC(Base):
    __tablename__ = 'tc_tariffchangeinet_accounts_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    tc_tariffchangeinet_accountsaccounts_ida = Column(String(36), index=True)
    tc_tariffchangeinet_accountstc_tariffchangeinet_idb = Column(String(36), index=True)


class TcTariffchangeinetAudit(Base):
    __tablename__ = 'tc_tariffchangeinet_audit'

    id = Column(CHAR(36), primary_key=True)
    parent_id = Column(CHAR(36), nullable=False, index=True)
    date_created = Column(DateTime)
    created_by = Column(String(36))
    field_name = Column(String(100))
    data_type = Column(String(100))
    before_value_string = Column(String(255))
    after_value_string = Column(String(255))
    before_value_text = Column(Text)
    after_value_text = Column(Text)


class TcTariffchangeinetCstm(Base):
    __tablename__ = 'tc_tariffchangeinet_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    status_c = Column(String(100), server_default=text("'transmit'"))


class Tracker(Base):
    __tablename__ = 'tracker'
    __table_args__ = (
        Index('idx_tracker_userid_vis_id', 'user_id', 'visible', 'id'),
        Index('idx_tracker_userid_itemid_vis', 'user_id', 'item_id', 'visible')
    )

    id = Column(INTEGER(11), primary_key=True)
    monitor_id = Column(CHAR(36), nullable=False, index=True)
    user_id = Column(String(36))
    module_name = Column(String(255))
    item_id = Column(String(36), index=True)
    item_summary = Column(String(255))
    date_modified = Column(DateTime, index=True)
    action = Column(String(255))
    session_id = Column(String(36))
    visible = Column(TINYINT(1), server_default=text("'0'"))
    deleted = Column(TINYINT(1), server_default=text("'0'"))


class UpgradeHistory(Base):
    __tablename__ = 'upgrade_history'

    id = Column(CHAR(36), primary_key=True)
    filename = Column(String(255))
    md5sum = Column(String(32), unique=True)
    type = Column(String(30))
    status = Column(String(50))
    version = Column(String(64))
    name = Column(String(255))
    description = Column(Text)
    id_name = Column(String(255))
    manifest = Column(LONGTEXT)
    date_entered = Column(DateTime)
    enabled = Column(TINYINT(1), server_default=text("'1'"))


class UserPreference(Base):
    __tablename__ = 'user_preferences'
    __table_args__ = (
        Index('idx_userprefnamecat', 'assigned_user_id', 'category'),
    )

    id = Column(CHAR(36), primary_key=True)
    category = Column(String(50))
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    assigned_user_id = Column(CHAR(36))
    contents = Column(LONGTEXT)


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        Index('idx_user_name', 'user_name', 'is_group', 'status', 'last_name', 'first_name', 'id'),
    )

    id = Column(CHAR(36), primary_key=True)
    user_name = Column(String(60))
    user_hash = Column(String(255))
    system_generated_password = Column(TINYINT(1))
    pwd_last_changed = Column(DateTime)
    authenticate_id = Column(String(100))
    sugar_login = Column(TINYINT(1), server_default=text("'1'"))
    first_name = Column(String(30))
    last_name = Column(String(30))
    is_admin = Column(TINYINT(1), server_default=text("'0'"))
    external_auth_only = Column(TINYINT(1), server_default=text("'0'"))
    receive_notifications = Column(TINYINT(1), server_default=text("'1'"))
    description = Column(Text)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    title = Column(String(50))
    department = Column(String(50))
    phone_home = Column(String(50))
    phone_mobile = Column(String(50))
    phone_work = Column(String(50))
    phone_other = Column(String(50))
    phone_fax = Column(String(50))
    status = Column(String(100))
    address_street = Column(String(150))
    address_city = Column(String(100))
    address_state = Column(String(100))
    address_country = Column(String(100))
    address_postalcode = Column(String(20))
    deleted = Column(TINYINT(1))
    portal_only = Column(TINYINT(1), server_default=text("'0'"))
    show_on_employees = Column(TINYINT(1), server_default=text("'1'"))
    employee_status = Column(String(100))
    messenger_id = Column(String(100))
    messenger_type = Column(String(100))
    reports_to_id = Column(CHAR(36))
    is_group = Column(TINYINT(1))


class UsersCstm(Base):
    __tablename__ = 'users_cstm'

    id_c = Column(CHAR(36), primary_key=True)
    dept_c = Column(String(100), server_default=text("'installer'"))


t_users_feeds = Table(
    'users_feeds', metadata,
    Column('user_id', String(36)),
    Column('feed_id', String(36)),
    Column('rank', INTEGER(11)),
    Column('date_modified', DateTime),
    Column('deleted', TINYINT(1), server_default=text("'0'")),
    Index('idx_ud_user_id', 'user_id', 'feed_id')
)


class UsersLastImport(Base):
    __tablename__ = 'users_last_import'

    id = Column(CHAR(36), primary_key=True)
    assigned_user_id = Column(CHAR(36), index=True)
    import_module = Column(String(36))
    bean_type = Column(String(36))
    bean_id = Column(CHAR(36))
    deleted = Column(TINYINT(1))


class UsersPasswordLink(Base):
    __tablename__ = 'users_password_link'

    id = Column(CHAR(36), primary_key=True)
    username = Column(String(36), index=True)
    date_generated = Column(DateTime)
    deleted = Column(TINYINT(1))


class UsersSignature(Base):
    __tablename__ = 'users_signatures'

    id = Column(CHAR(36), primary_key=True)
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1))
    user_id = Column(String(36), index=True)
    name = Column(String(255))
    signature = Column(Text)
    signature_html = Column(Text)


class Vcal(Base):
    __tablename__ = 'vcals'
    __table_args__ = (
        Index('idx_vcal', 'type', 'user_id'),
    )

    id = Column(CHAR(36), primary_key=True)
    deleted = Column(TINYINT(1))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    user_id = Column(CHAR(36), nullable=False)
    type = Column(String(100))
    source = Column(String(100))
    content = Column(Text)


class Version(Base):
    __tablename__ = 'versions'
    __table_args__ = (
        Index('idx_version', 'name', 'deleted'),
    )

    id = Column(CHAR(36), primary_key=True)
    deleted = Column(TINYINT(1))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    name = Column(String(255))
    file_version = Column(String(255))
    db_version = Column(String(255))


class Zr2Querytemplate(Base):
    __tablename__ = 'zr2_querytemplate'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    sql1 = Column(Text)


class Zr2Report(Base):
    __tablename__ = 'zr2_report'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    filename = Column(String(255))


class Zr2Reportcontainer(Base):
    __tablename__ = 'zr2_reportcontainer'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))


class Zr2ReportcontainerZr2ReportC(Base):
    __tablename__ = 'zr2_reportcontainer_zr2_report_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    zr2_reportcontainer_zr2_reportzr2_reportcontainer_ida = Column(String(36), index=True)
    zr2_reportcontainer_zr2_reportzr2_report_idb = Column(String(36), index=True)


class Zr2Reportparameter(Base):
    __tablename__ = 'zr2_reportparameter'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    friendly_name = Column(String(255))
    default_name = Column(String(255))
    default_value = Column(String(255))
    range_name = Column(String(255))
    range_options = Column(Text)


class Zr2Reportparameterlink(Base):
    __tablename__ = 'zr2_reportparameterlink'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    default_value = Column(String(255))
    bind_to_module_name = Column(String(255))


class Zr2ReportparameterlinkZr2QuerytemplateC(Base):
    __tablename__ = 'zr2_reportparameterlink_zr2_querytemplate_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    zr2_query313cemplate_ida = Column(String(36), index=True)
    zr2_report0ed1terlink_idb = Column(String(36), index=True)


class Zr2ReportparameterlinkZr2ReportparameterC(Base):
    __tablename__ = 'zr2_reportparameterlink_zr2_reportparameter_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    zr2_report29aerameter_ida = Column(String(36), index=True)
    zr2_report53a6terlink_idb = Column(String(36), index=True)


class Zr2ReportparameterlinkZr2ReporttemplateC(Base):
    __tablename__ = 'zr2_reportparameterlink_zr2_reporttemplate_c'

    id = Column(String(36), primary_key=True)
    date_modified = Column(DateTime)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    zr2_report313cemplate_ida = Column(String(36), index=True)
    zr2_report0ed1terlink_idb = Column(String(36), index=True)


class Zr2Reporttemplate(Base):
    __tablename__ = 'zr2_reporttemplate'

    id = Column(CHAR(36), primary_key=True)
    name = Column(String(255))
    date_entered = Column(DateTime)
    date_modified = Column(DateTime)
    modified_user_id = Column(CHAR(36))
    created_by = Column(CHAR(36))
    description = Column(Text)
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    assigned_user_id = Column(CHAR(36))
    filename = Column(String(255))
    export_as = Column(String(255))
    error_message = Column(Text)
