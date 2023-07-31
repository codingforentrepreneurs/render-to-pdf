from . import renderers


def invoice_view(request):
    context = {
        "bill_to": "Ethan Hunt",
        "invoice_number": "007cae",
        "amount": 100_000,
        "date": "2021-07-04",
    }
    return renderers.render_to_pdf("pdfs/invoice.html", context)
