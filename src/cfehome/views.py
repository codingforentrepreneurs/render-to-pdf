import locale

from . import renderers


def invoice_view(request):
    context = {
        "bill_to": "Ethan Hunt",
        "invoice_number": "007cae",
        "amount": 100_000,
        "date": "2021-07-04",
    }
    return renderers.render_to_pdf("pdfs/invoice.html", context)


def advanced_pdf_view(request):
    locale.setlocale(locale.LC_ALL, "")
    invoice_number = "007cae"
    context = {
        "bill_to": "Ethan Hunt",
        "invoice_number": f"{invoice_number}",
        "amount": locale.currency(100_000, grouping=True),
        "date": "2021-07-04",
        "pdf_title": f"Invoice #{invoice_number}",
    }
    response = renderers.render_to_pdf("pdfs/invoice.html", context)
    if response.status_code == 404:
        raise HTTP404("Invoice not found")

    filename = f"Invoice_{invoice_number}.pdf"
    """
    Tell browser to view inline (default)
    """
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        """
        Tells browser to initiate download
        """
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response
    return response
