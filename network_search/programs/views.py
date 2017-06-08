from django.views.generic import DetailView

from easy_pdf.views import PDFTemplateResponseMixin
from network_search.core.views import SearchView
from network_search.programs.forms import ProgramSearchForm
from network_search.programs.models import Program


class ProgramView(DetailView):
    queryset = Program.programs.active()
    template_name = "programs/program_detail.html"


class ProgramPDFView(PDFTemplateResponseMixin, ProgramView):
    template_name = "programs/program_pdf.html"


class ProgramSearchView(SearchView):
    """
    List and search for programs
    """
    context_object_name = "programs"
    form_class = ProgramSearchForm
    queryset = Program.programs.active()
    template_name = "programs/program_list.html"
