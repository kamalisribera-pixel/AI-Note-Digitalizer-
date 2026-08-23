from src.layout.document_block import DocumentBlock


block = DocumentBlock(
    text="Introduction",
    bbox=[100, 50, 300, 90],
    confidence=0.98
)


print(block)
print(block.to_dict())