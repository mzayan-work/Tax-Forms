from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator
from .validators import validate_file_size

from encrypted_model_fields.fields import EncryptedCharField

# Create your models here.
class TaxForm(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        SUBMITTED = 'submitted', 'Submitted'
        CONFIRMED = 'confirmed', 'Confirmed'

    class ApplyMethod(models.TextChoices):
        ONLINE = 'online', 'Online'
        OFFICE = 'office', 'Office'

    class MaritalStatus(models.TextChoices):
        SINGLE = 'single', 'Single'
        MARRIED = 'married', 'Married'
        DIVORCED = 'divorced', 'Divorced'
        SEPARATED = 'separated', 'Separated'
        WIDOWER = 'widower', 'Widower'

    class SupportPaymentStatus(models.TextChoices):
        PAY = 'pay', 'Pay'
        RECEIVE = 'receive', 'Receive'
        NONE = 'none', 'None'

    class ChildrenStatus(models.TextChoices):
        NOT_LIVING_WITH_YOU = 'not_living_with_you', 'No'
        LIVING_WITH_YOU = 'living_with_you', 'Yes'
        SHARED = 'shared', 'Shared'

    #Form Info..................
    client = models.ForeignKey(
        "otploginapp.Client",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Client",
        related_name="tax_forms",
    )

    create_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name="Create Date"
    )

    update_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Update Date"
    )

    status = models.CharField(
        blank=False,
        null=False,
        max_length=128,
        choices=Status.choices,
        default="DRAFT",
        verbose_name="Status"
    )

    apply_method = models.CharField(
        blank=False,
        max_length=128,
        choices=ApplyMethod.choices,
        default="ONLINE",
        verbose_name="Apply Method"
    )

    is_sub_form = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )

    basic_form = models.ForeignKey(
        "TaxForm",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    #Personal Info.................
    first_name = models.CharField(
        blank=True,
        null=False,
        max_length=50,
        verbose_name="First Name"
    )

    last_name = models.CharField(
        blank=True,
        null=False,
        max_length=50,
        verbose_name="Last Name"
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date Of Birth"
    )

    sin_number = EncryptedCharField(
        blank=True,
        null=True,
        max_length=9,
        verbose_name="SIN",
        validators=[
            RegexValidator(
                regex=r'^\d{9}$',  # Ensures exactly 9 digits
                message="SIN number must be exactly 9 digits."
            )
        ]
    )

    enter_canada_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Date of entry to Canada"
    )

    #Contact Info............
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Email",
    )

    street_number = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Street Number",
    )

    apartment_number = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Apartment Number",
    )

    town = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Town",
    )

    province = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Province",
    )

    postal_code = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Postal Code",
    )

    #Marital Status Info..............
    marital_status = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        choices=MaritalStatus.choices,
        verbose_name="Marital Status"
    )

    marital_status_start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name= "Date of begin this statue?"
    )

    support_payments_status = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        choices=SupportPaymentStatus.choices,
        verbose_name="Did you pay or receive supporting payment for your ex-spouse?"
    )

    payment_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Payment Amount"
    )

    with_children = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Do you have children?"
    )

    children_status = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        choices=ChildrenStatus.choices,
        verbose_name="Do you have children living with you all the time?"
    )

    #Another Questions.................
    has_approved_disability = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Do you have approved disability from CRA?"
    )

    medical_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Medical Expenses (family)"
    )

    donations = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Any donations (family)"
    )

    activities = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Any childcare or activities (Family)"
    )

    rent_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Rent Amount (Paid in this year only)"
    )

    has_house = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Do you Own a house?"
    )

    property_tax_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Property tax amount"
    )

    has_investment_income = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Do you have RRSP constitution account or any investment income?"
    )

    purchase_first_home = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Did you purchase your first home in canada in this year?"
    )

    work_from_home = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Did you work from home during this year?"
    )

    #Documents...............
    id_document = models.FileField(
        upload_to='documents/',  # Files will be saved to MEDIA_ROOT/documents/
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg']),
            validate_file_size
        ],
        help_text="Upload a PDF or image file (max 4 MB).",
        blank=True,
        null=True,
        verbose_name="ID(PR, Driver License, Photo ID, Passport, Health Card, Birth Certificate)"
    )

    void_check_document = models.FileField(
        upload_to='documents/',  # Files will be saved to MEDIA_ROOT/documents/
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg']),
            validate_file_size
        ],
        help_text="Upload a PDF or image file (max 4 MB).",
        blank=True,
        null=True,
        verbose_name="Void Check"
    )


class Children(models.Model):
    tax_form = models.ForeignKey(
        'TaxForm',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Form",
        related_name="children"
    )

    child_name = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        verbose_name="Name"
    )

    birth_date = models.DateField(
        blank=False,
        null=False,
        verbose_name="DOB"
    )

    id_document = models.FileField(
        upload_to='documents/',  # Files will be saved to MEDIA_ROOT/documents/
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg']),
            validate_file_size
        ],
        help_text="Upload a PDF or image file (max 4 MB).",
        blank=True,
        null=True,
        verbose_name="ID(PR, Driver License, Photo ID, Passport, Health Card, Birth Certificate)"
    )

class StudentClient(models.Model):
    tax_form = models.ForeignKey(
        'TaxForm',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Form",
        related_name="students"
    )

    t4a_document = models.FileField(
        upload_to='documents/',  # Files will be saved to MEDIA_ROOT/documents/
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg']),
            validate_file_size
        ],
        help_text="Upload a PDF or image file (max 4 MB).",
        blank=True,
        null=True,
        verbose_name="T4A"
    )

    t2202_document = models.FileField(
        upload_to='documents/',  # Files will be saved to MEDIA_ROOT/documents/
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg']),
            validate_file_size
        ],
        help_text="Upload a PDF or image file (max 4 MB).",
        blank=True,
        null=True,
        verbose_name="T2202"
    )

class EmployedClient(models.Model):
    tax_form = models.ForeignKey(
        'TaxForm',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Form",
        related_name="employed"
    )

    t4_document = models.FileField(
        upload_to='documents/',  # Files will be saved to MEDIA_ROOT/documents/
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg']),
            validate_file_size
        ],
        help_text="Upload a PDF or image file (max 4 MB).",
        blank=True,
        null=True,
        verbose_name="T4"
    )

class SelfEmployedClient(models.Model):
    tax_form = models.ForeignKey(
        'TaxForm',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Form",
        related_name="self_employed"
    )

    business_number = models.CharField(
        blank=True,
        null=True,
        verbose_name="Business Number"
    )

    hst_access_code = models.CharField(
        verbose_name="HST Access Code"
    )

    fuel_expenses = models.DecimalField(
        blank=True,
        null=True,
        max_digits=6,
        decimal_places=2,
        verbose_name="Fuel(monthly)"
    )

    insurance_expenses = models.DecimalField(
        blank=True,
        null=True,
        max_digits=6,
        decimal_places=2,
        verbose_name="Insurance(monthly)"
    )

    car_repair_expenses = models.DecimalField(
        blank=True,
        null=True,
        max_digits=6,
        decimal_places=2,
        verbose_name="Car Repair"
    )

    meals_expenses = models.DecimalField(
        blank=True,
        null=True,
        max_digits=6,
        decimal_places=2,
        verbose_name="Meals"
    )

    new_car_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="New Car Price"
    )

    mobile_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Mobile(monthly)"
    )

    other_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Other Expenses"
    )

    other_expenses_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Other Expenses Description"
    )

    year_total_income = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Total Income (Year)"
    )

class ForeignIncomeClient(models.Model):
    tax_form = models.ForeignKey(
        'TaxForm',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Form",
        related_name="foreign_income"
    )

    income_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Amount"
    )

class RentalIncomeClient(models.Model):
    tax_form = models.ForeignKey(
        'TaxForm',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Form",
        related_name="rental_income"
    )

    ownership_percentage = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Ownership Percentage"
    )

    year_total_income = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Total income for the Year"
    )

    street_number = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Street Number",
    )

    apartment_number = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Apartment Number",
    )

    town = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Town",
    )

    province = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Province",
    )

    postal_code = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        verbose_name="Postal Code",
    )

    legal_fees_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Legal Fees"
    )

    commission_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Commission"
    )

    property_tax_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Property Tax"
    )

    utilities_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Utilities"
    )

    repair_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Repair"
    )

    insurance_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Insurance(monthly)"
    )

    condo_fees_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Condo Fees(monthly)"
    )

    other_expenses = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Other Expenses"
    )

    other_expenses_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Other Expenses Description"
    )

class GovernmentAssistanceClient(models.Model):
    tax_form = models.ForeignKey(
        'TaxForm',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Form",
        related_name="government_assistance"
    )

    t5007_document = models.FileField(
        upload_to='documents/',  # Files will be saved to MEDIA_ROOT/documents/
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg']),
            validate_file_size
        ],
        help_text="Upload a PDF or image file (max 4 MB).",
        blank=True,
        null=True,
        verbose_name="T5007"
    )









