from transformers import CLIPProcessor, CLIPModel
import torch


class ImageClassifier:

    def __init__(self):

        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        )
        self.model.eval()

        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

        # Prompts for CLIP
        self.labels = [
            "a natural photograph",
            "a table with rows and columns",
            "a labeled scientific or engineering diagram",
            "a mathematical formula or equation",
            "a mathematical graph with x and y axes",
            "a data visualization chart such as a bar chart, pie chart, or line chart",
            "a flowchart with connected boxes and arrows",
            "a mind map with a central topic and connected branches"
        ]

        # Internal labels used by your project
        self.image_types = [
            "photo",
            "table",
            "diagram",
            "formula",
            "graph",
            "chart",
            "flowchart",
            "mindmap"
        ]

    def classify(self, image_block, image):

        x1, y1, x2, y2 = image_block.bbox

        crop = image[y1:y2, x1:x2]

        if crop.size == 0:
            raise ValueError("Empty image crop.")

        inputs = self.processor(
            text=self.labels,
            images=crop,
            return_tensors="pt",
            padding=True
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        scores = outputs.logits_per_image.softmax(dim=1)

        index = scores.argmax().item()

        image_block.image_type = self.image_types[index]
        image_block.confidence = scores[0, index].item()

        return image_block