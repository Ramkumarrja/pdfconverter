from pdf2docx import parse

pdf_file = 'MedFit form.pdf'
docx_file = 'MedFit form.docx'

parse(pdf_file=pdf_file, docx_with_path=docx_file)
