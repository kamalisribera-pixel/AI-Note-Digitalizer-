class ListItem:

    def __init__(
        self,
        text,
        marker=None,
        level=0
    ):
        self.text = text
        self.marker = marker
        self.level = level


    def __repr__(self):

        return (
            f"ListItem("
            f"text='{self.text}', "
            f"marker='{self.marker}', "
            f"level={self.level}"
            f")"
        )