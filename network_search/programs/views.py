from django.views.generic import DetailView

from network_search.core.views import PDFMixin
from network_search.core.views import SearchView
from network_search.programs.forms import ProgramSearchForm
from network_search.programs.models import Program


class ProgramView(DetailView):
    queryset = Program.programs.active()
    template_name = "programs/program_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'org_type': 'Program',
        })
        return context


class ProgramPDFView(PDFMixin, ProgramView):
    template_name = "programs/program_pdf.html"


class ProgramSearchView(SearchView):
    """
    List and search for programs
    """
    context_object_name = "programs"
    form_class = ProgramSearchForm
    queryset = Program.programs.active()
    template_name = "programs/program_list.html"
