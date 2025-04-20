from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
result_markdown = result.document.export_to_markdown()
output_file = "output.md"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(result_markdown)
print(f"Markdown content written to {output_file}")