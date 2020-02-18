"""
Django Forms for interacting with Part objects
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext as _

from common.models import Currency
from mptt.fields import TreeNodeChoiceField

from InvenTree.forms import HelperForm
from InvenTree.helpers import GetExportFormats

from .models import (
    BomItem,
    Part,
    PartAttachment,
    PartCategory,
    PartParameter,
    PartParameterTemplate,
)


class PartImageForm(HelperForm):
    """ Form for uploading a Part image """

    class Meta:
        model = Part
        fields = [
            "image",
        ]


class BomExportForm(forms.Form):
    """ Simple form to let user set BOM export options,
    before exporting a BOM (bill of materials) file.
    """

    file_format = forms.ChoiceField(
        label=_("File Format"), help_text=_("Select output file format")
    )

    cascading = forms.BooleanField(
        label=_("Cascading"),
        required=False,
        initial=False,
        help_text=_("Download cascading / multi-level BOM"),
    )

    def get_choices(self):
        """ BOM export format choices """

        return [(x, x.upper()) for x in GetExportFormats()]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["file_format"].choices = self.get_choices()


class BomValidateForm(HelperForm):
    """ Simple confirmation form for BOM validation.
    User is presented with a single checkbox input,
    to confirm that the BOM for this part is valid
    """

    validate = forms.BooleanField(
        required=False, initial=False, help_text=_("Confirm that the BOM is correct")
    )

    class Meta:
        model = Part
        fields = ["validate"]


class BomUploadSelectFile(HelperForm):
    """ Form for importing a BOM. Provides a file input box for upload """

    bom_file = forms.FileField(
        label="BOM file", required=True, help_text=_("Select BOM file to upload")
    )

    class Meta:
        model = Part
        fields = [
            "bom_file",
        ]


class EditPartAttachmentForm(HelperForm):
    """ Form for editing a PartAttachment object """

    class Meta:
        model = PartAttachment
        fields = ["part", "attachment", "comment"]


class SetPartCategoryForm(forms.Form):
    """ Form for setting the category of multiple Part objects """

    part_category = TreeNodeChoiceField(
        queryset=PartCategory.objects.all(),
        required=True,
        help_text=_("Select part category"),
    )


class EditPartForm(HelperForm):
    """ Form for editing a Part object """

    deep_copy = forms.BooleanField(
        required=False,
        initial=True,
        help_text=_(
            "Perform 'deep copy' which will duplicate all BOM data for this part"
        ),
        widget=forms.HiddenInput(),
    )

    confirm_creation = forms.BooleanField(
        required=False,
        initial=False,
        help_text=_("Confirm part creation"),
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = Part
        fields = [
            "deep_copy",
            "confirm_creation",
            "category",
            "name",
            "IPN",
            "description",
            "revision",
            "keywords",
            "variant_of",
            "is_template",
            "URL",
            "default_location",
            "default_supplier",
            "units",
            "minimum_stock",
            "active",
        ]


class EditPartParameterTemplateForm(HelperForm):
    """ Form for editing a PartParameterTemplate object """

    class Meta:
        model = PartParameterTemplate
        fields = ["name", "units"]


class EditPartParameterForm(HelperForm):
    """ Form for editing a PartParameter object """

    class Meta:
        model = PartParameter
        fields = ["part", "template", "data"]


class EditCategoryForm(HelperForm):
    """ Form for editing a PartCategory object """

    class Meta:
        model = PartCategory
        fields = [
            "parent",
            "name",
            "description",
            "default_location",
            "default_keywords",
        ]


class EditBomItemForm(HelperForm):
    """ Form for editing a BomItem object """

    class Meta:
        model = BomItem
        fields = ["part", "sub_part", "quantity", "reference", "overage", "note"]

        # Prevent editing of the part associated with this BomItem
        widgets = {"part": forms.HiddenInput()}


class PartPriceForm(forms.Form):
    """ Simple form for viewing part pricing information """

    quantity = forms.IntegerField(
        required=True, initial=1, help_text=_("Input quantity for price calculation")
    )

    currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(),
        label="Currency",
        help_text=_("Select currency for price calculation"),
    )

    class Meta:
        model = Part
        fields = [
            "quantity",
            "currency",
        ]
