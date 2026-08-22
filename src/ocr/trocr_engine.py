from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch


class TrOCREngine:
    def __init__(
        self,
        model_name="microsoft/trocr-base-handwritten"
    ):
        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.processor = TrOCRProcessor.from_pretrained(
            model_name,
            use_fast=False
        )

        self.model = VisionEncoderDecoderModel.from_pretrained(
            model_name
        )

        self.model.to(self.device)
        self.model.eval()


    def extract_text(self, image):

        pixel_values = self.processor(
            images=image,
            return_tensors="pt"
        ).pixel_values

        pixel_values = pixel_values.to(self.device)

        with torch.no_grad():

            generated_ids = self.model.generate(
                pixel_values,
                max_new_tokens=64
            )

        generated_text = self.processor.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0]

        return generated_text