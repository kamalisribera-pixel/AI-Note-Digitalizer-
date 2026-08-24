from src.document.images.image_validators.decision_engine import DecisionEngine


evidences = [

    {
        "source": "vision",
        "type": "table",
        "score": 0.608
    },

    {
        "source": "geometry",
        "type": "table",
        "score": 1.0
    },

    {
        "source": "ocr",
        "type": "table",
        "score": 0.7
    },

    {
        "source": "shape",
        "type": "table",
        "score": 1.0
    },

    {
        "source": "layout",
        "type": "table",
        "score": 1.0
    }

]


engine = DecisionEngine()

result = engine.calculate(
    evidences
)


print("DECISION RESULT")
print(result)