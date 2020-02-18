"""
Django views for interacting with Company app
"""


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import HiddenInput
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views.generic import DetailView, ListView, UpdateView

from part.models import Part

from InvenTree.helpers import str2bool
from InvenTree.status_codes import OrderStatus
from InvenTree.views import AjaxCreateView, AjaxDeleteView, AjaxUpdateView

from .forms import (
    CompanyImageForm,
    EditCompanyForm,
    EditPriceBreakForm,
    EditSupplierPartForm,
)
from .models import Company, SupplierPart, SupplierPriceBreak


class CompanyIndex(ListView):
    """ View for displaying list of companies
    """

    model = Company
    template_name = "company/index.html"
    context_object_name = "companies"
    paginate_by = 50

    def get_queryset(self):
        """ Retrieve the Company queryset based on HTTP request parameters.

        - supplier: Filter by supplier
        - customer: Filter by customer
        """
        queryset = Company.objects.all().order_by("name")

        if self.request.GET.get("supplier", None):
            queryset = queryset.filter(is_supplier=True)

        if self.request.GET.get("customer", None):
            queryset = queryset.filter(is_customer=True)

        return queryset


class CompanyNotes(UpdateView):
    """ View for editing the 'notes' field of a Company object.
    """

    context_object_name = "company"
    template_name = "company/notes.html"
    model = Company

    fields = ["notes"]

    def get_success_url(self):
        return reverse("company-notes", kwargs={"pk": self.get_object().id})

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)

        ctx["editing"] = str2bool(self.request.GET.get("edit", ""))

        return ctx


class CompanyDetail(DetailView):
    """ Detail view for Company object """

    context_obect_name = "company"
    template_name = "company/detail.html"
    queryset = Company.objects.all()
    model = Company

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["OrderStatus"] = OrderStatus

        return ctx


class CompanyImage(AjaxUpdateView):
    """ View for uploading an image for the Company """

    model = Company
    ajax_template_name = "modal_form.html"
    ajax_form_title = _("Update Company Image")
    form_class = CompanyImageForm

    def get_data(self):
        return {
            "success": _("Updated company image"),
        }


class CompanyEdit(AjaxUpdateView):
    """ View for editing a Company object """

    model = Company
    form_class = EditCompanyForm
    context_object_name = "company"
    ajax_template_name = "modal_form.html"
    ajax_form_title = _("Edit Company")

    def get_data(self):
        return {
            "info": _("Edited company information"),
        }


class CompanyCreate(AjaxCreateView):
    """ View for creating a new Company object """

    model = Company
    context_object_name = "company"
    form_class = EditCompanyForm
    ajax_template_name = "modal_form.html"
    ajax_form_title = _("Create new Company")

    def get_data(self):
        return {
            "success": _("Created new company"),
        }


class CompanyDelete(AjaxDeleteView):
    """ View for deleting a Company object """

    model = Company
    success_url = "/company/"
    ajax_template_name = "company/delete.html"
    ajax_form_title = _("Delete Company")
    context_object_name = "company"

    def get_data(self):
        return {
            "danger": _("Company was deleted"),
        }


class SupplierPartDetail(DetailView):
    """ Detail view for SupplierPart """

    model = SupplierPart
    template_name = "company/supplier_part_detail.html"
    context_object_name = "part"
    queryset = SupplierPart.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["OrderStatus"] = OrderStatus

        return ctx


class SupplierPartEdit(AjaxUpdateView):
    """ Update view for editing SupplierPart """

    model = SupplierPart
    context_object_name = "part"
    form_class = EditSupplierPartForm
    ajax_template_name = "modal_form.html"
    ajax_form_title = _("Edit Supplier Part")


class SupplierPartCreate(AjaxCreateView):
    """ Create view for making new SupplierPart """

    model = SupplierPart
    form_class = EditSupplierPartForm
    ajax_template_name = "modal_form.html"
    ajax_form_title = _("Create new Supplier Part")
    context_object_name = "part"

    def get_form(self):
        """ Create Form instance to create a new SupplierPart object.
        Hide some fields if they are not appropriate in context
        """
        form = super(AjaxCreateView, self).get_form()

        if form.initial.get("supplier", None):
            # Hide the supplier field
            form.fields["supplier"].widget = HiddenInput()

        if form.initial.get("part", None):
            # Hide the part field
            form.fields["part"].widget = HiddenInput()

        return form

    def get_initial(self):
        """ Provide initial data for new SupplierPart:

        - If 'supplier_id' provided, pre-fill supplier field
        - If 'part_id' provided, pre-fill part field
        """
        initials = super(SupplierPartCreate, self).get_initial().copy()

        supplier_id = self.get_param("supplier")
        part_id = self.get_param("part")

        if supplier_id:
            try:
                initials["supplier"] = Company.objects.get(pk=supplier_id)
            except Company.DoesNotExist:
                initials["supplier"] = None

        if part_id:
            try:
                initials["part"] = Part.objects.get(pk=part_id)
            except Part.DoesNotExist:
                initials["part"] = None

        return initials


class SupplierPartDelete(AjaxDeleteView):
    """ Delete view for removing a SupplierPart.
    
    SupplierParts can be deleted using a variety of 'selectors'.

    - ?part=<pk> -> Delete a single SupplierPart object
    - ?parts=[] -> Delete a list of SupplierPart objects

    """

    success_url = "/supplier/"
    ajax_template_name = "company/partdelete.html"
    ajax_form_title = _("Delete Supplier Part")

    parts = []

    def get_context_data(self):
        ctx = {}

        ctx["parts"] = self.parts

        return ctx

    def get_parts(self):
        """ Determine which SupplierPart object(s) the user wishes to delete.
        """

        self.parts = []

        # User passes a single SupplierPart ID
        if "part" in self.request.GET:
            try:
                self.parts.append(
                    SupplierPart.objects.get(pk=self.request.GET.get("part"))
                )
            except (ValueError, SupplierPart.DoesNotExist):
                pass

        elif "parts[]" in self.request.GET:

            part_id_list = self.request.GET.getlist("parts[]")

            self.parts = SupplierPart.objects.filter(id__in=part_id_list)

    def get(self, request, *args, **kwargs):
        self.request = request
        self.get_parts()

        return self.renderJsonResponse(request, form=self.get_form())

    def post(self, request, *args, **kwargs):
        """ Handle the POST action for deleting supplier parts.
        """

        self.request = request
        self.parts = []

        for item in self.request.POST:
            if item.startswith("supplier-part-"):
                pk = item.replace("supplier-part-", "")

                try:
                    self.parts.append(SupplierPart.objects.get(pk=pk))
                except (ValueError, SupplierPart.DoesNotExist):
                    pass

        confirm = str2bool(self.request.POST.get("confirm_delete", False))

        data = {
            "form_valid": confirm,
        }

        if confirm:
            for part in self.parts:
                part.delete()

        return self.renderJsonResponse(self.request, data=data, form=self.get_form())


class PriceBreakCreate(AjaxCreateView):
    """ View for creating a supplier price break """

    model = SupplierPriceBreak
    form_class = EditPriceBreakForm
    ajax_form_title = _("Add Price Break")
    ajax_template_name = "modal_form.html"

    def get_data(self):
        return {"success": "Added new price break"}

    def get_part(self):
        try:
            return SupplierPart.objects.get(id=self.request.GET.get("part"))
        except SupplierPart.DoesNotExist:
            return SupplierPart.objects.get(id=self.request.POST.get("part"))

    def get_form(self):

        form = super(AjaxCreateView, self).get_form()
        form.fields["part"].widget = HiddenInput()

        return form

    def get_initial(self):

        initials = super(AjaxCreateView, self).get_initial()

        initials["part"] = self.get_part()

        return initials


class PriceBreakEdit(AjaxUpdateView):
    """ View for editing a supplier price break """

    model = SupplierPriceBreak
    form_class = EditPriceBreakForm
    ajax_form_title = _("Edit Price Break")
    ajax_template_name = "modal_form.html"

    def get_form(self):

        form = super(AjaxUpdateView, self).get_form()
        form.fields["part"].widget = HiddenInput()

        return form


class PriceBreakDelete(AjaxDeleteView):
    """ View for deleting a supplier price break """

    model = SupplierPriceBreak
    ajax_form_title = _("Delete Price Break")
    ajax_template_name = "modal_delete_form.html"
